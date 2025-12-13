from exercise_01 import ArrayQueue

def print_state(step, q):
    print(f"{step}: {q}")

def main(): # Eu fiz uma porma de printar, mas pode ser simplificado, inclusive no 07 eu simplifiquei, mas fica a gosto, 
    # como eu disse pode mudar já que está rodando de qualquer forma.
    q = ArrayQueue()
    ops = [
        ("enqueue", 5), ("enqueue", 3), ("dequeue", None),
        ("enqueue", 2), ("enqueue", 8), ("dequeue", None), ("dequeue", None),
        ("enqueue", 9), ("enqueue", 1),  ("dequeue", None),
        ("enqueue", 7), ("enqueue", 6), ("dequeue", None), ("dequeue", None),
        ("enqueue", 4), ("dequeue", None), ("dequeue", None)
    ]
    step = 1
    for op, val in ops:
        try:
            if op == "enqueue":
                q.enqueue(val)
                print_state(f"{step:02d} enqueue({val})", q)
            else:
                v = q.dequeue()
                print_state(f"{step:02d} dequeue() -> {v}", q)
        except Exception as e:
            print_state(f"{step:02d} {op} error: {e}", q)
        step += 1

if __name__ == "__main__":
    main()
