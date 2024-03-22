import pandas as pd
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

#Partitions and swaps elements
def rand_Partition(A,L,R):
    x = A[L]
    i = L
    for j in range(L+1, R+1):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i] #swap 
    A[i],A[L] = A[L],A[i]
    return i

#Picks random pivot
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

#Reads WhataburgerData and Queries and places in a dictonary
df_whataburger = pd.read_csv('WhataburgerData.csv')
df_queries = pd.read_csv('Queries.csv')

for i, row in df_queries.iterrows():
    lat = row['Latitude']
    long = row['Longitude']
    desired_store = row['Number of stores desired']

    distance = []
    for _, store_rows in df_whataburger.iterrows():
        distance = haversine(lat, long, store_rows['Latitude'], store_rows['Longitude'])
        distance.append(distance)


#TO DO NEED TO FIND CLOSEST STORES

