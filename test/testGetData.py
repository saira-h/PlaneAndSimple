from src.extractor import getData

departFrom = "BCN-sky"
arriveAt = "MAN-sky"
cabinClass = "Economy"

flyOn = "2018-11-02"

noOfPassengers = 1
noOfChildren = 0
noOfInfants = 0

print(getData(departFrom, arriveAt, flyOn, noOfPassengers, noOfChildren, noOfInfants, cabinClass))