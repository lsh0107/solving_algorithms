def solution(str1, str2):
    answer = 0
    str_list1 = []
    str_list2 = []
    
    for i in range(len(str1)-1):
        string = str1[i:i+2].lower()
        if string.isalpha():
            str_list1.append(string)
    
    for j in range(len(str2)-1):
        string = str2[j:j+2].lower()
        if string.isalpha():
            str_list2.append(string)
            
    len_str1, len_str2 = len(str_list1), len(str_list2)
    intersect = []
    
    if len_str1 == 0 and len_str2 == 0:
        return 65536
    
    for s in str_list1:
        if s in str_list2:
            intersect.append(s)
            str_list2.remove(s)
    
    u = len_str1 + len_str2 - len(intersect)
    i = len(intersect)
    answer = int(i/u * 65536)
    return answer