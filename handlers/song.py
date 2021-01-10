from pyrogram import filters
from pyrogram.handlers import MessageHandler
import player
from strings import get_string as _


async def song(client, message):
    if message.from_user.id == 981781935:
        return
    get = player.currently_playing()
    if get:
        await message.reply_text(
            _("song").format(
                "<a href=\"{}\">{}</a>".format(
                    get["url"],
                    get["title"]
                ),
                "<a href=\"tg://user?id={}\">{}</a>".format(
                    get["sent_by_id"],
                    get["sent_by_name"]
                ),
            ),
            parse_mode="HTML"
        )
    else:
        await message.reply_text(
            _("no_song_playing")
        )

__handlers__ = [
    [
        MessageHandler(
            song,
            filters.command("song", "/")
            & filters.private
        )
    ]
]
