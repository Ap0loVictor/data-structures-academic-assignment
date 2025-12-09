# linear_lists/07_deque_ops.py
ns = {}
with open('01_array_structures.py', 'r') as f:
    exec(f.read(), ns)
ArrayDeque = ns['ArrayDeque']

def print_state(step, d):
    print(f"{step}: {d} (first={d.first()}, last={d.last()})")

def main():
    d = ArrayDeque()
    try:
        d.add_first(4); print_state("add_first(4)", d)
        d.add_last(8); print_state("add_last(8)", d)
        d.add_last(9); print_state("add_last(9)", d)
        d.add_first(5); print_state("add_first(5)", d)
        # peek back equivalents:
        print_state("after adds (peek)", d)
        # remove first
        v = d.remove_first(); print(f"remove_first() -> {v}"); print_state("state", d)
        v = d.remove_last(); print(f"remove_last() -> {v}"); print_state("state", d)
        d.add_last(7); print_state("add_last(7)", d)
        print("first():", d.first(), "last():", d.last())
        d.add_last(6); print_state("add_last(6)", d)
        v = d.remove_first(); print(f"remove_first() -> {v}"); print_state("state", d)
        v = d.remove_last(); print(f"remove_last() -> {v}"); print_state("state", d)
    except Exception as e:
        print("Error during deque ops:", e)

if __name__ == "__main__":
    main()
