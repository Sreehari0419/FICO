def factorial(n):
    
    print("welcome")
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
  
def create_matrix(row, col):
 
    matrix = [[0 for x in range(col)] for y in range(row)]
    return matrix

print("Raju")