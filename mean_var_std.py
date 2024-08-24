import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    my_array = np.reshape(np.array(list), (3,3))
    mean = []
    var = []
    sd = []
    max_array = []
    min_array = []
    sum_array = []
    
    for i in range(2):  
        mean.append(np.mean(my_array, axis=i).tolist())
        var.append(np.var(my_array, axis=i).tolist())
        sd.append(np.std(my_array, axis=i).tolist())
        max_array.append(np.max(my_array, axis=i).tolist())
        min_array.append(np.min(my_array, axis=i).tolist())
        sum_array.append(np.sum(my_array, axis=i).tolist())
    
    mean.append(np.mean(my_array).tolist())
    var.append(np.var(my_array).tolist())
    sd.append(np.std(my_array).tolist())
    max_array.append(np.max(my_array).tolist())
    min_array.append(np.min(my_array).tolist())
    sum_array.append(np.sum(my_array).tolist())

    calculations = {
        'mean': mean,
        'variance': var,
        'standard deviation': sd,
        'max': max_array,
        'min': min_array,
        'sum': sum_array
    }
    return calculations
