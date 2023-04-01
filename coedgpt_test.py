#https://platform.openai.com/
# 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 == api key
#make a quicksort program ( t)

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


print(quicksort([3,6,8,10,1,2,1])) # [1, 1, 2, 3, 6, 8, 10]

# 이 코드는 퀵 정렬(Quick Sort) 알고리즘을 구현한 것입니다. 퀵 정렬은 리스트 내의 데이터를 빠르게 정렬하기 위한 비교적 효율적인 알고리즘입니다. 이 코드에서, pivot은 리스트 arr의 값 중 가운데 값을 나타냅니다. left, middle, right 3개의 리스트로 pivot 값 보다 작은 값, pivot 값, pivot 값 보다 큰 값을 분할합니다. quicksort()함수를 left, right 3개의 리스트로 recursive call합니다. recursive call함수(quicksort())이 return하는 left + middle + right 3개의 list를 concatenate합니다.

