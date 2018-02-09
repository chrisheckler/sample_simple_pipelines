#!/usr/bin/env python3
# Copyright (c) 2018 Chris Heckler <hecklerchris@hotmail.com>

# Stage 0
stage_0_data = {'x':1,'y':1, 'z':1}
print('Stage 0 data: ' + str(stage_0_data))


# Stage 1
def add_value(my_dict, value):
    stage_1 = {k: v+value for k,v in my_dict.items()}
    return stage_1

stage_1_data = add_value(stage_0_data, 1)
print('Stage 1 data: ' + str(stage_1_data))


# Stage 2
def get_sum(my_dict):
    stage_2 = {'x': 0.3 * sum(my_dict.values()),
               'y': 0.6 * sum(my_dict.values()),
               'z': 0.9 * sum(my_dict.values())} 
    return stage_2

stage_2_data = get_sum(stage_1_data)
print('Stage 2 data: ' + str(stage_2_data))
