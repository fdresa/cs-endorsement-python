# Lab 4: API Data Explorer
# Asks NASA which asteroids passed Earth on one date, using your key from a Codespaces secret.

import os
import requests

DATE = "1969-07-20"    # change this to any date, written year-month-day


def ask_nasa(date, key):
    """Send one request to NASA's asteroid feed for a single date and return the response."""
    settings = {"start_date": date, "end_date": date, "api_key": key}
    return requests.get("https://api.nasa.gov/neo/rest/v1/feed", params=settings)


def describe(asteroid):
    """Provided tool: print one asteroid's name, size, closest distance, speed, and hazard flag."""
    name = asteroid["name"]
    size = asteroid["estimated_diameter"]["meters"]["estimated_diameter_max"]
    approach = asteroid["close_approach_data"][0]    # [0] means the first item (Lesson 5)
    miles = float(approach["miss_distance"]["miles"])    # NASA sends these numbers as text
    moons = float(approach["miss_distance"]["lunar"])
    speed = float(approach["relative_velocity"]["miles_per_hour"])
    hazardous = asteroid["is_potentially_hazardous_asteroid"]
    print(name)
    print("  Size: up to", round(size), "meters across")
    print("  Closest approach:", f"{round(miles):,}", "miles, or", round(moons, 1), "times the distance to the Moon")
    print("  Speed:", f"{round(speed):,}", "miles per hour")
    print("  Potentially hazardous?", hazardous)
    print()


def report(data, date):
    """Provided tool: print every asteroid in NASA's answer for one date."""
    print(data["element_count"], "asteroids passed Earth on", date)
    print()
    for asteroid in data["near_earth_objects"][date]:
        describe(asteroid)


def explore(date):
    """Ask NASA about one date and print what comes back."""
    key = os.environ.get("NASA_API_KEY")    # the key comes from your Codespaces secret
    if not key:
        print("No NASA_API_KEY found. Add the Codespaces secret, then stop and restart your codespace.")
        return    # a bare return ends the function early
    response = ask_nasa(date, key)
    print("Status code:", response.status_code)
    print()

    # YOUR CODE (Part B): report only when the status code is 200.
    # Otherwise, print that NASA did not send data, then print response.text.
    report(response.json(), date)


explore(DATE)
