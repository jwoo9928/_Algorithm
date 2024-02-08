answerList = []
def solution(numbers, target):
    v = numbers.pop()
    cal_for_numbers(v, numbers)
    cal_for_numbers(-v, numbers)
    return len(list(filter(lambda x: x == target, answerList)))

def cal_for_numbers(val, list):
    if len(list) <= 1:
        pValue = val + list[0]
        mValue = val - list[0]
        answerList.append(pValue)
        answerList.append(mValue)
        return 0
    nextValue = list.pop()
    cal_for_numbers(val + nextValue, list)
    cal_for_numbers(val - nextValue, list)
    list.insert(0, nextValue)
    return 0
