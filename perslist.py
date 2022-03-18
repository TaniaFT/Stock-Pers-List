import string
import requests
import datetime
from config import api_key
import perslistClasses
import sys
reload(sys)
sys.setdefaultencoding('utf8')

safechars = string.ascii_lowercase + string.ascii_uppercase + string.digits + '.-,<>" &/()+%'

per_page = 250

r = requests.get(
    'https://api.notonthehighstreet.com/api/v1/orders?token={}&state=placed&per_page='.format(api_key)
    + str(per_page))
callsNeeded = (r.json()["query"]["total"] / per_page) + 1

traceList = []
traceA5List = []
letterList = []
genList = []
sockList = []
embList = []
feltList = []
jewelList = []

for x in range(0, callsNeeded):
    r = requests.get(
        'https://api.notonthehighstreet.com/api/v1/orders?token={}&state=placed&per_page='.format(api_key)
        + str(per_page) + "&offset=" + str(per_page * x))
    for order in r.json()["data"]:
        if order["dispatch_overdue"]:
            continue
        for item in order["items"]:
            if ("bookmark" in item["item_title"].lower() or
                    "face mask" in item["item_title"].lower() or
                    "cat socks" in item["item_title"].lower() or
                    "photo" in item["item_title"].lower() or
                    "headband" in item["item_title"].lower() or
                    "bridesmaid" in item["item_title"].lower() or
                    "keyring" in item["item_title"].lower()):
                continue

            if "gold foil birth" in item["item_title"].lower():
                if "insert" in item["options"][1]["name"].lower() and "insert" in item["options"][1]["value"].lower():
                    newItem = perslistClasses.TracingProductItem(item)
                    traceList.append(newItem)

            if "choose your 'birth" in item["item_title"].lower():
                if ("insert" in item["options"][-1]["name"].lower() and "insert" in item["options"][-1]["value"].lower() or
                        "insert" in item["options"][-2]["name"].lower() and "insert" in item["options"][-2]["value"].lower()):
                    newItem = perslistClasses.A5TracingProductItem(item)
                    traceA5List.append(newItem)

            if "dandelion" in item["item_title"].lower() or "letterbox gift" in item["item_title"].lower():
                if "card" in item["options"][-2]["name"].lower() and "no" not in item["options"][-2]["value"].lower():
                    newItem = perslistClasses.LetterboxProductItem(item)
                    letterList.append(newItem)

            if "cat paw print" in item["item_title"].lower() and "no" not in item["options"][1]["value"]:
                newItem = perslistClasses.LetterboxProductItem(item)
                letterList.append(newItem)

            if "socks" in item["item_title"].lower() and "men" in item["item_title"].lower() and "name" in item["options"][0]["name"].lower():
                newItem = perslistClasses.MenSockProductItem(item)
                sockList.append(newItem)

            if "hobby socks" in item["item_title"].lower():
                newItem = perslistClasses.HobbySockProductItem(item)
                sockList.append(newItem)

            if "socks" in item["item_title"].lower() and "name" in item["options"][0]["name"].lower():
                newItem = perslistClasses.SockProductItem(item)
                sockList.append(newItem)

            if ("embroider" in item["options"][1]["name"].lower() and "yes" in item["options"][1]["value"].lower()) or "embroider" in item["options"][1]["value"]:
                newItem = perslistClasses.ColourEmbroideredProductItem(item)
                embList.append(newItem)

            if ("embroider" in item["options"][0]["name"].lower() and "yes" in item["options"][0]["value"].lower()) or "embroider" in item["options"][0]["value"]:
                newItem = perslistClasses.EmbroideredProductItem(item)
                embList.append(newItem)

            if "felt" in item["options"][1]["value"].lower():
                newItem = perslistClasses.FeltedProductItem(item)
                feltList.append(newItem)

            if "bracelet" in item["item_title"].lower() or "necklace" in item["item_title"].lower() or "earrings" in item["item_title"].lower():
                if "gift card" in item["options"][-2]["name"].lower() and "yes" in item["options"][-2]["value"].lower():
                    newItem = perslistClasses.JewelleryProductItem(item)
                    jewelList.append(newItem)

            if "personalise" in item["options"][1]["name"].lower() and "yes" in item["options"][1]["value"].lower() and "embroider" not in item["options"][1]["value"].lower():
                newItem = perslistClasses.BasicProductItem(item)
                genList.append(newItem)


traceList = sorted(traceList, key=lambda TracingProductItem: TracingProductItem.personalisationString)
traceA5List = sorted(traceA5List, key=lambda A5TracingProductItem: A5TracingProductItem.personalisationString)
embList = sorted(embList, key=lambda BasicProductItem: BasicProductItem.itemTitle)

def printTest(listChoice):
    for printItem in listChoice:
        print(printItem.fullName())


printTest(traceList)
printTest(traceA5List)
printTest(letterList)
printTest(jewelList)
printTest(sockList)
printTest(embList)
printTest(feltList)
printTest(genList)


today_as_string = datetime.datetime.now().strftime('%d-%m-%y')
fMain = open("perslist-" + today_as_string + ".txt", "w")
fMain.write("NOTHS PERSONALISATION: " + today_as_string)

def writeTo(chosenList, listName):
    fMain.write("\n-------------" + listName + "----------------\n \n")
    for printItem in chosenList:
        fMain.write(printItem.fullName() + '\n')
    return


writeTo(traceList, "A6 Inserts")
writeTo(traceA5List, "A5 Inserts")
writeTo(letterList, "A6 Cards")
writeTo(jewelList, "Jewellery")
writeTo(sockList, "Sock Labels")
writeTo(embList, "Embroidery")
writeTo(feltList, "Felting")
writeTo(genList, "Misc")



fMain.close()
