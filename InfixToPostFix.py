def getPriority(op):
    
    if op is '-' or op is '+':
        return 1
    elif op is '*' or  op is '/':
        return 2
    elif op is '^':
        return 3    
    
    else:
        return 5


def isOperator(op):
    return op is '^' or op is '-' or op is '+' or op is '*' or op is '/'

def isOpening(brac):
    if brac == '(':
        return True
    return False

def isClosing(brac):
    if brac == ')':
        return True
    return False

def isOperand(op):
    return op.isalpha() or op.isnumeric()    

def inFixToPostFix(expr):

    experssion = list(expr)
    stack = []
    top = -1
    output = []
    

    for item in experssion:

        if isOpening(item):
            output.append(item)
            stack.append(item)
            top+=1

        elif isClosing(item):
            if len(stack) >= 1:
    
               while  len(stack) > 0 and not isOpening(stack[top])  :
                    output.append(stack[top])
                    del stack[top]
                    top -= 1
                    
               del stack[top]
               top-=1
               output.append(item)
        
        elif  isOperand(item):
            output.append(item)

        
            
        elif isOperator(item):
            
            if len(stack) >= 1:

               while  len(stack) > 0 and getPriority(item) >= getPriority(stack[top])  :
                    
                    output.append(stack[top])
                    del stack[top]
                    top -= 1
                    
               stack.append(item)
               top+=1
            else:
               stack.append(item)
               top+=1  
               
                      
    print(output+stack)

inFixToPostFix('(A * (B + (C / D) ) )')   


# Infix	                     Postfix	              Prefix
# ( (A * B) + (C / D) )	# ( (A B *) (C D /) +) #	(+ (* A B) (/ C D) )
# ((A * (B + C) ) / D) #	( (A (B C +) *) D /) #	(/ (* A (+ B C) ) D)
# (A * (B + (C / D) ) )	# (A (B (C D /) +) *) #	(* A (+ B (/ C D) ) )


