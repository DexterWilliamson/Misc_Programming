def triangle(n): 
      
    k = 2*n - 2
    
    for i in range(0, n): 

        for j in range(0, k): 
            print(end=" ") 
        k = k - 1
    
        for j in range(0, i+1): 
          
            print("* ", end="") 
      

        print("\r")

        print(i)

        area_per_level = j * 108.26
        
        total = area_per_level + area_per_level

        print (area_per_level)        
   
n = int(input("How many?: "))
triangle(n) 
