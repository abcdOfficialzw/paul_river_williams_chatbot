import logging
import os

from dotenv import load_dotenv
from heyoo import WhatsApp

greetings = ['hie',
             'hey',
             'hi',
             'yoh',
             'wassup',
             'hello',
             'how are you',
             'good morning',
             'good afternoon',
             'good evening',
             'morning',
             'afternoon',
             'evening']
# Load .env file
load_dotenv()
messenger = WhatsApp(os.getenv("TOKEN"), phone_number_id=os.getenv("PHONE_NUMBER_ID"))
# Logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


def handle_text_message(message: str, name: str, mobile: str):
    if message.lower() in greetings:
        logging.info("Message is a greeting: %s", message)

        messenger.send_button(
            recipient_id=mobile,
            button={
                "header": "Paul River Williams",
                "body": f"Hie {name}👋🏾, how may I assist you today?",
                "footer": "Consultancy Services",
                "action": {
                    "button": "Menu",
                    "sections": [
                        {
                            "title": " ",
                            "rows": [
                                {
                                    "id": "who_am_i",
                                    "title": "Who am I?",
                                    "description": "Find out who Paul is and how I can help you"
                                },
                                {
                                    "id": "how_i_can_solve_your_problem",
                                    "title": "Have a problem?",
                                    "description": "Do you have a complex problem that you need help solving?",
                                },
                                {
                                    "id": "book_a_chat_with_me",
                                    "title": "Want to chat with me?",
                                    "description": "Let's sit down and chat while we sip coffee"
                                },

                            ],
                        },
                        {
                            "title": "Connect with me",
                            "rows": [

                                {
                                    "id": "twitter",
                                    "title": "X(formerly Twitter)",
                                    "description": "@the_tent_maker",
                                },
                                {
                                    "id": "tiktok",
                                    "title": "TikTok",
                                    "description": "@paul_charming",
                                },

                            ],
                        },
                        # {
                        #     "title": "My Services",
                        #     "rows": [
                        #         {"id": "mobile_apps", "title": "Mobile Apps", "description": "I develop mobile applications for both Android and iOS."},
                        #         {
                        #             "id": "chatbots",
                        #             "title": "WhatsApp Chatbots",
                        #             "description": "I develop fast, interactive whatsapp chatbots",
                        #         },
                        #
                        #     ],
                        # }
                    ],
                },
            }
        )
