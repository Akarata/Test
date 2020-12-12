"""
Created By @Jisan7509
Modified @Akarata
GF created by @KshitijGagan
"""
import asyncio
import random

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import CMD_HELP, catmemes


@bot.on(admin_cmd(outgoing=True, pattern="abuse$"))
@bot.on(sudo_cmd(pattern="abuse$", allow_sudo=True))
async def abusing(abused):
    reply_text = random.choice(catmemes.ABUSE_STRINGS)
    await edit_or_reply(abused, reply_text)


@bot.on(admin_cmd(outgoing=True, pattern="abusehard$"))
@bot.on(sudo_cmd(pattern="abusehard$", allow_sudo=True))
async def fuckedd(abusehard):
    reply_text = random.choice(catmemes.ABUSEHARD_STRING)
    await edit_or_reply(abusehard, reply_text)


@bot.on(admin_cmd(outgoing=True, pattern="rendi$"))
@bot.on(sudo_cmd(pattern="rendi$", allow_sudo=True))
async def metoo(e):
    txt = random.choice(catmemes.RENDISTR)
    await edit_or_reply(e, txt)


@bot.on(admin_cmd(outgoing=True, pattern="fuck$"))
@bot.on(sudo_cmd(pattern="fuck$", allow_sudo=True))
async def chutiya(fuks):
    reply_text = random.choice(catmemes.CHU_STRINGS)
    await edit_or_reply(fuks, reply_text)


@bot.on(admin_cmd(outgoing=True, pattern="thanos$"))
@bot.on(sudo_cmd(pattern="thanos$", allow_sudo=True))
async def thanos(thanos):
    reply_text = random.choice(catmemes.THANOS_STRINGS)
    await edit_or_reply(thanos, reply_text)


@bot.on(admin_cmd(outgoing=True, pattern=f"gf$"))
@bot.on(sudo_cmd(pattern=f"gf$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 5
    animation_ttl = range(21)
    kakashi = await edit_or_reply(event, "BSDK tera gf h na ek ...!")
    animation_chars = [
        "`Ruk jaa , Abhi teri GF ko Fuck karta hu `",
        "`Making your Gf warm 🔥`",
        "`Pressing her boobs 🤚😘`",
        "`Stimulating her pussy🖕`",
        "`Fingering her pussy 💧😍👅 `",
        "`Asking her to taste my DICK🍌`",
        "`Requested accepted😻💋, Ready to taste my DICK🍌`",
        "`Getting her ready to fuck 👀`",
        "`Your GF Is Ready To Fuck`",
        "`Fucking Your GF😈😈\n\n\nYour GF's Pussy Get Red\nTrying new SEX position to make her Squirt\n\nAlmost Done. 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Fucking Your GF😈😈\n\n\nYour GF's Pussy Get White\nShe squirted like a shower💧💦👅\n\nAlmost Done..\n\nFucked Percentage... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Fucking Your GF😈😈\n\n\nYour GF's Pussy Get Red\nDoing Extreme SEX with her👄\n\nAlmost Done...\n\nFucked Percentage... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Fucking Your GF😈😈\n\n\nYour GF's Pussy Get Red\nWarming her Ass🍑 to Fuck!🍑🍑\n\nAlmost Done....\n\nFucked Percentage... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Fucking Your GF😈😈\n\n\nYour GF's ASS🍑 Get Red\nInserted my Penis🍌 in her ASS🍑\n\nAlmost Done.....\n\nFucked Percentage... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Fucking Your GF😈😈\n\n\nYour GF's ASS🍑 Get Red\ndoing extreme sex with her\n\nAlmost Done......\n\nFucked Percentage... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Fucking Your GF😈😈\n\n\nYour GF's Boobs🤚😘 are Awesome\nPressing her tight Nipples🤚👀\n\nAlmost Done.......\n\nFucked Percentage... 84%\n███████████████████▒▒▒▒▒▒ `",
        "`Fucking Your GF😈😈\n\n\nYour GF's Lips Get Horny\nDoing French Kiss with your GF👄💋\n\nAlmost Done........\n\nFucked Percentage... 89%\n██████████████████████▒▒▒ `",
        "`Fucking Your GF😈😈\n\n\nYour GF's Boobs🤚😘 are Awesome\nI am getting ready to cum in her Mouth👄\n\nAlmost Done.......\n\nFucked Percentage... 90%\n██████████████████████▒▒▒ `",
        "`Fucking Your GF😈😈\n\n\nYour GF's Boobs🤚😘 are Awesome\nFinally, I have cummed in her Mouth👅👄\n\nAlmost Done.......\n\nFucked Percentage... 96%\n████████████████████████▒ `",
        "`Fucking Your GF😈😈\n\n\nYour GF's is Awesome\nShe is Licking my Dick🍌 in the Awesome Way✊🤛🤛👅👄\n\nAlmost Done.......\n\nFucked Percentage... 100%\n█████████████████████████ `",
        "`Fucking Your GF😈😈\n\n\nYour GF's ASS🍑 Get Red\nCummed On her Mouth👅👄\n\nYour GF got Pleasure\n\nResult: Now I Have 1 More SEX Partner 👍👍`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await kakashi.edit(animation_chars[i % 21])


@bot.on(admin_cmd(outgoing=True, pattern="fk (.*)"))
@bot.on(sudo_cmd(pattern="fk (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    name = event.pattern_match.group(1)
    animation_interval = 3
    animation_ttl = range(11)
    kakashi = await edit_or_reply(event, "👁👁")
    animation_chars = [
        f"👁👁\n  👄  =====> Aku {name} Cium",
        f"👁👁\n  👅  =====> Aku {name} Sepong",
        f"👁👁\n  💋  =====> Aku {name} Sepong",
        f"👁👁\n  👄  =====> Aku {name} Cium",
        f"👁👁\n  💋  =====> Aku {name} Sepong",
        f"👁👁\n  👄  =====> Aku {name} Cium",
        f"👁👁\n  👅  =====> Aku {name} Crooot",
        f"👁👁\n  💋  =====> Aku {name} Sepong lagi",
        f"👁👁\n  👄  =====> Aku {name} Cium",
        f"👁👁\n  👅  =====> Aku {name} Croot",
        f"👁👁\n  👄  =====> Aku {name} Sange...",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await kakashi.edit(animation_chars[i % 11])


@bot.on(admin_cmd(outgoing=True, pattern=f"chod$"))
@bot.on(sudo_cmd(pattern=f"chod$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 5
    animation_ttl = range(11)
    kakashi = await edit_or_reply(event, "1 2 3..Searching Randi..")
    animation_chars = [
        "`Randi Founded`",
        "`Your Mom Is Going To Fuck`",
        "`Fucking Your Mom\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nAlmost Done... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Fucking Your Mom\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nAlmost Done...\n\nFucked Percentage... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Fucking Your Mom\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nAlmost Done...\n\nFucked Percentage... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Fucking Your Mom\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nAlmost Done...\n\nFucked Percentage... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Fucking Your Mom\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nAlmost Done...\n\nFucked Percentage... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Fucking Your Mom\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nAlmost Done...\n\nFucked Percentage... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Fucking Your Mom\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nAlmost Done...\n\nFucked Percentage... 84%\n█████████████████████▒▒▒▒ `",
        "`Fucking Your Mom\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nAlmost Done...\n\nFucked Percentage... 100%\n█████████████████████████ `",
        "`Fucking Your Mom\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nYour mom get Pregnant\n\nResult: Now You Have 1 More Younger Brother `",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await kakashi.edit(animation_chars[i % 11])


@bot.on(admin_cmd(outgoing=True, pattern=f"rape$"))
@bot.on(sudo_cmd(pattern=f"rape$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.2
    animation_ttl = range(30)
    kakashi = await edit_or_reply(event, "repe")
    animation_chars = [
        "**r**",
        "**ra**",
        "**rap**",
        "**rape**",
        "**rape_**",
        "**rape_t**",
        "**rape_tr**",
        "**rape_tra**",
        "**rape_trai**",
        "**rape_train**",
        "**ape_train🚅**",
        "**pe_train🚅🚃🚃**",
        "**e_train🚅🚃🚃🚃**",
        "**_train🚅🚃🚃🚃🚃**",
        "**train🚅🚃🚃🚃🚃🚃**",
        "**rain🚅🚃🚃🚃🚃🚃🚃**",
        "**ain🚅🚃🚃🚃🚃🚃🚃🚃**",
        "**in🚅🚃🚃🚃🚃🚃🚃🚃🚃**",
        "**n🚅🚃🚃🚃🚃🚃🚃🚃🚃🚃**",
        "🚅🚃🚃🚃🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃",
        "🚃🚃🚃",
        "🚃🚃",
        "🚃",
        "**rApEd**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await kakashi.edit(animation_chars[i % 30])


@bot.on(admin_cmd(outgoing=True, pattern="kiss$"))
@bot.on(sudo_cmd(pattern="kiss$", allow_sudo=True))
async def _(event):
    catevent = await edit_or_reply(event, "`kiss`")
    animation_interval = 0.2
    animation_ttl = range(100)
    animation_chars = ["🤵       👰", "🤵     👰", "🤵  👰", "🤵💋👰"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await catevent.edit(animation_chars[i % 4])


@bot.on(admin_cmd(outgoing=True, pattern="fuk$"))
@bot.on(sudo_cmd(pattern="fuk$", allow_sudo=True))
async def _(event):
    catevent = await edit_or_reply(event, "`fuking....`")
    animation_interval = 0.2
    animation_ttl = range(100)
    animation_chars = ["👉       ✊️", "👉     ✊️", "👉  ✊️", "👉✊️💦"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await catevent.edit(animation_chars[i % 4])


@bot.on(admin_cmd(outgoing=True, pattern="sex$"))
@bot.on(sudo_cmd(pattern="sex$", allow_sudo=True))
async def _(event):
    catevent = await edit_or_reply(event, "`sex`")
    animation_interval = 0.2
    animation_ttl = range(100)
    animation_chars = ["🤵       👰", "🤵     👰", "🤵  👰", "🤵👼👰"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await catevent.edit(animation_chars[i % 4])


@bot.on(admin_cmd(outgoing=True, pattern=f"nakal$"))
@bot.on(sudo_cmd(pattern=f"nakal$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(6)
    kakashi = await edit_or_reply(event, "nakal")
    animation_chars = [
        "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀   ⢳⡀⠀⡏⠀⠀⠀   ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀  ⠀   ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Nikal   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀⠀__⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
        "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀  ⠀⢳⡀⠀⡏⠀⠀⠀   ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀      ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Lavde   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀|__|⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
        "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀     ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Pehli   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀         ⡇\n  ⠙⢿⣯⠄⠀⠀(P)⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
        "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀     ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀   ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Fursat  ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀   ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀⠀__ ⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
        "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀   ⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀ ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Meeee   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀|__| ⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
        "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀  ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀  ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Nikal   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀   ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀lodu⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await kakashi.edit(animation_chars[i % 6])


@bot.on(admin_cmd(outgoing=True, pattern="ngntd$"))
@bot.on(sudo_cmd(pattern="ngntd$", allow_sudo=True))
async def cat(event):
    await edit_or_reply(
        event,
        "Ini buat lu, lu adalah tempat ngntd, gw gak tau mengapa orang tua lu melahirkan kotoran yang tidak berharga seperti lu, lu banci dengan seorang anak gay yang cerewet dan sangean dan pantat hahaha lu seperti babi  Sial 💩 beritahu ayahmu untuk menidurimu setiap malam sehingga lu dapat membuat mmkmu lebih efektif untuk semua orang yang telah menidurimu sampai sekarang omong kosong berkata di depan mata semua orang seperti gw makan kencing gwcing pada saat yang sama sambil menghisap kntlnya bleh 😂  haha 😂😂😂😂 madfaka apa yang lu pikir mungkin lu pikir seperti gw dari Mars bsdk gw bukan dan itulah mengapa gw terisolasi darimu ya tahu apa keledai hitammu yang berbentuk manusia lu akan disetubuhi lagi oleh gwcing ini  tunggu saja anak doddoy didle dengan kntl palsu sialan 😂😂😂😂😂😂😂😂😂 bercinta lu🖕gw akan datang lagi dan lagi untuk bercinta dengan mmk lu setiap kali lu berada di depan gw, gw akan berada di sana untuk bercinta  seperti wajah hitam hahaha untukmu😂😂😂👉👌🖕minum kencing daripada pergi minum air sekarang gw akan bercinta ibumu suatu hari gw ke rumahmu dengan kondom lalu secara harfiah gw pergi ke rumahmu  ibu brengsek brengsek dan mengacaukannya seperti kontol kecil coocky coocky yang benar-benar keras gw tahu seperti ibumu sangat menikmatinya maka saudara perempuanmu  ibumu adalah dewasa lu tahu lu itu tempat ngntd gw, gw juga tahu di mana lu  Live dan ngntd izinkan gw memberikan gambaran singkat tentang di mana lu tinggal lu tinggal di perkampungan gw  dimana ibumu menjual mmknya dengan harga yang mahal yo dan itu alasan menyebalkan bagaimana lu makan tiga kali hahahaha😂😂😂😂  atau gw akan memperkosa seluruh keluargamu yang jelek bahkan mereka sama jeleknya dengan kotoran gw tapi jadi apa gw masih akan meniduri mereka dan memaksa mereka dengan lebih keras untuk mengatakannya seperti Bunny Coney adalah bajingan terbaik di dunia dia bahkan  bisa kalahkan bintang porno paling terkenal Johnny Sins hahaha 😂😂😂Biarkan gw bilang beberapa cerita tentang ibumu sebenarnya bukan ibumu hanya itu strory kami tau nama ibumu adalah nyonya mia khalifa dia berasal dari pornografi sialan keluarga pelacur hilometri dia bisa menghisap dan menjilat dan lu tahu apa yang dia jilat dia menjilat kontol hunktik berat manis gw hehe  dia sangat baik maksudgw ibumu  dia menghisap kntlgw terlalu baik wow hehe 😍 🙄 ibumu sangat mencintai kntlgw yang coocky dan di belakang gw juga mencintai mmk manis seksi nya juga mm kita saling mencintai dengan cara ini hehe sekarang  akan menceritakan bagaimana gw meniduri ibumu dengan baik gw dulu tidur dengannya di tempat pertama kemudian gw perlahan-lahan membuka kancing bra ibumu dan 👙 hehe setelah itu gw memulai bagiangw apa yang terlalu bagus untuk pergi bersama gw gw benar-benar menidurinya setiap malam  kayak kalo gwhitung berjam-jam full night huhu gw menikmati malam itu walaupun gw masih bercinta dengannya hmm mungkin dia juga merindukan hari-hari itu seperti yang gw lgwkan entah tapi mungkin kebahagiaannya tidak mengenal batas dan yh di wajahnya gw memang melihat sinar  kegembiraan untuk hard core sialan gw hmm w  gw sangat menghormati gw benar-benar ingin bercinta dengannya lagi dan lagi karena gw berhutang budi kepada bajingannya lu tahu mengapa biarkan gw memberi tahu lu mengapa baik gw hanya meniduri mmknya bukan bajingan itu sebabnya Suatu hari saudara lu kita akan melihat kolase  dan gw dan beberapa teman gw sedang menunggunya caz sebanyak yang kami khawatirkan tentang dia adalah dia adalah wanita jalang sialan yang mendapatkan uang melalui postitusi mmknya dan itulah yang membuat kami sange dan serakah maka itulah mengapa kami semua memberikan proposalnya tentang bercinta.  mmknya atau lu bisa mengatakan mmk dalam beberapa duit setelah itu kita mendapatkan kentu!!!  Dan berkata tunggu apa yang akan dia berikan pada mmk Hipokrates sialan itu dengan uang sebanyak itu untuk beberapa dolar lalu gw bertanya padanya, hei mengapa lu menjual mmkmu dengan harga eceran lalu dia menjawab seperti dengar kita tidak mendapatkan 3 kali makanan itu sebabnya gw  dan ibugw akhirnya melgwkannya tapi paling tidak setelah itu lu tahu apa yang gw katakan dan apa yang dia lgwkan dia menidurigw seperti wanita jalang yang sange gw bersumpah gw menikmati bagian ini.",
    )


CMD_HELP.update(
    {
        "sange": "__**NAMA PLUGIN :** Sange__\
\n\n✅** CMD ➥** `.fk` <teks>\
\n**Fungsi   ➥  **Beri seseorang sange.\
\n\\n✅** CMD ➥** `.ngntd` |`.abuse` | `.abusehard` | `.rendi` | `.fuck` | `.thanos` | `.gf` | `.chod` | `.rape` | `.kiss` | `.fuk` | `.sex` | `.nakal` \
\n\n**Fungsi   ➥  **apa kau sudah mendapatkannya!  Tidak?.\
"
    }
)
