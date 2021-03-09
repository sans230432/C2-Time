## Time 
A class that handles time-related tasks

## Formula 
`import time`

### usful functions 
1. time.time() 
- returns floating-point numbers in seconds passed since epoch (january 1st, 1970, 00:00 at UTC)
- use it for date arithmetics (etc. duration) 
```python 
import time 
#function: time() 
print("Seconds since epoch = " + str(time.time()))

2. time.sleep() 
- Suspends (delays) execution for a given number of seconds 
`time.sleep(3.3)` pause  our code for 3.3 seconds