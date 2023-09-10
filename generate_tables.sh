#!/bin/bash

python ./ticky_check.py

python ./csv_to_html.py error_report.csv ./error_report.html

python ./csv_to_html.py user_report.csv ./user_report.html