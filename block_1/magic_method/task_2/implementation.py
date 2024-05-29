from datetime import time, timedelta

class MathClock:
    def __init__(self):
        self.time = time(00, 00)
 
    def __add__(self, min):        
        self.time = set_result_time(self.time, timedelta(minutes=min), True)

    def __sub__(self, min):       
        self.time = set_result_time(self.time, timedelta(minutes=min), False)

    def __mul__(self, h):
        self.time = set_result_time(self.time, timedelta(hours=h), True)
    
    def __truediv__(self, h):
        self.time = set_result_time(self.time, timedelta(hours=h), False)

    def get_time(self):
        return self.time.strftime("%H:%M")


def set_result_time(self_time, timedel, is_sum):
    all_td =  timedelta(hours=self_time.hour, minutes=self_time.minute)
    if is_sum:
        all_td = all_td + timedel
    else:
        all_td = all_td - timedel
    sec = all_td.total_seconds()
    return time(int(all_td.seconds//3600), int((sec-sec//3600*3600)/60))
