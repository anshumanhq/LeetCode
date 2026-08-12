class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Basic Roman symbols (unit and five)
        cons = {
            1: 'I', 5: 'V', 10: 'X', 50: 'L',
            100: 'C', 500: 'D', 1000: 'M'
        }
        res = ''
        num_str = str(num)
        length = len(num_str)

        for index, ch in enumerate(num_str):
            digit = int(ch)                      # IMPORTANT: string se int mein convert karo
            pos = 10 ** (length - index - 1)     # place value: 1, 10, 100, 1000

            if digit == 0:
                continue                         # kuch nahi karna

            # For place value 1000, only M repeats
            if pos == 1000:
                res += 'M' * digit
                continue

            # Determine the symbols for this place
            unit = cons[pos]                     # e.g., 1->'I', 10->'X', 100->'C'
            five = cons[pos * 5]                 # e.g., 5->'V', 50->'L', 500->'D'
            ten = cons[pos * 10]                 # e.g., 10->'X', 100->'C', 1000->'M'

            if digit <= 3:
                res += unit * digit
            elif digit == 4:
                res += unit + five
            elif digit == 5:
                res += five
            elif digit <= 8:
                res += five + unit * (digit - 5)
            elif digit == 9:
                res += unit + ten

        return res