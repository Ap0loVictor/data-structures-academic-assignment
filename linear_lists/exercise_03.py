from exercise_01 import ArrayStack

def transfer(S, T):
    while not S.is_empty():
        T.push(S.pop())

def main():
    s = ArrayStack()
    for v in [1, 2, 3, 4, 5]: 
        s.push(v)
    t = ArrayStack()
    print("Before transfer:")
    print("S:", s)
    print("T:", t)
    transfer(s, t)
    print("\nAfter transfer:")
    print("S:", s)
    print("T:", t)

if __name__ == "__main__":
    main()
