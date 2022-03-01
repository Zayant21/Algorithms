import sys
import ast

def sort (arr):
    size = len(arr)
    for i in range(size-1):
        for j in range (i,size):
            if (arr[i] > arr[j]):
                arr[i], arr[j] = arr[j], arr[i]
            else : continue
    return arr

            


def main():
    for line in sys.stdin:                                            # For loop Going through the input file line by line
        arr = ast.literal_eval(line) 
        print(arr)                              # Formatting the string of lists into acutual lists
        print(sort(arr))

main()