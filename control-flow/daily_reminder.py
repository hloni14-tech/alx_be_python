question = input('Enter your task: ')
priority = input('high/medium/low: ').lower()
time_bound = input('Is it time bound? (yes/no): ').lower()

if time_bound == 'yes':
    print('Reminder:',question,'is a high priority task that requires immediate attention today!' )
elif time_bound == 'no':
    print('Note:',question,'is a low priority task.Consider completing it when you have free time.')