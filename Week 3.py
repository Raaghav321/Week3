# Starting off

print(22/7)
print(355/113)

import math
print(9801/(2206 * math.sqrt(2)))

def archimedes(numSides):
    innerAngles = 360.0 / numSides
    halfAngleA = innerAnglesB / 2
    oneHalfSideS = math.sin(math.radians(halfAngleA))
    sideS = oneHalfSideS
    polygonCircumference = numSides * sideS
    pi = polygonCircumference
    return pi

print(archimedes(8))

