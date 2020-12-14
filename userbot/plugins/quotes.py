# inspired from uniborg Quotes plugin
import random

import requests

from ..utils import admin_cmd, sudo_cmd
from . import CMD_HELP


@bot.on(admin_cmd(pattern="quote ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="quote ?(.*)", allow_sudo=True))
async def quote_search(event):
    if event.fwd_from:
        return
    catevent = await edit_or_reply(event, "`Tunggu beberapa saat...`")
    input_str = event.pattern_match.group(1)
    if not input_str:
        api_url = "https://quotes.cwprojects.live/random"
        try:
            response = requests.get(api_url).json()
        except:
            response = None
    else:
        api_url = f"https://quotes.cwprojects.live/search/query={input_str}"
        try:
            response = random.choice(requests.get(api_url).json())
        except:
            response = None
    if response is not None:
        await catevent.edit(f"`{response['text']}`")
    else:
        await edit_delete(catevent, "`Maaf Tidak ada hasil yang ditemukan`", 5)


CMD_HELP.update(
    {
        "quotes": "__**NAMA PLUGIN :** Quotes__\
    \n\n✅** CMD ➥** `.quote` <category>\
    \n**Fungsi   ➥  **__Api yang Mengambil Kutipan acak dari `goodreads.com`__\
    "
    }
)
