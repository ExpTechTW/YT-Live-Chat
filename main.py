import pytchat
import time
import requests
import json
import asyncio
import signal

class LiveChatMonitor:
    def __init__(self, video_id: str, webhook_url: str):
        self.video_id = video_id
        self.webhook_url = webhook_url
        self.chat = pytchat.create(video_id=video_id)
    
    def send_webhook(self, data: dict) -> None:
        payload = {
            "username": data["author"]["name"],
            "avatar_url": data["author"].get("imageUrl", ""),
            "content": data.get("message", "")
        }
        print(f"{payload['username']}: {payload['content']}")
        try:
            response = requests.post(
                self.webhook_url,
                json=payload
            )
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(e)

async def main():
    with open('config.json', 'r') as f:
        config = json.load(f)
    
    VIDEO_ID = config['video_id']
    WEBHOOK_URL = config['webhook_url']
    monitor = LiveChatMonitor(VIDEO_ID, WEBHOOK_URL)
    print(f"開始監測 {VIDEO_ID}")

    def signal_handler(sig, frame):
        print("接收到退出信號，正在關閉...")
        monitor.chat.terminate()
        exit(0)
    signal.signal(signal.SIGINT, signal_handler)

    while True:
        try:
            if not monitor.chat.is_alive():
                print("聊天室連接中斷，嘗試重新連接...")
                monitor = LiveChatMonitor(VIDEO_ID, WEBHOOK_URL)
                await asyncio.sleep(5)
                
                if monitor.chat.is_alive():
                    print("重新連線成功！")
                    continue

            for c in monitor.chat.get().sync_items():
                data = json.loads(c.json())
                monitor.send_webhook(data)
            await asyncio.sleep(0.1)

        except Exception as e:
            print(e)
            await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(main())