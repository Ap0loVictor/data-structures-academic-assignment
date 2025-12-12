# exercise_23.py
from exercise_01 import LinkedBinaryTree

if __name__ == "__main__":
    T1 = LinkedBinaryTree()
    r = T1.add_root(1)
    n2 = T1.add_left(r, 2)    
    n3 = T1.add_right(r, 3)   
    T1.add_left(n2, 4)        
    T1.add_right(n2, 5)       
    n6 = T1.add_left(n3, 6)  
    n7 = T1.add_right(n3, 7) 
    T1.add_left(n6, 8)   
    T1.add_right(n7, 9)      

    print("=== Testes do Exercício 3 ===\n")

    print("Preorder obtido:    ", T1.preorder())
    print()
    print("Inorder obtido:     ", T1.inorder())
    print()
    print("Postorder obtido:   ", T1.postorder())
    print()
    
