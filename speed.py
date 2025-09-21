avg_speed, speed_limit, distance = map(float, [
    input("Enter your average speed (mph): "),
    input("Enter the speed limit (mph): "),
    input("Enter the distance traveled (miles): ")
])

time_saved = ((distance / speed_limit) - (distance / avg_speed)) * 60
print(f"Time saved by speeding: {time_saved:.2f} minutes")
