import os

from flask import Flask, request, make_response
from heyoo import WhatsApp
from dotenv import load_dotenv
import logging

import require_token
from messaging.interactive_messages import handle_interactive_message
from messaging.text_message import handle_text_message

app = Flask(__name__)

# Load .env file
load_dotenv()
messenger = WhatsApp(os.getenv("TOKEN"), phone_number_id=os.getenv("PHONE_NUMBER_ID"))

# Logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


@app.route('/')
def hello_world():  # put application's code here


    # media_id = messenger.upload_media(
    #     media="/Users/titus/projects/paul_river_willims_chatbot/assets/paul_intro_video.mp4",
    # )
    # print(f"media id is {media_id}")








    resp = messenger.send_button(
        recipient_id="263776392244",
        button={
            "header": "Takudzwa Nyanhanga",
            "body": "How may I assist you today?",
            "footer": "Software Company",
            "action": {
                "button": "Menu",
                "sections": [
                    {
                        "title": "Services",
                        "rows": [
                            {"id": "row 1", "title": "Mobile Apps",
                             "description": "Development of a mobile application for both Android and Ios"},
                            {
                                "id": "row 2",
                                "title": "Whatsapp chatbot",
                                "description": "Development of a whatsapp chatbot",
                            },
                        ],
                    }
                ],
            },
        },
    )
    print(resp)
    return 'Hello World!'


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    changed_field = messenger.changed_field(data)
    if changed_field == "messages":
        new_message = messenger.is_message(data)
        if new_message:
            mobile = messenger.get_mobile(data)
            name = messenger.get_name(data)
            message_type = messenger.get_message_type(data)
            logging.info(
                f"New Message; sender:{mobile} name:{name} type:{message_type}"
            )
            if message_type == "text":
                message = messenger.get_message(data)
                name = messenger.get_name(data)
                logging.info("Message: %s", message)
                handle_text_message(
                    message=message, name=name, mobile=mobile
                )

                # messenger.send_message(f"Hi {name}, nice to connect with you", mobile)

            elif message_type == "interactive":
                message_response = messenger.get_interactive_response(data)
                interactive_type = message_response.get("type")
                message_id = message_response[interactive_type]["id"]
                message_text = message_response[interactive_type]["title"]
                logging.info(f"Interactive Message; {message_id}: {message_text}")

                logging.info(f"Messaging object: {message_response}")
                handle_interactive_message(
                    reply_id=message_id,
                    phone_number=mobile,
                    name=name
                )

            elif message_type == "location":
                message_location = messenger.get_location(data)
                message_latitude = message_location["latitude"]
                message_longitude = message_location["longitude"]
                logging.info("Location: %s, %s", message_latitude, message_longitude)

            elif message_type == "image":
                image = messenger.get_image(data)
                image_id, mime_type = image["id"], image["mime_type"]
                image_url = messenger.query_media_url(image_id)
                image_filename = messenger.download_media(image_url, mime_type)
                logging.info(f"{mobile} sent image {image_filename}")

            elif message_type == "video":
                video = messenger.get_video(data)
                video_id, mime_type = video["id"], video["mime_type"]
                video_url = messenger.query_media_url(video_id)
                video_filename = messenger.download_media(video_url, mime_type)
                logging.info(f"{mobile} sent video {video_filename}")

            elif message_type == "audio":
                audio = messenger.get_audio(data)
                audio_id, mime_type = audio["id"], audio["mime_type"]
                audio_url = messenger.query_media_url(audio_id)
                audio_filename = messenger.download_media(audio_url, mime_type)
                logging.info(f"{mobile} sent audio {audio_filename}")

            elif message_type == "document":
                file = messenger.get_document(data)
                file_id, mime_type = file["id"], file["mime_type"]
                file_url = messenger.query_media_url(file_id)
                file_filename = messenger.download_media(file_url, mime_type)
                logging.info(f"{mobile} sent file {file_filename}")
            else:
                logging.info(f"{mobile} sent {message_type} ")
                logging.info(data)
        else:
            delivery = messenger.get_delivery(data)
            if delivery:
                logging.info(f"Message : {delivery}")
            else:
                logging.info("No new message")
    return "OK", 200


@app.route("/webhook", methods=["GET"])
def verify_token():
    print(os.getenv("VERIFY_TOKEN"))
    if request.args.get("hub.verify_token") == os.getenv("VERIFY_TOKEN"):
        logging.info("Verified webhook")
        response = make_response(request.args.get("hub.challenge"), 200)
        response.mimetype = "text/plain"
        return response
    logging.error("Webhook Verification failed")
    return "Invalid verification token"


if __name__ == '__main__':
    app.run()
