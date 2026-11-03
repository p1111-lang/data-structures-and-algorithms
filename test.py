from stack import Stack
from LinkedList import LinkedList, Node


def run_test(name, test_case):
    test_case()
    print(f"✅ 通过：{name}")


def test_stack_push_pop_sequence():
    stack = Stack()
    for value in (10, 20, 30):
        stack.push(value)

    assert stack.get_size() == 3
    assert stack.peek() == 30
    assert [stack.pop(), stack.pop(), stack.pop()] == [30, 20, 10]
    assert stack.is_empty()


def test_empty_stack_pop():
    stack = Stack()
    assert stack.pop() is None


def test_empty_stack_peek():
    stack = Stack()
    assert stack.peek() is None


def test_empty_stack_size_and_state():
    stack = Stack()
    assert stack.get_size() == 0
    assert stack.is_empty()


def test_empty_linked_list_delete():
    linked_list = LinkedList()
    linked_list.delete(1)
    assert linked_list.to_list() == []
    assert len(linked_list) == 0


def test_empty_linked_list_insert():
    linked_list = LinkedList()
    linked_list.prepend(1)
    assert linked_list.to_list() == [1]
    assert isinstance(linked_list.head, Node)


def test_linked_list_delete_head():
    linked_list = LinkedList()
    for value in (1, 2, 3):
        linked_list.append(value)

    linked_list.delete(1)
    assert linked_list.to_list() == [2, 3]


def test_linked_list_delete_tail():
    linked_list = LinkedList()
    for value in (1, 2, 3):
        linked_list.append(value)

    linked_list.delete(3)
    assert linked_list.to_list() == [1, 2]


def test_linked_list_delete_missing_value():
    linked_list = LinkedList()
    for value in (1, 2, 3):
        linked_list.append(value)

    linked_list.delete(99)
    assert linked_list.to_list() == [1, 2, 3]


def test_linked_list_insert_at_beginning():
    linked_list = LinkedList()
    linked_list.append(2)
    linked_list.prepend(1)
    assert linked_list.to_list() == [1, 2]


def test_linked_list_insert_at_end():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    assert linked_list.to_list() == [1, 2, 3]


def test_linked_list_insert_in_middle():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(3)
    linked_list.insert(1, 2)
    assert linked_list.to_list() == [1, 2, 3]


if __name__ == "__main__":
    tests = (
        ("栈连续入栈连续出栈", test_stack_push_pop_sequence),
        ("空栈 pop", test_empty_stack_pop),
        ("空栈 peek", test_empty_stack_peek),
        ("空栈大小与状态", test_empty_stack_size_and_state),
        ("空链表删除", test_empty_linked_list_delete),
        ("空链表插入", test_empty_linked_list_insert),
        ("删除链表头节点", test_linked_list_delete_head),
        ("删除链表尾节点", test_linked_list_delete_tail),
        ("删除链表中不存在的值", test_linked_list_delete_missing_value),
        ("链表开头插入", test_linked_list_insert_at_beginning),
        ("链表末尾插入", test_linked_list_insert_at_end),
        ("链表中间插入", test_linked_list_insert_in_middle),
    )
    for name, test_case in tests:
        run_test(name, test_case)
