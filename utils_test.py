from utils import *

def reversed_test():
    test = utils()
    assert(test.reversed(123456) == 654321), "Reversed int test failed"
    assert(test.reversed(123456.3) == 654321), "Reversed float test failed"
    assert(test.reversed("123456") == 654321), "Reversed string test failed"

def formatter_test():
    test = utils()
    assert(test.formatter(10) == ('0b1010','0o12')), "Formatter int test failed"
    assert(test.formatter(10.3) == ('0b1010','0o12')), "Formatter float test failed"
    assert(test.formatter("10") == ('0b1010','0o12')), "Formatter string test failed"

if __name__ == "__main__":
    reversed_test()
    print("reversed test passed")
    formatter_test()
    print("formatter test passed")