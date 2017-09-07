import graphviz as gv

tree = gv.Graph(format='svg')
#tree object to draw nodes

file_input = open('input.txt','r')
#taking input from file

input_data = file_input.readlines()
#Reading data in file line by line

char_arr = input_data[0].split(' ')
#parsing the variables

n = len(char_arr)
#Number of variables in the expression
index = 0

var_arr = []
leaf_node_arr = []

for i in range(0,n):
    char_arr[i] = char_arr[i].strip('\n')
    temp = ord(char_arr[i]) - 65
    var_arr.append(temp)
#parsing variable array from character array

print(char_arr)
print(var_arr)

min_arr = input_data[1]
min_arr = min_arr.split(' ')

for i in range(0,len(min_arr)):
    min_arr[i] = min_arr[i].rstrip('\n')
    if(min_arr[i] == '00'):
        min_arr[i] = 0
    elif(min_arr[i] == '01'):
        min_arr[i] = 1
    elif(min_arr[i] == '10'):
        min_arr[i] = 2
    else:
        min_arr[i] = 3
#parsing the minterms given in file in to integers

"""
0
1 2
3 4 5 6
7 8 9 10 11 12 13 14
"""
index = 0
NUM_MINTERMS = int(len(min_arr)/n)
arr = [[0 for x in range(len(min_arr))] for y in range(((2**(n+1))-1))]
#2D array to store all the nodes of tree(Cofactors)
arr[0] = min_arr
temp = str(index)
tree.node(str(index),char_arr[0])

def check_zeroes(index):
    count = -1
    for i in range(0,len(arr[index])):
        if(i%n == 0):
            count = count + 1
        if(arr[index][i] == 0):
            for j in range(0,n):
                arr[index][count*n + j] = 0
            i = count*(n+1)

def leaf_nodes(index):
    for i in range(0,NUM_MINTERMS):
        count = 0
        for j in  range(0,n):
            if(arr[index][i*n + j] == 3):
                count = count + 1
        if(count == n):
            break
        else:
            continue
    if(count == n):
        print(index)
        leaf_node_arr.append(1)
    else:
        leaf_node_arr.append(0)

for i in range(0,n):
    for j in range(0,2**i):
        arr[2*index+1] = arr[index] + []
        arr[2*index+2] = arr[index] + []
        for k in range(0,NUM_MINTERMS):
            if(arr[index][n*k + var_arr[i]] == 1):
                arr[2*index+1][n*k + var_arr[i]] = 0
                arr[2*index+2][n*k + var_arr[i]] = 3
            elif(min_arr[n*k + var_arr[i]] == 2):
                arr[2*index+1][n*k + var_arr[i]] = 3
                arr[2*index+2][n*k + var_arr[i]] = 0
        if(i < n-1):
            tree.node(str(2*index+1),char_arr[i+1])
            tree.edge(str(index),str(2*index+1))
            tree.node(str(2*index+2),char_arr[i+1])
            tree.edge(str(index),str(2*index+2))
        else:
            leaf_nodes(2*index+1)
            leaf_nodes(2*index+2)
            tree.node(str(2*index+1),str(leaf_node_arr[2*index+1-(2**n)+1]))
            tree.edge(str(index),str(2*index+1))
            tree.node(str(2*index+2),str(leaf_node_arr[2*index+2-(2**n)+1]))
            tree.edge(str(index),str(2*index+2))

        index = index + 1

for i in range(0,(2**(n+1))-1):
    check_zeroes(i)
    print(arr[i])

print(leaf_node_arr)

filename = tree.render(filename='img/tree')
print(filename)
