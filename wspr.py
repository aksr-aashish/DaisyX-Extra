
from telethon import events, Button
import re, os
from Skem import skemmers as id
from DaisyX import xbot
@xbot.on(events.InlineQuery(pattern='wspr'))
async def inline_proboy(event):
  CHUTX = event.text[5:]
  CHUTX, PARRYX = CHUTX.split('@')
  os.system("rm -rf wspr.txt")
  with open("wspr.txt", "a") as f:
    f.write(CHUTX + "\n" + PARRYX)
  LUNDX = event.builder
  LUNDBOI = [[Button.inline("🔐 Sʜᴏᴡ", data='secret')]]
  LUNDBOI += [[Button.switch_inline("Rᴇᴘʟʏ", query="wspr", same_peer=True)]]
  ALAIN = LUNDX.article(title=f"Wʜɪsᴘᴇʀ Fᴏʀ @{PARRYX}", text=f"<b>📩 Sᴇᴄʀᴇᴛ Msɢ</b> Tᴏ <b>@{PARRYX}</b>. Oɴʟʏ Hᴇ/Sʜᴇ Cᴀɴ Oᴘᴇɴ Iᴛ..", buttons=LUNDBOI, parse_mode="html")
  await event.answer([ALAIN])

@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'secret')))
async def wspr(event):
  try:
    with open("wspr.txt") as f:
      LUNDX = f.readlines()[0]
    with open("wspr.txt") as pro:
      CHUTX = pro.readlines()[1].lower()
    bot = await xbot.get_me()
    sender = f"{event.sender.username}".lower()
    me = f"{borg.me.username}".lower()
    if sender == CHUTX or sender == me or event.sender_id == id:
       await event.answer(LUNDX, alert=True)
    else:
       await event.answer("Yes You, Little Shit, Why're u seeing my msg??", alert=False)
  except:
    await event.answer(f"Use @{bot.username} wspr <msg> <@ sender username>\n\nAnd ofc, remove those <>", alert=True)
