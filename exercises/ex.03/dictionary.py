__author__ = "730549114"
"""Function skeletons and implementations"""


def invert(dictionaryx: dict[str, str]) -> dict[str, str]:
    """Invert keys and values of a dictionary"""
    inverted_dict = {}
    for key in dictionaryx:
        if value in inverted_dict:
            raise KeyError(f"Oops! Duplicate key found.")
        inverted_dict[value] = key
    return inverted_dict


def count(listx: list[str]) -> dict[str, int]:
    """Makes a dictionary with a given list including the frequencies of each unqiue value within the list."""
    count_dict = {}
    for item in listx:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict


def favorite_color(colors: dict[str, str]) -> str:
    """returns the mode (favorite) color. Tie = first encountered."""
    color_count = {}
    for key in colors:
        color = colors[key]
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    max_color = None
    max_count = -1
    for color in color_count:
        count = color_count[color]
        if count > max_count:
            max_count = count
            max_color = color
    return max_color


def bin_len(lst: list[str]) -> dict[int, list[str]]:
    """Bins strings by length, creating lists within dictionaries. Key equals length of word and value is the list of words that length."""
    length_dict = {}
    for word in lst:
        word_len = len(word)
        if word_len not in length_dict:
            length_dict[word_len] = []  # Create a new list if key doesn't exist
        length_dict[word_len].append(word)  # Append the word to the appropriate list
    return length_dict
