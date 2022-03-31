import requests
import datetime
from config import api_key
import string

safechars = string.ascii_lowercase + string.ascii_uppercase + string.digits + '.- /&()%\n'

per_page = 250

r = requests.get(
    'https://api.notonthehighstreet.com/api/v1/orders?token={}&state=accepted&per_page='.format(api_key)
    + str(per_page))
callsNeeded = (r.json()["query"]["total"] / per_page) + 1

stocklist = {}
for x in range(0, int(callsNeeded)):
    r = requests.get(
        'https://api.notonthehighstreet.com/api/v1/orders?token={}&state=accepted&per_page='.format(api_key)
        + str(per_page) + "&offset=" + str(per_page * x))
    for order in r.json()["data"]:
        if order["dispatch_overdue"]:
            continue
        for item in order["items"]:
            if ("bookmark" in item["item_title"].lower() or
                    "brooch" in item["item_title"].lower() or
                    "face mask" in item["item_title"].lower() or
                    "belt" in item["item_title"].lower() or
                    "bracelet" in item["item_title"].lower() or
                    "necklace" in item["item_title"].lower() or
                    "earrings" in item["item_title"].lower() or
                    "brooch" in item["item_title"].lower() or
                    "coffee" in item["item_title"].lower() or
                    "cat socks" in item["item_title"].lower() or
                    "cheese knife" in item["item_title"].lower() or
                    "tea towel" in item["item_title"].lower() or
                    "photo" in item["item_title"].lower() or
                    "keyring" in item["item_title"].lower()):
                continue
            extra = ""
            if len(item["options"]) > 0 and (
                    "style" in item["options"][0]["name"].lower() or
                    "animal" in item["options"][0]["name"].lower() or
                    "month" in item["options"][0]["name"].lower() or
                    "colour" in item["options"][0]["name"].lower()):
                extra = " - " + item["options"][0]["value"]
            itemName = item["item_title"] + extra
            itemName = itemName.replace('Personalised ', '')
            itemName = ''.join([c for c in itemName if c in safechars])

            if itemName not in stocklist:
                stocklist[itemName] = item["quantity"]
            else:
                stocklist[itemName] = stocklist[itemName] + item["quantity"]


today_as_string = datetime.datetime.now().strftime('%d-%m-%y')
fMain = open("stocklist-" + today_as_string + ".txt", "w")
fMain.write("NOTHS STOCKLIST: " + today_as_string)

sortedKeys = list(stocklist.keys())
sortedKeys.sort()

sockList = []
gloveList = []
foilList = []
genList = []
for search in sortedKeys:
    if "socks" in search.lower():
       sockList.append(search)
    elif "gloves" in search.lower() or "beret" in search.lower() or "headband" in search.lower() or "hat" in search.lower():
        gloveList.append(search)
    elif "foil" in search.lower() or "letterbox" in search.lower():
        foilList.append(search)
    else:
        genList.append(search)


def writeTo(chosenList, listName):
    fMain.write("\n-------------" + listName + "----------------\n \n")
    for line in chosenList:
        fMain.write(str(stocklist[line]) + " x " + line + "\n")
    return

writeTo(genList, "GENERAL")
writeTo(sockList, "SOCKS")
writeTo(gloveList, "GLOVES")
writeTo(foilList, "FOIL")

fMain.close()