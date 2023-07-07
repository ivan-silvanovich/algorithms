states_needed = {"mt", "wa", "or", "id", "nv", "ut", "са", "az"}

stations = {
    "one": {"id", "nv", "ut"},
    "two": {"wa", "id", "mt"},
    "three": {"or", "nv", "са"},
    "four": {"nv", "ut"},
    "five": {"ca", "az"}
}

final_stations = set()
while states_needed:
    best_station = max(stations, key=lambda s: len(stations[s] & states_needed))
    final_stations.add(best_station)
    states_needed -= stations[best_station]

print(final_stations)
