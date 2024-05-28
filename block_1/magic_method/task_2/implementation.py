from datetime import time, timedelta

class MathClock:
    def __init__(self):
        self.time = time(00, 00)
    
    def __add__(self, min):
        td =  timedelta(hours=self.time.hour, minutes=self.time.minute)
        alltd = td + timedelta(minutes=min)
        sec = alltd.total_seconds()
        self.time = time(int(alltd.seconds//3600), int((sec-sec//3600*3600)/60))

    def __sub__(self, min):
        td =  timedelta(hours=self.time.hour, minutes=self.time.minute)
        alltd = td - timedelta(minutes=min)
        sec = alltd.total_seconds()
        self.time = time(int(alltd.seconds//3600), int((sec-sec//3600*3600)/60))

    def __mul__(self, h):
        td =  timedelta(hours=self.time.hour, minutes=self.time.minute)
        alltd = td + timedelta(hours=h)
        sec = alltd.total_seconds()
        self.time = time(int(alltd.seconds//3600), int((sec-sec//3600*3600)/60))
    
    def __truediv__(self, h):
        td =  timedelta(hours=self.time.hour, minutes=self.time.minute)
        alltd = td - timedelta(hours=h)
        sec = alltd.total_seconds()
        self.time = time(int(alltd.seconds//3600), int((sec-sec//3600*3600)/60))

    def get_time(self):
        return self.time.strftime("%H:%M")
