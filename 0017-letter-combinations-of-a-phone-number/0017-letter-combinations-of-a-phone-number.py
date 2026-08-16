import itertools

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        #suppose digit='23'
        value={1:'',2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz',0:' '}
        com=[]
        comb=[]
        for digit in digits:
            comb.append(value[int(digit)])
        #now comb=['abc','def']
        com= [''.join(p) for p in itertools.product(*comb)]
        return com