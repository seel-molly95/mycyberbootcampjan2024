#!/bin/bash
# Condtinal Statment 
# This ops challenges is about conditinal stamtment of if else statments and how they work
# We are going to take a varibale with the number and have the computer tell us if its greater than 5 less than 5 or equals 5

number=7

if  [ "$number" -gt 5 ]
then
  echo "greater than 5"
else 
echo "equal to 5"
fi