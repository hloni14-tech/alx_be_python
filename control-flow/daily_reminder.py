task = input('Enter your task: ')
time_bound = input('Is it time bound? (yes/no): ')
priority = input('high/medium/low: ')

if time_bound == 'yes'and  priority == 'high':
    print('Reminder:',question,'is a high priority task that requires immediate attention today!' )
elif time_bound == 'no' and priority == 'low':
    print('Note:',question,'is a low priority task.Consider completing it when you have free time.')