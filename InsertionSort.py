import time # To help us visualize this algorithm step by step

def InsertionSort(data, drawDataArray, sortSpeedTime):
    # Traverse through length of data array
    for i in range (1, len(data)):
        key = data[i]
        # Move elements of arr[0..i-1], that are > key, to one position ahead of current position
        j = i-1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
            # Blue = Done with Sorted, Red = Unsorted, Purple = Being Swap / Being Sorted
            drawDataArray(data, ['purple' if x == j or x == j + 1 else 'red' for x in range(len(data))])
            time.sleep(sortSpeedTime)
        data[j + 1] = key