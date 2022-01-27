with open("/Users/fafakhan/PycharmProjects/Machine_Learning_Projects/data_dir/input_for_prgs.txt","r") as f:
    temp = f.readlines()

for number in temp:
    a=int(number)
    print("")
    for j in range(a,(2*a + 1),2):
        print(j,end='\t')

        
Output
2	4	
10	12	14	16	18	20	
3	5	
17	19	21	23	25	27	29	31	33	
Process finished with exit code 0
