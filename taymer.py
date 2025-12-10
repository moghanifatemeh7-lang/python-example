import time
from datetime import datetime
def start_timer():

 while True:
    now=datetime.now()
    hours = now.hour
    minutes = now.minute
    seconds = now.second
    milliseconds = now.microsecond // 1000
    microseconds = now.microsecond % 1000
    time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d},{microseconds:03d}"
    print(f"\r{ time_str}", end="", flush=True)

    time.sleep(0.01)

start_timer()