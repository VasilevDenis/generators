class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.i = 0

    def __iter__(self):
        self.list = [item for sublist in self.list_of_list for item in sublist]
        return self

    def __next__(self):
        if self.i < len(self.list):
            item = self.list[self.i]
            self.i += 1
        else:
            raise StopIteration
        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
