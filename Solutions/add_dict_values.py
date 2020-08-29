def add_dic_val(input_dict):
    
    print("\n\nInput : ",input_dict)
    sum_of_all_values = sum(input_dict.values())
    print("Output",sum_of_all_values)

input_dict ={"Rick": 85, "Amit": 42, "George": 53, "Tanya": 60, "Linda": 35}
add_dic_val(input_dict)