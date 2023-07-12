from discord_notifier import send_discord_hook

def process(data):
    pullrequest = data['pullrequest']
    actor = data['actor']

    return send_discord_hook(pullrequest['title'], pullrequest['description'], data['pullrequest']['links']['html']['href'],
                      "5814783", actor['display_name'], data['actor']['links']['avatar']['href'],
                      pullrequest['created_on'], os.getenv('DISCORD_WEBHOOK'))
