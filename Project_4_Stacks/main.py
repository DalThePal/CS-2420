'''main'''

from stack import Stack

def equal_or_higher_precidence(top, next_input):
    '''returns True if the precidence of top is greater or equal to next_input'''
    if top in ('*', '/'):
        return True
    if next_input in ("*", "/"):
        return False
    return True

def eval_postfix(expression):
    '''idk'''
    if not isinstance(expression, str):
        raise ValueError('Postfix expression not a string')

    stk = Stack()
    expr = expression.split()

    for item in expr:

        if item.isnumeric():
            stk.push(float(item))
        else:
            top1 = stk.pop()
            top2 = stk.pop()

            if len(item) > 1:
                raise SyntaxError('Bad operand')

            value = eval(str(top2) + item + str(top1))
            value = float(value)
            stk.push(value)

    return stk.top()

def in2post(expression):
    '''idk'''
    if not isinstance(expression, str):
        raise ValueError('expression is not a string')

    stk = Stack()
    postfix = ""

    for next_input in expression:
        if next_input == " ":
            continue

        if next_input == "(":
            stk.push(next_input)

        elif next_input.isnumeric():
            postfix += next_input + ' '

        elif next_input in ('/', '*', '-', '+'):
            while stk.size() > 0 and \
                stk.top() != '(' and \
                equal_or_higher_precidence(stk.top(), next_input):
                postfix += stk.pop() + ' '
            stk.push(next_input)

        else:
            if next_input != ")":
                raise SyntaxError("Equation not balanced")

            while stk.top() != "(":
                if stk.size() == 0:
                    raise SystemError("Equation not balanced")
                postfix += stk.pop() + ' '
            stk.pop()

    while stk.size() != 0:
        if stk.top() == "(":
            raise SyntaxError('Equation not balanced')
        postfix += stk.pop() + ' '

    return postfix[:-1]

def main():
    '''main'''
    file = open('data.txt', 'r')
    data = file.read().splitlines()

    for item in data:
        print('infix: ' + item)
        postfix = in2post(item)
        print('postfix: ' + postfix)
        answer = eval_postfix(postfix)
        print('answer: {0}'.format(answer) + '\n')

if __name__ == "__main__":
    main()
