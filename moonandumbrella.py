#Problem: https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d1145

def calculate_cost(x, y, curr ,index):
    cost = 0
    lookup = {'CJ':x, 'JC':y, 'JJ':0, 'CC':0}
    for i in range(index,len(query)):
        if query[i] != '?':
            cost += lookup[curr+query[i]]
            curr = query[i]
        else:
            temp_c = lookup[curr + 'C']
            temp_j = lookup[curr + 'J']

            if (temp_c + cost)<(temp_j + cost):
                cost += temp_c
                curr = 'C'
            else:
                cost += temp_j
                curr = 'J'

    return cost
            

def mural(x,y,query):
    total_cost = float('-inf')
    if query[0] == '?':
        c_cost = calculate_cost(x,y,'C', 1)
        j_cost = calculate_cost(x,y,'J', 1)
        return min(c_cost,j_cost)
    return calculate_cost(x,y,query[0],1)


if __name__ == '__main__':
    size = int(input())
    for i in range(size):
            x, y, s = input().split()
            x = int(x)
            y = int(y)
            query = str(s)
            print("Case #{}: {}".format(i+1, mural(x,y,query)))

