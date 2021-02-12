# code
def rankMatrix(diction):
    for i in range(0,n):
        li = diction[i]

        r3 = li[0][0] * ((li[1][1] * li[2][2])-(li[2][1] * li[1][2])) - li[0][1] * ((li[1][0] * li[2][2])-(li[2][0] * li[1][2])) + li[0][2] * ((li[1][0] * li[2][1])-(li[2][0] * li[1][1]))
        if r3 == 0:
            if ((li[1][1] * li[2][2]) - (li[2][1] * li[1][2])) or  ((li[0][0] * li[1][1]) - (li[1][0] * li[0][1])) or ((li[0][1] * li[1][2]) - (li[1][1] * li[0][2])) or ((li[1][0] * li[2][1]) - (li[2][0] * li[1][1])) != 0:
                print(2);
            else:
                print(1);
        else:
            print(3)




n = int(input())
diction = {}
for i in range(0, n):
    temp_list = []
    for j in range(0, 3):
        j = input()
        numbers = [int(x) for x in j.split()]
        temp_list.append(numbers)
    diction[i] = temp_list
rankMatrix(diction)
