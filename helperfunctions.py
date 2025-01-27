import os
import json
import ast
import streamlit as st
file_path = 'log_file.json'

def logger(log):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            my_list = json.load(file)
    else:
        my_list = []
    my_list.append(log)
    with open(file_path, 'w') as file:
        json.dump(my_list, file, indent=4)

def plotter(train_number=None):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            logs = json.load(file)
        all_issues = []
        for item in logs:
            if train_number is None or item['train_number'] == train_number:
                all_issues += ast.literal_eval(item['issues'])
        if(len(all_issues) == 0):
            for item in logs:
                all_issues += ast.literal_eval(item['issues'])
            print("No trains found.")
            st.warning("No trains found.")
        return all_issues
    else:
        return ['Train Delay']
