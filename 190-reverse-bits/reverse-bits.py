class Solution(object):
    def reverseBits(self, n):
        result = 0                 # Store the reversed bits

        for i in range(32):        # Process all 32 bits
            last_bit = n & 1       # Get the last bit (0 or 1)
            result = (result << 1) | last_bit   # Add it to the result
            n = n >> 1             # Remove the last bit from n

        return result              # Return the reversed integer