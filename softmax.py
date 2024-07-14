command_format='./benchdnn --softmax -v5 --dt={src_data_type}:{dst_data_type} \n'

data_type=['f32', 'f16',  'bf16']
file='softmax.txt'
with open(file, mode='a') as filename:
    for src_datatype in data_type:
        for dst_datatype in data_type:
            command=command_format.format(src_data_type=src_datatype, dst_data_type=dst_datatype)
            filename.write(command)
