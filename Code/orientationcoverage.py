#!/usr/bin/env python3

# From the bits 16 and 32 of the flag, calculate the relative orientation of the reads for every genomic position.
# se f forward e r reverse le possibilita' sono: ff, fr, rf, rr
import sys

if len(sys.argv) == 1: # significa che non ci sono argomenti
	print("Syntax: " + sys.argv[0] + " file.sam genomelength max_fragment_size orientation") # orientation that we decide of apply
	exit()

#initialize genome_change variable as a list constituted by 0 with length = genomelength
genome_length = int(sys.argv[2])
genome_change_forward = [0]*genome_length
genome_change_reverse = [0]*genome_length
max_fragment_size = int(sys.argv[3]) 
orientation = int(sys.argv[4])

sam_file = open(sys.argv[1])   # open sam file and read each line not starting with @
for line in sam_file:
	if line[0] == '@':
		continue

	fields = line.split("\t")   # makes a list of individual tab-separated fields # separo i campi
	if ((int(fields[1]) & 12) == 0):   # flag unset indicates that both segment map
		if (int(fields[8]) < max_fragment_size): # for consider all direction reads
			if((int(fields[1])) & 48 == orientation):
			# 16 + 32 both evaluate
				starting_read_position = int(fields[3])
				read_length = 100
				if(int(fields[8])  > 0): # forward
					end_read_position = starting_read_position + read_length # considering each read
				else: # reverse
					end_read_position = starting_read_position - read_length

				
				if(int(fields[8]) > 0): # forward
					# increment start position by one
					genome_change_forward[starting_read_position] += 1
					# decrement end position by one
					genome_change_forward[end_read_position] -= 1
				else: # reverse
					# increment start position by one
					genome_change_reverse[starting_read_position] += 1
					# decrement end position by one
					genome_change_reverse[end_read_position] -= 1  
sam_file.close()
	
# print genomic profile as a wiggle file
print("fixedStep chrom=genome start=1 step=1 span=1")
current_coverage_forward = 0
current_coverage_reverse = 0
reverse = []
forward = []
# cicle over all positions of the genome
for position in range(genome_length):
	current_coverage_forward += genome_change_forward[position]
	forward.append(current_coverage_forward) # forward[0,...genome_length-1]		
for position in range(genome_length-1, -1, -1): # genome_change[genome_length-1...0]
	current_coverage_reverse += genome_change_reverse[position]
	reverse.append(current_coverage_reverse) # reverse[genome_length-1...0]
for i,j in zip(range(genome_length-1, -1, -1), range(genome_length)):
	print(reverse[i] + forward[j])
	
	

