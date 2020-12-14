# Userbot module containing various scrapers.
# Copyright (C) 2019 The Raphielscape Company LLC.(some are ported from there)
# Copyright (c) JeepBot | 2019(for imdb)
# # kanged from Blank-x ;---;

import os
import re

import bs4
import requests
from wikipedia import summary
from wikipedia.exceptions import DisambiguationError, PageError

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import BOTLOG, BOTLOG_CHATID, CMD_HELP


@bot.on(admin_cmd(outgoing=True, pattern=r"wiki (.*)"))
@bot.on(sudo_cmd(allow_sudo=True, pattern=r"wiki (.*)"))
async def wiki(wiki_q):
    """ For .wiki command, fetch content from Wikipedia. """
    match = wiki_q.pattern_match.group(1)
    try:
        summary(match)
    except DisambiguationError as error:
        await edit_or_reply(wiki_q, f"Ditemukan halaman yang tidak ambigu.\n\n{error}")
        return
    except PageError as pageerror:
        await edit_or_reply(wiki_q, f"halaman tidak ditemukan.\n\n{pageerror}")
        return
    result = summary(match)
    if len(result) >= 4096:
        with open("output.txt", "w+") as file:
            file.write(result)
        await wiki_q.client.send_file(
            wiki_q.chat_id,
            "output.txt",
            reply_to=wiki_q.id,
            caption="`Output terlalu besar, dikirim sebagai file`",
        )
        await wiki_q.delete()
        if os.path.exists("output.txt"):
            os.remove("output.txt")
        return
    await edit_or_reply(wiki_q, "**Cari:**\n`" + match + "`\n\n**Hasil:**\n" + result)
    if BOTLOG:
        await wiki_q.client.send_message(
            BOTLOG_CHATID, f"Kueri wiki `{match}` berhasil dieksekusi"
        )


@bot.on(admin_cmd(pattern="imdb (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="imdb (.*)", allow_sudo=True))
async def imdb(e):
    catevent = await edit_or_reply(e, "`mencari........")
    try:
        movie_name = e.pattern_match.group(1)
        remove_space = movie_name.split(" ")
        final_name = "+".join(remove_space)
        page = requests.get(
            "https://www.imdb.com/find?ref_=nv_sr_fn&q=" + final_name + "&s=all"
        )
        str(page.status_code)
        soup = bs4.BeautifulSoup(page.content, "lxml")
        odds = soup.findAll("tr", "odd")
        mov_title = odds[0].findNext("td").findNext("td").text
        mov_link = (
            "http://www.imdb.com/" + odds[0].findNext("td").findNext("td").a["href"]
        )
        page1 = requests.get(mov_link)
        soup = bs4.BeautifulSoup(page1.content, "lxml")
        if soup.find("div", "poster"):
            poster = soup.find("div", "poster").img["src"]
        else:
            poster = ""
        if soup.find("div", "title_wrapper"):
            pg = soup.find("div", "title_wrapper").findNext("div").text
            mov_details = re.sub(r"\s+", " ", pg)
        else:
            mov_details = ""
        moviecredits = soup.findAll("div", "credit_summary_item")
        director = moviecredits[0].a.text
        if len(moviecredits) == 1:
            writer = "Not available"
            stars = "Not available"
        elif len(moviecredits) > 2:
            writer = moviecredits[1].a.text
            actors = [x.text for x in moviecredits[2].findAll("a")]
            actors.pop()
            stars = actors[0] + "," + actors[1] + "," + actors[2]
        else:
            writer = "Not available"
            actors = [x.text for x in moviecredits[1].findAll("a")]
            actors.pop()
            stars = actors[0] + "," + actors[1] + "," + actors[2]
        if soup.find("div", "inline canwrap"):
            story_line = soup.find("div", "inline canwrap").findAll("p")[0].text
        else:
            story_line = "Not available"
        info = soup.findAll("div", "txt-block")
        if info:
            mov_country = []
            mov_language = []
            for node in info:
                a = node.findAll("a")
                for i in a:
                    if "country_of_origin" in i["href"]:
                        mov_country.append(i.text)
                    elif "primary_language" in i["href"]:
                        mov_language.append(i.text)
        if soup.findAll("div", "ratingValue"):
            for r in soup.findAll("div", "ratingValue"):
                mov_rating = r.strong["title"]
        else:
            mov_rating = "Not available"
        await catevent.edit(
            "<a href=" + poster + ">&#8203;</a>"
            "<b>Judul : </b><code>"
            + mov_title
            + "</code>\n<code>"
            + mov_details
            + "</code>\n<b>Peringkat : </b><code>"
            + mov_rating
            + "</code>\n<b>Negara : </b><code>"
            + mov_country[0]
            + "</code>\n<b>Bahasa : </b><code>"
            + mov_language[0]
            + "</code>\n<b>Direktur : </b><code>"
            + director
            + "</code>\n<b>Penulis : </b><code>"
            + writer
            + "</code>\n<b>Bintang : </b><code>"
            + stars
            + "</code>\n<b>Url IMDB : </b>"
            + mov_link
            + "\n<b>Alur Cerita : </b>"
            + story_line,
            link_preview=True,
            parse_mode="HTML",
        )
    except IndexError:
        await catevent.edit("harap memasukkan **Nama film yang valid**")


CMD_HELP.update(
    {
        "scrapers": """__**NAMA PLUGIN :** Scrapers__\
\n\n✅** CMD ➥** `.wiki` <pertanyaan>
\n**Fungsi   ➥  **__Ambil kueri yang diberikan di wikipedia dan menunjukkan kepada Anda__
\n\n✅** CMD ➥** `.imdb` <pertanyaan>
\n**Fungsi   ➥  **__Fetches Diberikan detail film dari imdb__
"""
    }
)
