#!/bin/python3
import re
import sys
import glob
import os 
import yaml
from pathlib import Path


location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
location_bitstream = (location.replace("scripts",""))+"src/designs/"+sys.argv[1]+"/"+"*.bit"
# print ("location:",location_bitstream)
file_bin = open('bitstream.bin', 'w')
file_hex = open('bitstream.hex', 'a')
size=74504
wl_list=[]
arrange_list=[]
write_bin_list=[]
write_hex_list=[]
conv_list=[]
dummy= [None]*size

a_yaml_file = open("config.yaml")
# print(a_yaml_file)
# parsed_yaml_file = yaml.load(a_yaml_file, Loader=yaml.FullLoader)
# heloo=parsed_yaml_file['BL_MAX_LENGTH']
# print()




def file_read ():
    for filename in glob.glob(location_bitstream):
        with open(filename, 'r') as f:
            lines = f.readlines()
    # return lines
    for line in range(len(lines)) :
        if "Bitstream wl word size:" in lines[line]:
             wl_size=lines[line].split()[-1]
             wl_size=int(wl_size)
        if "Bitstream bl word size:" in lines[line]:
             bl_size=lines[line].split()[-1]
             bl_size=int(bl_size)
            #  print(bl_size)
    return lines, wl_size, bl_size
            #  print(type(wl_size))
    # print (wl_size)
            # return lines

def wl_word (wl_list,wl_size):
    # print(len(wl_list))
    # count=0
    # print("----------first\n",wl_list[0:3])
    try:
        for i in range(len(wl_list)):
            if "// WL" in wl_list[i] and (i+1+wl_size) <= len(wl_list):
                # count=count+1
                
                del wl_list[(i):(i+1+wl_size+1)]
    except:
        # print(len(wl_list))
        ""
    return wl_list


def arrange_txt (arrange_list):
    index = 0
    # # print("----------first-----\n",arrange_list[0:3])
    # length=len(arrange_list)
    for i in arrange_list:
        conv_list.append(i.strip())
    while index < len(conv_list):
    # check if element begins with 'd'
      if conv_list[index].startswith('//'):
        # remove it
         del(conv_list[index])
      else:
        index += 1
    return conv_list


# def config_append (write_bin_list):
#     # parsed_yaml_file = yaml.load(a_yaml_file, Loader=yaml.FullLoader)
#     a_yaml_file = open("config.yaml")
#     parsed_yaml_file = yaml.load(a_yaml_file, Loader=yaml.FullLoader)
#     values=parsed_yaml_file.values()
#     values_index = list(values)
#     for i in range (len(values_index)):
#         write_bin_list.insert(i,values_index[i])
#         print(write_bin_list[i])
#         # file_bin.write(write_bin_list[i]+"\n")
#     return write_bin_list


git@github.com:RapidFlex/flex_efpga4k.git



def write_funct (write_bin_list,wl_size,bl_size):
    length=len(write_bin_list)
    # print("length us",length)
    # print("length us",write_bin_list)  
    # write_bin_list
    write_bin_list = [sub.replace('x', '0') for sub in write_bin_list]
    # print("length us",length) 
    # print(write_bin_list) 
    a_yaml_file = open("config.yaml")
    parsed_yaml_file = yaml.load(a_yaml_file, Loader=yaml.FullLoader)
    values=parsed_yaml_file.values()
    values_index = list(values)
    # print(values_index[1])
    for i in range (len(values_index)):
        values_index[i] = '{:032b}'.format(int(values_index[i], 16))
        file_bin.write(values_index[i]+"\n")
        # print("Yaml list",values_index[i])
    dummy=values_index+write_bin_list
    # print (write_bin_list)
    # print("Length of dummy is",len(dummy))

    for i in range (wl_size):  
        # print("Element is",dummy[5])
        for k in range(length-bl_size,length,+1):
            write_bin_list[k]   =  "0000000000000000000000000000000"+dummy[k+6]
            # print(write_bin_list[k])
            # write_bin_list[i].replace(write_bin_list[i],("0000000000000000000000000000000"+write_bin_list[i]))
            # dummy.append(write_bin_list[i])
            # print(write_bin_list[k])
            # print(write_bin_list[i])
            # file_hex.write(hex(int(write_bin_list[i]))+"\n")
            # file_hex.write(str('{0:08X}'.format(int(write_bin_list[i])))+"\n")
            file_bin.write(write_bin_list[k]+"\n")
    
        # print(dummy[0])  
        length=length-bl_size
    write_bin_list=dummy[0:6]+write_bin_list
    # for o in range (len(write_bin_list)):
    #     file_bin.write(write_bin_list[o]+"\n")
    # print("list length is",write_bin_list[0])
    # dummy
    # for j in range (len(dummy)):
    #     # print("Length is ",len(dummy))
    #     print(dummy[j])
    file_bin.close()
    file_hex.close()
    return dummy



        # print(write_bin_list[59])
    # a_yaml_file = open("config.yaml")
    # parsed_yaml_file = yaml.load(a_yaml_file, Loader=yaml.FullLoader)
    # values=parsed_yaml_file.values()
    # values_index = list(values)
    # print(values_index[1])
    # for i in range (len(values_index)):
    #     values_index[i] = '{:032b}'.format(int(values_index[i], 16))
    #     print("Yaml list",values_index[i])
    # write_bin_list=values_index+write_bin_list
    # # #print(write_bin_list)
    # for i in range(len(write_bin_list)):
    #     file_bin.write(write_bin_list[i]+"\n")
    #     file_hex.write(str('{0:08X}'.format(int(write_bin_list[i])))+"\n")



    # for i in range (len(values_index)):
  
        # write_bin_list_n.insert(i,values_index[i])
  
        # print(write_bin_list_n[i])
  
        # file_bin.write(write_bin_list[i]+"\n")
  
        # print(write_bin_list_n[i].strip())



    # return write_bin_list
    
def config_append (write_bin_list_n):
    # parsed_yaml_file = yaml.load(a_yaml_file, Loader=yaml.FullLoader)
    a_yaml_file = open("config.yaml")
    parsed_yaml_file = yaml.load(a_yaml_file, Loader=yaml.FullLoader)
    values=parsed_yaml_file.values()
    values_index = list(values)
    # print(write_bin_list_n)
    for i in range (len(values_index)):
        values_index[i] = '{:032b}'.format(int(values_index[i], 16))
        # print("Yaml list",values_index[i])
    write_bin_list_n=values_index+write_bin_list_n
    # print(write_bin_list_n)
    for i in range(len(write_bin_list_n)):
        file_bin.write(write_bin_list_n[i]+"\n")
        file_hex.write(str('{0:08X}'.format(int(write_bin_list_n[i])))+"\n")

    file_bin.close()
    file_hex.close()




wl_list,wl_size,bl_size=file_read()
# print("----------first\n",wl_list[0:3])
arrange_list=wl_word (wl_list,wl_size)

# print("----------first---\n",arrange_list[0:3])

write_bin_list=arrange_txt (arrange_list)


# write_bin_list_n=config_append (write_bin_list)


write_bin_list_n=write_funct (write_bin_list,wl_size,bl_size)



# config_append (write_bin_list_n)