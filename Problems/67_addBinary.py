class Solution:
    def addBinary(self, a: str, b: str) -> str:
        longer = max(len(a), len(b))
        carry = 0
        output = ""
        for i in range(longer):
            n1 = int(a[-i-1]) if len(a)>i else 0
            n2 = int(b[-i-1]) if len(b)>i else 0
            total = n1+n2+carry
            output = str(total%2) + output
            carry = total//2
        output = str(carry) + output if carry != 0 else output
        return output
