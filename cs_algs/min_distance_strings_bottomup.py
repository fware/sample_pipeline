def min_operations(word1, word2, m, n):
    tbl = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        tbl[i][0] = i

    for j in range(n + 1):
        tbl[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                tbl[i][j] = tbl[i - 1][j - 1]
            else:
                tbl[i][j] = 1 + min(tbl[i - 1][j - 1], tbl[i][j - 1], tbl[i - 1][j])
    return tbl[m][n]


w1 = "fred"
w2 = "ware"
l1 = len(w1)
l2 = len(w2)

ans = min_operations(w1, w2, l1, l2)

print(f"Min # of operations are: {ans}")
