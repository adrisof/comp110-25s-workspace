__author__ = "730549114"
"""Defining unit test functions"""

from dictionary import invert, favorite_color, count, bin_len


def test_invert1() -> None:
    """Use case: regular"""
    input_dict1 = {"a": "1", "b": "2", "c": "3"}
    exp_output1 = {"1": "a", "2": "b", "3": "c"}
    assert invert(input_dict1) == exp_output1


def test_invert2() -> None:
    """Use case: regular2"""
    input_dict2 = {"c": "3", "d": "4"}
    exp_output2 = {"3": "c", "4": "d"}
    assert invert(input_dict2) == exp_output2


def test_invert3() -> None:
    """Edge case: empty dict"""
    input_dict3: dict[str, str] = {}
    exp_output3: dict[str, str] = {}
    assert invert(input_dict3) == exp_output3


def test_count1() -> None:
    """Use case: basic list."""
    input_list1 = ["apple", "banana", "apple"]
    exp_list1 = {"apple": 2, "banana": 1}
    assert count(input_list1) == exp_list1


def test_count2() -> None:
    """Edge case: empty list"""
    input_list2: list[str] = []
    exp_list2: dict[str, int] = {}
    assert count(input_list2) == exp_list2


def test_count3() -> None:
    """Use case: one item"""
    input_list3 = ["apple"]
    exp_list3 = {"apple": 1}
    assert count(input_list3) == exp_list3


def test_favorite_color_basic() -> None:
    """Use case: basic"""
    input_dict1 = {"Belinda": "blue", "Victoria": "blue", "Chelsea": "green"}
    exp_color1 = "blue"
    assert favorite_color(input_dict1) == exp_color1


def test_favorite_color_tie() -> None:
    """Use case: tie"""
    input_dict2 = {
        "Belinda": "blue",
        "Victoria": "green",
        "Chelsea": "green",
        "Sritala": "blue",
    }
    exp_color2 = "blue"
    assert favorite_color(input_dict2) == exp_color2


def test_favorite_color_empty() -> None:
    """Edge case: empty"""
    input_dict3: dict[str, str] = {}
    exp_color3 = ""
    assert favorite_color(input_dict3) == exp_color3


def test_bin_len1() -> None:
    """Edge Case: Empty list"""
    input_list1: list[str] = []
    exp_output1: dict[int, set[str]] = {}
    assert bin_len(input_list1) == exp_output1


def test_bin_len2() -> None:
    """Use case: website example"""
    input_list2 = ["the", "quick", "fox"]
    exp_output2 = {3: {"the", "fox"}, 5: {"quick"}}
    assert bin_len(input_list2) == exp_output2


def test_bin_len3() -> None:
    """Use case: same lengths"""
    input_list3 = ["thirteen", "fourteen"]
    exp_output3 = {8: {"thirteen", "fourteen"}}
    assert bin_len(input_list3) == exp_output3
