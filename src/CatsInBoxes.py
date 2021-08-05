class Box():
    def __init__(self):
        self.cat = cat
        self.nextcat = None


class LinkedList:
    def __init__(self):
        self.head = None

    # проверить наличие кота
    def contains(self, cat):
        lastbox = self.head
        while lastbox:
            if lastbox.cat == cat:
                return True
            else:
                lastbox = lastbox.nextcat
        return False


    # добавить кота в конец
    def addToEnd(self, newCat):
        newbox = Box(newCat)
        if self.head is None:
            self.head = newbox
            return
        lastbox = self.head
        while lastbox.nextcat:
            lastbox = lastbox.nextcat
        lastbox.nextcat = newbox

    # получить узел по индексу
    def get(self, catIndex):
        lastbox = self.head
        boxIndex = 0
        while boxIndex <= catIndex:
            if boxIndex == catIndex:
                return lastbox.cat
            boxIndex += 1
            lastbox = lastbox.nextcat

    # удалить кота
    def removeBox(self, rmcat):
        headcat = self.head

        if headcat is not None:
            if headcat.cat == rmcat:
                self.head = headcat.nextcat
                headcat = None
                return

        while headcat is not None:
            if headcat.cat == rmcat:
                break
            lastcat = headcat
            headcat = headcat.nextcat

        if headcat.cat == None:
            return
        lastcat.nextcat = headcat.nextcat
        headcat = None

