import pandas as pd
import sys
import math

#Calculates the great circle distance, this case the Earth
def haversine(lat1, long1, lat2, long2):

    radiusOfEarthInMiles = 3958.8

    lat1Radians = math.radians(lat1)
    long1Radians = math.radians(long1)
    lat2Radians = math.radians(lat2)
    long2Radians = math.radians(long2)

    a = pow(math.sin((lat2Radians-lat1Radians)/2),2) + math.cos(lat1Radians) * math.cos(lat2Radians) * pow(math.sin((long2Radians-long1Radians)/2),2)
    c = 2 * math.atan2(math.sqrt(a),math.sqrt(1-a))

    return radiusOfEarthInMiles*c


#Reads file and places in a dictonary
df = pd.read_csv('your file path')

df.head()
locations = pd.read_csv('your file path')
locations.head()
lat1 = df.at[0,'Latitude']
long1 = df.at[0,'Longitude']
lat2 = locations.at[0,'Latitude']
long2 = locations.at[0,'Longitude']
distance = haversine(lat1,long1,lat2,long2)
distance

def rand_Partition(A,L,R):
    x = A[L]
    i = L
    for j in range(L+1, R+1):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i],A[L] = A[L],A[i]
    return i

def rand_Select(A,L,R,i):
    if L == R:
        return A[L]
    z = rand_Partition(A,L,R)
    k = z - L
    if k == i:
        return A[z]
    elif i < k:
        return rand_Select(A,L,z-1,i)
    else:
        return rand_Select(A,z+1,R,i-(k+1))

stores = locations.at[0,'Number of stores desired']
stores
