# linear_lists/11_palindrome.py
ns = {}
with open('01_array_structures.py', 'r') as f:
    exec(f.read(), ns)
ArrayStack = ns['ArrayStack']
ArrayQueue = ns['ArrayQueue']

def is_palindrome(s):
    st = ArrayStack()
    q = ArrayQueue()
    for ch in s:
        if ch.isalnum():
            c = ch.lower()
            st.push(c)
            q.enqueue(c)
    while not st.is_empty():
        if st.pop() != q.dequeue():
            return False
    return True

def main():
    tests = ["A man, a plan, a canal: Panama", "racecar", "hello", "No lemon, no melon"]
    for t in tests:
        print(f"{t!r} -> {is_palindrome(t)}")

if __name__ == "__main__":
    main()
