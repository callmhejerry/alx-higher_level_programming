#!/usr/bin/python3

'''A Node class'''


class Node:
    '''A Node class with data and next_node instance private variables'''
    def __init__(self, data, next_node=None):
        '''Initializes the data and next_node variables'''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''retrieves the private data varibale'''
        return self.__data

    @property
    def next_node(self):
        '''retrieves the private next_node variable'''
        return self.__next_node

    @data.setter
    def data(self, value):
        '''sets the private instance data variable'''
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @next_node.setter
    def next_node(self, value):
        '''sets the private instance next_node variable'''
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    '''implementation of the singly linked list
        data structure'''
    def __init__(self):
        '''initializing the instance head variable to None'''
        self.head = None

    def sorted_insert(self, value):
        '''adds a new node to the list in a sorted manner'''
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
        '''returns the string representation of the linked list structure'''
        string = ""
        temp = self.head
        while temp is not None:
            string += temp.data.__str__()
            string += '\n'
            temp = temp.next_node
        return string
