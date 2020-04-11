def iterative_search(list, target):
    for item in list:
        if item == target:
            return item
        
    return None


#| 9 | 4 | 3 |

target = 3

def recursive_search(list, target, index):
    if list[index] == target:
        return target #found it!
    if index == len(list):
        return None #didn't find it
    else:
        recursive_search(list, target, index + 1)
