class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        longer = len(num1) if len(num1) >= len(num2) else len(num2)
        final = ""
        carry = 0
        for i in range(longer):
            n1 = int(num1[-i-1]) if len(num1) > i else 0
            n2 = int(num2[-i-1]) if len(num2) > i else 0
            tot = n1 + n2 + carry
            carry = tot // 10
            final = str(tot % 10) + final
        if carry > 0:
            final = str(carry) + final
        return final
