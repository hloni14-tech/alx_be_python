task = input('Enter your task: ')
time_bound = input('Is it time-bound? (yes/no): ')
priority = input('Priority (high\/medium\/low): ')

if time_bound == 'yes'and  priority == 'high':
    print('Reminder:',task,'is a high priority task that requires immediate attention today!' )
elif time_bound == 'no' and priority == 'low':
    print('Note:',task,'is a low priority task.Consider completing it when you have free time.')
elif time_bound == 'yes' or time_bound == 'no' and priority == 'medium':
    print('Remember:',task,'is a medium priority task.Complete it when you are not busy.')