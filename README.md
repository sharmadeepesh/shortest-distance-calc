# shortest-distance-calc
This script calculates the shortest distance to travel the given coordinates.

<strong>The program finds out the solution for below given problem:</strong>

<i>The members of ACE are going on a trip to Manali. A bus is going to pick them up one by one and then travel to Manali. You are provided the current location of the bus, location of Manali drop point and house of "N" ACE members. Bus is going to pick them up one by one and can travel only in straight lines i.e. when travelling from (x0,y0) to (x1,y1) either x0=x1 or y0=y1. 
Assuming that all the coordinates exist on a 2D plane and there is no traffix, find out the shortest route to pick all the members and then reach the destnation.</i><br><br>
<b>Example Input :<br>
0 0 (Starting Point)<br>
3 4 (Ending Point)<br>
3 (Number of Members)<br>
1 1 (Coordinate1)<br>
1 3 (Coordinate2)<br>
2 1 (Coordinate3)<br>
Output <br>
9 (Length of Route)</b><br>

<h3>Working</h3>
The script works in this way that at first, it takes all the inputs from the user. Then it sorts the coordinate_list so that the starting and ending coordinates are at the first and last indices of the coordinate_list respectively. Then, a new object is defined which contains the collection of all Permutations of the coordinate_list. The permutated_list is then filtered so that the starting point and Ending point are at the first and last indices, same as the fcoordinate_list. Then, distance is calculated for each permutated_list and is stored in a "Distance_list". Finally, the minimum value from the Distance_list is returned as the <strong>"Shortest Distance"</strong>.

<b>NOTE</b> : The script uses the module "Itertools" for the permutation of the coordinate_list. The module can be easily installed by entering the following command in the terminal:<br>
<code>pip install itertools</code>
