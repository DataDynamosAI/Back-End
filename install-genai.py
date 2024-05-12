# Work the same as commands: "pip install -q -U google-generativeai"

import subprocess

def install_generativeai():
    try:
        subprocess.run(["pip", "install", "-q", "-U", "google-generativeai"])
        print("Google-GenerativeAI Installed Successfully!")
    except Exception as e:
        print(f"Error Installing Google-GenerativeAI: {e}")

if __name__ == "__main__":
    install_generativeai()
