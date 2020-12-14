# created by @eve_enryu
# edited & fix by @Jisan7509


from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import CMD_HELP


@bot.on(admin_cmd(pattern="firmware(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="firmware(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    firmware = f"firmware"
    catevent = await edit_or_reply(event, "```Processing```")
    async with event.client.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{firmware} {link}")
            respond = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("```Unblock @XiaomiGeeksBot plox```")
            return
        else:
            await catevent.delete()
            await event.client.forward_messages(event.chat_id, respond.message)


@bot.on(admin_cmd(pattern="vendor(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="vendor(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    vendor = f"vendor"
    catevent = await edit_or_reply(event, "```Processing```")
    async with event.client.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{vendor} {link}")
            respond = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("```Unblock @XiaomiGeeksBot plox```")
            return
        else:
            await catevent.delete()
            await event.client.forward_messages(event.chat_id, respond.message)


@bot.on(admin_cmd(pattern="specs(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="specs(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    specs = f"specs"
    catevent = await edit_or_reply(event, "```Processing```")
    async with event.client.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{specs} {link}")
            respond = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("```Unblock @XiaomiGeeksBot plox```")
            return
        else:
            await catevent.delete()
            await event.client.forward_messages(event.chat_id, respond.message)


@bot.on(admin_cmd(pattern="fastboot(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="fastboot(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    fboot = f"fastboot"
    catevent = await edit_or_reply(event, "```Processing```")
    async with event.client.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{fboot} {link}")
            respond = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("```Unblock @XiaomiGeeksBot plox```")
            return
        else:
            await catevent.delete()
            await event.client.forward_messages(event.chat_id, respond.message)


@bot.on(admin_cmd(pattern="recovery(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="recovery(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    recovery = f"recovery"
    catevent = await edit_or_reply(event, "```Processing```")
    async with event.client.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{recovery} {link}")
            respond = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("```Unblock @XiaomiGeeksBot plox```")
            return
        else:
            await catevent.delete()
            await event.client.forward_messages(event.chat_id, respond.message)


@bot.on(admin_cmd(pattern="pb(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="pb(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    pitch = f"pb"
    catevent = await edit_or_reply(event, "```Processing```")
    async with event.client.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{pitch} {link}")
            respond = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("```Unblock @XiaomiGeeksBot plox```")
            return
        else:
            await catevent.delete()
            await event.client.forward_messages(event.chat_id, respond.message)


@bot.on(admin_cmd(pattern="of(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="of(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    ofox = f"of"
    catevent = await edit_or_reply(event, "```Processing```")
    async with event.client.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{ofox} {link}")
            respond = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("```Unblock @XiaomiGeeksBot plox```")
            return
        else:
            await catevent.delete()
            await event.client.forward_messages(event.chat_id, respond.message)


CMD_HELP.update(
    {
        "xiaomi": "__**NAMA PLUGIN :** Xiaomi__\
        \n\n__**hanya untuk perangkat xiaomi !**__\
\n\n✅** CMD ➥** `.firmware` (nama kode)\
\n**Fungsi   ➥  **Dapatkan Firmware terbaru\
\n\n✅** CMD ➥** `.vendor` (nama kode)\
\n**Fungsi   ➥  **Dapatkan Vendor terbaru\
\n\n✅** CMD ➥** `.pb` (nama kode)\
\n**Fungsi   ➥  **Dapatkan PBRP terbaru\
\n\n✅** CMD ➥** `.specs` (nama kode)\
\n**Fungsi   ➥  **Dapatkan informasi spesifikasi cepat tentang perangkat\
\n\n✅** CMD ➥** `.fastboot` (nama kode)\
\n**Fungsi   ➥  **Dapatkan MIUI fastboot terbaru\
\n\n✅** CMD ➥** `.recovery` (nama kode)\
\n**Fungsi   ➥  **Dapatkan MIUI pemulihan terbaru\
\n\n✅** CMD ➥** `.of` (nama kode)\
\n**Fungsi   ➥  **Dapatkan Pemulihan ORangeFox terbaru"
    }
)
