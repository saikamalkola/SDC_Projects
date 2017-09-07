n = 4   #Number of Variables

exp_str = "01011110+01101011+10110111+10110110"  #Positional Cube Notation



pcn_notation = ["00" "01" "10" "11"]
exp_var = ['A' 'B' 'C' 'D']
exp_var_comp = ['a' 'b' 'c' 'd']
k =0

exp_arr_var = []
class Node():
    #Tree Node
    def _init_(self):
        self.data = none
        self.left = none
        self.right = none

def parse_string():
    exp_arr_str = exp_str.split('+')
    for i in range(0,len(exp_arr_str)):
        for j in range(0,n):
            temp = ''
            temp += exp_arr_str[i][2*j]
            temp += exp_arr_str[i][2*j+1]
            if(temp == '00'):
                temp = 0
            elif(temp == '01'):
                temp = 1
            elif(temp == '10'):
                temp = 2
            else:
                temp = 3
            exp_arr_var.append(temp)
            exp_arr_var[n*i+j] = (exp_arr_var[n*i+j])
    print(exp_arr_var)

parse_string()
