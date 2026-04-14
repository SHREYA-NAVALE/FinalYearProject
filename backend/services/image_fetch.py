import subprocess
import os

KEY = "C:/Users/Shreya/Downloads/s2dr3-keypair.pem"
SAVE_PATH = "C:/Users/Shreya/Desktop/results"
HOST = "ubuntu@18.218.167.97"

def fetch_images(lat, lon):
    os.makedirs(SAVE_PATH, exist_ok=True)

    # 🔥 Run remote fetch
    remote_cmd = (
        f'cd ~ && '
        f'source ~/s2env/bin/activate && '
        f'python3 -c "from fetch import get_images; get_images({lat}, {lon})"'
    )

    subprocess.run(["ssh", "-i", KEY, HOST, remote_cmd], check=True)

    # 🔥 Download files
    for name in ["current.tif", "previous.tif"]:
        subprocess.run([
            "scp",
            "-i", KEY,
            f"{HOST}:/home/ubuntu/results/{name}",
            SAVE_PATH
        ], check=True)

    return {
        "current": f"{SAVE_PATH}/current.tif",
        "previous": f"{SAVE_PATH}/previous.tif"
    }