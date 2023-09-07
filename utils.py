class utils:
    def reversed(self, num:int) -> int:
        num = str(int(num))
        return int(num[::-1])
    
    def formatter(self, num:int):
        num = int(num)
        return bin(num), oct(num)