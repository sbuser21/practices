def pascalArray(input):
    input = int(input)
    newArray = []

    if(input == 1):
        newArray.insert(0,1)
        
    else:
        previousArray = pascalArray(input - 1)
        newArray.insert(0, 1)
        
        if (input > 2):
            for i in range(1, input-1):
                newArray.insert(i, previousArray[i-1] + previousArray[i]) 
            
        newArray.insert(input, 1)
    
    print(newArray)
    return newArray
        
        
N = input()

result = pascalArray(N)
