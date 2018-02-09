#!/usr/bin/env python3
# Copyright (c) 2018 Chris Heckler <hecklerchris@hotmail.com>

# Stage 0
stage_0_data = {'x':0, 'y':0, 'z':0}
print('Stage 0 data: ' + str(stage_0_data))


# Stage 1
def add_value(my_dict, value):
    stage1 = {k: v+value for k,v in my_dict.items()}
    return stage1

stage_1_data = add_value(stage_0_data, 1)
print('Stage 1 data: ' + str(stage_1_data))


