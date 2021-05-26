
# Merge Sort


def Merge(array):
    print("Divided array: " + str(array))
    if len(array) > 1:  
        mid = len(array) // 2  

        leftArray = array[:mid] 
        rightArray = array[mid:]  

        Merge(leftArray)
        Merge(rightArray)
        MergeSort(array, leftArray, rightArray)


def MergeSort(array,leftArray,rightArray):

    i=0  #left array index
    j=0  #right array index
    k=0  #merged array index

    while i < len(leftArray) and j < len(rightArray):
        if leftArray[i] < rightArray[j]:
            array[k] = leftArray[i]

            i = i + 1
        else:
            array[k] = rightArray[j]
            j = j+1
        k = k+1


        while i < len(leftArray):
            array[k]=leftArray[i]
            i = i+1
            k = k+1

        while j < len(rightArray):
            array[k]=rightArray[j]
            j = j+1
            k = k+1
    print("Merged Array: " + str(array))



array = [10,20,-5,6,3,2,55,7,11,13]

Merge(array)
