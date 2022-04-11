import requests
import datetime
from config import api_key
import perslistClasses

per_page = 250

# &state=dispatched&estimated_dispatch_at%5Bfrom%5D=2022-04-07 - change date to current and replace '&state=accepted' in links below, to check orders already dispatched

r = requests.get(
    'https://api.notonthehighstreet.com/api/v1/orders?token={}&state=accepted&per_page='.format(
        api_key)
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
        'https://api.notonthehighstreet.com/api/v1/orders?token={}&state=accepted&per_page='.format(
            api_key)
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

            if "gold foil birth" in item["item_title"].lower():
                if "insert" in item["options"][1]["name"].lower() and "insert" in item["options"][1]["value"].lower():
                    newItem = perslistClasses.TracingProductItem(item)
                    traceList.append(newItem)

            if "eco birth" in item["item_title"].lower():
                newItem = perslistClasses.EcoBirthProductItem(item)
                genList.append(newItem)
                if "insert" in item["options"][2]["name"].lower() and "insert" in item["options"][2]["value"].lower():
                    newItem = perslistClasses.TracingProductItem(item)
                    traceList.append(newItem)

            if "choose your 'birth" in item["item_title"].lower():
                if ("insert" in item["options"][-1]["name"].lower() and "insert" in item["options"][-1]["value"].lower() or
                        "insert" in item["options"][-2]["name"].lower() and "insert" in item["options"][-2][
                            "value"].lower()):
                    newItem = perslistClasses.A5TracingProductItem(item)
                    traceA5List.append(newItem)

            if "dandelion" in item["item_title"].lower() or "letterbox gift" in item["item_title"].lower():
                if "card" in item["options"][-2]["name"].lower() and "no" not in item["options"][-2]["value"].lower():
                    newItem = perslistClasses.LetterboxProductItem(item)
                    letterList.append(newItem)

            if "cat paw print" in item["item_title"].lower() and "no" not in item["options"][1]["value"]:
                newItem = perslistClasses.LetterboxProductItem(item)
                letterList.append(newItem)

            if "baby play mat" in item["item_title"].lower():
                if "animal" in item["item_title"].lower() and "yes" in item["options"][1]["value"].lower():
                    newItem = perslistClasses.ChoosePlayProductItem(item)
                    genList.append(newItem)
                if "animal" not in item["item_title"].lower() and "yes" in item["options"][0]["value"].lower():
                    newItem = perslistClasses.PlainPlayProductItem(item)
                    genList.append(newItem)

            if "milestone cotton" in item["item_title"].lower() and "blanket" in item["item_title"].lower():
                newItem = perslistClasses.SockProductItem(item)
                genList.append(newItem)

            if ("embroider" in item["options"][0]["name"].lower() and "yes" in item["options"][0]["value"].lower()) or "embroider" in item["options"][0]["value"]:
                newItem = perslistClasses.EmbroideredProductItem(item)
                embList.append(newItem)

            if ("embroider" in item["options"][1]["name"].lower() and "yes" in item["options"][1]["value"].lower()) or "embroider" in item["options"][1]["value"]:
                newItem = perslistClasses.ColourEmbroideredProductItem(item)
                embList.append(newItem)

            if "felt" in item["options"][1]["value"].lower():
                newItem = perslistClasses.FeltedProductItem(item)
                feltList.append(newItem)

            if "bracelet" in item["item_title"].lower() or "necklace" in item["item_title"].lower() or "earrings" in item["item_title"].lower():
                if "locket" in item["item_title"].lower() and "card" in item["options"][-2]["name"].lower():
                    newItem = perslistClasses.LetterboxProductItem(item)
                    jewelList.append(newItem)
                elif "globe" in item["item_title"].lower() and "yes" in item["options"][2]["value"].lower():
                    newItem = perslistClasses.LetterboxProductItem(item)
                    jewelList.append(newItem)
                elif "clover" in item["item_title"].lower() and "yes" in item["options"][-2]["value"].lower():
                    newItem = perslistClasses.LetterboxProductItem(item)
                    jewelList.append(newItem)
                elif "card" in item["options"][-2]["name"].lower() and "yes" in item["options"][-2]["value"].lower() and "delicate birth" in item["item_title"].lower():
                    newItem = perslistClasses.JewelleryBirthProductItem(item)
                    jewelList.append(newItem)
                elif "card" in item["options"][-2]["name"].lower() and ("yes" in item["options"][-2]["value"].lower() or "no" not in item["options"][-2]["value"].lower()):
                    newItem = perslistClasses.JewelleryProductItem(item)
                    jewelList.append(newItem)

            if "personalis" in item["options"][0]["name"].lower() and "yes" in item["options"][0]["value"].lower() and "embroider" not in item["options"][0]["value"].lower() and "play mat" not in item["item_title"].lower() and "mile" not in item["item_title"].lower() and "felt" not in item["options"][0]["value"].lower():
                newItem = perslistClasses.BasicProductItem(item)
                genList.append(newItem)

            if "personalis" in item["options"][1]["name"].lower() and "yes" in item["options"][1]["value"].lower() and "embroider" not in item["options"][1]["value"].lower() and "play mat" not in item["item_title"].lower() and "mile" not in item["item_title"].lower() and "felt" not in item["options"][1]["value"].lower():
                if "eco colour" in item["item_title"].lower() or "summer colourblock" in item["item_title"].lower():
                    newItem = perslistClasses.FontOptionProductItem(item)
                    genList.append(newItem)

                else:
                    newItem = perslistClasses.BasicProductItem(item)
                    genList.append(newItem)

            if "socks" in item["item_title"].lower():
                if "men" in item["item_title"].lower():
                    newItem = perslistClasses.SockProductItem(item)
                    sockList.append(newItem)

                if "hobby socks" in item["item_title"].lower():
                    newItem = perslistClasses.HobbySockProductItem(item)
                    sockList.append(newItem)

                if "wise owl" in item["item_title"].lower() or "fleur" in item["item_title"].lower():
                    newItem = perslistClasses.ChooseSockProductItem(item)
                    sockList.append(newItem)

                elif "name" in item["options"][0]["name"].lower() and "men" not in item["item_title"].lower():
                    newItem = perslistClasses.SockProductItem(item)
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
def writeTo(chosenList, listName):
    fMain.write("\n-------------" + listName + "----------------\n \n")
    for printItem in chosenList:
        fMain.write(printItem.fullName() + '\n')
    return


# As above, but with an additional space between each line - helpful for products with potential multi-line personalisations such as gift cards
def writeToSpace(chosenList, listName):
    fMain.write("\n-------------" + listName + "----------------\n \n")
    for printItem in chosenList:
        fMain.write(printItem.fullName() + '\n \n')
    return


# Calling above functions to write to file
writeTo(traceList, "A6 Inserts")
writeTo(traceA5List, "A5 Inserts")
writeToSpace(letterList, "A6 Cards")
writeToSpace(jewelList, "Jewellery")
writeTo(sockList, "Sock Labels")
writeTo(genList, "Misc")
writeTo(embList, "Embroidery")
writeTo(feltList, "Felting")


fMain.close()
