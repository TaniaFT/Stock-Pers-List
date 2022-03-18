class BasicProductItem(object):
    def __init__(self, productOrder):
        self.itemTitle = productOrder['item_title'].replace('Personalised ', '')
        self.personalisationString = (str(productOrder["options"][-2]["value"]))
        self.originalOrder = productOrder

    def fullName(self):
        return self.itemTitle + ' - ' + self.personalisationString


class TracingProductItem(BasicProductItem):
    def __init__(self, productOrder):
        super(TracingProductItem, self).__init__(productOrder)
        self.personalisationString = str(productOrder["options"][0]["value"]) + ' - ' + (str(productOrder["options"][-1]["value"]))

    def fullName(self):
        return 'A6 Insert - ' + self.personalisationString


class A5TracingProductItem(BasicProductItem):
    def __init__(self, productOrder):
        super(A5TracingProductItem, self).__init__(productOrder)
        self.personalisationString = str(productOrder["options"][1]["value"]) + ' - ' + (str(productOrder["options"][-1]["value"]))

    def fullName(self):
        return 'A5 Insert - ' + self.personalisationString


class LetterboxProductItem(BasicProductItem):
    def __init__(self, productOrder):
        super(LetterboxProductItem, self).__init__(productOrder)
        self.personalisationString = str(productOrder["options"][-2]["value"]) + ' - ' + (str(productOrder["options"][-1]["value"]))

class MenSockProductItem(BasicProductItem):
    def __init__(self, productOrder):
        super(MenSockProductItem, self).__init__(productOrder)
        self.personalisationString = str(productOrder["options"][0]["value"])

class HobbySockProductItem(BasicProductItem):
    def __init__(self, productOrder):
        super(HobbySockProductItem, self).__init__(productOrder)
        self.personalisationString = str(productOrder["options"][3]["value"])

class SockProductItem(BasicProductItem):
    def __init__(self, productOrder):
        super(SockProductItem, self).__init__(productOrder)
        self.personalisationString = str(productOrder["options"][0]["value"])

class ColourEmbroideredProductItem(BasicProductItem):
    def __init__(self, productOrder):
        super(ColourEmbroideredProductItem, self).__init__(productOrder)
        self.personalisationString = str(productOrder["options"][0]["value"]) + ' - ' + str(productOrder["options"][1]["value"]) + ' - ' + (str(productOrder["options"][2]["value"]))

class EmbroideredProductItem(BasicProductItem):
    def __init__(self, productOrder):
        super(EmbroideredProductItem, self).__init__(productOrder)
        self.personalisationString = (str(productOrder["options"][1]["value"]))

class FeltedProductItem(BasicProductItem):
    def __init__(self, productOrder):
        super(FeltedProductItem, self).__init__(productOrder)
        self.personalisationString = str(productOrder["options"][0]["value"]) + ' - ' + (str(productOrder["options"][2]["value"]))

class JewelleryProductItem(BasicProductItem):
    def __init__(self, productOrder):
        super(JewelleryProductItem, self).__init__(productOrder)
        self.personalisationString = ' - ' + (str(productOrder["options"][-1]["value"]))

class BirthBlanketProductItem(BasicProductItem):
    def __init__(self, productOrder):
        super(BirthBlanketProductItem, self).__init__(productOrder)
        self.personalisationString = str(productOrder["options"][1]["value"])

class BirthBlanketTwoProductItem(BasicProductItem):
    def __init__(self, productOrder):
        super(BirthBlanketTwoProductItem, self).__init__(productOrder)
        self.personalisationString = str(productOrder["options"][1]["value"]) + ' - ' + str(productOrder["options"][2]["value"])

class BirthBlanketThreeProductItem(BasicProductItem):
    def __init__(self, productOrder):
        super(BirthBlanketThreeProductItem, self).__init__(productOrder)

