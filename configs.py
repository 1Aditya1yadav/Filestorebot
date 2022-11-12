import os


class Config(object):
	API_ID = int(os.environ.get("19207498", "0"))
	API_HASH = os.environ.get("174c00bab9c841383cee419c3da13651")
	BOT_TOKEN = os.environ.get("5661182742:AAGQEawDxbVJ--nixJtUHIprh_bpOAwo2Bs")
	BOT_USERNAME = os.environ.get("@Savefileherebot ")
	DB_CHANNEL = int(os.environ.get("-1001834516148 ", "-100"))
	BOT_OWNER = int(os.environ.get("1444300019", "1445283714"))
	DATABASE_URL = os.environ.get("mongodb+srv://Aditya65:<Ab 9596 ek>@cluster0.37y2cxz.mongodb.net/?retryWrites=true&w=majority")
	UPDATES_CHANNEL = os.environ.get(" -1001806508673", "")
	LOG_CHANNEL = os.environ.get(" -1001705724548 ", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File.I can Work In Channel too Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ **🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅**]────⍟
│
├🔸🤖 **My Name:** [𝐅𝐢𝐥𝐞 𝐒𝐭𝐨𝐫𝐞 𝐁𝐨𝐭](https://t.me/{BOT_USERNAME})
│
├🔸📝 **Language:** [𝐏𝐲𝐭𝐡𝐨𝐧𝟑](https://www.python.org)
│
├🔹📚 **Library:** [𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦](https://docs.pyrogram.org
│
├🔹👥 **Bot Support:** [𝐒𝐮𝐩𝐩𝐨𝐫𝐭](https://t.me/+RqxzcGxXVZM0N2Vl)
│
├🔸🔔 **Bot Updates:** [𝐔𝐩𝐝𝐚𝐭𝐞𝐬](https://t.me/+rGt9jb6xI-w1ZDA1)
│
╰──────[ 😎 ]───────────⍟
"""
	ABOUT_DEV_TEXT = f"""

𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 𝐢𝐬 𝐒𝐮𝐩𝐞𝐫 𝐍𝐨𝐨𝐛. 𝐉𝐮𝐬𝐭 𝐋𝐞𝐚𝐫𝐧𝐢𝐧𝐠 𝐟𝐫𝐨𝐦 𝐎𝐟𝐟𝐢𝐜𝐢𝐚𝐥 𝐃𝐨𝐜𝐬. 𝐀𝐧𝐝 𝐒𝐞𝐞𝐤𝐢𝐧𝐠 𝐇𝐞𝐥𝐩 𝐅𝐫𝐨𝐦 𝐏𝐫𝐨 𝐂𝐨𝐝𝐞𝐫𝐬\

"""
	HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.
