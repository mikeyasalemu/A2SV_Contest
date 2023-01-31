size = int(input())
for i in range(size):
    length = int(input())
    arr = []
    for i in range (length):
        arr.append(list(map(int, input())))
    
    side_length = len(arr) 
  
   
    ans = 0
    for row in range(side_length//2) : 
      
        col_lim = side_length - row - 1 
        
        for col in range(row, col_lim) :
            count = 0
            row_lim = side_length - col - 1
            count+= arr[row][col]+arr[col][col_lim]+arr[col_lim][row_lim]+arr[row_lim][row] 
            ans+= min(count, 4 - count)
    print (ans)      
    
