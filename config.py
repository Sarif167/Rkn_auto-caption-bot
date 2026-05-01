# AutoCaptionBot by RknDeveloper
# Copyright (c) 2024 RknDeveloper
# Licensed under the MIT License
# https://github.com/RknDeveloper/Rkn-AutoCaptionBot/blob/main/LICENSE
# Please retain this credit when using or forking this code.

# Developer Contacts:
# Telegram: @RknDeveloperr
# Updates Channel: @Rkn_Bots_Updates & @Rkn_Botz
# Special Thanks To: @ReshamOwner
# Update Channels: @Digital_Botz & @DigitalBotz_Support

# ⚠️ Please do not remove this credit!

import os
import time

class Rkn_Botz(object):

    # Rkn client config (required)
    API_ID = int(os.environ.get("API_ID", "23621595"))
    API_HASH = os.environ.get(
        "API_HASH",
        "de904be2b4cd4efe2ea728ded17ca77d"
    )
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    # Start pic (default image link)
    RKN_PIC = os.environ.get(
        "RKN_PIC",
        "https://image.zaw-myo.workers.dev/image/c6a08278-321f-4f4f-84f2-2aa14ba31000"
    )

    # Bot uptime (start time)
    BOT_UPTIME = time.time()

    # Server port (default 8080)
    PORT = int(os.environ.get("PORT", "8080"))

    # Force subscribe channel username
    FORCE_SUB = os.environ.get(
        "FORCE_SUB",
        "Prime_Movie_YT_Group"
    )

    # Database config (required)
    DB_NAME = os.environ.get(
        "DB_NAME",
        "AutoCaption_V05_Bot"
    )

    DB_URL = os.environ.get(
        "DB_URL",
        "mongodb+srv://wajsarif461_db_user:TwacJh76mwpHHpjw@cluster0.biueyst.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    )

    # Default caption
    DEFAULT_CAPTION = os.environ.get(
        "DEFAULT_CAPTION",
        "<b><a href='https://t.me/Prime_Movie_YT_Group'>{file_name} Main Telegram Channel: @Prime_Movie_YT_Group</a></b>"
    )

    # Sticker ID
    STICKER_ID = os.environ.get(
        "STICKER_ID",
        "CAACAgIAAxkBAAELFqBllhB70i13m-woXeIWDXU6BD2j7wAC9gcAAkb7rAR7xdjVOS5ziTQE"
    )

    # Admin IDs Fix
    ADMINS = os.environ.get("ADMINS", "1249672673")
    ADMIN = [int(admin) for admin in ADMINS.split()]

# ——————————————————————————
# End of file
# Original author: @RknDeveloperr
# GitHub: https://github.com/RknDeveloper

# Developer Contacts:
# Telegram: @RknDeveloperr
# Updates Channel: @Rkn_Bots_Updates & @Rkn_Botz
# Special Thanks To: @ReshamOwner
# Update Channels: @Digital_Botz & @DigitalBotz_Support

# ⚠️ Please do not remove this credit!
