print("--PERSONILIZED STUDY TIMER--")

total_study_time = float(input("how many hours do you want to study for ? "))
no_subjects = int(input("How many subjects do you want to study ? "))
subject_array = [None] * (no_subjects) #creating an array to store the subjects

for i in range(no_subjects):
    subject_array[i] = str(input("Enter Your Subject name: ").upper())

study_time = total_study_time * 0.7
break_time = total_study_time * 0.3
#a 30% break time and 70% study time is a good balance

choice = input("do you want pomodor cycle or just simple time suggestion ? (Yes/No) ").lower()
if choice == "yes":
    print("Pomodoro cycle: 25 minutes study, 5 minutes break")
    cycles = int(study_time // (25/60))
    print(f"You can do {cycles} pomodoro cycles in {study_time:.2f} hours")
else:
    time_per_subject = study_time / no_subjects

    for x in range(no_subjects):
        print(f"Study {subject_array[x]}: {time_per_subject:.2f} hours")

    print(f"take a break for {break_time:.2f} hours")
    