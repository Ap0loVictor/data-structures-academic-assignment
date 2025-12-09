# linear_lists/05_invert_list.py
ns = {}
with open('01_array_structures.py', 'r') as f:
    exec(f.read(), ns)
ArrayStack = ns['ArrayStack']

def invert_list(lst):
    s = ArrayStack()
    for item in lst:
        s.push(item)
    res = []
    while not s.is_empty():
        res.append(s.pop())
    return res

def main():
    original = [1, 2, 3, 4, 5]
    print("Original:", original)
    inverted = invert_list(original)
    print("Inverted:", inverted)

if __name__ == "__main__":
    main()
