from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import command, other_filters2, other_filters



@Client.on_message(command("help") & other_filters2)
async def helper(ok, message: Message):
    await message.reply_text(
        f"""💞 مرحبا الاوامر المتوفرة هي كالتالي **{bn}** - __A الاوامر المتاحة لتشغيل اغنية:

🔥 ** اوامر الاعضاء :**
⚜️ /play - **[ في الكروب فقط ]** > __لتشغيل ملف صوتي بالرد عليه او من خلال الرابط.__
⚜️ /song - **[ في الكروب & الخاص ]** > __لتحميل اغنية عن طريق كتبتة الامر ومعه اسم الاغنية.__
⚜️ /ytplay - **[ في الكروب فقط ]** > __لتشغيل الاغنية عن طريق الاسم فقط.__
⚜️ /repo - **[ الخاص فقط ]** > __Gets the source code and YouTube Tutorial Video.__


🔰 **اوامر الادمنية & المطور :**
⚜️ /pause - **[الكروب فقط ]** > __ايقاف التشغيل مؤقتا.__
⚜️ /resume - **[Groups Only ]** > __اطمال التشغيل.__
⚜️ /skip - **[Groups Only ]** > __تخطي الاغنية.__
⚜️ /stop - **[Groups Only ]** > __ ايقاف الاغنية.__""")

@Client.on_message(command("help") & other_filters)
async def ghelp(_, message: Message):
    await message.reply_text(f"**{bn} :-** راسلني بالخاص حتى انطيك كل الاوامر 😉")
