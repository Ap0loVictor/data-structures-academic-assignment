from exercise_01 import build_from_tuple

def are_identical(n1, n2):
    if n1 is None and n2 is None:
        return True
    if n1 is None or n2 is None:
        return False
    if n1.element != n2.element:
        return False
    return are_identical(n1.left, n2.left) and are_identical(n1.right, n2.right)

if __name__ == "__main__":
    t = (44, (9,(4,),(5,)), (13,(6,),(7,)))
    a = build_from_tuple(t)
    b = build_from_tuple(t)
    print("identical (should be True):", are_identical(a,b))
    b.left.element = 99
    print("identical after change (should be False):", are_identical(a,b))
