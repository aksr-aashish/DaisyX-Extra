from telethon import Button, events

from DaisyX import xbot, CMD_HELP
from DaisyX.utils import admin_cmd, sudo_cmd, edit_or_reply as eor


@borg.on(admin_cmd(pattern="btn (.*)"))
@borg.on(sudo_cmd(pattern="btn", allow_sudo=True))
async def Buttons(event):
    await eor(event, "`Mᴀᴋɪɴɢ Yᴏᴜʀ Bᴜᴛᴛᴏɴ ᴡᴇɪᴛ ᴍᴀsᴛᴇʀ !!!`")
    DAISYX = Var.TG_BOT_USER_NAME_BF_HER
    pro = event.text[7:]
    pro, boy = pro.split("|")
    with open("Button.txt", "w") as f:
        f.write(f'{pro}\n{boy}')
    LUNDX = await bot.inline_query(DAISYX, "BUTTON")
    await LUNDX[0].click(event.chat_id)
    await event.delete()

@xbot.on(events.InlineQuery(pattern='BUTTON'))
async def file(event):
    with open("Button.txt") as f:
        ok = f.readlines()[0]
    with open("Button.txt") as CHUTX:
        bc = CHUTX.readlines()[1]
    LUNDX = event.builder
    DEVIL = [[Button.url(f'{ok}', f'{bc}')]]
    INUKA = LUNDX.article(title='Button by DaisyX', text=f'{ok}', buttons=DEVIL)
    await event.answer([INUKA])

CMD_HELP.update(
    {
        "buttons": ".btn <button name>|<link>\n`.btn DaisyX|https://t.me/DAISYXOT`\nmake sure your name and link no have Useless spece"
    }
)
