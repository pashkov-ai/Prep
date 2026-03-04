class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        result = []
        carry = 0
        for i in range(1, max_len + 1):
            bit_c = 0
            bit_a = a[len(a) - i] if i <= len(a) else '0'
            bit_b = b[len(b) - i] if i <= len(b) else '0'
            if carry:
                if bit_a == '1'and bit_b == '1':
                    carry = 1
                    bit_c = 1
                elif bit_a == '0' and bit_b == '0':
                    carry = 0
                    bit_c = 1
                else:
                    carry = 1
                    bit_c = 0
            else:
                if bit_a == '1'and bit_b == '1':
                    carry = 1
                    bit_c = 0
                elif bit_a == '0' and bit_b == '0':
                    carry = 0
                    bit_c = 0
                else:
                    carry = 0
                    bit_c = 1
            result.append('1' if bit_c else '0')
        if carry:
            result.append('1')
        return ''.join(result[::-1])