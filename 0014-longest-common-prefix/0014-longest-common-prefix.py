class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix=strs[0]
        for s in strs[1:]:
            i=0
            while i<len(prefix) and len(s)>i and prefix[i]==s[i]:
                i+=1
            prefix=prefix[:i]
            if prefix=="":
                break
        return prefix