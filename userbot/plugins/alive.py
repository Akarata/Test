import time
from platform import python_version

from telethon import version

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import CMD_HELP, StartTime, catdef, catversion, hmention, mention

CAT_IMG = Config.ALIVE_PIC
JISAN = (
    str(Config.CUSTOM_ALIVE_TEXT)
    if Config.CUSTOM_ALIVE_TEXT
    else "✘   I'm Alive,  Master   ✘"
)


@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = alive.message
    uptime = await catdef.get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    if alive.reply_to_msg_id:
        reply_to_id = await alive.get_reply_message()
    if CAT_IMG:
        cat_caption = f"<b>{JISAN}</b>\n\n"
        cat_caption += f"<b> ✘   [   👤   ]    My Master : {hmention}</b>\n"
        cat_caption += f"<b> ✘   [   ⏱️   ]    Bot Uptime :</b> <code>{uptime}</code>\n"
        cat_caption += (
            f"<b> ✘   [   🐍   ]    Python :</b> <code>{python_version()}</code>\n"
        )
        cat_caption += (
            f"<b> ✘   [   ⚙️   ]    Telethon :</b> <code>{version.__version__}</code>\n"
        )
        cat_caption += (
            f"<b> ✘   [   🤖   ]    Aka Version :</b> <code>{catversion}</code>\n"
        )
        cat_caption += f"<b> ✘   [   ⚔️   ]    Running on :</b> <code>Master</code>\n"

        await alive.client.send_file(
            alive.chat_id,
            CAT_IMG,
            caption=cat_caption,
            parse_mode="html",
            reply_to=reply_to_id,
            link_preview=False,
            allow_cache=True,
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"<b>{JISAN}</b>\n\n"
            f"<b> »» [👤] ➥ My Master : {hmention}</b>\n"
            f"<b> »» [🕒] ➥ Uptime :</b> <code>{uptime}</code>\n"
            f"<b> »» [🐍] ➥ Python :</b> <code>{python_version()}</code>\n"
            f"<b> »» [⚙️] ➥ Telethon :</b> <code>{version.__version__}</code>\n"
            f"<b> »» [🤖] ➥ Bot :</b> <code>{catversion}</code>\n",
        )


@bot.on(admin_cmd(outgoing=True, pattern="ialive$"))
@bot.on(sudo_cmd(pattern="ialive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    tgbotusername = Var.TG_BOT_USER_NAME_BF_HER
    reply_to_id = alive.message
    if alive.reply_to_msg_id:
        reply_to_id = await alive.get_reply_message()
    cat_caption = f"**Catuserbot is Up and Running**\n"
    cat_caption += f"**  -Master :** {mention}\n"
    cat_caption += f"**  -Python Version :** `{python_version()}\n`"
    cat_caption += f"**  -Telethon version :** `{version.__version__}\n`"
    cat_caption += f"**  -Catuserbot Version :** `{catversion}`\n"
    results = await bot.inline_query(tgbotusername, cat_caption)  # pylint:disable=E0602
    await results[0].click(alive.chat_id, reply_to=reply_to_id, hide_via=True)
    await alive.delete()


# UniBorg Telegram UseRBot
# Copyright (C) 2020 @UniBorg
# This code is licensed under
# the "you can't use this for anything - public or private,
# unless you know the two prime factors to the number below" license
# 543935563961418342898620676239017231876605452284544942043082635399903451854594062955
# വിവരണം അടിച്ചുമാറ്റിക്കൊണ്ട് പോകുന്നവർ
# ക്രെഡിറ്റ് വെച്ചാൽ സന്തോഷമേ ഉള്ളു..!
# uniborg


def check_data_base_heal_th():
    # https://stackoverflow.com/a/41961968
    is_database_working = False
    output = "No Database is set"
    if not Config.DB_URI:
        return is_database_working, output
    from userbot.plugins.sql_helper import SESSION

    try:
        # to check database we will execute raw query
        SESSION.execute("SELECT 1")
    except Exception as e:
        output = f"❌ {str(e)}"
        is_database_working = False
    else:
        output = "Functioning"
        is_database_working = True
    return is_database_working, output


CMD_HELP.update(
    {
        "alive": "__**NAMA PLUGIN :** Alive__\
      \n\n✅** CMD ➥** `.alive`\
      \n**Fungsi   ➥  **Untuk melihat apakah bot Anda berfungsi atau tidak.\
      \n\n✅** CMD ➥** `.ialive`\
      \n**Fungsi   ➥  **__Status bot akan ditampilkan dalam mode inline dengan button__."
    }
)
