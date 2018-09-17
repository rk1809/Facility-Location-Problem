#IMPORT
import string
import re

# Initializing the list, needed.
cities=[]
coordinates=[]
population=[]
distance=[['0']]
updated_distance=[]
c_list=[]
served=['False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False']

#Unserved cities list,covered by each city within the radius
def unserved_list(cities,updated_distance,r,served):
	us_list=[]
	for city_ind,city_name in enumerate(cities):
		total=0
		c_dummylist=[]
		s_i=0
		for dis_index,dis_iList in enumerate(updated_distance[city_ind]):
			if int(dis_iList)<=r and served[s_i]=='False':
				total+=1
				c_dummylist.append(dis_index)
			s_i=s_i+1
		c_list.append(c_dummylist)
		us_list.append(total)
	return us_list

#Finding max from the unserved cities list, which covers the maximum
def finding_max(us,cities):
	dummy=[]
	unserved=[]
	f_c=None
	max=0
	k=0
	for us_ind,us_value in enumerate(us):
		if us_value>max:
			max=us_value
			k=us_ind
	for city_ind,city_name in enumerate(cities):
		if city_ind==k:
			f_c=city_name
		for d,d1 in enumerate(c_list[k]):
			if d1==city_ind:
				served[d1]='True'
	if max==0:
		return None
	return f_c

#Locating the Facilities
def locatefacilities(cities,updated_distance,r):
	Facility_Centre=[]
	us=unserved_list(cities,updated_distance,r,served)
	f=findingmax(us,cities)
	Facility_Centre.append(f)
	while f:
		us=unserved_list(cities,updated_distance,r,served)
		f=finding_max(us,cities)
		if f!=None:
			Facility_Centre.append(f)
	print("Facility Centres:",Facility_Centre,"\nSorted FC:",sorted(Facility_Centre),"\nLength of FC",len(Facility_Centre))

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
	r=1000
	locatefacilities(cities,updated_distance,r)

if __name__=="__main__":
	main()