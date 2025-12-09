# linear_lists/08_parentheses.py
ns = {}
with open('01_array_structures.py', 'r') as f:
    exec(f.read(), ns)
ArrayStack = ns['ArrayStack']

def parentheses_balanced(s):
    mapping = {')':'(', ']':'[', '}':'{'}
    st = ArrayStack()
    for ch in s:
        if ch in "([{":
            st.push(ch)
        elif ch in ")]}":
            if st.is_empty() or st.pop() != mapping[ch]:
                return False
    return st.is_empty()

def main():
    tests = [
        "(a + b) * (c + d)",
        "([{}])",
        "((])",
        "([]{})",
        "( [ ) ]"
    ]
    for t in tests:
        print(f"{t!r} -> {parentheses_balanced(t)}")

if __name__ == "__main__":
    main()
