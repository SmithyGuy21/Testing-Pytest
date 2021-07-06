def mode_finder(numbers):
    if numbers is None:
        return None
    elif len(numbers) == 0:
        return None
    elif len(numbers) == 1:
        return numbers[0]
    else:
        itemOccurances = {}
        for item in numbers:
            itemOccurances[item] = itemOccurances.get(item, 0) + 1  # if not in numbers, set occurances to one
        setModes = set()
        modeOccurances = max(itemOccurances.values())
        if modeOccurances == 1: #if the most common number appears one time, there is no mode (unless there is one term)
            return None
        for item in numbers:
            if itemOccurances[item] == modeOccurances:
                setModes.add(item)
        if len(setModes) == 1:
            return setModes.pop()
        else:
            return list(setModes).sort()


def test_mode_finder():
    assert mode_finder([1, 1, 1]) == 1, "All elements are same"
    assert mode_finder([0, 9, 0, 57, -5]) == 0, "Elements given out of order"
    assert mode_finder([0, 4253, -342]) is None, "All elements are different"
    assert mode_finder([0, 9, 0, 57, -5]) == 0, "Elements given out of order"
    assert mode_finder([-1, -1, 20]) == -1, "Mode of negative numbers"
    assert mode_finder([42]) == 42, "Single number should return itself"
    assert mode_finder([]) is None, "Empty list should give None"
    print("No errors")

