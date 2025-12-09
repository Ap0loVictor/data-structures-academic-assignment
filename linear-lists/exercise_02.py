from exercise_01 import atividade_01
# linear_lists/02_stack_ops.py
# Execute this in the same folder that contains 01_array_structures.py

# load classes from 01_array_structures.py dynamically
ns = {}
with open('exercise_01.py', 'r') as f:
    exec(f.read(), ns)
ArrayStack = ns['ArrayStack']

def print_state(step, s):
    print(f"{step}: {s}")

def main():
    s = ArrayStack()
    ops = [
        ("push", 5), ("push", 3), ("pop", None),
        ("push", 2), ("push", 8), ("pop", None), ("pop", None),
        ("push", 9), ("push", 1), ("pop", None),
        ("push", 7), ("push", 6), ("pop", None), ("pop", None),
        ("push", 4), ("pop", None), ("pop", None)
    ]
    step = 1
    for op, val in ops:
        try:
            if op == "push":
                s.push(val)
                print_state(f"{step:02d} push({val})", s)
            elif op == "pop":
                popped = s.pop()
                print_state(f"{step:02d} pop() -> {popped}", s)
        except Exception as e:
            print_state(f"{step:02d} {op} error: {e}", s)
        step += 1

if __name__ == "__main__":
    main()
