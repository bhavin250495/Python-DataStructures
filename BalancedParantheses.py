
def balanced_paranthesis(string):

    stack = []
    top = 0

    for char in string:

        # Add all opening braces in stack
        if char == "(" or char == "{" or char == "[" : 
            stack.append(char)
            top +=1 
        # Keep removing each opening brace when closing brace comes in         
        elif char == ")":
            stack.remove("(")
            top -=1
        elif char == "}":
            stack.remove("{")
            top -=1
        elif char == "]":
            stack.remove("[")
            top -=1
            
    return (len(stack) == 0)            
    

if balanced_paranthesis("({{{{{{{{[][}}}}}}}})]{}[][][][][]"):
    print("BALANCED")
else:
    print("UN-BALANCED")
