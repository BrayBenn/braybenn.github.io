# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 00:05:50 2020

@author: brayd
"""

import os
from operator import itemgetter

def attempt_float(x):
    try:
        return float(x)
    except:
        return(x)
         
print(os.getcwd())
os.chdir("/Users/brayd/Documents/CIS 325")
print(os.getcwd())
input_filename = 'loan-data-v1.csv'
        
def main():
    
    customer_list = []
            
    frh = open(input_filename, 'r', encoding='utf-8', errors='ignore')
    next(frh)
    
    for line in frh:
        ls = line.strip().split(',')
        ls[7] = attempt_float(ls[7])
        ls[10] = attempt_float(ls[10])
        customer_list.append(ls)
        
    customer_list = sorted(customer_list, key=itemgetter(7), reverse = True) 
    
    delinquent = filter(lambda x: x[7] >= 90, customer_list)
    
    output_filename = 'loan-data-output-v1.csv'
    fwh = open(output_filename, 'w', encoding='utf-8')
    
    header_list = ['Name', 'State', 'Days Delinquent', 'Years as Customer']
    header_string = ','.join(header_list)
    fwh.write(header_string + '\n')
    
    for index in delinquent:
        fwh.write(index[0]+ ',' +index[1]+ ',' +str(index[7])+ ',' +str(index[10])+ '\n')
    
    frh.close()
    fwh.close()
    
main()