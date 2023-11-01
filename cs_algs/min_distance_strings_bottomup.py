def min_operations(word1, word2, m, n):
    replacements = 0
    insertions = 0
    deletions = 0

    # tbl = [[0] * (n + 1) for _ in range(m + 1)]
    tbl = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        tbl[i][0] = i

    for j in range(n + 1):
        tbl[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                tbl[i][j] = tbl[i - 1][j - 1]
            else:
                chosen = 0
                # tbl[i][j] = 1 + min(tbl[i - 1][j - 1], tbl[i][j - 1], tbl[i - 1][j])
                if tbl[i - 1][j - 1] < tbl[i][j - 1]:       # replacement < insertion?
                    if tbl[i - 1][j - 1] < tbl[i - 1][j]:   # replacement < deletion?
                        replacements += 1
                        chosen = 1 + tbl[i - 1][j - 1]
                    elif tbl[i - 1][j] < tbl[i][j - 1]:     # deletion < insertion?
                        deletions += 1
                        chosen = 1 + tbl[i - 1][j]
                    else:                                   # otherwise insertion is the minimal
                        insertions += 1
                        chosen = 1 + tbl[i][j - 1]
                elif tbl[i][j - 1] < tbl[i - 1][j]:         # insertion < deletion?
                    insertions += 1
                    chosen = 1 + tbl[i][j - 1]
                else:                                       # otherwise deletion is the minimal
                    deletions += 1
                    chosen = 1 + tbl[i - 1][j]

                tbl[i][j] = chosen

    return tbl[m][n], replacements, insertions, deletions


w1 = "horse"
w2 = "ho"
l1 = len(w1)
l2 = len(w2)

num_ops, replace, insert, delete = min_operations(w1, w2, l1, l2)

print(f"Min # of operations are: {num_ops}")
print(f"# of replacements: {replace}")
print(f"# of insertions: {insert}")
print(f"# of deletions: {delete}")
