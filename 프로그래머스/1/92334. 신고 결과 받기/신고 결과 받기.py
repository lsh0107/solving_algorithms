def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    report = set(report)
    reports = []

    for r in report:
        reports.append(r.split(' '))
    
    reporter = {name[1]: [] for name in reports}
    got_reported = {name[1]: 0 for name in reports}
    id_dict = {name: 0 for name in id_list}

    for name in reports:
        if name[1] in got_reported:
            got_reported[name[1]] += 1
            reporter[name[1]].append(name[0])

    for name, cnt in got_reported.items():
        if cnt >= k:
            for i in reporter[name]:
                id_dict[i] += 1

    return list(id_dict.values())
