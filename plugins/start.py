from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/ArshadTheKing")]

        [InlineKeyboardButton(
            "Report Bugs 📤", url="https://t.me/MrUnknown_hacker")]
    ])
    welcomed = f"Hey<b>{message.from_user.first_name}</b>\nSend Me A YouTube Link To Download\n\nRegards @ArshadTheKing"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
