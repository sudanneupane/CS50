from twttr import shorten


# pytest gathers tests according to a naming convention.
# By default any file that is to contain tests must be named starting with test_,
# classes that hold tests must be named starting with Test,
# and any function in a file that should be treated as a test must also start with test_


def test_word():
    assert shorten("twetter") == "twttr"
    assert shorten("sudan") == "sdn"


def test_text():
    assert shorten("a") == ""
    assert shorten("b") == "b"


def test_number():
    assert shorten("4") == "4"


def test_capitalized():
    assert shorten("SUDAN") == "SDN"

def test_puncuation():
    assert shorten("sudan. neupane") == "sdn. npn"