```py

import datetime 

# convert datetime to timestamp in milliseconds
timestamp_ms = int(datetime.datetime.now().timestamp() * 1000)

print(timestamp_ms)
