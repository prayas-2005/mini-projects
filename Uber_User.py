def uber_ride(l, fares):
    uber = ["UberX", "UberXL", "UberPlus", "UberBlack", "UberSUV"]
    best_car = []
    for f in range(len(fares) -1, -1, -1):
         total_fares = l * fares[f]
         if total_fares <= 200:
             best_car.append(uber[f])
     
             
    if len(best_car) != 0:
        return best_car[0]
    else:
        return

fares = [3, 5, 7, 10, 13]
l = (int)(input("Enter the ride distance : "))
print(uber_ride(l, fares))

