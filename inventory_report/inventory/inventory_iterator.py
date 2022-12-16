from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, importer):
        self.importer = importer
        self._pos = 0

    def __next__(self):
        try:
            importer = self.importer[self._pos]
        except IndexError:
            raise StopIteration()
        else:
            self._pos += 1
            return importer
