# linear_lists/09_prefix_convert.py
ns = {}
with open('01_array_structures.py', 'r') as f:
    exec(f.read(), ns)
ArrayStack = ns['ArrayStack']

# assume tokens separated by space OR single-character tokens
def tokenize(expr):
    return expr.split()

def is_operator(tok):
    return tok in "+-*/^"

def prefix_to_infix_postfix(prefix_expr):
    tokens = tokenize(prefix_expr)
    st_infix = ArrayStack()
    st_post = ArrayStack()
    # scan from right to left
    for tok in reversed(tokens):
        if is_operator(tok):
            # pop two operands from each stack
            a_in = st_infix.pop()
            b_in = st_infix.pop()
            new_infix = f"({a_in} {tok} {b_in})"
            st_infix.push(new_infix)

            a_post = st_post.pop()
            b_post = st_post.pop()
            new_post = a_post + " " + b_post + " " + tok
            st_post.push(new_post)
        else:
            # operand
            st_infix.push(tok)
            st_post.push(tok)
    infix = st_infix.pop() if not st_infix.is_empty() else ""
    postfix = st_post.pop() if not st_post.is_empty() else ""
    return infix, postfix

def main():
    examples = [
        "+ A * B C",      # A + (B * C)
        "- * A B / C D",  # (A*B) - (C/D)
        "+ 3 * 4 5"       # 3 + (4*5)
    ]
    for ex in examples:
        infix, postfix = prefix_to_infix_postfix(ex)
        print(f"Prefix: {ex}")
        print(" Infix :", infix)
        print(" Postfix:", postfix)
        print()

if __name__ == "__main__":
    main()
