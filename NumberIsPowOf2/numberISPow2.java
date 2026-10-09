public static boolean isPowerOfTwo(long n) {
    // return true if n is a power of two, otherwise false
    if (n <=0) {
        return false;
    }
    return (n & (n-1)) == 0;
}