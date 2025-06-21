from time import sleep

Processes = [
    {"pid": "P1", "arrival_time": 0, "burst_time": 5},
    {"pid": "P2", "arrival_time": 1, "burst_time": 3},
    {"pid": "P3", "arrival_time": 2, "burst_time": 1}
]

time_quantum = 2

order = []

def runProcess(index, time):
    global Processes
    Processes[index]["burst_time"] -= time

done = False
completed = [False, False, False]
index = 0
wait_times = [None, None, None]
turnaround_times = [None, None, None]
time = 0
order = []
while not done:
    if not completed[index]:
        order.append(index)
        runProcess(index, time_quantum)
        if Processes[index]["burst_time"] <= 0:
            completed[index] = True
            turnaround_times[index] = time - Processes[index]["arrival_time"]
            wait_times[index] = turnaround_times[index] - Processes[index]["burst_time"]
            if completed[0] and completed[1] and completed[2]:
                done = True
    if index < 2:
        index += 1
    else:
        index = 0
    time += 1

order_message = ''
for i in order:
    order_message += 'P' + str(i+1) + '(2) → '
order_message = order_message[:-2]

avg_waiting = 0
for i in wait_times:
    avg_waiting += i
avg_waiting /= 3

avg_turnaround = 0
for i in turnaround_times:
    avg_turnaround += i
avg_turnaround /= 3

print("Order:", order_message)
print("Average Waiting Time:", avg_waiting)
print("Average Turnaround tTime:", avg_turnaround)