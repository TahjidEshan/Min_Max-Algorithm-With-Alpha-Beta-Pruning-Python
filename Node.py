class Node(object):

    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.children = []
        self.terminal = False

    def addChild(self, obj):
        self.children.append(obj)
