class CustomList():
    def __init__(self, *data) -> None:
        """
        Initializes list and adds data into list
        :param data: some kind of data
        """
        self.list = [*data]

    def append(self, value) -> None:
        """
        Adds value to the end of the list

        :param value: some kind of data
        :return: None
        """
        self.list.append(value)

    def add_start(self, value) -> None:
        """
        Adds value to the beginning of the list

        :param value: some kind of data
        :return: None
        """
        self.list.insert(0, value)

    def remove(self, value) -> None:
        """
        Removes first element which value is equal to parameter value

        :param value: some kind of data
        :return: None
        """
        if value in self.list:
            self.list.remove(value)
        else:
            raise ValueError

    def check_index(self, index: int) -> None:
        """
        Checks whether index is valid

        :param index: integer value
        :return: None
        """
        if index > len(self.list) - 1:
            raise ValueError
        if not isinstance(index, int):
            raise TypeError
        if isinstance(index, bool):
            raise TypeError

    def __getitem__(self, index):
        """
        Gets item by index
        :param index:
        :return: item by its index
        """
        self.check_index(index)
        return self.list[index]

    def __setitem__(self, index, data) -> None:
        """
        Insert item by index
        :param index: just an index
        :param data: some kind of data
        :return: None
        """
        self.check_index(index)
        self.list.insert(index, data)

    def __delitem__(self, index) -> None:
        """
        Delete item by index
        :param index: just an index
        :return: None
        """
        self.check_index(index)
        self.list.__delitem__(index)

    def find(self, value):
        """
        Receive index of predetermined value
        :param value: some kind of value
        :return: index
        """

        for index, el in enumerate(self.list):
            if el == value:
                return index
        raise ValueError


    def clear(self) -> None:
        """
        Clear the list
        :return: None
        """
        self.list.clear()
    def __len__(self) -> int:
        """
        Returns length of the list
        :return: length of the list
        """
        return len(self.list)
    def __iter__(self):
        return self.list.__iter__()


