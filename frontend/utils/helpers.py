import requests
import time
import rasterio
import numpy as np
import matplotlib.pyplot as plt

# 🔹 USER CONFIG
USER_ID = "66546448"

API_BASE = f"https://s2dr3-job-20250428-862134799361.europe-west1.run.app/{USER_ID}"

# 🔹 STEP 1: SUBMIT JOB
def submit_job():
    print("🚀 Submitting job...")

    payload = {
        "date": "2023-02-10",
        "aoi": "77.03512220042157 28.632175744308128 77.07839560282194 28.670347594283285"
    }

    response = requests.post(API_BASE, json=payload)

    if response.status_code != 200:
        print("❌ Error:", response.text)
        exit()

    data = response.json()
    print("✅ Job started:", data)

    return data


# 🔹 STEP 2: WAIT FOR COMPLETION
def wait_for_completion(job_id):
    print("⏳ Waiting for processing...")

    url = f"{API_BASE}/{job_id}"

    while True:
        try:
            response = requests.get(url)
            data = response.json()

            state = data.get("state", None)
            print("Status:", state)

            if state == "completed":
                print("✅ Job completed!")
                return data

        except Exception as e:
            print("⚠️ Network error:", e)

        time.sleep(10)


# 🔹 STEP 3: CONVERT gs:// → https://
def convert_to_download_url(gs_url):
    return gs_url.replace(
        "gs://sentinel-s2dr3/",
        "https://storage.googleapis.com/sentinel-s2dr3/"
    )


# 🔹 STEP 4: DOWNLOAD FILE
def download_file(url, filename):
    print("⬇️ Downloading:", filename)

    response = requests.get(url, stream=True)

    if response.status_code != 200:
        print("❌ Download failed:", response.text)
        return

    with open(filename, "wb") as f:
        for chunk in response.iter_content(1024):
            if chunk:
                f.write(chunk)

    print("✅ Download complete:", filename)


# 🔹 STEP 5: CORRECT RGB (MAIN FIX ✅)
def show_correct_rgb(ms_path):
    print("🖼️ Generating REAL RGB image...")

    with rasterio.open(ms_path) as src:
        red = src.read(4).astype(float)    # B04
        green = src.read(3).astype(float)  # B03
        blue = src.read(2).astype(float)   # B02

    img = np.stack([red, green, blue], axis=-1)

    # 🔥 Percentile stretch (fixes dark/green issue)
    p2 = np.percentile(img, 2)
    p98 = np.percentile(img, 98)

    img = np.clip((img - p2) / (p98 - p2), 0, 1)

    plt.imshow(img)
    plt.title("Correct RGB Image")
    plt.axis("off")
    plt.show()


# 🔹 STEP 6: NDVI (GREEN AREA DETECTION 🌱)
def show_ndvi(ms_path):
    print("🌱 Calculating NDVI...")

    with rasterio.open(ms_path) as src:
        red = src.read(4).astype(float)
        nir = src.read(8).astype(float)

    ndvi = (nir - red) / (nir + red + 1e-5)

    plt.imshow(ndvi, cmap="RdYlGn")
    plt.title("NDVI (Green Areas)")
    plt.colorbar()
    plt.axis("off")
    plt.show()


# 🔹 MAIN PIPELINE
def run_pipeline():
    # Step 1
    job_data = submit_job()

    job_id = job_data["job_id"]
    save_path_MS = job_data["save_path_MS"]   # ✅ only MS needed

    # Step 2
    wait_for_completion(job_id)

    # Step 3
    ms_url = convert_to_download_url(save_path_MS)

    # Step 4
    download_file(ms_url, "output_MS.tif")

    # Step 5 → FIXED RGB ✅
    show_correct_rgb("output_MS.tif")

    # Step 6 → GREEN DETECTION 🌱
    show_ndvi("output_MS.tif")


# 🔹 RUN
if __name__ == "__main__":
    run_pipeline()