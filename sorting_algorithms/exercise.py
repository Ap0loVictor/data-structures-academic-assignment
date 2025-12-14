from copy import deepcopy

def insertion_sort(a):
    arr = deepcopy(a)
    n = len(arr)
    comps = 0
    swaps = 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comps += 1  
            if arr[j] > key:
                arr[j+1] = arr[j]  
                swaps += 1
                j -= 1
            else:
                break
        arr[j+1] = key
        swaps += 1 
    return arr, comps, swaps

def selection_sort(a):
    arr = deepcopy(a)
    n = len(arr)
    comps = 0
    swaps = 0
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            comps += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
    return arr, comps, swaps

def bubble_sort(a):
    arr = deepcopy(a)
    n = len(arr)
    comps = 0
    swaps = 0
    for i in range(n):
        made_swap = False
        for j in range(0, n-1-i):
            comps += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
                made_swap = True
        if not made_swap:
            break
    return arr, comps, swaps

def shell_sort(a):
    arr = deepcopy(a)
    n = len(arr)
    comps = 0
    swaps = 0
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap:
                comps += 1
                if arr[j-gap] > temp:
                    arr[j] = arr[j-gap]
                    swaps += 1
                    j -= gap
                else:
                    break
            arr[j] = temp
            swaps += 1
        gap //= 2
    return arr, comps, swaps

def merge_sort(a):
    arr = deepcopy(a)
    comps = 0
    swaps = 0
    def _merge_sort(lo, hi):
        nonlocal comps, swaps, arr
        if lo >= hi:
            return
        mid = (lo + hi) // 2
        _merge_sort(lo, mid)
        _merge_sort(mid+1, hi)
        left = arr[lo:mid+1]
        right = arr[mid+1:hi+1]
        i = j = 0
        k = lo
        while i < len(left) and j < len(right):
            comps += 1
            if left[i] <= right[j]:
                arr[k] = left[i]
                swaps += 1
                i += 1
            else:
                arr[k] = right[j]
                swaps += 1
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            swaps += 1
            i += 1; k += 1
        while j < len(right):
            arr[k] = right[j]
            swaps += 1
            j += 1; k += 1
    _merge_sort(0, len(arr)-1)
    return arr, comps, swaps

def quick_sort(a):
    arr = deepcopy(a)
    comps = 0
    swaps = 0
    def _partition(lo, hi):
        nonlocal comps, swaps, arr
        pivot = arr[hi]
        i = lo - 1
        for j in range(lo, hi):
            comps += 1
            if arr[j] <= pivot:
                i += 1
                if i != j:
                    arr[i], arr[j] = arr[j], arr[i]
                    swaps += 1
        if i+1 != hi:
            arr[i+1], arr[hi] = arr[hi], arr[i+1]
            swaps += 1
        return i+1
    def _quick(lo, hi):
        if lo < hi:
            p = _partition(lo, hi)
            _quick(lo, p-1)
            _quick(p+1, hi)
    _quick(0, len(arr)-1)
    return arr, comps, swaps

def heap_sort(a):
    arr = deepcopy(a)
    n = len(arr)
    comps = 0
    swaps = 0
    def heapify(n_local, i):
        nonlocal comps, swaps, arr
        largest = i
        l = 2*i + 1
        r = 2*i + 2
        if l < n_local:
            comps += 1
            if arr[l] > arr[largest]:
                largest = l
        if r < n_local:
            comps += 1
            if arr[r] > arr[largest]:
                largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            swaps += 1
            heapify(n_local, largest)
    for i in range(n//2 - 1, -1, -1):
        heapify(n, i)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        swaps += 1
        heapify(i, 0)
    return arr, comps, swaps

def counting_sort(a):
    arr = deepcopy(a)
    if len(arr) == 0:
        return arr, 0, 0
    comps = 0
    min_val = min(arr)
    if min_val < 0:
        shift = -min_val
        shifted = [x + shift for x in arr]
    else:
        shift = 0
        shifted = arr
    k = max(shifted) + 1
    count = [0] * k
    for v in shifted:
        count[v] += 1
    index = 0
    swaps = 0
    for value, c in enumerate(count):
        for _ in range(c):
            arr[index] = value - shift
            swaps += 1
            index += 1
    return arr, comps, swaps

# Opcional: mapa de nomes para funções
algos = {
    "Insertion": insertion_sort,
    "Selection": selection_sort,
    "Bubble": bubble_sort,
    "Shell": shell_sort,
    "Merge": merge_sort,
    "Quick": quick_sort,
    "Heap": heap_sort,
    "Counting": counting_sort
}


test_lists = [
    [12,42,83,25,67,71,3,4,94,53],
    [100,48,19,61,86,33,13,43,84,28],
    [81,60,6,49,40,41,38,64,44,36],
    [45,27,11,89,63,39,9,58,52,17],
    [88,77,26,62,30,96,56,65,98,99],
    [76,73,16,95,35,87,68,69,51,92],
    [37,75,90,82,8,18,23,93,57,10],
    [15,97,14,29,7,24,31,59,78,85],
    [5,70,55,91,47,72,2,20,34,74],
    [50,66,32,22,54,79,21,1,80,46]
]

if __name__ == "__main__":
    for name, func in algos.items():
        print(f"\n=== Algorithm: {name} ===")
        for i, arr in enumerate(test_lists, start=1):
            sorted_arr, comps, swaps = func(arr)
            ok = sorted_arr == sorted(arr)
            # Se 'ok' for True, significa:
            # (Esse sorted é algo nativo do Python, usado só para validação)
            # O algoritmo produziu uma sequência totalmente ordenada (crescente)
            # Todos os elementos do original estão presentes no resultado
            # Não há elementos duplicados indevidos nem elementos faltando
            # A ordenação está matematicamente correta
            print(f"Test {i:02d}: comps={comps:4d}, swaps={swaps:4d}, sorted_ok={ok}")
