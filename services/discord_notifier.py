import requests

def send_discord_hook(title, description, title_url, color, footer, footer_icon_url, time, webhook_url):
    payload = {
        "embeds": [
            {
                "title": title,
                "description": description,
                "url": title_url,
                "color": color,
                "footer": {
                    "text": footer,
                    "icon_url": footer_icon_url
                },
                "timestamp": time
            }
        ]
    }
    return requests.post(webhook_url, json=payload)