class BitManipulation {
    static getBit(n, k) {
        return (n >> k) & 1;
    }

    static setBit(n, k) {
        return n | (1 << k);
    }

    static clearBit(n, k) {
        return n & ~(1 << k);
    }

    static toggleBit(n, k) {
        return n ^ (1 << k);
    }

    static isPowerOfTwo(n) {
        return n > 0 && (n & (n - 1)) === 0;
    }
}   
