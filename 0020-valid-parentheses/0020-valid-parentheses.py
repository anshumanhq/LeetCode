class Solution:
    def isValid(self, s: str) -> bool:
        #brackets={1:['(',')'],2:['{','}'],3:['[',']']}
        store=[]
        for check in s:
            if check in '({[':
                store.append(check)
            elif check in ')}]':
                if not store:
                    return False
                if store[-1]=='(' and check==')':
                    store.pop()
                elif store[-1]=='{' and check=='}':
                    store.pop()
                elif store[-1]=='[' and check==']':
                    store.pop()
                else:
                    return False
        return not store
            