


def main():
    # 从文件读取数据
    with open('input.txt', 'r') as f:
        data = f.readline().split()
        N, M = int(data[0]), int(data[1])

        for i in range(N):
            score = list(map(int, f.readline().split()))
            teacher_Score = score[0]
            others_score = score[1:]

            valid_Scores = [s for s in others_score if 0 <= s <= M]

            if len(valid_Scores) < 2:
                avg_final = int(teacher_Score + 0.5)
            else:
                max_score = max(valid_Scores)
                min_score = min(valid_Scores)
                g1 = (sum(valid_Scores) - max_score - min_score) / (len(valid_Scores) - 2)
                avg_final = int(((g1 + teacher_Score) / 2) + 0.5)

            print(avg_final)


if __name__ == "__main__":
    main()