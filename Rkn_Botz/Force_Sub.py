# AutoCaptionBot by RknDeveloper

from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram.errors import UserNotParticipant
from config import Rkn_Botz
from .database import rkn_botz

# ✅ Proper async filter function
async def force_sub_filter(_, client: Client, message: Message):

    user_id = message.from_user.id

    # register user
    await rkn_botz.register_user(user_id)

    channel = Rkn_Botz.FORCE_SUB

    if not channel:
        return False

    try:
        member = await client.get_chat_member(channel, user_id)

        if member.status in [
            enums.ChatMemberStatus.LEFT,
            enums.ChatMemberStatus.BANNED
        ]:
            return True

        return False

    except UserNotParticipant:
        return True

    except Exception:
        return False


# ✅ Create filter correctly
ForceSub = filters.create(
    force_sub_filter,
    name="ForceSub"
)


# ✅ Handler
@Client.on_message(filters.private & ForceSub)
async def handle_force_sub(client: Client, message: Message):

    user_id = message.from_user.id
    channel = Rkn_Botz.FORCE_SUB

    chat_link = f"https://t.me/{channel.lstrip('@')}"

    button = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🔔 Join Update Channel",
                    url=chat_link
                )
            ]
        ]
    )

    try:
        member = await client.get_chat_member(channel, user_id)

        if member.status == enums.ChatMemberStatus.BANNED:
            return await message.reply_text(
                "**🚫 You are banned from using this bot.**"
            )

    except UserNotParticipant:
        pass

    except Exception as e:
        return await message.reply_text(
            f"⚠️ Error: `{e}`"
        )

    return await message.reply_text(
        "**🔐 Please join our updates channel to use this bot.**",
        reply_markup=button
    )
