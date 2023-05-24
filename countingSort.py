def countingSort(arr):
    assert 100 <= len(arr) <= 1000000
    answer = [0 * i for i in (range(100))]
    for i in arr:
        assert 0 <= i <= 100
        answer[i] +=1
    return answer
