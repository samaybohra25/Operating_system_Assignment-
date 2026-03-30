# CPU Scheduling: FCFS & SJF (Non-Preemptive)

class Process:
    def __init__(self, pid, at, bt):
        self.pid = pid
        self.at = at
        self.bt = bt
        self.ct = 0
        self.tat = 0
        self.wt = 0


# ---------- INPUT ----------
def take_input():
    processes = []
    n = int(input("Enter number of processes: "))
    
    for i in range(n):
        pid = f"P{i+1}"
        at = int(input(f"Enter Arrival Time of {pid}: "))
        bt = int(input(f"Enter Burst Time of {pid}: "))
        processes.append(Process(pid, at, bt))
    
    return processes


def display(processes):
    print("\nPID\tAT\tBT")
    for p in processes:
        print(f"{p.pid}\t{p.at}\t{p.bt}")


# ---------- FCFS ----------
def fcfs(processes):
    processes.sort(key=lambda x: x.at)
    
    time = 0
    gantt = []

    for p in processes:
        if time < p.at:
            time = p.at  # CPU idle
        
        time += p.bt
        p.ct = time
        p.tat = p.ct - p.at
        p.wt = p.tat - p.bt
        
        gantt.append((p.pid, time))

    return gantt


# ---------- SJF (Non-Preemptive) ----------
def sjf(processes):
    n = len(processes)
    completed = 0
    time = 0
    visited = [False] * n
    gantt = []

    while completed < n:
        idx = -1
        min_bt = float('inf')

        for i in range(n):
            if processes[i].at <= time and not visited[i]:
                if processes[i].bt < min_bt:
                    min_bt = processes[i].bt
                    idx = i
        
        if idx != -1:
            visited[idx] = True
            time += processes[idx].bt
            processes[idx].ct = time
            processes[idx].tat = processes[idx].ct - processes[idx].at
            processes[idx].wt = processes[idx].tat - processes[idx].bt
            
            gantt.append((processes[idx].pid, time))
            completed += 1
        else:
            time += 1  # CPU idle
    
    return gantt


# ---------- OUTPUT ----------
def show_result(processes):
    print("\nPID\tAT\tBT\tCT\tTAT\tWT")
    for p in processes:
        print(f"{p.pid}\t{p.at}\t{p.bt}\t{p.ct}\t{p.tat}\t{p.wt}")


def avg_time(processes):
    n = len(processes)
    avg_tat = sum(p.tat for p in processes) / n
    avg_wt = sum(p.wt for p in processes) / n
    print(f"\nAverage TAT = {avg_tat:.2f}")
    print(f"Average WT = {avg_wt:.2f}")


def gantt_chart(gantt):
    print("\nGantt Chart:")
    for p, _ in gantt:
        print(f"| {p} ", end="")
    print("|")
    
    print("0", end="")
    for _, t in gantt:
        print(f"\t{t}", end="")
    print()


# ---------- MAIN ----------
processes = take_input()
display(processes)

# FCFS
print("\n--- FCFS ---")
fcfs_processes = [Process(p.pid, p.at, p.bt) for p in processes]
gantt_fcfs = fcfs(fcfs_processes)
show_result(fcfs_processes)
avg_time(fcfs_processes)
gantt_chart(gantt_fcfs)

# SJF
print("\n--- SJF ---")
sjf_processes = [Process(p.pid, p.at, p.bt) for p in processes]
gantt_sjf = sjf(sjf_processes)
show_result(sjf_processes)
avg_time(sjf_processes)
gantt_chart(gantt_sjf)


# ---------- CREDIT ----------
print("\n" + "="*30)
print("      Coded by Dipesh")
print("="*30)