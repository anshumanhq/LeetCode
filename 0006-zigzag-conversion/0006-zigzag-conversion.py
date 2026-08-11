class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        #jitna anumRows hoga utna list hoga
        data=[[] for _ in range(numRows)]
        if numRows == 1: #mera aage ka code num row 1 ke liye index error de dega es liye direct return krna jada better tha
            return s
        
        # WHILE LOOP HATAA KAR FOR LOOP LAGAYA
        x = 0
        y = True #true means assending and False means desending
        
        for ch in s:   # <--- Pehle while i<n tha, ab for ch in s
            data[x].append(ch)   # <--- Pehle s[i] tha, ab ch
            
            if y:
                if x == numRows - 1: #agar ye last list per pahuch gya then mujhe esko reverse krna padega
                    y = False
                    x -= 1  
                else:
                    x += 1
            else:
                if x == 0: #aur agar reverse chalte chalte 0 per aa gye then fir se forward chalenge
                    y = True
                    x += 1  
                else:
                    x -= 1
        
        m=''
        for sublist in data:
            m += ''.join(sublist)  

        return m