import requests


def send_discord_hook(username, avatar_url, title, description, title_url, color, fields, footer, time, webhook_url):
    payload = {
        "username": username,
        "avatar_url": avatar_url,
        "embeds": [
            {
                "title": title,
                "description": description,
                "url": title_url,
                "color": color,
                "fields": fields,
                "footer": {
                    "text": footer
                },
                "timestamp": time
            }
        ]
    }
    return requests.post(webhook_url, json=payload)
