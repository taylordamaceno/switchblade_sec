#!/bin/bash
echo "Testando rede: $1.*"

for num in $(seq 1 255) 
do

	ping -c1 -w1 $1.$num | grep "64 bytes" | cut -d " " -f 4
done
