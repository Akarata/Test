""".admin Plugin for @UniBorg"""
import html

import userbot.plugins.sql_helper.warns_sql as sql

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import CMD_HELP


@bot.on(admin_cmd(pattern="warn (.*)"))
@bot.on(sudo_cmd(pattern="warn (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    warn_reason = event.pattern_match.group(1)
    if not warn_reason:
        warn_reason = "No reason"
    reply_message = await event.get_reply_message()
    limit, soft_warn = sql.get_warn_setting(event.chat_id)
    num_warns, reasons = sql.warn_user(
        reply_message.sender_id, event.chat_id, warn_reason
    )
    if num_warns >= limit:
        sql.reset_warns(reply_message.sender_id, event.chat_id)
        if soft_warn:
            logger.info("TODO: kick user")
            reply = "{} warnings, [user](tg://user?id={}) has to bee kicked!".format(
                limit, reply_message.sender_id
            )
        else:
            logger.info("TODO: ban user")
            reply = "{} warnings, [user](tg://user?id={}) has to bee banned!".format(
                limit, reply_message.sender_id
            )
    else:
        reply = "[user](tg://user?id={}) has {}/{} warnings... watch out!".format(
            reply_message.sender_id, num_warns, limit
        )
        if warn_reason:
            reply += "\nReason for last warn:\n{}".format(html.escape(warn_reason))
    await edit_or_reply(event, reply)


@bot.on(admin_cmd(pattern="warns$"))
@bot.on(sudo_cmd(pattern="warns$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    result = sql.get_warns(reply_message.sender_id, event.chat_id)
    if result and result[0] != 0:
        num_warns, reasons = result
        limit, soft_warn = sql.get_warn_setting(event.chat_id)
        if reasons:
            text = "This user has {}/{} warnings, for the following reasons:".format(
                num_warns, limit
            )
            text += "\r\n"
            text += reasons
            await event.edit(text)
        else:
            await edit_or_reply(
                event,
                "this user has {} / {} warning, but no reasons for any of them.".format(
                    num_warns, limit
                ),
            )
    else:
        await edit_or_reply(event, "this user hasn't got any warnings!")


@bot.on(admin_cmd(pattern="resetwarns$"))
@bot.on(sudo_cmd(pattern="resetwarns$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    sql.reset_warns(reply_message.sender_id, event.chat_id)
    await edit_or_reply(event, "Warnings have been reset!")


CMD_HELP.update(
    {
        "warns": "__**NAMA PLUGIN :** Warns__\
      \n\n✅** CMD ➥** `.warn` <alasan> <balas ke pengguna>\
      \n**Fungsi   ➥  **__Memperingatkan pengguna tertentu dalam obrolan yang Anda gunakan__\
      \n\n✅** CMD ➥** `.warns` <balas>\
      \n**Fungsi   ➥  **__Mendapat peringatan dari pengguna tertentu dalam obrolan yang Anda gunakan__\
      \n\n✅** CMD ➥** `.resetwarns` <balas>\
      \n**Fungsi   ➥  **__Menyetel ulang peringatan dari pengguna yang menjawab di obrolan tempat Anda menggunakan perintah__"
    }
)
