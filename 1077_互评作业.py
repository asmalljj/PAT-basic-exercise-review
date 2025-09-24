N, M = map(int,input().split())

for i in range(N):
    score = list(map(int, input().split()))
    teacher_Score = score[0]
    others_score = score[1:]

    valid_Scores = []
    for _ in others_score:
        if 0 <= _ <= M:
            valid_Scores.append(_)

    max_others_score = max(valid_Scores)
    min_others_score = min(valid_Scores)
    g1 = (sum(valid_Scores) - max_others_score - min_others_score) / (len(valid_Scores) - 2)
    avg_final = int(((g1 + teacher_Score) / 2) + 0.5)
    print(avg_final)
'''最终版本吧 反正原因就是input最后一组需要回车才会说输入 也许只有放在文件里读取才不会出问题'''