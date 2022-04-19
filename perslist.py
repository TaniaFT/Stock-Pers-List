import requests
import datetime
from config import api_key
import perslistClasses

per_page = 250

# "&state=dispatched&estimated_dispatch_at%5Bfrom%5D=2022-04-19" - change date to current and replace order_status below, to check orders already dispatched

order_status = "accepted"

r = requests.get(
    'https://api.notonthehighstreet.com/api/v1/orders?token={}&state={}&per_page='.format(
        api_key, order_status)
    + str(per_page))
callsNeeded = (r.json()["query"]["total"] / per_page) + 1

# Creating empty lists for each style of personalisation, to append to later
traceList = []
traceA5List = []
letterList = []
genList = []
sockList = []
embList = []
feltList = []
jewelList = []

for x in range(0, int(callsNeeded)):
    r = requests.get(
    'https://api.notonthehighstreet.com/api/v1/orders?token={}&state={}&per_page='.format(
            api_key, order_status)
        + str(per_page) + "&offset=" + str(per_page * x))
    for order in r.json()["data"]:
        if order["dispatch_overdue"]:
            continue
        for item in order["items"]:
            if ("bookmark" in item["item_title"].lower() or
                    # NOTE FOR USERS - ADD ERROR-CAUSING PRODUCT TITLES HERE, IN SAME FORMAT AS BELOW LINES
                    "face mask" in item["item_title"].lower() or
                    "cat socks" in item["item_title"].lower() or
                    " bag " in item["item_title"].lower() or
                    "headband" in item["item_title"].lower() or
                    "bridesmaid" in item["item_title"].lower() or
                    "key holder" in item["item_title"].lower() or
                    "floral bird" in item["item_title"].lower() or
                    "tea towel" in item["item_title"].lower() or
                    " tie " in item["item_title"].lower() or
                    "and sun" in item["item_title"].lower() or
                    "brooch" in item["item_title"].lower() or
                    "initial charm" in item["item_title"].lower() or
                    "keyring" in item["item_title"].lower()):
                continue

            # Checks titles and personalisation details for each order, adding to required lists as objects using relevant class

            if "birth " in item["item_title"].lower():
                if "gold foil" in item["item_title"].lower() and "insert" in item["options"][1]["name"].lower() and "insert" in item["options"][1]["value"].lower():
                        newItem = perslistClasses.TwoOptionItem(item, 0, -1)
                        traceList.append(newItem)
                elif "eco" in item["item_title"].lower():
                    newItem = perslistClasses.TwoOptionItem(item, 0, 1)
                    genList.append(newItem)
                    if "insert" in item["options"][2]["name"].lower() and "insert" in item["options"][2]["value"].lower():
                        newItem = perslistClasses.TwoOptionItem(item, 0, -1)
                        traceList.append(newItem)
                elif "choose your '" in item["item_title"].lower():
                    if ("insert" in item["options"][-1]["name"].lower() and "insert" in item["options"][-1]["value"].lower() or
                            "insert" in item["options"][-2]["name"].lower() and "insert" in item["options"][-2][
                                "value"].lower()):
                        newItem = perslistClasses.TwoOptionItem(item, 1, -1)
                        traceA5List.append(newItem)

            elif "dandelion" in item["item_title"].lower() or "letterbox gift" in item["item_title"].lower():
                if "cat paw print" in item["item_title"].lower() and "no" not in item["options"][1]["value"]:
                    newItem = perslistClasses.BasicProductItem(item, -1)
                    letterList.append(newItem)
                if "card" in item["options"][-2]["name"].lower() and "no" not in item["options"][-2]["value"].lower():
                    newItem = perslistClasses.TwoOptionItem(item, -2, -1)
                    letterList.append(newItem)

            elif "baby play mat" in item["item_title"].lower():
                if "animal" in item["item_title"].lower() and "yes" in item["options"][1]["value"].lower():
                    newItem = perslistClasses.TwoOptionItem(item, 0, -2)
                    genList.append(newItem)
                elif "animal" not in item["item_title"].lower() and "yes" in item["options"][0]["value"].lower():
                    newItem = perslistClasses.BasicProductItem(item, -2)
                    genList.append(newItem)

            elif "milestone" in item["item_title"].lower():
                newItem = perslistClasses.BasicProductItem(item, 1)
                genList.append(newItem)

            elif ("embroider" in item["options"][0]["name"].lower() and "yes" in item["options"][0]["value"].lower()) or "embroider" in item["options"][0]["value"]:
                newItem = perslistClasses.BasicProductItem(item, 1)
                embList.append(newItem)

            elif ("embroider" in item["options"][1]["name"].lower() and "yes" in item["options"][1]["value"].lower()) or "embroider" in item["options"][1]["value"]:
                newItem = perslistClasses.ThreeOptionItem(item, 0, 1, 2)
                embList.append(newItem)

            elif "felt" in item["options"][1]["value"].lower():
                newItem = perslistClasses.TwoOptionItem(item, 0, 2)
                feltList.append(newItem)

            elif "bracelet" in item["item_title"].lower() or "necklace" in item["item_title"].lower() or "earrings" in item["item_title"].lower():
                if "locket" in item["item_title"].lower() and "card" in item["options"][-2]["name"].lower():
                    newItem = perslistClasses.TwoOptionItem(item, -2, -1)
                    jewelList.append(newItem)
                elif "globe" in item["item_title"].lower() or "clover" in item["item_title"].lower() and "yes" in item["options"][2]["value"].lower():
                    newItem = perslistClasses.TwoOptionItem(item, -2, -1)
                    jewelList.append(newItem)
                elif "card" in item["options"][-2]["name"].lower() and "yes" in item["options"][-2]["value"].lower() and "delicate birth" in item["item_title"].lower():
                    newItem = perslistClasses.TwoOptionItem(item, 0, -1)
                    jewelList.append(newItem)
                elif "card" in item["options"][-2]["name"].lower() and ("yes" in item["options"][-2]["value"].lower() or "no" not in item["options"][-2]["value"].lower()):
                    newItem = perslistClasses.BasicProductItem(item, -1)
                    jewelList.append(newItem)

            elif "personalis" in item["options"][0]["name"].lower() and "yes" in item["options"][0]["value"].lower():
                if "eco colour" in item["item_title"].lower() or "summer colourblock" in item["item_title"].lower():
                    newItem = perslistClasses.TwoOptionItem(item, 1, 2)
                    genList.append(newItem)
                else:
                    newItem = perslistClasses.BasicProductItem(item, 1)
                    genList.append(newItem)

            elif "socks" in item["item_title"].lower():
                if "men" in item["item_title"].lower() or "name" in item["options"][0]["name"].lower():
                    newItem = perslistClasses.BasicProductItem(item, 0)
                    sockList.append(newItem)
                elif "hobby socks" in item["item_title"].lower():
                    newItem = perslistClasses.BasicProductItem(item, 3)
                    sockList.append(newItem)
                elif "wise owl" in item["item_title"].lower() or "fleur" in item["item_title"].lower():
                    newItem = perslistClasses.BasicProductItem(item, 1)
                    sockList.append(newItem)



# Sorts relevant lists into alphabetical order, ready for writing to final doc. Note, some are sorted by product name, others by personalisation
traceList = sorted(traceList, key=lambda TracingProductItem: TracingProductItem.personalisationString)
traceA5List = sorted(traceA5List, key=lambda A5TracingProductItem: A5TracingProductItem.personalisationString)
embList = sorted(embList, key=lambda EmbroideredProductItem: EmbroideredProductItem.itemTitle)
feltList = sorted(feltList, key=lambda FeltedProductItem: FeltedProductItem.itemTitle)
genList = sorted(genList, key=lambda BasicProductItem: BasicProductItem.itemTitle)


# Function for using console to test, rather than writing in full. Use currently double-commented line below, with desired list
def printTest(listChoice):
    for printItem in listChoice:
        print(printItem.fullName())

## printTest(traceList)


# Creates a file with date based name, and adds title line
today_as_string = datetime.datetime.now().strftime('%d-%m-%y')
fMain = open("perslist-" + today_as_string + ".txt", "w")
fMain.write("NOTHS PERSONALISATION: " + today_as_string)


# Function to write the title of a product type, followed by full name and personalisation of product objects in specified list
def writeTo(chosenList, listName, spacing):
    fMain.write("\n-------------" + listName + "----------------\n \n")
    for printItem in chosenList:
        fMain.write(printItem.fullName() + spacing)
    return

def traceWriteTo(chosenList, listName):
    fMain.write("\n-------------" + listName + "----------------\n \n")
    for printItem in chosenList:
        fMain.write(printItem.personalisationString + '\n')
    return


# Calling above functions to write to file
traceWriteTo(traceList, "A6 Inserts")
traceWriteTo(traceA5List, "A5 Inserts")
writeTo(letterList, "A6 Cards", '\n \n')
writeTo(jewelList, "Jewellery", '\n \n')
writeTo(sockList, "Sock Labels", '\n')
writeTo(genList, "Misc", '\n')
writeTo(embList, "Embroidery", '\n')
writeTo(feltList, "Felting", '\n')


fMain.close()