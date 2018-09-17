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
serveddummy_list=[]
served_list=[]

#Get cities names
def getcities_names(cityind):
	for city_ind,city_name in enumerate(cities):
		if city_ind==cityind:
			return city_name

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
			#print(f_c)
		for d,d1 in enumerate(c_list[k]):
			if d1==city_ind:
				if served[d1]=='False':
					served[d1]='True'
					c1=getcities_names(d1)
					serveddummy_list.append(c1)
	served_list.append(serveddummy_list)
	if max==0:
		return None
	return f_c

#Locating the Facilities
def locatefacilities(cities,updated_distance,r):
	Facility_Centre=[]
	us=unserved_list(cities,updated_distance,r,served)
	f=finding_max(us,cities)
	Facility_Centre.append(f)
	while f:
		us=unserved_list(cities,updated_distance,r,served)
		f=finding_max(us,cities)
		if f!=None:
			Facility_Centre.append(f)
	return Facility_Centre

#Defining the function getCoordinates to get the coordinates of each city.
def getCoordinates(cityNamestateName):
	get_value=cityNamestateName
	city_index=0
	for cityname in cities:
		if get_value.lower().strip()==cityname.lower().strip():
			break
		else:
			city_index+=1
	return coordinates[city_index]

#Creating KML File
def display(facilities,cities,distances,coordinates):
	s=""
	f=open("display_file.kml","w")
	f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
	f.write("<kml xmlns=\"http://www.opengis.net/kml/2.2\">\n")
	f.write("<Document>\n")
	f.write("<Style id=\"smallLine\">\n")
	f.write("<LineStyle>\n")
	f.write("<color>7f00007f</color>\n")
	f.write("<width>4</width>\n")
	f.write("</LineStyle>\n")
	f.write("<PolyStyle>\n")
	f.write("<color>7f00007f</color>\n")
	f.write("</PolyStyle>\n")
	f.write("</Style>\n")
	f.write("<Folder>\n")
	i=0
	while i<len(facilities):
		f.write("\n<Placemark>\n") 
		f.write("\t<name>%s</name>\n" %(facilities[i]))
		j=getCoordinates(facilities[i])
		k=j.split(",")
		f.write("\t<description>The start of our journey!</description>\n")
		f.write("\t<Point>\n")
		f.write("\t\t<coordinates>-%s,%s,0</coordinates>\n" %(int(k[1])/100,int(k[0])/100))
		f.write("\t</Point>\n")
		f.write("</Placemark>\n")
		for s in served_list[i]:
			f.write("\n<Placemark>\n")
			f.write("<name>%s,%s</name>\n" %(facilities[i],s))
			f.write("<description>Facility Centre</description>\n")
			f.write("<styleUrl>#smallLine</styleUrl>\n")
			f.write("<LineString>\n")
			f.write("<extrude>1</extrude>\n")
			f.write("<tessellate>1</tessellate>\n")
			f.write("<altitudeMode>absolute</altitudeMode>\n")
			j_1=getCoordinates(s)
			k_1=j_1.split(",")
			f.write("<coordinates>-%s,%s,0</coordinates>\n" %(int(k[1])/100,int(k[0])/100))
			f.write("<coordinates>-%s,%s,0</coordinates>\n" %(int(k_1[1])/100,int(k_1[0])/100))
			f.write("</LineString>\n")
			f.write("</Placemark>\n")
		i+=1
	f.write("\n</Folder>\n")
	f.write("</Document>\n")
	f.write("</kml>")

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
	facilities=locatefacilities(cities,updated_distance,r)
	display(facilities,cities,updated_distance,coordinates)

if __name__=="__main__":
	main()