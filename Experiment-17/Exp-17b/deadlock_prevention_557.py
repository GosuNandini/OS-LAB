def deadlock_prevention():
    n = int(input("Enter no of jobs: "))
    jobs = []
    for i in range(n):
        job_name, job_time = input(f"Enter name and time: ").split()
        jobs.append((job_name, int(job_time)))
    avail = int(input("Enter the available resources: "))
    jobs.sort(key=lambda x: x[1])
    safe_sequence = []
    for job_name, job_time in jobs:
        if job_time <= avail:
            safe_sequence.append((job_name, job_time))
            avail -= job_time
        else:
            print("No safe sequence")
            return
    print("Safe sequence is:")
    for job_name, job_time in safe_sequence:
        print(f"{job_name} {job_time}")
deadlock_prevention()
