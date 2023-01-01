#!/usr/bin/python3

'''A Node class'''


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def data(self, value):
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @next_node.setter
    def next_node(self, value):
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            prev_node = None
            next_node = temp.next_node
            while temp is not None:
                if node.data <= temp.data:
                    if prev_node is None:
                        node.next_node = temp
                        self.head = node
                    else:
                        node.next_node = temp
                        prev_node.next = node
                    break
                elif node.data >= temp.data and \
                        (next_node is None or node.data <= next_node.data):
                    node.next_node = next_node
                    temp.next_node = node
                    break
                prev_node = temp
                temp = temp.next_node
                next_node = next_node.next_node

    def __str__(self):
        string = ""
        temp = self.head
        while temp is not None:
            string += temp.data.__str__()
            string += '\n'
            temp = temp.next_node
        return string
