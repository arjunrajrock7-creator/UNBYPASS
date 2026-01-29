# ⛩️ FILE STORE BOT | SHORTNER EDITION ⛩️

<p align="center">
  <img src="https://freeimage.host/i/fr18bpe" alt="Banner" width="100%">
</p>

<p align="center">
  <a href="https://t.me/anixzone"><img src="https://img.shields.io/badge/Telegram-Channel-blue?style=for-the-badge&logo=telegram" alt="Telegram"></a>
  <a href="https://render.com/deploy"><img src="https://img.shields.io/badge/Deploy%20To-Render-black?style=for-the-badge&logo=render" alt="Deploy"></a>
</p>

---

## 🌸 OVERVIEW
Welcome to the **@ALONEKINGSTAR77 File Store Bot**. This is a premium, high-performance Telegram bot designed specifically for secure file storage and link shortening with an advanced **Anime Themed Verification Flow**.

Built for speed, stability, and aesthetics, this bot ensures your files are safe while providing a seamless user experience with a specialized verification flow.

## ✨ FEATURES
- 🏮 **Anime Themed UI:** Dark aesthetics with neon, cyber, and sakura vibes.
- 🔐 **Secure Storage:** Store private files in authorized channels.
- 🔗 **Auto Shortener:** Mandatory link shortening for unverified users.
- 📢 **Unlimited Force Subscribe:** Enforce membership in multiple channels/groups.
- ⚡ **High Speed:** Built with Pyrogram and Motor for asynchronous performance.
- 🤖 **Render Ready:** Fully compatible with Render deployment out-of-the-box.
- 🎟️ **Premium System:** Built-in subscription management for power users.
- 🔄 **Auto-Delete:** Settable timer for message auto-deletion.
- 🛡️ **Anti-Bypass System:** Advanced time-based verification to block bypass tools.
- 🚫 **Auto-Ban:** Automatically bans users attempting to bypass verification.
- 🧩 **reCAPTCHA v3:** Invisible Google reCAPTCHA integration for bot protection.

## 🛠️ TECH STACK
- **Language:** Python 3.x
- **Framework:** Pyrogram (Telegram API)
- **Web Server:** Aiohttp
- **Database:** MongoDB (Motor)
- **Deployment:** Render / Docker

## 🚀 DEPLOYMENT STEPS (RENDER)
1. **Fork this repository.**
2. Create a new **Web Service** on [Render](https://render.com).
3. Connect your forked repository.
4. Set the **Start Command**: `python3 main.py`
5. Add all environment variables from `.env.example`.
6. Deploy!

## 🔐 ENVIRONMENT VARIABLES
| Variable | Description |
|---|---|
| `TG_BOT_TOKEN` | Your Telegram Bot Token from @BotFather |
| `APP_ID` | Your API ID from my.telegram.org |
| `API_HASH` | Your API Hash from my.telegram.org |
| `DATABASE_URL` | Your MongoDB Connection URI |
| `CHANNEL_ID` | The ID of your Database Channel |
| `FORCE_SUB_CHANNELS` | List of Channel IDs for Force Subscribe (Space separated) |
| `WEB_DOMAIN` | Your Render App URL (e.g., https://app.onrender.com) |
| `SHORTLINK_URL` | Your Shortener Domain (e.g., arolinks.com) |
| `SHORTLINK_API` | Your Shortener API Key |
| `RECAPTCHA_SITE_KEY` | Google reCAPTCHA v3 Site Key |
| `RECAPTCHA_SECRET_KEY` | Google reCAPTCHA v3 Secret Key |

## 🤖 COMMANDS
- `/start` - Start the bot.
- `/reset_short` - Reset your own shortener verification status.
- `/help` - Show help information.
- `/about` - About the bot.
- `/ban` - (Admin) Ban a user.
- `/unban` - (Admin) Unban a user.
- `/banlist` - (Admin) View list of banned users.
- `/reset_short <user_id>` - (Admin) Reset shortener for a specific user.

## 👑 CREDITS
- **Owner:** HEMANTH
- **Username:** [@ALONEKINGSTAR77](https://t.me/anixzone)
- **Telegram Support:** [Join @anixzone](https://t.me/anixzone)

---

<p align="center">
  Developed with 💙 by <b>@ALONEKINGSTAR77</b>
</p>
