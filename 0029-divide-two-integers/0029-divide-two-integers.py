class Solution(object):
    def divide(self, dividend, divisor):
        # Edge case: Overflow ( jab -2^31 ko -1 se divide karo toh 2^31 aata hai, jo range se bahar hai )
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        # Sign decide karo
        negative = (dividend < 0) ^ (divisor < 0)
        
        # Positive numbers ke saath kaam karo (absolute values)
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quotient = 0
        
        # Jab tak dividend divisor se bada hai
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            
            # Double karo jab tak temp * 2 dividend se chhota hai
            while dividend >= (temp << 1):
                temp <<= 1          # temp = temp * 2
                multiple <<= 1      # multiple = multiple * 2
            
            # Dividend mein se temp subtract karo
            dividend -= temp
            quotient += multiple
        
        # Sign lagao
        if negative:
            quotient = -quotient
        
        # Result 32-bit range mein hona chahiye (extra safety)
        if quotient > 2**31 - 1:
            return 2**31 - 1
        if quotient < -2**31:
            return -2**31
        return quotient