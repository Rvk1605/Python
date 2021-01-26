from time import*
init=time()
print (init)

for i in range(100):
    sleep(0.5)
    i = i + 1
    print(i)
print(time())
print("For Loop Time = ",init-time())


#Local Time
local=asctime(localtime(time()))
print(local)