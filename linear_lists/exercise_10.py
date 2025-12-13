from exercise_01 import ArrayStack

prec = {'+':1, '-':1, '*':2, '/':2, '^':3}
def tokenize(expr):
    if ' ' in expr:
        return expr.split()
    tokens = []
    num = ''
    for ch in expr:
        if ch.isdigit():
            num += ch
        else:
            if num:
                tokens.append(num); num=''
            if ch.strip():
                tokens.append(ch)
    if num:
        tokens.append(num)
    return tokens

def infix_to_postfix(tokens):
    output = []
    ops = ArrayStack()
    for tok in tokens:
        if tok.isdigit():
            output.append(tok)
        elif tok == '(':
            ops.push(tok)
        elif tok == ')':
            while not ops.is_empty() and ops.top() != '(':
                output.append(ops.pop())
            ops.pop()  
        else:  
            while (not ops.is_empty() and ops.top() != '(' and
                   ((prec.get(ops.top(),0) > prec.get(tok,0)) or
                    (prec.get(ops.top(),0) == prec.get(tok,0) and tok != '^'))):
                output.append(ops.pop())
            ops.push(tok)
    while not ops.is_empty():
        output.append(ops.pop())
    return output

def eval_postfix(postfix_tokens):
    st = ArrayStack()
    for tok in postfix_tokens:
        if tok.isdigit():
            st.push(int(tok))
        else:
            b = st.pop(); a = st.pop()
            if tok == '+': st.push(a + b)
            elif tok == '-': st.push(a - b)
            elif tok == '*': st.push(a * b)
            elif tok == '/': st.push(a // b)  
            elif tok == '^': st.push(a ** b)
            else:
                raise ValueError("unknown op " + tok)
    return st.pop()

def calculate(expr):
    tokens = tokenize(expr)
    postfix = infix_to_postfix(tokens)
    return eval_postfix(postfix), postfix

def main():
    expressions = [
        "3 + 4 * 2",
        "( 1 + 2 ) * ( 3 + 4 )",
        "10 + 2 * 6",
        "100 * ( 2 + 12 ) / 14"
    ]
    for ex in expressions:
        value, postfix = calculate(ex)
        print(f"{ex} = {value}")
        # print(f"{ex} => postfix: {' '.join(postfix)} => value: {value}")
        # Deixei pra poder dar pra ver o postfix se quiser (pós-fixo)

if __name__ == "__main__":
    main()
