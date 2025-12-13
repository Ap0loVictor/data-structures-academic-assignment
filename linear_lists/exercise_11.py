from exercise_01 import ArrayStack
from exercise_01 import ArrayQueue

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
    # tests = ["A man, a plan, a canal: Panama", "racecar", "hello", "No lemon, no melon"] # I searched for palindromes
    tests = ["", "A", "aa", "ab", "aba", "abc", "Arara", "aibofobia"]
    for t in tests:
        print(f"{t!r} -> {is_palindrome(t)}")

if __name__ == "__main__":
    main()
