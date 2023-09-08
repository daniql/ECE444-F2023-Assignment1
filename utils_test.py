from utils import *

def test_reversed():
    test_class = utils()
    assert test_class.reversed(123456) == 654321, "Failed reversed int: Should be 654321"
    assert catch_exception(test_class.reversed, 123456.3) is TypeError, "Failed reversed float: Should cause TypeError"
    assert catch_exception(test_class.reversed, "123456") is TypeError, "Failed reversed string: Should cause TypeError"

def test_formatter():
    test_class = utils()
    assert test_class.formatter(8) == ('0b1000', '0o10'), "Failed formatter int: Should be ('0b1000', '0o10')"
    assert catch_exception(test_class.formatter, 8.0) is TypeError, "Failed formatter float: Should cause TypeError"
    assert catch_exception(test_class.formatter, "8") is TypeError, "Failed formatter string: Should cause TypeError"

def catch_exception(method, input):
    try:
        method(input)
    except Exception as e:
        return e.__class__

if __name__ == "__main__":
    test_reversed()
    print("passed reversed")
    test_formatter()
    print("passed formatter")