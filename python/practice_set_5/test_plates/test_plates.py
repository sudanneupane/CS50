from plates import is_valid


def test_first_two_letter():
    assert is_valid("s11315") == False


def test_letter_first():
    assert is_valid("sd1231") == True


def test_num_first():
    assert is_valid("123asd") == False


def test_num_middle():
    assert is_valid("as12fd") == False


def test_first_num_zero():
    assert is_valid("sdd021") == False


def test_length():
    assert is_valid("s") == False
    assert is_valid("saf4488") == False


def test_symbols():
    assert is_valid("sd#s54") == False