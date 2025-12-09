# linear_lists/03_transfer.py
ns = {}
with open('01_array_structures.py', 'r') as f:
    exec(f.read(), ns)
ArrayStack = ns['ArrayStack']

def transfer(S, T):
    """Transfer all elements from S to T as described."""
    while not S.is_empty():
        T.push(S.pop())

def main():
    s = ArrayStack()
    for v in [1, 2, 3, 4, 5]:  # sample: bottom 1 ... top 5
        s.push(v)
    t = ArrayStack()
    print("Before transfer:")
    print("S:", s)
    print("T:", t)
    transfer(s, t)
    print("\nAfter transfer:")
    print("S:", s)
    print("T:", t)
    # Note: element that was top of S becomes bottom of T,
    # and element that was bottom of S becomes top of T.

if __name__ == "__main__":
    main()
