# collage plugin for catuserbot by @sandy1709

# Copyright (C) 2020 Alfiananda P.A
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.

import os

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import CMD_HELP, make_gif, runcmd


@bot.on(admin_cmd(pattern="collage(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="collage(?: |$)(.*)", allow_sudo=True))
async def collage(cat):
    if cat.fwd_from:
        return
    catinput = cat.pattern_match.group(1)
    reply = await cat.get_reply_message()
    catid = cat.reply_to_msg_id
    cat = await edit_or_reply(
        cat,
        "```membuat kolase, ini mungkin membutuhkan waktu beberapa menit juga..... :D```",
    )
    if not (reply and (reply.media)):
        await cat.edit("`Media tidak ditemukan...`")
        return
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    catsticker = await reply.download_media(file="./temp/")
    if not catsticker.endswith((".mp4", ".mkv", ".tgs")):
        os.remove(catsticker)
        await cat.edit("`Format media tidak didukung...`")
        return
    if catinput:
        if not catinput.isdigit():
            os.remove(catsticker)
            await cat.edit("`You input is invalid, check help`")
            return
        catinput = int(catinput)
        if not 0 < catinput < 10:
            os.remove(catsticker)
            await cat.edit(
                "`Mengapa grid terlalu besar Anda tidak dapat melihat gambar, gunakan ukuran grid antara 1 hingga 9`"
            )
            return
    else:
        catinput = 3
    if catsticker.endswith(".tgs"):
        hmm = await make_gif(cat, catsticker)
        if hmm.endswith(("@tgstogifbot")):
            os.remove(catsticker)
            return await cat.edit(hmm)
        collagefile = hmm
    else:
        collagefile = catsticker
    endfile = "./temp/collage.png"
    catcmd = f"vcsi -g {catinput}x{catinput} '{collagefile}' -o {endfile}"
    stdout, stderr = (await runcmd(catcmd))[:2]
    if not os.path.exists(endfile):
        for files in (catsticker, collagefile):
            if files and os.path.exists(files):
                os.remove(files)
        return await edit_delete(
            cat,
            f"`media tidak didukung atau coba dengan ukuran kisi yang lebih kecil`",
            5,
        )
    await cat.client.send_file(
        cat.chat_id,
        endfile,
        reply_to=catid,
    )
    await cat.delete()
    for files in (catsticker, collagefile, endfile):
        if files and os.path.exists(files):
            os.remove(files)


CMD_HELP.update(
    {
        "collage": "__**NAMA PLUGIN :** Collage__\
        \n\n✅** CMD ➥** `.collage` <grid size>\
        \n**Fungsi   ➥  **__Menunjukkan gambar kisi gambar yang diekstrak dari video \n\nUkuran grid harus antara 1 sampai 9 secara default adalah 3__"
    }
)
