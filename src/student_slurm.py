#! /bin/bash

import sys

# sacctmgr add user name=blah cluster=mcscn DefaultAccount=cs_class
add_cmd = "sacctmgr add user name=%s cluster=mcscn DefaultAccount=cs_class"

if __name__=='__main__':
    # check arg length
    if len(sys.argv)!=2 or sys.argv[1]=='-h':
        print("Usage: python3 %s <users_file.txt>")
        print("\nPrints a shell script to add slurm users to stdout.")
        print("users_file.txt should contain usernames, 1 per line.")
        exit(1)
    
    with open(sys.argv[1]) as f:
        print('#!/bin/bash')
        print('')
        for line in f:
            line = line.strip()
            cmd = add_cmd%line
            print(cmd)
