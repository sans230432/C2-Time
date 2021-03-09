import time
#function: time() 
print("Seconds since epoch = " + str(time.time()))

countdown = 3 
while(countdown >= 0): 
  print(countdown) 
  countdown -= 1
  time.sleep(1)
print("AAAAAAAAAAAAAAAAA!")

startTime = time.time()
userName = input("type your name: ")
endtime = time.time() 
print("Elapsed time: " + str(endTime-startTime))