# Banker's Algorithm (Deadlock Avoidance)

# ---------- INPUT ----------
n = int(input("Enter number of processes: "))
m = int(input("Enter number of resources: "))

print("\nEnter Allocation Matrix:")
allocation = []
for i in range(n):
    row = list(map(int, input(f"P{i}: ").split()))
    allocation.append(row)

print("\nEnter Maximum Matrix:")
maximum = []
for i in range(n):
    row = list(map(int, input(f"P{i}: ").split()))
    maximum.append(row)

print("\nEnter Available Resources:")
available = list(map(int, input().split()))


# ---------- NEED MATRIX ----------
need = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(maximum[i][j] - allocation[i][j])
    need.append(row)

print("\nNeed Matrix:")
for i in range(n):
    print(f"P{i}: {need[i]}")


# ---------- SAFETY ALGORITHM ----------
finish = [False] * n
safe_sequence = []
work = available.copy()

while len(safe_sequence) < n:
    found = False

    for i in range(n):
        if not finish[i]:
            if all(need[i][j] <= work[j] for j in range(m)):
                
                # allocate resources
                for j in range(m):
                    work[j] += allocation[i][j]
                
                safe_sequence.append(f"P{i}")
                finish[i] = True
                found = True

    if not found:
        break


# ---------- RESULT ----------
if len(safe_sequence) == n:
    print("\nSystem is in SAFE state ✅")
    print("Safe Sequence:", " -> ".join(safe_sequence))
else:
    print("\nSystem is NOT in safe state ❌")


# ---------- CREDIT ----------
print("\n" + "="*30)
print("      Coded by Dipesh")
print("="*30)