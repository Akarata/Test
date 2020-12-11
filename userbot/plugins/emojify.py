"""
Created by @Jisan7509
Peru helper @mrconfused
Userbot plugin for CatUserbot
"""
from userbot import CMD_HELP
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd

from . import *


@bot.on(admin_cmd(pattern="emoji(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="emoji(?: |$)(.*)", allow_sudo=True))
async def itachi(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(
            event, "`What am I Supposed to do with this nibba/nibbi, Give me a text. `"
        )
        return
    string = "  ".join(args).lower()
    for chutiya in string:
        if chutiya in emojify.kakashitext:
            bsdk = emojify.kakashiemoji[emojify.kakashitext.index(chutiya)]
            string = string.replace(chutiya, bsdk)
    await edit_or_reply(event, string)


@bot.on(admin_cmd(pattern="cmoji(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="cmoji(?: |$)(.*)", allow_sudo=True))
async def itachi(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(
            event, "`What am I Supposed to do with this nibba/nibbi, Give me a text. `"
        )
        return
    emoji, args = args.split(" ", 1)
    string = "  ".join(args).lower()
    for chutiya in string:
        if chutiya in emojify.kakashitext:
            bsdk = emojify.itachiemoji[emojify.kakashitext.index(chutiya)].format(
                cj=emoji
            )
            string = string.replace(chutiya, bsdk)
    await edit_or_reply(event, string)


CMD_HELP.update(
    {
        "emojify": "__**NAMA PLUGIN :** Emojify__\
      \n\n✅** CMD ➥** `.emoji` <teks>\
      \n**Fungsi   ➥  **Ubah teks Anda menjadi teks emoji besar, dengan emoji default. \
      \n\n✅** CMD ➥** `.cmoji` <emoji> <teks>\
      \n**Fungsi   ➥  **Ubah teks Anda menjadi teks emoji besar, dengan emoji khusus Anda.\
      \n\n**☞ NOTE :** Untuk memberi jarak antara dua kata, gunakan **@** simbol.\
      \n**CONTOH :**  `.emoji Akarata@Jisoo`\
      \n                    `.cmoji 💖 Akarata@Jichu`"
    }
)
