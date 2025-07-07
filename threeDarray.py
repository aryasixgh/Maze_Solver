litVal = [1,1,1,1]
#arrayThreeD = [[list(litVal) for _ in range(10)] for _ in range(10)]
def printer(arrayThreeD):
    for i in range(10):
        for j in range(10):
            print(arrayThreeD[i][i], end="")
        print()
        
