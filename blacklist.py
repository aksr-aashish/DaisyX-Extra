
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins, ChannelParticipantAdmin, ChannelParticipantCreator
from DaisyX.utils import admin_cmd
from telethon.errors.rpcerrorlist import (UserIdInvalidError,
                                          MessageTooLongError)
                                          
@borg.on(admin_cmd(pattern=r"plist ?(.*)", outgoing=True))
async def get_users(show):
    """ For .userslist command, list all of the users of the chat. """
    if show.text[0].isalpha() or show.text[0] in ("/", "#", "@", "!"):
        return
    if not show.is_group:
        await show.edit("Are you sure this is a group?")
        return
    info = await show.client.get_entity(show.chat_id)
    title = info.title or "this chat"
    mentions = "id,reason"
    try:
        if not show.pattern_match.group(1):
            async for user in show.client.iter_participants(show.chat_id):
                mentions += f"\n{user.id},⚠️Porn / incest / ch//AntiPornFed #Massban🔞🛑"
        else:
            searchq = show.pattern_match.group(1)
            async for user in show.client.iter_participants(show.chat_id, search=f'{searchq}'):
                mentions += f"\n{user.id},⚠️Porn / incest / ch//AntiPornFed #Massban🔞🛑"
    except ChatAdminRequiredError as err:
        mentions += " " + str(err) + "\n"
    try:
        await show.edit(mentions)
    except MessageTooLongError:
        await show.edit("Damn, this is a huge group. Uploading users lists as file.")
        with open("userslist.csv", "w+") as file:
            file.write(mentions)
        await show.client.send_file(
            show.chat_id,
            "userslist.csv",
            caption='Group members in {}'.format(title),
            reply_to=show.id,
        )
        remove("userslist.csv")


@borg.on(admin_cmd(pattern=r"blist ?(.*)", outgoing=True))
async def get_users(show):
    """ For .userslist command, list all of the users of the chat. """
    if show.text[0].isalpha() or show.text[0] in ("/", "#", "@", "!"):
        return
    if not show.is_group:
        await show.edit("Are you sure this is a group?")
        return
    info = await show.client.get_entity(show.chat_id)
    title = info.title or "this chat"
    mentions = "id,reason"
    try:
        if not show.pattern_match.group(1):
            async for user in show.client.iter_participants(show.chat_id):
                mentions += f"\n{user.id},⚠️Suspicious/Blaclisted Group/You Are Member of Blacklisted Group #Massban🛑"
        else:
            searchq = show.pattern_match.group(1)
            async for user in show.client.iter_participants(show.chat_id, search=f'{searchq}'):
                if not user.deleted:
                    mentions += f"\n{user.id},⚠️Suspicious/Blaclisted Group/You Are Member of Blacklisted Group #Massban #Massban🛑"
                else:
                    mentions += f"\n{user.id},⚠️Suspicious/Blaclisted Group/You Are Member of Blacklisted Group #Massban🛑"
    except ChatAdminRequiredError as err:
        mentions += " " + str(err) + "\n"
    try:
        await show.edit(mentions)
    except MessageTooLongError:
        await show.edit("Damn, this is a huge group. Uploading users lists as file.")
        with open("userslist.csv", "w+") as file:
            file.write(mentions)
        await show.client.send_file(
            show.chat_id,
            "userslist.csv",
            caption='Group members in {}'.format(title),
            reply_to=show.id,
        )
        remove("userslist.csv")
