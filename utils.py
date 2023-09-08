class utils:
    def reversed(self, num:int) -> int:
        if not type(num) is int:
            raise TypeError("input should be an int")
        
        ret = str(num)
        return int(ret[::-1])

    def formatter(self, num:int):
        if not type(num) is int:
            raise TypeError("input should be an int")
        
        return bin(num), oct(num)