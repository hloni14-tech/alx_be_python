priority = input('Priority (high/medium/low):')

match priority:
    case 'high':
        print('Complete this task immediately.')
    case 'medium':
        print('Try to finish this task today.')
    case 'low':
        print('Handle this task when you have time.')
    case _:
        print('Unknown priority level.')
