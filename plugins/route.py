from aiohttp import web
import aiohttp
from config import OWNER

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("@ALONEKINGSTAR77 Shortner")

@routes.get("/verify")
async def verify_page(request):
    payload = request.query.get("payload")
    if not payload:
        return web.Response(text="Missing payload", status=400)

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

    if not payload:
        return web.Response(text="Invalid Request", status=400)

    bot_username = (await request.app['bot'].get_me()).username
    return web.HTTPFound(f"https://t.me/{bot_username}?start=yu3elk{payload}7")
