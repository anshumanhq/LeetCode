class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        #jitna anumRows hoga utna list hoga
        data=[[] for _ in range(numRows)]
        if numRows == 1:
            return s
        n=len(s)
        i=0
        x=0
        y=True #true means assending and False means desending
        while i<n:
            data[x].append(s[i])
            i+=1
            if y:
                if x == numRows - 1:
                    y = False
                    x -= 1  
                else:
                    x += 1
            else:
                if x == 0:
                    y = True
                    x += 1  
                else:
                    x -= 1
        m=''
        for sublist in data:
            #if sublist:
            #    m+=sublist[0]
            m += ''.join(sublist)  

        return m