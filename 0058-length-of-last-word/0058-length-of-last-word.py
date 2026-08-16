class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        sl=s.split(' ')
        if '' in sl:
            sl=[x for x in sl if x!='']
            sl=sl[-1]
        else:
            sl=sl[-1]
        return len(sl)