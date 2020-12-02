def solution(numbers):
    answer = ''
    numbers = list(map(str,numbers))
    numbers.sort(key = lambda x: 3*x, reverse = True) # 문자열은 정렬은 인덱스 맨앞자리를 아스키숫자로 만들어서 비교
    # 0000일 경우 답은 0이므로 int로 형변환 해줘서 0 만들고 다시 문자열처리
    return str(int(''.join(numbers)))
