# credits to @mrconfused (@sandy1709)
import io
import os

import lyricsgenius
from tswift import Song

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import CMD_HELP

GENIUS = os.environ.get("GENIUS_API_TOKEN", None)


@bot.on(admin_cmd(outgoing=True, pattern="lirik ?(.*)"))
@bot.on(sudo_cmd(allow_sudo=True, pattern="lirik ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    catevent = await edit_or_reply(event, "Sedang mencari lirik....`")
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
    elif reply.text:
        query = reply.message
    else:
        await catevent.edit("`Apa yang Seharusnya saya temukan `")
        return
    song = ""
    song = Song.find_song(query)
    if song:
        if song.lyrics:
            reply = song.format()
        else:
            reply = "Tidak dapat menemukan lirik apa pun untuk lagu itu!  coba dengan nama artis beserta lagunya jika masih tidak berhasil coba `.glyrics`"
    else:
        reply = "lirik tidak ditemukan!  coba dengan nama artis beserta lagunya jika masih tidak berhasil coba `.glyrics`"
    if len(reply) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(reply)) as out_file:
            out_file.name = "lyrics.text"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=query,
                reply_to=reply_to_id,
            )
            await catevent.delete()
    else:
        await catevent.edit(reply)


@bot.on(admin_cmd(outgoing=True, pattern="glirik ?(.*)"))
@bot.on(sudo_cmd(allow_sudo=True, pattern="glirik ?(.*)"))
async def lyrics(lyric):
    if lyric.pattern_match.group(1):
        query = lyric.pattern_match.group(1)
    else:
        await edit_or_reply(
            lyric,
            "Error: mohon gunakan '-' sebagai pembatas untuk <artis> dan <lagu> \neg: `.glyrics Blackpink - Lovesick Girls`",
        )
        return
    if r"-" not in query:
        await edit_or_reply(
            lyric,
            "Error: mohon gunakan '-' sebagai pembatas untuk <artis> dan <lagu> \neg: `.glyrics Blackpink - Lovesick Girls`",
        )
        return
    if GENIUS is None:
        await edit_or_reply(
            lyric,
            "`Berikan token akses genius ke config.py atau Heroku Var terlebih dahulu`",
        )
    else:
        genius = lyricsgenius.Genius(GENIUS)
        try:
            args = query.split("-", 1)
            artist = args[0].strip(" ")
            song = args[1].strip(" ")
        except Exception as e:
            await edit_or_reply(lyric, f"Error:\n`{e}`")
            return
    if len(args) < 1:
        await edit_or_reply(lyric, "`Sebutkan nama artis dan lagu`")
        return
    catevent = await edit_or_reply(
        lyric, f"`Mencari lirik {artist} - {song}...`"
    )
    try:
        songs = genius.search_song(song, artist)
    except TypeError:
        songs = None
    if songs is None:
        await catevent.edit(f"lagu **{artist} - {song}** tidak ditemukan!")
        return
    if len(songs.lyrics) > 4096:
        await catevent.edit("`Lirik terlalu besar, lihat file untuk melihatnya.`")
        with open("lyrics.txt", "w+") as f:
            f.write(suran: \n{artist} - {song}\n\n{songs.lyrics}")
        await lyric.client.send_file(
            lyric.chat_id,
            "lyrics.txt",
            reply_to=lyric.id,
        )
        os.remove("lyrics.txt")
    else:
        await catevent.edit(
            f"**Kueri penelusuran**: \n`{artist} - {song}`\n\n```{songs.lyrics}```"
        )
    return


CMD_HELP.update(
    {
        "lirik": "__**NAMA PLUGIN :** Lirik__\
    \n\n✅** CMD ➥** `.lirik` <nama artis - nama lagu> atau `.lyrics` <nama_lagu>\
    \n**Fungsi   ➥  **Mencari lirik lagu dan mengirimi Anda jika nama lagu tidak berfungsi, coba bersama dengan nama artis\
    \n\n✅** CMD ➥** `.glirik <nama artis - nama lagu>`\
    \n**Fungsi   ➥  **Mencari lirik lagu dan mengirim Anda.\
    \n__**Note**__: **-** diperlukan saat mencari lirik untuk artis dan lagu yang dibagi\
    \n\n**Plugin lirik Genius**\
    \ndapatkan nilai ini dari [Sini](https://genius.com/developers)\
    \nTambahkan var `GENIUS_API_TOKEN` dan nilai token di setelan aplikasi heroku."
    }
)
