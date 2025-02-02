'''
def solution(phone_book):
    phone_book.sort()
    length = len(phone_book)
    # 23, 88, 123, 567, 2351
    for i in range(length-1):
        for j in range(i+1,length):
            pi = phone_book[i]
            pj = phone_book[j]
            if len(pj) >= len(pi) and pj.startswith(pi):
                return False
    return True
    '''
def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book) - 1) :
        if phone_book[i+1].startswith(phone_book[i]) : return False
    return answer