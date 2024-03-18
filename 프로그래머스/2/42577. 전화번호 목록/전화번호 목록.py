def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book)
    for i in range(1, len(phone_book)):
        num = phone_book[i-1]
        if num == phone_book[i][:len(num)]:
            return False
        
    return True

