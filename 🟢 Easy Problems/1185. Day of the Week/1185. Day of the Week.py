import calendar

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day_of_week = calendar.weekday(year, month, day)

        return days[day_of_week]