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
                video="https://youtu.be/K4TOrB7at0Y?si=8Z79JZKiV2gXAzAN",
                caption="Words don't really do justice, so take two minute to know more about 'me', from 'me'",
                recipient_id=phone_number
            )

