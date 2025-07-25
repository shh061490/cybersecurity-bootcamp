#!/bin/bash

# We are practicing basic scripting in bash
# We perform a funcion that adds or subtracts two numbers
# Lets create an until loop that takes a variable and adds 1 till it reachs 10
# Have the script echo out what are current number is
# Start with a number called counter. It begins at 0.


counter=0

# Repeat this loop while the counter is less than 10
while [ $counter -lt 10 ]
do
  # Add 1 to the counter
  counter=$((counter + 1))
  
  # Show the counter's value
  echo "Counter is now: $counter"
done




