class StudySession:
    
    def __init__(self, subject, hours, productivity, date):
        self.subject = subject
        self.hours = hours
        self.productivity = productivity
        self.date = date

    def to_list(self):
        return [self.subject, self.hours, self.productivity, self.date]
