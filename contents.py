
def validParenthesis(s):
    stack = []
    brackets = { '(': ')',
                 "{": "}",
                 '[': ']' }
    
    for bracket in s:
        if bracket in brackets.keys(): stack.append(bracket)
        else:
            if len(stack) == 0:
                return False
            
            deleted = stack.pop()
            if brackets[deleted] != bracket:
                return False
            
    if len(stack) != 0:
        return False
    
    return True
