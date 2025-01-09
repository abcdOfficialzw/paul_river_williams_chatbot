import logging
import os

from dotenv import load_dotenv
from heyoo import WhatsApp

load_dotenv()
messenger = WhatsApp(os.getenv("TOKEN"), phone_number_id=os.getenv("PHONE_NUMBER_ID"))
# Logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


def handle_interactive_message(reply_id: str, phone_number: str, name: str):
    match reply_id:
        case "who_am_i":
            messenger.send_video(
                link=True,
                video="https://github.com/abcdOfficialzw/paul_river_williams_chatbot/raw/refs/heads/main/assets/ScreenRecording_01-09-2025%2018-06-03_1.mov",
                caption="Words don't really do justice, so take two minute to know more about 'me', from 'me'",
                recipient_id=phone_number
            )

