# Lab 4: Trace One Request
# Shows the steps behind one API call: the DNS lookup, the round trip, and what came back.

import os
import socket
import requests

host = "api.nasa.gov"

# Step 1: DNS turns the name into an IP address
address = socket.gethostbyname(host)
print("DNS lookup:", host, "is at", address)

# Step 2: send one request over HTTPS and time the round trip
key = os.environ.get("NASA_API_KEY", "DEMO_KEY")    # falls back to NASA's shared practice key
settings = {"start_date": "1969-07-20", "end_date": "1969-07-20", "api_key": key}
response = requests.get("https://" + host + "/neo/rest/v1/feed", params=settings)
print("Status code:", response.status_code)
print("Round trip:", round(response.elapsed.total_seconds() * 1000), "milliseconds")

# Step 3: headers are labeled notes the server sends along with the data
print("Content type:", response.headers.get("Content-Type"))
print("Requests left this hour:", response.headers.get("X-RateLimit-Remaining"), "of", response.headers.get("X-RateLimit-Limit"))
print("Size of the data:", f"{len(response.content):,}", "bytes")
