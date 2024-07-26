class Solution:
    def isValid(self, s: str) -> bool:
        stackList = []
        flag = False
        for char in s:
            if(char in ["(", "{", "["]):
                stackList.append(char)
                if(s.endswith(char)):
                    return False
            else:
                if(not stackList):
                    return False
                x = stackList.pop()
                if(char == ")"):
                    if(x == "("):
                        flag = True
                    else:
                        return False
                elif(char == "}"):
                    if(x == "{"):
                        flag = True
                    else:
                        return False
                elif(char == "]"):
                    if(x == "["):
                        flag = True
                    else:
                        return False
        if(stackList):
            return False
        return flag

        
