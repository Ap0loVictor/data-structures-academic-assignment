from exercise_01 import ArrayStack

def invert_list(lst):
    s = ArrayStack()
    for item in lst:
        s.push(item)
    for i in range(len(lst)):
        lst[i] = s.pop()
    return lst

def main():
    original = [1, 2, 3, 7, 5]
    print("Original:", original)
    inverted = invert_list(original)
    print("Inverted:", inverted)

if __name__ == "__main__":
    main()
