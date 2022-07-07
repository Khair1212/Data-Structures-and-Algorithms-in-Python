# Title: Plus One

class Solution:
    def plusOne(self, digits):
        k = 1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] + k == 10:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        digits.insert(0, k)
        return digits
