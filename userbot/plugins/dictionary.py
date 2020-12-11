# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""Urban Dictionary
Syntax: .ud Query"""
import asyncurban
from PyDictionary import PyDictionary

from .. import CMD_HELP
from ..utils import admin_cmd, edit_or_reply, sudo_cmd


@bot.on(admin_cmd(pattern="ud (.*)"))
@bot.on(sudo_cmd(pattern="ud (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    word = event.pattern_match.group(1)
    urban = asyncurban.UrbanDictionary()
    try:
        mean = await urban.get_word(word)
        await edit_or_reply(
            event,
            "Text: **{}**\n\nBerarti: **{}**\n\nContoh: __{}__".format(
                mean.word, mean.definition, mean.example
            ),
        )
    except asyncurban.WordNotFoundError:
        await edit_or_reply(event, "Tidak ada hasil untuk **" + word + "**")


@bot.on(admin_cmd(pattern="meaning (.*)"))
@bot.on(sudo_cmd(pattern="meaning (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    word = event.pattern_match.group(1)
    dictionary = PyDictionary()
    cat = dictionary.meaning(word)
    output = f"**Kata :** __{word}__\n\n"
    try:
        for a, b in cat.items():
            output += f"**{a}**\n"
            for i in b:
                output += f"☞__{i}__\n"
        await edit_or_reply(event, output)
    except Exception:
        await edit_or_reply(event, f"Tidak dapat memahami arti dari {word}")


CMD_HELP.update(
    {
        "dictionary": "__**NAMA PLUGIN :** Dictionary__\
    \n\n✅** CMD ➥** `.ud` query\
    \n**Fungsi   ➥  **Mengambil makna dari kamus Urban\
    \n\n✅** CMD ➥** `.meaning` query\
    \n**Fungsi   ➥  **Mengambil arti dari kata yang diberikan\
    "
    }
)
