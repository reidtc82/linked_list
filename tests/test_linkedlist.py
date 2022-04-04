from traceback import print_list
import pytest
from linked_list.src.linkedlist import LinkedList
from linked_list.src.exceptions import NonExistentNodeError
from linked_list.src.node import Node
from src.linkedlist import Node


def test_insert_head_returns_none():
    ll = LinkedList()
    assert ll.insert_head(1) is None


def test_insert_head():
    ll = LinkedList()
    ll.insert_head(5)
    assert ll.head.value == 5


def test_only_head_next_none():
    ll = LinkedList()
    ll.insert_head(5)
    assert ll.head.next is None


def test_diff_head():
    ll = LinkedList()
    ll.insert_head(5)
    ll.insert_head("banana")
    assert ll.head.value == "banana"
    assert ll.head.next.value == 5


def test_head_is_type_node():
    ll = LinkedList()
    ll.insert_head(5)
    assert type(ll.head).__name__ == "Node"


def test_print_list(capfd):
    ll = LinkedList()
    ll.insert_head(5)
    ll.insert_head("banana")
    ll.print_list()
    out, err = capfd.readouterr()
    assert type(out).__name__ == "str"


def test_insert_tail_returns_none():
    ll = LinkedList()
    assert ll.insert_tail(1) is None


def test_insert_tail():
    ll = LinkedList()
    ll.insert_tail(5)
    assert ll.head.value == 5


def test_only_tail_next_none():
    ll = LinkedList()
    ll.insert_tail(5)
    assert ll.head.next is None


def test_diff_tail():
    ll = LinkedList()
    ll.insert_tail(5)
    ll.insert_tail("banana")
    assert ll.head.value == 5
    assert ll.head.next.value == "banana"


def test_tail_is_type_node():
    ll = LinkedList()
    ll.insert_tail(5)
    assert type(ll.head).__name__ == "Node"


def test_node():
    nd = Node("banana")
    assert type(nd).__name__ == "Node"
    assert nd.next is None
    assert nd.value == "banana"


def test_node_str():
    nd = Node("banana")
    assert nd.__str__() == "banana"


def test_list_values():
    ll = LinkedList()
    ll.insert_head(5)
    ll.insert_head("banana")
    assert ll.values == ["banana", 5]


def test_list_str(capfd):
    ll = LinkedList()
    ll.insert_head(5)
    ll.insert_head("banana")
    print(ll)
    out, err = capfd.readouterr()
    assert type(out).__name__ == "str"
