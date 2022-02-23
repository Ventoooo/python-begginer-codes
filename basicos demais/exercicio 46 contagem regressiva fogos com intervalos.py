from time import sleep
for qualquervariavel in range(10,-1,-1):
    print("Os a sequencia de fogos estourara em: {}".format(qualquervariavel))
    sleep(1)
print('\033[31m!'*10,"BUM",'!'*10)