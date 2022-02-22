def solution(new_id):
    newid = new_id.lower()
    available = '1234567890abcdefghijklmnopqrstuvwxyz-_.'
    
    for i in newid:
        if i not in available:
            newid = newid.replace(i, '')
        
        else:
            continue

    
    newid = newid.replace('..', '.')
    newid = newid.strip('.')
    
    if newid == '':
        newid = 'a'
        
    if len(newid) >= 16:
        newid = newid[0:15].strip('.')
    
    if len(newid) <= 2:
        while len(newid) <3:
            newid += newid[-1]
    
    return newid


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
