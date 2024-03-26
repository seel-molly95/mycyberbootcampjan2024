#!/bin/bash
# Lets create a while loop than runs a conditinal statment
#Ask the user for an input if they choose:
# 1 then echo hello world
# 2 ping a website or ip address
# 3 run ifconfig
# else echo invalid entry
# Start a while loop
while true; do
    echo "Please choose an option:"
    echo "1. Echo Hello"
    echo "2. Ping a website or IP address"
    echo "3. Run ifconfig"
    echo "4. Exit"

    read choice

    case $choice in
        1)
            echo "Hello"
            ;;
        2)
            echo "Enter website or IP address to ping:"
            read target
            ping -c 4 $target
            ;;
        3)
            echo "Running ifconfig:"
            ifconfig
            ;;
        4)
            echo "Exiting..."
            break
            ;;
        *)
            echo "Invalid entry"
            ;;
    esac
done  