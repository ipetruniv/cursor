from typing import Any
from typing import List


class OurAwesomeException(Exception):
    pass


def is_two_object_has_same_value(first: Any, second: Any) -> bool:
    """
    If @first and @second has same value should return True
    In another case should return False
    """
    return first == second


def is_two_objects_has_same_type(first: Any, second: Any) -> bool:
    """
    If @first and @second has same type should return True
    In another case should return False
    """
    return type(first) == type(second)


def is_two_objects_is_the_same_objects(first: Any, second: Any) -> bool:
    """
    If @first and @second has same type should return True
    In another case should return False
    """
    """
    #Old solution
    return (id(first) == id(second))
    """
    #New
    return  first is second


def multiple_ints(first_value: int, second_value: int) -> int:
    """
    Should calculate product of all args.
    if first_value or second_value is not int should raise ValueError

    Raises:
        ValueError

    Params:
        first_value: value for multiply
        second_value
    Returns:
        Product of elements
    """
    """
    #The previous version
    
    result = "The incorrect values provided"
    if type(first_value) == int and type(second_value) == int:
        result = first_value * second_value
    else:
        raise ValueError
    return result
    """
    #The new one
    if isinstance(first_value, int) and isinstance(second_value, int):
        return first_value * second_value
    else:
        raise ValueError


def multiple_ints_with_conversion(first_value: Any, second_value: Any) -> int:
    try:
        return int(first_value) * int(second_value)
    except ValueError:
        raise OurAwesomeException



def is_word_in_text(word: str, text: str) -> bool:
    """
    If text contain word return True
    In another case return False.

    Args:
        word: Searchable substring
        text: Text for searching

    Examples:
        is_word_in_text("Hello", "Hello word")
        >>> True
        is_word_in_text("Glad", "Nice to meet you ")
        >>> False

    """
    return word in text


def some_loop_exercise() -> list:
    """
    Use loop to create list that contain int values from 0 to 12 except 6 and 7
    """
    mylist = [a for a in range(13) if a != 6 and a != 7]
    return mylist


def remove_from_list_all_negative_numbers(data: List[int]) -> list:
    """
    Use loops to solve this task.
    You could use data.remove(negative_number) to solve this issue.
    Also you could create new list with only positive numbers.
    Examples:
        remove_from_list_all_negative_numbers([1, 5, -7, 8, -1])
        >>> [1, 5, 8]
    """
    count = 0
    newlist = data.copy()
    for count in range(len(data)):
        if data[count] <= 0:
            newlist.remove(data[count])
    return newlist


def alphabet() -> dict:
    """
    Create dict which keys is alphabetic characters. And values their number in alphabet
    Notes You could see an implementaion of this one in test, but create another one
    Examples:
        alphabet()
        >>> {"a": 1, "b": 2 ...}
    """
    """
    The ASCII code of a = 97 ... z = 122
    """
    myalpha = {}
    for letter in range(97, 123):
        myalpha[(letter-96)] = chr(letter)
    return myalpha



def simple_sort(data: List[int]) -> List[list]:
    """
    Sort list of ints without using built-in methods.
    Examples:
        simple_sort([2, 9, 6, 7, 3, 2, 1])
        >>> [1, 2, 2, 3, 6, 7, 9]
    Returns:

    """
    count = 1
    while count == 1:
        element_num = 0
        count = 0
        for element_num in range(len(data) - 1):
            if data[element_num] > data[element_num + 1]:
                data[element_num], data[element_num + 1] = data[element_num + 1], data[element_num]
                count = 1

    return data