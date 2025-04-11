__author__ = "730549114"
"""Function skeletons and implementations"""


def invert(dictionaryx: dict[str, str]) -> dict[str, str]:
    """Invert keys and values of a dictionary"""
    inverted_dict = {}
    for key in dictionaryx:
        value = dictionaryx[key]
        if value in inverted_dict:
            raise KeyError("Oops! Duplicate key found.")
        inverted_dict[value] = key
    return inverted_dict


def count(listx: list[str]) -> dict[str, int]:
    """Dict: word, frequency."""
    count_dict: dict[str, int] = {}
    for item in listx:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict


def favorite_color(colors: dict[str, str]) -> str:
    """returns the mode (favorite) color. Tie = first encountered."""
    color_count: dict[str, int] = {}
    for key in colors:
        color = colors[key]
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    max_color: str = ""
    max_count = -1
    for color in color_count:
        count = color_count[color]
        if count > max_count:
            max_count = count
            max_color = color
    return max_color


def bin_len(list: list[str]) -> dict[int, set[str]]:
    """Organize strs by length: dict of strs."""
    length_dict: dict[int, set[str]] = {}
    for word in list:
        word_len = len(word)
        if word_len not in length_dict:
            length_dict[word_len] = {word}
        length_dict[word_len].add(word)
    return length_dict
