from urllib.request import urlopen
import json
from pprint import pprint

def read_positions(data):
    driver_positions_list = [i["position"] for i in data]
    return driver_positions_list

def comprehend_positions(data:list[int],):
    worst_position_during_race = max(data)
    starting_position = data[0]
    finishing_position = data[-1]
    print(f"Worst Position During Race: {worst_position_during_race}\nStarting Position: {starting_position}\nFinishing Position: {finishing_position}")

response = urlopen('https://api.openf1.org/v1/position?meeting_key=latest&driver_number=44')
data = json.loads(response.read())
driver_positions = read_positions(data)

print(driver_positions)
comprehend_positions(driver_positions)


