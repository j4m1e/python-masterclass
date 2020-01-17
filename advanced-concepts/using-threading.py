"""
Threading. 
Every process that runs within an operating system contains a least one thread and can initiate multiple
threads which are then executed simultaneously in the same process space. This is simular to executing multiple 
applications at the same time. In Python threading can be used to run several functions calls or other tasks 
concurrently especially if those tasks involve some waiting times. This is the case for networking applications and
web related tasks for instance. This is a large and advanced topic in Python so this is only the basics of
threading. A specific library is provided for this specific purpose which is called threading and it is a 
built-in library.  

The threading.Thread() class will be used. The most used methods within this class are start() and join() 

The start() method starts or initiates a thread
The join() method makes sure that the code waits for all threads to terminate
"""
import threading
import time # the sleep() method will be used to interrupt the execution of the code for x seconds

def myFunction():
    print(f"Start a thread")
    time.sleep(3)
    print(f"End a thread")

# run myFunction 5 times concurrently and to wait for all threads to terminate
threads = []

# 5 concurrent instances of the function to be executed 

for i in range(5):
    # use thread class to execute the function
    th = threading.Thread(target = myFunction)
    # start the thread and append each threading object to the threads list
    th.start()
    threads.append(th)

# Use another for loop to iterate over the threads list use the join() method to instruct the code to wait
# for all threads to finish 
for th in threads:
    th.join()


