from typing import Any

class Stack:
    """
    A class to represent the ADT of a stack using a list.

    Attributes
    ----------
    __items : list[Any]
        list in which the data is stored

    Methods
    -------
    push(item: Any) -> None:
        Adds an element to the stack
    pop() -> Any:
        Removes an element from the stack
    
    Optional Methods --> do not have to be implemented, but could be useful
    -------
    size() -> int:
        Returns the number of elements in the stack
    is_empty() -> bool:
        Returns whether the stack is empty
    peek() -> Any:
        Returns the top element of the stack
    """
    def __init__(self) -> None:
        self.__items: list[Any] = []

    def push(self, elem: Any) -> None:
        self.__items.append(elem)

    def pop(self) -> Any:
        return self.__items.pop()
    
    def size(self) -> int:
        return len(self.__items)
    
    def is_empty(self) -> bool:
        return True if self.__items == [] else False

    def peek(self) -> Any:
        return self.__items[-1]

def dijkstras_two_stack_algorithm(expression: str) -> int:
    """Uses the two-stack algorithm to evaluate an arithmetic expression.

    Parameters
    ----------
    expression : str
        The mathematical expression in fully parenthesized infix notation.
        Must only contain the 5 listed operators and single-digit operands.

    Returns
    -------
    int
        The result of the evaluated expression.
    """
    operands = Stack()
    operators = Stack()

    operators_dict = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y if y != 0 else float('inf'),
    '^': lambda x, y: x ** y
    }
    buffer = []
    for char in expression:
        if char.isdigit() or char == ".":
            buffer.append(char)
            continue
        else:
            if buffer != []: operands.push("".join(buffer))
            buffer = []
        if char in ["+", "-", "*", "/", "^"]:
            operators.push(char)
        elif char == ")":
            operand2 = int(operands.pop())
            operand1 = int(operands.pop())
            operator = operators.pop()

            operands.push(operators_dict[operator](operand1, operand2))

    return operands.pop()

# Testfall hier für "expression" einfügen
expression = "((((3 - 2) - (2 ^ 3)) + (2 * 4)) + 3)"
result = dijkstras_two_stack_algorithm(expression)
print(F"{expression} = {result}")