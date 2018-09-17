#Phase1.py

#IMPORT
import string
import re
# Initializing the list, needed.
cities=[]
coordinates=[]
population=[]
distance=[['0']]
updated_distance=[]

#Defining the function getCoordinates to get the coordinates of each city.
def getCoordinates(cityNamestateName):
	get_value=cityNamestateName
	city_index=0
	for cityname in cities:
		if get_value.lower().strip()==cityname.lower().strip():
			break
		else:
			city_index+=1
	#print("{0}, coordinates are {1}".format(cityname,coordinates[city_index]))
	return coordinates[city_index]

#Defining the function getPopulation to get the Population of each city.
def getPopulation(cityNamestateName):
	get_value=cityNamestateName
	city_index=0
	for cityname in cities:
		if get_value.lower().strip()==cityname.lower().strip():
			break
		else:
			city_index+=1
	#print("{0}, population is {1}".format(cityname,population[city_index]))
	return population[city_index]

#Defining the function getDistance to get the distances from the given city to other cities.
def getDistance(cityNamestateName,cityNamestateName1):
	get_value=cityNamestateName
	get_othervalue=cityNamestateName1
	city_index=0
	city_index1=0
	for cityname in cities:
		if get_value.lower().strip()==cityname.lower().strip():
			break
		else:
			city_index+=1
	for cityname1 in cities:
		if get_othervalue.lower().strip()==cityname1.lower().strip():
			break
		else:
			city_index1+=1
	#print("The distance between {0} and {1} is {2}".format(cityname,cityname1,updated_distance[city_index][city_index1]))
	return updated_distance[city_index][city_index1]

#Defining the function nearbycities to find out the distance between the given city and other cities.
def nearbyCities(cityNamestateName,r):
	n_c=[]
	i_2=cityNamestateName
	for j_2 in cities:
		if j_2!=i_2:
			k_2=getDistance(i_2,j_2)
		else:
			k_2=getDistance(i_2,j_2)
		if int(k_2)<=int(r):
			n_c.append(j_2)
	return sorted(n_c)

#Main Function
def main():
	file=open('milesorg.dat','r')
	file_read=file.read()
	file_lines=file_read.split('\n')
	masterlist=[]
	#Breaking each lines in to a list elements.
	for line in file_lines:
		for line1 in line.split('\t'):
			t=line1.split()
			for t1 in t:
				masterlist.append(t1.replace('['," ").replace(']'," "))
	j=0
	for i in masterlist:
		if len(i.split(" "))==1 and i.isdigit() == False:
			temp3=masterlist[j+1].split(" ")
			temp4=i+temp3[0]
			cities.append(temp4.replace(','," ")) #Each City gets appended in to Master Citites List
			coordinates.append(temp3[1])          #Each Coordinates gets appended in to Master Coordinates List 
			population.append(temp3[2])           #Each Population gets appended in to Master Population List
			temp_k=j
			sublist=[]
			while masterlist[temp_k+2].isdigit()==True and (temp_k+2)<=len(masterlist): #Getting all distances in to one mainList
				sublist.append(masterlist[temp_k+2])
				temp_k+=1
				if(temp_k==(len(masterlist)-2)):
					break;
			if sublist!=[]:
				distance.append(sublist)
		j+=1

	#print("d:",distance)
	#print("\n")
	#print("Cities:",cities,"\n")
	#print("Coordinates:",coordinates,"\n")
	#print("Population:",population,"\n")
	
	for num in range(len(distance)):
		templist = [0]*len(distance)
		templist[num]='0'
		k1=num
		m1=1
		while k1>0:
			templist[k1-1]=distance[num][m1-1]
			k1-=1
			m1+=1
		k=num
		m=1
		for num1 in range(k+1,len(distance)):
			tempj=distance[num1]
			templist[num1]=tempj[m-1]
			m+=1
		updated_distance.append(templist)

	#print("Distance:",updated_distance)
	#Getting the Input Value
	#cityNamestateName=input("Enter the City:")
	#r=input("Enter the radius:")
	#cityNamestateName1=input("Enter the other City to find the distance:")

	#Calling all Function Modules
	'''cityNamestateName="Youngstown OH"
	cityNamestateName1="Ravenna OH"
	getCoordinates(cityNamestateName)
	getPopulation(cityNamestateName)
	getDistance(cityNamestateName,cityNamestateName1)'''

if __name__=="__main__":
	main()