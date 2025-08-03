from telegram import Update
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext):
    user = update.message.from_user
    update.message.reply_text(
        f'Assalomu alaykum! Botimizga xush kelibsiz {user.full_name}.\n\n'
        'Bu bot testing uchun ishlayapti.'
    )


def help(update: Update, context: CallbackContext):
    update.message.reply_text('Qanday yordam kerak?')


def echo(update: Update, context: CallbackContext):
    message = update.message

    if message.text:
        message.reply_text(f"{message.text}")

    elif message.contact:
        message.reply_contact(
            phone_number=message.contact.phone_number,
            first_name=message.contact.first_name
        )

    elif message.sticker:
        message.reply_sticker(sticker=message.sticker.file_id)

    elif message.dice:
        message.reply_dice(emoji=message.dice.emoji)

    elif message.photo:
        message.reply_photo(photo=message.photo[-1].file_id, caption="Rasm qabul qilindi.")

    elif message.video:
        message.reply_video(video=message.video.file_id, caption="Video qabul qilindi.")

    elif message.audio:
        message.reply_audio(audio=message.audio.file_id, caption="Audio qabul qilindi.")

    elif message.voice:
        message.reply_voice(voice=message.voice.file_id, caption="Ovozli xabar qabul qilindi.")

    else:
        message.reply_text("Bu turdagi xabarni hali echo qila olmayman.")
