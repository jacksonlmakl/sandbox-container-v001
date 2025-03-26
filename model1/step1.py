from datetime import datetime
from zoneinfo import ZoneInfo  # Available in Python 3.9+

# Get current time in New York
nyc_time = datetime.now(ZoneInfo("America/New_York"))

# Print formatted time
print("Port 1201")
print("Current time in NYC:", nyc_time.strftime("%Y-%m-%d %H:%M:%S"))
