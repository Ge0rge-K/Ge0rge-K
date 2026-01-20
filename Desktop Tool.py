import time
import io
import requests
import pyautogui
from datetime import datetime

WEBHOOK_URL = "https://discord.com/api/webhooks/1460054469302812682/rhYFUVeIh7RGCPk4cSqz-0xgLb-2U5SXS1ahj1Yxtfw8vKSYv35seFsnxvQrqnqduTDT"
INTERVAL_SECONDS = 30 * 60  # 30 minutes


def send_screenshot():
    try:
        screenshot = pyautogui.screenshot()

        buffer = io.BytesIO()
        screenshot.save(buffer, format="PNG")
        buffer.seek(0)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        payload = {
            "content": f"Bee Swarm Simulator macro status check\nTime: {timestamp}"
        }

        files = {
            "file": ("screenshot.png", buffer, "image/png")
        }

        response = requests.post(
            WEBHOOK_URL,
            data=payload,
            files=files,
            timeout=15
        )

        if response.status_code not in (200, 204):
            raise Exception(response.text)

    except Exception as e:
        # silent failure to avoid crashing the loop
        pass


def main():
    while True:
        send_screenshot()
        time.sleep(INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
