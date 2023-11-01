# Dynamic Programming Python3
# implementation to find minimum
# number of deletions and insertions

# Returns length of length
# common subsequence for
# str1[0..m-1], str2[0..n-1]
def lcs(str1_local, str2_local, m, n):
    l = [[0 for i in range(n + 1)]
         for i in range(m + 1)]

    # Following steps build L[m+1][n+1]
    # in bottom up fashion. Note that
    # L[i][j] contains length of LCS
    # of str1[0..i-1] and str2[0..j-1]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                l[i][j] = 0
            elif str1_local[i - 1] == str2_local[j - 1]:
                l[i][j] = l[i - 1][j - 1] + 1
            else:
                l[i][j] = max(l[i - 1][j],
                              l[i][j - 1])

    # L[m][n] contains length of LCS
    # for X[0..n-1] and Y[0..m-1]
    return l[m][n]


# function to find minimum number
# of deletions and insertions
def print_min_del_and_insert(str1_local, str2_local):
    m = len(str1_local)
    n = len(str2_local)
    leng = lcs(str1_local, str2_local, m, n)
    print(f"Going from {str1_local} to {str2_local}")
    print("Minimum number of deletions = ",
          m - leng, sep=' ')
    print("Minimum number of insertions = ",
          n - leng, sep=' ')


# Driver Code
str1 = "horse"
str2 = "ros"

# Function Call
print_min_del_and_insert(str1, str2)