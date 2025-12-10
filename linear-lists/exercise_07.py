from exercise_01 import ArrayDeque


def main():
    d = ArrayDeque()
    try:
        d.add_first(4)
        d.add_last(8) 
        d.add_last(9) 
        d.add_first(5)
       
        print("back():", d.last()) 
        
        d.remove_first()
        d.remove_last()
        d.add_last(7)
        print("first():", d.first())  
        print("last():", d.last())    
        d.add_last(6)      
        d.remove_first()   
        d.remove_first()   

        print("final:", d)   


    except Exception as e:
        print("Error during deque ops:", e)

if __name__ == "__main__":
    main()

