from aiohttp import web
import aiohttp
import time
from config import OWNER, RECAPTCHA_SITE_KEY, RECAPTCHA_SECRET_KEY, SHORTLINK_URL, SHORTLINK_API, WEB_DOMAIN
from database.database import db
from helper_func import get_shortlink

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("@ALONEKINGSTAR77 Shortner")

@routes.get("/go")
async def go_handler(request):
    payload = request.query.get("payload")
    user_id = request.query.get("user_id")
    token = request.query.get("token")

    if not all([payload, user_id, token]):
        return web.Response(text="Missing parameters", status=400)

    try:
        user_id = int(user_id)
    except ValueError:
        return web.Response(text="Invalid User ID", status=400)

    if await db.ban_user_exist(user_id):
        return web.Response(text="Bypass detected. You are permanently banned.", status=403)

    user_status = await db.get_verify_status(user_id)
    if user_status.get('verify_token') != token:
        return web.Response(text="Invalid or expired token. Please get a new link from the bot.", status=403)

    # Set verification start time
    await db.update_verify_start_time(user_id, time.time())

    # Generate shortlink
    verify_url = f"{WEB_DOMAIN}/verify?payload={payload}&user_id={user_id}"
    try:
        shortlink = await get_shortlink(SHORTLINK_URL, SHORTLINK_API, verify_url)
    except Exception as e:
        print(f"Error generating shortlink in web route: {e}")
        # Fallback to direct link if shortener fails (not ideal but keeps it working)
        return web.HTTPFound(verify_url)

    return web.HTTPFound(shortlink)

@routes.get("/verify")
async def verify_page(request):
    payload = request.query.get("payload")
    user_id = request.query.get("user_id")
    if not payload:
        return web.Response(text="Missing payload", status=400)

    if user_id:
        try:
            if await db.ban_user_exist(int(user_id)):
                return web.Response(text="Bypass detected. You are permanently banned.", status=403)
        except ValueError:
            pass

    recaptcha_widget = ""
    if RECAPTCHA_SITE_KEY:
        recaptcha_widget = f"""
        <script src="https://www.google.com/recaptcha/api.js?render={RECAPTCHA_SITE_KEY}"></script>
        <input type="hidden" id="g-recaptcha-response" name="g-recaptcha-response">
        <script>
            grecaptcha.ready(function() {{
                grecaptcha.execute('{RECAPTCHA_SITE_KEY}', {{action: 'verify'}}).then(function(token) {{
                    document.getElementById('g-recaptcha-response').value = token;
                }});
            }});
        </script>
        """

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Verification | @ALONEKINGSTAR77</title>
        <style>
            body {{
                margin: 0;
                padding: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: #0f0c29;
                background: linear-gradient(to right, #24243e, #302b63, #0f0c29);
                color: white;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                overflow: hidden;
            }}
            .container {{
                background: rgba(0, 0, 0, 0.7);
                padding: 40px;
                border-radius: 20px;
                box-shadow: 0 0 20px rgba(0, 255, 255, 0.5);
                text-align: center;
                border: 2px solid #00ffff;
                max-width: 400px;
                width: 90%;
                position: relative;
            }}
            h1 {{
                font-size: 24px;
                margin-bottom: 20px;
                color: #ff00ff;
                text-shadow: 0 0 10px #ff00ff;
                font-family: 'Courier New', Courier, monospace;
            }}
            p {{
                margin-bottom: 30px;
                font-size: 16px;
                color: #00ffff;
            }}
            button {{
                background: transparent;
                border: 2px solid #ff00ff;
                color: #ff00ff;
                padding: 10px 30px;
                font-size: 18px;
                border-radius: 50px;
                cursor: pointer;
                transition: 0.3s;
                text-transform: uppercase;
                letter-spacing: 2px;
                font-weight: bold;
            }}
            button:hover {{
                background: #ff00ff;
                color: white;
                box-shadow: 0 0 20px #ff00ff;
            }}
            .container::before {{
                content: "⛩️";
                font-size: 50px;
                position: absolute;
                top: -30px;
                left: 50%;
                transform: translateX(-50%);
                background: #0f0c29;
                padding: 0 10px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>SYSTEM VERIFICATION</h1>
            <p>Prove you are not a Baka! Click the button to access your file.</p>
            <form action="/verify_token" method="POST">
                <input type="hidden" name="payload" value="{payload}">
                <input type="hidden" name="user_id" value="{user_id if user_id else ''}">
                {recaptcha_widget}
                <button type="submit">UNLOCK FILE</button>
            </form>
        </div>
    </body>
    </html>
    """
    return web.Response(text=html_content, content_type='text/html')

@routes.post("/verify_token")
async def verify_token(request):
    data = await request.post()
    payload = data.get("payload")
    user_id = data.get("user_id")

    if not payload:
        return web.Response(text="Invalid Request", status=400)

    if user_id:
        try:
            if await db.ban_user_exist(int(user_id)):
                return web.Response(text="Bypass detected. You are permanently banned.", status=403)
        except ValueError:
            pass

    if RECAPTCHA_SECRET_KEY:
        recaptcha_response = data.get("g-recaptcha-response")
        if not recaptcha_response:
            return web.Response(text="Please complete the reCAPTCHA", status=400)

        async with aiohttp.ClientSession() as session:
            async with session.post("https://www.google.com/recaptcha/api/siteverify", data={
                "secret": RECAPTCHA_SECRET_KEY,
                "response": recaptcha_response
            }) as resp:
                result = await resp.json()
                # For v3, we check success and optionally score
                if not result.get("success") or result.get("score", 1.0) < 0.5:
                    return web.Response(text=f"reCAPTCHA verification failed. Score: {result.get('score', 'N/A')}", status=400)

    bot_username = (await request.app['bot'].get_me()).username
    return web.HTTPFound(f"https://t.me/{bot_username}?start=yu3elk{payload}7")
