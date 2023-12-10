from collections import defaultdict

def calculate_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def min_distance_traveled(N, M, passengers, vehicles):
    passenger_allocation = {}
    vehicle_allocation = defaultdict(list)

    passengers.sort()
    vehicles.sort()

    total_distance = 0

    for passenger in passengers:
        passenger_name, px, py = passenger[0], passenger[1], passenger[2]
        min_distance = float('inf')
        assigned_vehicle = ""

        for vehicle in vehicles:
            vehicle_number, vx, vy = vehicle[0], vehicle[1], vehicle[2]
            distance = calculate_distance(px, py, vx, vy)

            if distance < min_distance or (distance == min_distance and vehicle_number < assigned_vehicle):
                min_distance = distance
                assigned_vehicle = vehicle_number

        passenger_allocation[passenger_name] = assigned_vehicle
        vehicle_allocation[assigned_vehicle].append(passenger_name)
        total_distance += min_distance

    return total_distance

def main():
    N, M = map(int, input().split())
    passengers = [input().split() for _ in range(N)]
    vehicles = [input().split() for _ in range(M)]

    result = min_distance_traveled(N, M, passengers, vehicles)
    print(result)

if __name__ == "__main__":
    main()
