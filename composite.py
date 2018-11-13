import abc


class Component(metaclass=abc.ABCMeta):
 
    @abc.abstractmethod
    def operation(self):
        pass


class Composite(Component):

    def __init__(self):
        self._children = set()

    def operation(self):
        for child in self._children:
            child.operation()

    def add(self, component):
        self._children.add(component)

    def remove(self, component):
        self._children.discard(component)


class Leaf(Component):

    def operation(self):
        pass


def main():
    leaf = Leaf()
    composite = Composite()
    composite.add(leaf)
    composite.operation()


if __name__ == "__main__":
    main()