def solve (N, M, visit):
    # fix bugs in this function
    cnt = [0] * N           # count of visitors for each shop

    for i in range(M):
        l, r = visit[i]
        l -= 1
        r -= 1
        # cnt[l - 1] += 1         # вычитаем единицы (индексация с нуля)
        # does not count shops between left and right
        # cnt[r - 1] += 1         # вычитаем единицы (индексация с нуля)
        for j in range(l, r+1):
            cnt[j] += 1

    print(cnt)
    # get the most popular shops
    top3 = []
    for _ in range(3):
        top = cnt.index(max(cnt))
        cnt[top] = -1
        top3.append(top + 1)    # возвращаем единицу (магазины считаются с первого)
    return sorted(top3)




T = int(input())    # number of test cases

for _ in range(T):
    # N - number of shops
    # M - number of persons
    N, M = map(int, input().split())
    # L - R
    visit = [list(map(int, input().split())) for i in range(M)]

    out_ = solve(N, M, visit)
    print (' '.join(map(str, out_)))