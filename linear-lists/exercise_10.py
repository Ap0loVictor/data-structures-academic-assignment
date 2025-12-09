# linear_lists/10_calculator.py
ns = {}
with open('01_array_structures.py', 'r') as f:
    exec(f.read(), ns)
ArrayStack = ns['ArrayStack']

# shunting-yard to convert infix -> postfix (tokens separated by spaces or single-digit)
prec = {'+':1, '-':1, '*':2, '/':2, '^':3}
def tokenize(expr):
    # simple tokenizer: split by spaces if present, else split chars (handles multi-digit if spaced)
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
            while not ops.is_empty() and ops.peek() != '(':
                output.append(ops.pop())
            ops.pop()  # pop '('
        else:  # operator
            while (not ops.is_empty() and ops.peek() != '(' and
                   ((prec.get(ops.peek(),0) > prec.get(tok,0)) or
                    (prec.get(ops.peek(),0) == prec.get(tok,0) and tok != '^'))):
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
            elif tok == '/': st.push(a // b)  # integer division
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
        print(f"{ex} => postfix: {' '.join(postfix)} => value: {value}")

if __name__ == "__main__":
    main()
