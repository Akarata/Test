# corona virus stats for catuserbot
from covid import Covid

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import CMD_HELP, covidindia


@bot.on(admin_cmd(pattern="covid(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="covid(?: |$)(.*)", allow_sudo=True))
async def corona(event):
    if event.pattern_match.group(1):
        country = (event.pattern_match.group(1)).title()
    else:
        country = "World"
    catevent = await edit_or_reply(event, "`mengumpulkan data...........`")
    covid = Covid(source="worldometers")
    try:
        country_data = covid.get_status_by_country_name(country)
    except ValueError:
        country_data = ""
    if country_data:
        hmm1 = country_data["confirmed"] + country_data["new_cases"]
        hmm2 = country_data["deaths"] + country_data["new_deaths"]
        data = ""
        data += f"\n⚠️Dikonfirmasi   : <code>{hmm1}</code>"
        data += f"\n😔Aktif           : <code>{country_data['active']}</code>"
        data += f"\n⚰️Meninggal         : <code>{hmm2}</code>"
        data += f"\n🤕Kritis          : <code>{country_data['critical']}</code>"
        data += f"\n😊Dipulihkan   : <code>{country_data['recovered']}</code>"
        data += f"\n💉Tes total    : <code>{country_data['total_tests']}</code>"
        data += f"\n🥺Kasus Baru   : <code>{country_data['new_cases']}</code>"
        data += f"\n😟Kematian Baru : <code>{country_data['new_deaths']}</code>"
        await catevent.edit(
            "<b>Corona Virus Info of {}:\n{}</b>".format(country, data),
            parse_mode="html",
        )
    else:
        data = await covidindia(country)
        if data:
            cat1 = int(data["new_positive"]) - int(data["positive"])
            cat2 = int(data["new_death"]) - int(data["death"])
            cat3 = int(data["new_cured"]) - int(data["cured"])
            result = f"<b>Corona virus info of {data['state_name']}\
                \n\n⚠️Dikonfirmasi   : <code>{data['new_positive']}</code>\
                \n😔Aktif           : <code>{data['new_active']}</code>\
                \n⚰️Meninggal         : <code>{data['new_death']}</code>\
                \n😊Dipulihkan   : <code>{data['new_cured']}</code>\
                \n🥺Kasus Baru   : <code>{cat1}</code>\
                \n😟Kematian Baru : <code>{cat2}</code>\
                \n😃Baru sembuh  : <code>{cat3}</code> </b>"
            await catevent.edit(result, parse_mode="html")
        else:
            await edit_delete(
                catevent,
                "`Corona Virus Info of {} is not avaiable or unable to fetch`".format(
                    country
                ),
                5,
            )


CMD_HELP.update(
    {
        "covid": "__**PLUGIN NAME :** Covid__\
        \n\n✅** CMD ➥** `.covid` <country name>\
        \n**Fungsi   ➥  **__Dapatkan informasi tentang data covid-19 di negara tertentu.__\
        \n\n✅** CMD ➥** `.covid` <state name>\
        \n**Fungsi   ➥  ** __Dapatkan informasi tentang data covid-19 di negara bagian tertentu di India saja.__\
        "
    }
)
