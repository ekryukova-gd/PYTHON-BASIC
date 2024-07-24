# """
# Write function which deletes defined element from list.
# Restriction: Use .pop method of list to remove item.
# Examples:
#     >>> delete_from_list([1, 2, 3, 4, 3], 3)
#     [1, 2, 4]
#     >>> delete_from_list(['a', 'b', 'c', 'b', 'd'], 'b')
#     ['a', 'c', 'd']
#     >>> delete_from_list([1, 2, 3], 'b')
#     [1, 2, 3]
#     >>> delete_from_list([], 'b')
#     []
# """
from typing import List, Any


# ver.1
# def delete_from_list(list_to_clean: List, item_to_delete: Any) -> List:
#     for _ in range(list_to_clean.count(item_to_delete)):
#         i = list_to_clean.index(item_to_delete)
#         list_to_clean.pop(i)
#     return list_to_clean

# ver.2
def delete_from_list(list_to_clean: List, item_to_delete: Any) -> List:
    res = []
    while list_to_clean:
        elem = list_to_clean.pop()
        if elem != item_to_delete:
            res.append(elem)
    return res[::-1]


if __name__ == '__main__':
    delete_from_list([1, 2, 3, 4, 3], 3)
