from services.google_calendar_helper import CalendarAccess
from services.todoist_helper import TodoistAccess
from services.motivational_helper import formatted_quotes_calendar, formatted_quotes_todoist, formatted_quotes_todoist_due, formatted_quotes_todoist_keyword, formatted_quotes_todoist_keyword_due
import random

def first_lower(s):
   if not s: # Added to handle case where s == None
    return
   else:
    return s[0].lower() + s[1:]

class MessageGenerator:

    def __init__(self, keyword = None):
        calendar_access = CalendarAccess()
        todoist_access = TodoistAccess()
        self.tasks = todoist_access.get_tasks_info()
        self.events = calendar_access.get_events_info(10)
        self.keyword = keyword

    def generate_random_calendar_message(self):
        descr, start, end = random.choice(self.events)
        quote = random.choice(formatted_quotes_calendar)
        return quote.format(first_lower(descr), self.extract_time(start), self.extract_time(end), self.extract_date(start))

    def generate_random_todoist_message(self):
        descr, due = random.choice(self.tasks)

        if self.keyword != None:
            if due:
                quote = random.choice(formatted_quotes_todoist_keyword_due)
                return quote.format(str.lower(self.keyword), first_lower(descr),due["string"])
            else:
                quote = random.choice(formatted_quotes_todoist_keyword)
                return quote.format(str.lower(self.keyword), first_lower(descr))
        else:
            if due:
                quote = random.choice(formatted_quotes_todoist_due)
                return quote.format(first_lower(descr), due["string"])
            else:
                quote = random.choice(formatted_quotes_todoist)
                return quote.format(first_lower(descr))

    def extract_date(self, time):
        return time[:10]

    def extract_time(self, time):
        return time[11:16]


if __name__ == '__main__':
    g = MessageGenerator("sports")
    print(g.generate_random_calendar_message())
    print(g.generate_random_todoist_message())