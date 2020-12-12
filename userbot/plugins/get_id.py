from telethon.utils import pack_bot_file_id

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import CMD_HELP


@bot.on(admin_cmd(pattern="(get_id|id)( (.*)|$)"))
@bot.on(sudo_cmd(pattern="(get_id|id)( (.*)|$)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(2)
    if input_str:
        try:
            p = await event.client.get_entity(input_str)
        except Exception as e:
            return await edit_delete(event, f"`{str(e)}`", 5)
        try:
            if p.first_name:
                return await edit_or_reply(
                    event, f"ID pengguna `{input_str}` adalah `{p.id}`"
                )
        except:
            try:
                if p.title:
                    return await edit_or_reply(
                        event, f"ID obrolan / saluran `{p.title}` adalah `{p.id}`"
                    )
            except:
                pass
        await edit_or_reply(
            event, "`Berikan masukan sebagai nama pengguna atau balas ke pengguna`"
        )
    elif event.reply_to_msg_id:
        await event.get_input_chat()
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await edit_or_reply(
                event,
                f"**ID Obrolan Saat Ini : **`{str(event.chat_id)}`\n**Dari User ID: **`{str(r_msg.sender_id)}`\n**ID File Media: **`{bot_api_file_id}`",
            )
        else:
            await edit_or_reply(
                event,
                f"**ID Obrolan Saat Ini : **`{str(event.chat_id)}`\n**Dari User ID: **`{str(r_msg.sender_id)}`",
            )
    else:
        await edit_or_reply(event, f"**ID Obrolan Saat Ini : **`{str(event.chat_id)}`")


CMD_HELP.update(
    {
        "get_id": "__**NAMA PLUGIN :** Get_id__\
    \n\n✅** CMD ➥** `.get_id` atau `.id` <balas di pesan user>\
    \n**Fungsi   ➥  **__Jika diberi masukan maka tunjukkan id dari obrolan / saluran / pengguna yang diberikan lain jika Anda membalas ke pengguna maka tunjukkan id dari pengguna yang menjawab \
    bersama dengan id obrolan saat ini dan jika tidak dibalas ke pengguna atau diberi masukan maka cukup tampilkan id obrolan di mana Anda menggunakan perintah__"
    }
)
