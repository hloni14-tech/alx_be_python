from datetime import datetime, timedelta

def display_current_datetime():   
    add = input('Enter a number of days to add to the current date: ')
    try:
        number_of_days = int(add)
    except ValueError:
        print('Please enter a valid integer.')
        return
    current_datetime = datetime.now()
    print('Current date and time:', current_datetime)
    future_date = current_datetime + timedelta(days=number_of_days)
    print(f'Date after {number_of_days} days:', future_date)
def calculate_future_date():
    pass  

if __name__ == "__main__":
    display_current_datetime()