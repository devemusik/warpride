from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAIp9mBtwBBZGywWEmV-WC8gcMArjusuAAKMAgACTp1xV6m-mtC1YTfoHgQ")
    await message.reply_text(
        f"""<b>Alo {message.from_user.first_name}!
\nAing bisa nyetel musik keur sia, buatan si goblog @developerantibucin ❤
\nBisi dek make bot urang sok we asupkeun ngan loba minusan siga hirup sia.
\n ketik /help bisi sia teu ngarti.
\n Bot Official @DVMusikGrup_Bot.
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🤡 U.S.E.P", url="https://t.me/joinchat/J9MT9gn61MAwYzll",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🎭 Follow Instagram", url="https://www.instagram.com/irfanxirxyz"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/dvantibucin"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/DVMusikGrup_Bot?startgroup=true"
                    ) 
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Sia hayang neang bahan di yutup?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/dvantibucin"
                    ),
                    InlineKeyboardButton(
                        "🤡 U.S.E.P", url="https://t.me/joinchat/J9MT9gn61MAwYzll"
                    )
                ],    
                [    
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
\n/play <song name> - play song you requested
/dplay <song name> - play song you requested via deezer
/splay <song name> - play song you requested via jio saavn
/playlist - Show now playing list
/current - Show now playing
/song <song name> - download songs you want quickly
/search <query> - search videos on youtube with details
/deezer <song name> - download songs you want quickly via deezer
/saavn <song name> - download songs you want quickly via saavn
/video <song name> - download videos you want quickly
\n*Admins only*
/player - open music player settings panel
/pause - pause song play
/resume - resume song play
/skip - play next song
/end - stop music play
/userbotjoin - invite assistant to your chat
/admincache - Refresh admin list
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Thanks To!", url="https://t.me/LaylaList"
                    ),
                    InlineKeyboardButton(
                        "🤡 U.S.E.P", url="https://t.me/joinchat/J9MT9gn61MAwYzll"
                    )
                ]
            ]
        )
    )    
