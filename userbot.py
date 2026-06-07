from telethon import TelegramClient, events

# ✅ নিচে তোমার API ID এবং HASH বসাও
API_ID = 35558481          # তোমার api_id এখানে
API_HASH = "1d844047bd1d2069069b528637c90c00"  # তোমার api_hash এখানে

# ✅ অটো রিপ্লাই মেসেজ (চাইলে বদলাও)
MESSAGE_1 = """✨ DKWin ✨
🎨 Color Trading Platform 🎨

━━━━━━━━━━━━━━━━━━━
💼 আমাদের সাথে কাজ করলে ইনশাল্লাহ ভালো প্রফিট করার সুযোগ পাবেন
━━━━━━━━━━━━━━━━━━━

🔗 Registration Link 👇
https://dkwin9.com/#/register?invitationCode=186731981267

━━━━━━━━━━━━━━━━━━━
📩 এটি একটি অটো রিপ্লাই সেট করা
🙏 অনুগ্রহ করে কেউ বিরক্ত হবেন না
━━━━━━━━━━━━━━━━━━━"""

MESSAGE_2 = """একটু অপেক্ষা করো ভাই! ⏳
শীঘ্রই রিপ্লাই দিচ্ছি।"""

MESSAGE_3 = """ভাই দেখামাত্র রিপ্লাই করবো! 🙏"""

# কে কতবার মেসেজ দিয়েছে মনে রাখবে
user_count = {}

# Telegram Client তৈরি করো
client = TelegramClient('glitch_userbot', API_ID, API_HASH)

# নতুন মেসেজ পেলে এই ফাংশন চলবে
@client.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def handler(event):
    uid = event.sender_id

    # এই মানুষ কতবার মেসেজ পাঠিয়েছে?
    if uid not in user_count:
        user_count[uid] = 0
    user_count[uid] += 1
    count = user_count[uid]

    # যে পাঠিয়েছে তার নাম নিয়ে আসো
    sender = await event.get_sender()
    name = sender.first_name if sender else "কেউ"
    
    # Console-এ দেখাও (শুধু লগের জন্য)
    print(f"📩 {name} → মেসেজ #{count}")

    # প্রথম মেসেজে MESSAGE_1 পাঠাও
    if count == 1:
        await event.reply(MESSAGE_1)
    # দ্বিতীয় মেসেজে MESSAGE_2 পাঠাও
    elif count == 2:
        await event.reply(MESSAGE_2)
    # তৃতীয় এবং তার পর থেকে MESSAGE_3
    else:
        await event.reply(MESSAGE_3)

# Bot চালু করো
print("✅ Userbot চলছে...")
client.start()
client.run_until_disconnected()
