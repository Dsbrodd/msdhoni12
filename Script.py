class script(object):
    START_TXT = """<b>Hᴇʟʟᴏ 
Sᴏʀʀʏ ɪ ᴏɴʟʏ ᴡᴏʀᴋ ᴏɴ ғɪʟᴍ ʜᴏᴜꜱᴇ Gʀᴏᴜᴘ. Nᴏ ᴏᴛʜᴇʀ ᴄᴏᴍᴍᴀɴᴅ ᴡɪʟʟ ᴡᴏʀᴋ ᴏɴ ᴛʜɪs ʙᴏᴛ ᴇxᴄᴇᴘᴛ sᴛᴀʀᴛ. ᴅᴏɴ’ᴛ ᴡᴀsᴛᴇ ʏᴏᴜʀ ᴛɪᴍᴇ</b>"""
    HELP_TXT = """<b> Tʜɪꜱ ɪꜱ ᴍʏ ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅꜱ</b>"""
    ABOUT_TXT = """🤖 ʙᴏᴛ ɴᴀᴍᴇ: {}
    
📝 ʟᴀɴɢᴜᴀɢᴇ : ᴘʏᴛʜᴏɴ

📚 ꜰʀᴀᴍᴇᴡᴏʀᴋ : ᴘʏʀᴏɢʀᴀᴍ

📡 ʜᴏsᴛᴇᴅ ᴏɴ : ʜᴇʀᴏᴋᴜ

👨‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ :  ᴀᴅɪᴛʜ ᴛɢ 🇮🇳

💡 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : ᴄʟɪᴄᴋ ʜᴇʀᴇ

👥 sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ : ʀᴇxɪᴇ sᴜᴘᴘᴏʀᴛ

📢 ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ : ᴍʜ ᴜᴘᴅᴀᴛᴇs

🔖 𝑸𝒖𝒐𝒕𝒆 : ആരും പേടിക്കേണ്ട എല്ലാവർക്കും കിട്ടും"""
    SOURCE_TXT = """<b>NOTE:</b>
- Eva Maria is a open source project. 
- Source - https://github.com/EvamariaTG/EvaMaria  

<b>DEVS:</b>
- <a href=https://t.me/TeamEvamaria>Team Eva Maria</a>"""
    MANUELFILTER_TXT = """<b>🔧 MANUAL FILTER</b>

Fɪʟᴛᴇʀ ɪꜱ ᴛʜᴇ ғᴇᴀᴛᴜʀᴇ ᴡᴇʀᴇ ᴜꜱᴇʀꜱ ᴄᴀɴ ꜱᴇᴛ ᴀᴜᴛᴏᴍᴀᴛᴇᴅ ʀᴇᴘʟɪᴇꜱ ғᴏʀ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴋᴇʏᴡᴏʀᴅ ᴀɴᴅ EᴠᴀMᴀʀɪᴀ ᴡɪʟʟ ʀᴇꜱᴘᴏɴᴅ ᴡʜᴇɴᴇᴠᴇʀ ᴀ ᴋᴇʏᴡᴏʀᴅ ɪꜱ ғᴏᴜɴᴅ ᴛʜᴇ ᴍᴇꜱꜱᴀɢᴇ

<b>📚 Available Commands</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>🛠️ AUTO FILTER</b>

<b>NOTE:</b>
𝟷. Mᴀᴋᴇ ᴍᴇ ᴛʜᴇ ᴀᴅᴍɪɴ ᴏғ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ɪғ ɪᴛ'ꜱ ᴘʀɪᴠᴀᴛᴇ.
𝟸. ᴍᴀᴋᴇ ꜱᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴅᴏᴇꜱ ɴᴏᴛ ᴄᴏɴᴛᴀɪɴꜱ ᴄᴀᴍʀɪᴘꜱ, ᴘᴏʀɴ ᴀɴᴅ ғᴀᴋᴇ ғɪʟᴇꜱ.
𝟹. Fᴏʀᴡᴀʀᴅ ᴛʜᴇ ʟᴀꜱᴛ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴍᴇ ᴡɪᴛʜ ǫᴜᴏᴛᴇꜱ.
 I'ʟʟ ᴀᴅᴅ ᴀʟʟ ᴛʜᴇ ғɪʟᴇꜱ ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴍʏ ᴅʙ."""
    CONNECTION_TXT = """Help: <b>🔗 Cᴏɴɴᴇᴄᴛɪᴏɴꜱ</b>

- Uꜱᴇᴅ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʙᴏᴛ ᴛᴏ PM ғᴏʀ ᴍᴀɴᴀɢɪɴɢ ғɪʟᴛᴇʀꜱ 
- ɪᴛ ʜᴇʟᴘꜱ ᴛᴏ ᴀᴠᴏɪᴅ ꜱᴘᴀᴍᴍɪɴɢ ɪɴ ɢʀᴏᴜᴘꜱ.

𝟷. Oɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴀᴅᴅ ᴀ ᴄᴏɴɴᴇᴄᴛɪᴏɴ.
𝟸. Sᴇɴᴅ /ᴄᴏɴɴᴇᴄᴛ ғᴏʀ ᴄᴏɴɴᴇᴄᴛɪɴɢ ᴍᴇ ᴛᴏ ᴜʀ PM

<b>📚 ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅꜱ</b>

• /ᴄᴏɴɴᴇᴄᴛ - ᴄᴏɴɴᴇᴄᴛ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ ᴛᴏ ʏᴏᴜʀ PM
• /ᴅɪꜱᴄᴏɴɴᴇᴄᴛ - ᴅɪꜱᴄᴏɴɴᴇᴄᴛ ғʀᴏᴍ ᴀ ᴄʜᴀᴛ
• /ᴄᴏɴɴᴇᴄᴛɪᴏɴꜱ - ʟɪꜱᴛ ᴀʟʟ ʏᴏᴜʀ ᴄᴏɴɴᴇᴄᴛɪᴏɴꜱ"""
    EXTRAMOD_TXT = """Help: <b>Exᴛʀᴀ Mᴏᴅᴜʟᴇꜱ</b>

<b>🎛 Exᴛʀᴀ Mᴏᴅᴜʟᴇꜱ</b>

ᴛʜᴇꜱᴇ ᴀʀᴇ ᴛʜᴇ ᴇxᴛʀᴀ ғᴇᴀᴛᴜʀᴇꜱ ᴏғ Eᴠᴀ Mᴀʀɪᴀ

<b>📚 ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅꜱ</b>
• /ɪᴅ - ɢᴇᴛ ɪᴅ ᴏғ ᴀ ꜱᴘᴇᴄɪғɪᴇᴅ ᴜꜱᴇʀ.
• /ɪɴғᴏ - ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜꜱᴇʀ.
• /ɪᴍᴅʙ - ɢᴇᴛ ᴛʜᴇ ғɪʟᴍ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ғʀᴏᴍ IMDʙ ꜱᴏᴜʀᴄᴇ.
• /ꜱᴇᴀʀᴄʜ - ɢᴇᴛ ᴛʜᴇ ғɪʟᴍ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ғʀᴏᴍ ᴠᴀʀɪᴏᴜꜱ ꜱᴏᴜʀᴄᴇꜱ."""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """<b>📁 𝙏𝙤𝙩𝙖𝙡 𝙁𝙞𝙡𝙚𝙨 : </b> <code>{}</code>
<b>👤 𝙏𝙤𝙩𝙖𝙡 𝙐𝙨𝙚𝙧𝙨 : </b> <code>{}</code>
<b>👥 𝙏𝙤𝙩𝙖𝙡 𝘾𝙝𝙖𝙩𝙨 : </b> <code>{}</code>
<b>⚙️ 𝙐𝙨𝙚𝙙 𝙎𝙩𝙤𝙧𝙖𝙜𝙚 : </b> <code>{}</code> MiB
<b>🆓 𝙏𝙤𝙩𝙖𝙡 𝙎𝙩𝙤𝙖𝙜𝙚 : </b> <code>{}</code> MiB"""
    FILESTORE_TXT = """<b>🗃️ File Store</b>

<b>A ᴍᴏᴅᴜʟᴇ ᴛᴏ ꜱᴛᴏʀᴇ ғɪʟᴇꜱ ɪɴ ʙᴏᴛ ᴅᴀᴛᴀʙᴀꜱᴇ ɪɴ ꜱɪᴍᴘʟᴇ ᴍᴇᴛʜᴏᴅ<b>

<b>📚 Available Commands</b>

◉ /batch - reply The file link in db channel"""
    PERSONAL_TXT = """<b>എന്തായാലും സ്റ്റാർട്ട് അടിച്ചതല്ലെ ഇനി ആ താഴെ കാണുന്ന നമ്മുടെ ഒഫീഷ്യൽ ചന്നെൽ കൂടി Subscribe ചെയ്തിട്ട് പൊക്കോ...🤣🤣.</b>"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
