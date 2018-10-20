from src.extractor import getData

departFrom = "BCN-sky"
arriveAt = "MAN-sky"
cabinClass = "Economy"

flyOn = "2019-01-06"

noOfPassengers = 1
noOfChildren = 0
noOfInfants = 0

minLayover = 500

print(getData(departFrom, arriveAt, flyOn, noOfPassengers, noOfChildren, noOfInfants, cabinClass, minLayover))