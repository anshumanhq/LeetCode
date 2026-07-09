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
        if store==[]:
            return True
        elif len(store)<=1:
            return False
        else:
            return False
            