import time
from datetime import date


today = date.today()
formatted = today.strftime("%b %d %Y")
epoch_time = time.time()


print("Seconds since January 1, 1970: {:,} or {:e} in scientific notation".format(epoch_time, epoch_time))
print(formatted)