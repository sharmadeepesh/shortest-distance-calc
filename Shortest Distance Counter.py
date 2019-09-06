#Import The Necessary Modules
from itertools import *


#Get The Input From The User
coordinates=[]
coordinates.append(input("[+] Enter the starting point : "))
coordinates.append(input("[+] Enter the ending point : "))
number = int(input("[+] Enter the number of members : "))
for i in range(number):
	coordinates.append(input("[+] Enter the coordinates of member : "))
lencount = len(coordinates)
coordinates.insert(len(coordinates),coordinates.pop(1))

#Generate Permutations Of The List
permutation = permutations(coordinates)
permutation = list(permutation)
new_permutation = []

#Filter the Permutations for a more efficient List
for i in range(len(permutation)):                                                       
        if permutation[i][0]==coordinates[1] and permutation[i][-1]==coordinates[-1]:
                new_permutation.append(permutation[i])

#Calculate The Shortest Distance
def calc_single_distance(new_permutation):
	finalcountlist=[]
	for j in range(len(new_permutation)):
		distance = 0
		for i in range(len(new_permutation[j])-1):
			var = new_permutation[j][i].split(" ")
			char = new_permutation[j][i+1].split(" ")
			for k in range(2):
				var[k] = int(var[k])
				char[k] = int(char[k])
				if var[k] != char[k]:
					distance= distance + abs(int(char[k] - var[k]))
		finalcountlist.append(distance)
	lowest_distance = min(finalcountlist)
	print("\n[+] The shortest distance is ",lowest_distance)

#Function Call
if __name__ == '__main__':
	calc_single_distance(new_permutation)
	
