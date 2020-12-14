# Thumbnail Utilities ported from uniborg
# credits @spechide

import os

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from PIL import Image

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import CMD_HELP, take_screen_shot

thumb_image_path = Config.TMP_DOWNLOAD_DIRECTORY + "/thumb_image.jpg"


@bot.on(admin_cmd(pattern="savethumb$"))
@bot.on(sudo_cmd(pattern="savethumb$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    catevent = await edit_or_reply(event, "Processing ...")
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if event.reply_to_msg_id:
        downloaded_file_name = await event.client.download_media(
            await event.get_reply_message(), Config.TMP_DOWNLOAD_DIRECTORY
        )
        if downloaded_file_name.endswith(".mp4"):
            metadata = extractMetadata(createParser(downloaded_file_name))
            if metadata and metadata.has("duration"):
                duration = metadata.get("duration").seconds
            downloaded_file_name = await take_screen_shot(
                downloaded_file_name, duration
            )
        # https://stackoverflow.com/a/21669827/4723940
        Image.open(downloaded_file_name).convert("RGB").save(thumb_image_path, "JPEG")
        # https://pillow.readthedocs.io/en/3.1.x/reference/Image.html#create-thumbnails
        os.remove(downloaded_file_name)
        await catevent.edit(
            "Thumbnail video / file kustom disimpan.  Gambar ini akan digunakan dalam unggahan, sampai `.clearthumb`."
        )
    else:
        await catevent.edit("Reply to a photo to save custom thumbnail")


@bot.on(admin_cmd(pattern="clearthumb$"))
@bot.on(sudo_cmd(pattern="clearthumb$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if os.path.exists(thumb_image_path):
        os.remove(thumb_image_path)
    else:
        await edit_or_reply(event, "No thumbnail is setted to clear")
    await edit_or_reply(event, "✅ Thumbnail kustom berhasil dihapus.")


@bot.on(admin_cmd(pattern="getthumb$"))
@bot.on(sudo_cmd(pattern="getthumb$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        r = await event.get_reply_message()
        try:
            a = await r.download_media(thumb=-1)
        except Exception as e:
            await edit_or_reply(event, str(e))
            return
        try:
            await event.client.send_file(
                event.chat_id,
                a,
                force_document=False,
                allow_cache=False,
                reply_to=event.reply_to_msg_id,
            )
            os.remove(a)
            await event.delete()
        except Exception as e:
            await edit_or_reply(event, str(e))
    elif os.path.exists(thumb_image_path):
        caption_str = "Currently Saved Thumbnail"
        await event.client.send_file(
            event.chat_id,
            thumb_image_path,
            caption=caption_str,
            force_document=False,
            allow_cache=False,
            reply_to=event.message.id,
        )
        await edit_or_reply(event, caption_str)
    else:
        await edit_or_reply(event, "Reply `.gethumbnail` as a reply to a media")


CMD_HELP.update(
    {
        "thumbnail": "__**NAMA PLUGIN :** Thumbnail__\
    \n\n✅** CMD ➥** `.savethumb`\
    \n**Fungsi   ➥  **Balas file atau video untuk menyimpannya sebagai thumbnail sementara\
    \n\n✅** CMD ➥** `.clearthumb`\
    \n**Fungsi   ➥  **Untuk menghapus Thumbnail, Anda tidak lagi mengupload menggunakan thumbnail kustom\
    \n\n✅** CMD ➥** `.getthumb`\
    \n**Fungsi   ➥  **Untuk mendapatkan thumbnail dari video tertentu atau memberikan thumbnail Anda saat ini\
    "
    }
)
