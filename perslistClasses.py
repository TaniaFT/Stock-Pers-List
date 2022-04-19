class BasicProductItem(object):
    def __init__(self, productOrder, firstIndex=0):
        self.itemTitle = productOrder['item_title'].replace('Personalised ', '')
        self.personalisationString = (str(productOrder["options"][firstIndex]["value"]))
        self.originalOrder = productOrder

    def fullName(self):
        return self.itemTitle + ' - ' + self.personalisationString


class TwoOptionItem(BasicProductItem):
    def __init__(self, productOrder, firstIndex=0, secondIndex=1):
        super(TwoOptionItem, self).__init__(productOrder)
        self.personalisationString = str(productOrder["options"][firstIndex]["value"]) + ' - ' + (str(productOrder["options"][secondIndex]["value"]))


class ThreeOptionItem(BasicProductItem):
    def __init__(self, productOrder, firstIndex=0, secondIndex=1, thirdIndex=-2):
        super(ThreeOptionItem, self).__init__(productOrder)
        self.personalisationString = str(productOrder["options"][firstIndex]["value"]) + ' - ' + (str(productOrder["options"][secondIndex]["value"]) + ' - ' + (str(productOrder["options"][thirdIndex]["value"])))