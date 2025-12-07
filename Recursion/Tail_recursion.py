def greet(count):
    if count==5:
        return 0
    
    greet(count+1)
    print("Ashish")

greet(0)