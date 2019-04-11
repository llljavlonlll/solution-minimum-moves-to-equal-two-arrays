def minimumMoves(a, m):
    #counter for number of total moves
    moves = 0

    for i in range(len(a)):
        #split numbers into single digits lists
        list_a = [int(l) for l in str(a[i])]
        list_m = [int(k) for k in str(m[i])]

        for i in range(len(list_a)):
            if  list_a[i] > list_m[i]:
                while list_a[i] != list_m[i]:
                    list_a[i] -= 1
                    moves += 1
            elif list_a[i] < list_m[i]:
                while list_a[i] != list_m[i]:
                    list_a[i] += 1
                    moves += 1

    return moves

print(minimumMoves([1234,4321],[2345,3214]))
