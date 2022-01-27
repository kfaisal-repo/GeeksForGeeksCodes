with open("/Users/fafakhan/PycharmProjects/Machine_Learning_Projects/data_dir/input_for_prgs.txt","r") as f:
    temp = f.readlines()

for number in temp:
    a=int(number)
    print("")
    for j in range(a,(2*a + 1),2):
        print(j,end='\t')
