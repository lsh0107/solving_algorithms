def solution(wallpaper):
    count = 0 
    for u in wallpaper:
        count += 1
        if '#' in u:
            lux = count - 1
            break
    
    count = 0
    for d in wallpaper[::-1]:
        count += 1
        if '#' in d:
            rdx = len(wallpaper) - count + 1
            break
    
    lefts = []
    for l in wallpaper:
        if '#' in l:
            lefts.append(l.index('#'))
    luy = min(lefts)

    rights = []
    for r in wallpaper:
        r = r[::-1]
        if '#' in r:
            rights.append(len(r) - r.index('#'))
    rdy = max(rights)

    return [lux, luy, rdx, rdy]