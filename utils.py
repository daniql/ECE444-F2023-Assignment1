class utils:
    def reversed(self, num:int) -> int:
        ret = str(int(num))
        return int(ret[::-1])

    def formatter(self, num:int):
        num = int(num)
        return bin(num), oct(num)