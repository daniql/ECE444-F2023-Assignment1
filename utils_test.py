from utils import *

def test_reversed():
    test_class = utils()
    assert test_class.reversed(123456) == 654321, "Failed reversed int: Should be 654321"
    assert test_class.reversed(123456.3) == 654321, "Failed reversed float: Should be 654321"
    assert test_class.reversed("123456") == 654321, "Failed reversed string: Should be 654321"

def test_formatter():
    test_class = utils()
    assert test_class.formatter(8) == ('0b1000', '0o10'), "Failed formatter int: Should be ('0b1000', '0o10')"
    assert test_class.formatter(8.0) == ('0b1000', '0o10'), "Failed formatter float: Should be ('0b1000', '0o10')"
    assert test_class.formatter("8") == ('0b1000', '0o10'), "Failed formatter string: Should be ('0b1000', '0o10')"

if __name__ == "__main__":
    test_reversed()
    print("passed reversed")
    test_formatter()
    print("passed formatter")