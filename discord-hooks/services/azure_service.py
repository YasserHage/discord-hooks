import os

from ..discord.discord_notifier import send_discord_hook
from ..discord.discord_utils import create_field


def process(data):
    fields = []
    reviewers_list = ""
    pullrequest = data['resource']
    actor = pullrequest['createdBy']
    reviewers = pullrequest['reviewers']

    for reviewer in reviewers:
        reviewers_list += "- " + reviewer['displayName'] + "\n"
    if reviewers_list != "":
        fields.append(create_field("Reviewers", reviewers_list))

    fields.append(create_field("From", "> " + pullrequest['sourceRefName']))
    fields.append(create_field("To", "> " + pullrequest['targetRefName']))

    return send_discord_hook(actor['display_name'] + " [Azure Devops]", actor['imageUrl'], pullrequest['title'],
                             pullrequest['description'],
                             data['url'], "5814783", fields, pullrequest['repository']['name'],
                             pullrequest['creationDate'][:-5] + "Z", os.getenv('DISCORD_WEBHOOK'))
