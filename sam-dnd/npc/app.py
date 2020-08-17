import json
import random
import textwrap
from tinydb import TinyDB, Query
import logging

# ! Doesn't work moving to sam
# ! Add structured logging
# ! Add dataclass for NPC card
# ! Tinydb doesn't find json file
# 
# import requests

wrapper = textwrap.TextWrapper(width=60)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e
    #db = TinyDB("legends.json")
    genders = ["Female", "Male"]
    stats_lst = ["str", "dex", "int", "con", "cha", "wis"]
    page = ''
    
    #race, desc = race_search()

    #page += ("Race: {0}\n".format(race))
    # page += ("Race Descriptions: \n\n{0}\n".format(wrapper.fill(text=desc)))
    page += ("Gender: {0}\n".format(genders[roll(1, len(genders), -1)]))
    page += ("Stats:")
    for i in stats_lst:
        page += ("\t{0}:\t{1}".format(i.capitalize(), roll(3, 6)))

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": page,
            # "location": ip.text.replace("\n", "")
        }),
    }


def roll(to_roll, high, modifier=0):
    """ because adding #nosec everwhere would be a drag"""
    i = 1
    total = 0
    while i <= to_roll:
        total += random.randint(1, high)  # nosec
        i += 1
    total += modifier
    return total


# def race_search():
#     """lookup against table 101 with optional table 101b"""
#     race_roll = roll(1, 20)
#     my_race = ""
#     my_desc = ""

#     if race_roll == 20:
#         table = db.table("101a")
#         race_roll = roll(1, 10)
#     else:
#         table = db.table("101")

#     result = Query()
#     result = table.search((result.low <= race_roll) & (result.high >= race_roll))[0]

#     return result["race"], result["desc"]

