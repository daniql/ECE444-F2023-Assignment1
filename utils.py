class utils:
    def reversed(self, num:int) -> int:
        if not type(num) is int:
            raise TypeError("input should be an int")
        if num >= 0:
            ret = str(num)
            return int(ret[::-1])
        else:
            ret = str(num)[1:]
            ret = '-'+ret[::-1]
            return int(ret)

    def formatter(self, num:int):
        if not type(num) is int:
            raise TypeError("input should be an int")
        
        return bin(num), oct(num)
    
test = utils()
print(test.reversed(-12345))