class BitManipulation:
    @staticmethod
    def getBit(n: int, k: int) -> int:
        return (n >> k) & 1

    @staticmethod
    def setBit(n: int, k: int) -> int:
        return n | (1 << k)

    @staticmethod
    def clearBit(n: int, k: int) -> int:
        return n & ~(1 << k)

    @staticmethod
    def toggleBit(n: int, k: int) -> int:
        return n ^ (1 << k)

    @staticmethod
    def isPowerOfTwo(n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0   