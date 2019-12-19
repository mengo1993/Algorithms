# Problem :
# I have a backpack of capacity C and I want to fill it with some objects.
# each object has a weight and a value.
# whick objects do I have to select in order to maximise the total value of the objects in the backpack without exceeding the capacity C ?


# I need :
# capacity of the backpack -> Capacity
# List of items values -> Values
# list of corresponding weights -> Weights

Capacity = 7
Values = [2,2,4,5,3]
Weights = [3,1,3,4,2]

def knapsack(c, v, w):
    
    n_obj = len(w)
    out_matrix = []
    first_line = [0 for i in range(c + 1)] # the first line will have c + 1 columns
    out_matrix.append(first_line)
    
    for current_obj_index in range(n_obj): # objects loop
        curr_out_line = []
        for current_capacity in range(c + 1):
            out = out_matrix[current_obj_index][current_capacity] # don't include the item by default
            
            # check if include the item : if the w is less than the current capacity and if the item value is > than the sum of the [top] matrix value + the [top - w] matrix value
            if w[current_obj_index] <= current_capacity and v[current_obj_index] + out_matrix[current_obj_index][current_capacity - w[current_obj_index]] > out:
                curr_out_line.append(v[current_obj_index] + out_matrix[current_obj_index][current_capacity - w[current_obj_index]])
            else: curr_out_line.append(out)
            
        out_matrix.append(curr_out_line)
            
    return out_matrix

out_m = knapsack(Capacity, Values, Weights)

def choose_items(knap_mtx, Capacity, Weights):
    col_index = Capacity
    n_obj = len(knap_mtx) - 1 # ok
    out = []
    for obj_index in range(1, n_obj + 1): # ok
        curr_obj = knap_mtx[- obj_index][col_index]
        prev_obj = knap_mtx[- obj_index - 1][col_index]
        if curr_obj != prev_obj:
            out.append(n_obj - obj_index + 1)
            obj_weight = Weights[- obj_index]
            col_index -=  obj_weight
    return out

out = choose_items(out_m, 3, Weights)
for obj in out:
    print " Choose object " + str(obj) 
 