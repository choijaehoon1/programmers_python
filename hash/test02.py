def solution(phone_book):
    # answer = True
    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if i == j:
                continue
            if phone_book[i] in phone_book[j]:
                if phone_book[j].index(phone_book[i]) == 0:
                    return False
    
    return True
