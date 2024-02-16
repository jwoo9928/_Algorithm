def solution(nums):
    n_choice = len(nums)//2
    setPocket = set(nums)
    return min(n_choice, len(setPocket))