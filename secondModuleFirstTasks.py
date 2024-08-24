

#Task 4
seconds_per_day = 86400
seconds_per_hour = 3600
seconds_per_minute = 60

seconds_input = int(input("Введите количество секунд: "))

days = seconds_input // seconds_per_day
hours = (seconds_input % seconds_per_day) // seconds_per_hour
minutes = (seconds_input % seconds_per_hour) // seconds_per_minute
seconds = seconds_input % seconds_per_minute

formated_time = "{}d {}:{:.0f}:{:.0f}".format(days,hours,minutes,seconds)
print(formated_time)