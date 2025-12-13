from exercise_01 import ArrayStack

def recursive_clear(stack):
    if stack.is_empty():
        return
    stack.pop()
    recursive_clear(stack)

def main(): 
    s = ArrayStack()
    for v in [10, 20, 30]:
        s.push(v)
    print("Before clear:", s)
    recursive_clear(s)
    print("After clear:", s)

if __name__ == "__main__":
    main()
