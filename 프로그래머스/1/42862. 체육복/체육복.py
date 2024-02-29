def solution(n, lost, reserve):
    # 1. 모든 학생이 체육복을 한 벌 가지고 있다고 가정
    clothes = [1]*n
    for i in lost:
        clothes[i-1] -= 1 # 도난당한 학생은 체육복을 하나 빼줌
    for i in reserve:
        clothes[i-1] += 1 # 여벌 체육복을 가진 학생에게는 체육복을 하나 더해줌

    # 2. 체육복이 없는 학생의 앞뒤로 체육복이 두 벌인 학생이 있는지 확인하고, 있다면 체육복을 빌려줌
    for i in range(n):
        if clothes[i] == 0: # 체육복이 없는 학생
            if i > 0 and clothes[i-1] == 2: # 앞번호 학생이 여벌 체육복이 있는 경우
                clothes[i-1] = 1
                clothes[i] = 1
            elif i < n-1 and clothes[i+1] == 2: # 뒷번호 학생이 여벌 체육복이 있는 경우
                clothes[i+1] = 1
                clothes[i] = 1

    return n - clothes.count(0) # 체육복이 없는 학생의 수를 전체 학생 수에서 빼서 체육수업을 들을 수 있는 학생의 수를 구함
