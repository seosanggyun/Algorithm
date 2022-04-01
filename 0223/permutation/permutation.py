def permutation(i, N, r):
    if i == N:
        print('='*15, P[0:r], '='*15)
        print()
    else:
        for j in range(i, N):
            P[i], P[j] = P[j], P[i]
            print(P, 'front', i, j)
            permutation(i+1, N, r)
            P[i], P[j] = P[j], P[i]
            print(P, 'back', i, j)


P = [1, 1, 3, 4]
permutation(0, len(P), 2)