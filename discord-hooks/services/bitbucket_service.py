import os

from ..discord.discord_notifier import send_discord_hook
from ..discord.discord_utils import create_field


def process(data):
    fields = []
    reviewers_list = ""
    pullrequest = data['pullrequest']
    actor = data['actor']

    reviewers = pullrequest['reviewers']

    for reviewer in reviewers:
        reviewers_list += "- " + reviewer['display_name'] + "\n"
    if reviewers_list != "":
        fields.append(create_field("Reviewers", reviewers_list))

    fields.append(create_field("From", "> " + pullrequest['source']['branch']['name']))
    fields.append(create_field("To", "> " + pullrequest['destination']['branch']['name']))

    return send_discord_hook(actor['display_name'] + " [BitBucket]", actor['links']['avatar']['href'],
                             pullrequest['title'], pullrequest['description'], pullrequest['links']['html']['href'],
                             "5814783", fields, pullrequest['source']['repository']['name'], pullrequest['created_on'],
                             os.getenv('DISCORD_WEBHOOK'))
