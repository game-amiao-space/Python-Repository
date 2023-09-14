m = int(input("请输入M:"))
lists = list(m)
for i in lists:
    if(m[i] != 9):
        print(0)
    else:
        print(m[i] + 1)

