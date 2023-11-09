#!/usr/bin/python3
def element_at(my_list, idx):
    # if idx is negetive return None
    if idx < 0:
        return(None)
    # if idx is above range
    elif idx > len(my_list):
        return(None)
    else:
        return(my_list[idx])
