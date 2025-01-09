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
                link=False,
                video="910058841211701",
                caption="Words don't really do justice, so take two minute to know more about 'me', from 'me'",
                recipient_id=phone_number
            )

        case "how_i_can_solve_your_problem":
            messenger.send_message(
                message="*Looking to solve your problem?*\n\n"
                        ""
                        "Please schedule a meeting at a time convenient to you so we may explore how to solve your problem\n\n"
                        ""
                        "_use this link to schedule the meeting_\n"
                        "https://calendly.com/vetech-info/problem-discovery-meeting",
                preview_url=True,
                recipient_id=phone_number
            )

        case "book_a_chat_with_me":
            messenger.send_message(
                message="*Want to sit down for a chat?*\n\n"
                        ""
                        "Fill in your details in this form and I'll get back to you as soon as I can.: https://forms.gle/1cFzfGSgpLMKfuCP9\n\n\n\n"
                        ""
                        "Looking to chat immediately?\n"
                        "Use this link to schedule a meeting at your earliest convenience.:   https://calendly.com/vetech-info/problem-discovery-meeting",
                preview_url=True,
                recipient_id=phone_number
            )

