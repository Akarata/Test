import sys
from os import execl
from time import sleep

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import BOTLOG, BOTLOG_CHATID, CMD_HELP, HEROKU_APP, bot


@bot.on(admin_cmd(pattern="restart$"))
@bot.on(sudo_cmd(pattern="restart$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if BOTLOG:
        await event.client.send_message(BOTLOG_CHATID, "#RESTART \n" "Bot Restarted")
    await edit_or_reply(
        event,
        "Dimulai kembali. `.ping` atau `.help` untuk mengecek apakah aku online, sebenarnya butuh 1-2 menit untuk restart",
    )
    await bot.disconnect()
    execl(sys.executable, sys.executable, *sys.argv)


@bot.on(admin_cmd(pattern="shutdown$"))
@bot.on(sudo_cmd(pattern="shutdown$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if HEROKU_APP is not None:
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID, "#SHUTDOWN \n" "Bot shut down"
            )
        await edit_or_reply(event, "`Turning off bot now ...Manually turn me on later`")
        HEROKU_APP.process_formation()["userbot"].scale(0)
    else:
        await edit_or_reply(
            event,
            "`Set HEROKU_APP_NAME and HEROKU_API_KEY to work this function properly`",
        )
        await bot.disconnect()


@bot.on(admin_cmd(pattern="sleep( [0-9]+)?$"))
@bot.on(sudo_cmd(pattern="sleep( [0-9]+)?$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if " " not in event.pattern_match.group(1):
        return await edit_or_reply(event, "Syntax: `.sleep time`")
    counter = int(event.pattern_match.group(1))
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "Anda meletakkan bot untuk tidur " + str(counter) + " detik",
        )
    event = await edit_or_reply(event, f"`ok, biarkan aku tidur {counter} detik`")
    sleep(counter)
    await event.edit("`Oke, aku sudah bangun sekarang.`")


CMD_HELP.update(
    {
        "power_tools": "**Plugin : **`power_tools`\
                \n\n**Syntax : **`.restart`\
                \n**Fungsi : **Mulai ulang bot !!\
                \n\n**Syntax : **'.sleep <detik>\
                \n**Fungsi: **Userbots juga lelah.  Biarkan punyamu tertidur selama beberapa detik.\
                \n\n**Syntax : **`.shutdown`\
                \n**Fungsi : **Untuk mematikan dyno heroku.  Anda tidak dapat mengaktifkan bot, Anda harus mengakses heroku dan mengaktifkan atau menggunakan @hk_heroku_bot"
    }
)
