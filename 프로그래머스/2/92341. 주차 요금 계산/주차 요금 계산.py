from datetime import datetime, timedelta
import math

def solution(fees, records):
    answer = []
    parked_cars = {}
    total_parking = {}

    for record in records:
        car_time, car_num, status = record.split(' ')
        car_time = datetime.strptime(car_time, '%H:%M')

        if status == 'IN':
            parked_cars[car_num] = car_time
        
        else:
            prev_time = car_time - parked_cars.pop(car_num)
            total_parking[car_num] = total_parking.get(car_num, timedelta(0)) + prev_time

    if parked_cars:
        for car_num, car_time in parked_cars.items():
            parked_time = datetime.strptime('23:59', '%H:%M') - parked_cars[car_num]
            total_parking[car_num] = total_parking.get(car_num, timedelta(0)) + parked_time

    for car_num in sorted(total_parking.keys()):
        total = total_parking[car_num].total_seconds() / 60
        final = total - fees[0]
        if final < 0:
            answer.append(fees[1])
        
        else:
            answer.append(fees[1] + math.ceil(final/fees[2]) * fees[3])

    return answer