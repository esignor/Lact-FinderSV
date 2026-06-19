#!/usr/bin/env python3

# Condition phycoverage:
# - Same seqcoverage
# - Must be considered to fragment (reads + mate)
# - Each fragment can be mapping to more position genome. For resolve this is necessary checking that the read not is already been contain to a other mapping fragment 
# - The reads considered go from left to right

import sys

if len(sys.argv) == 1:
	print("Syntax: " + sys.argv[0] + " file.sam genomelength max_fragment_size")
	exit()

# initialize genome_change variable as a list constituted by 0 with length = genomelength
genome_length = int(sys.argv[2])
genome_change = [0]*genome_length 
max_fragment_size = int(sys.argv[3]) 

sam_file = open(sys.argv[1]) # open sam file and read each line not starting with @  
for line in sam_file:
	if line[0] == '@':
		continue

	fields = line.split("\t")   # makes a list of individual tab-separated fields
	if ((int(fields[1]) & 12) == 0):   # flag unset indicates that both segment map 
		if (int(fields[8])  > 0) and ((int(fields[8])  < max_fragment_size)):
										      
			starting_read_position = int(fields[3])
			mate_length = 100
			end_read_position = int(fields[7])

			# increment start position by one
			genome_change[starting_read_position] += 1
			# decrement end position by one
			genome_change[end_read_position + mate_length] -= 1
sam_file.close()

# print genomic profile as a wiggle file
print("fixedStep chrom=genome start=1 step=1 span=1")
current_coverage = 0
# cicle over all positions of the genome
for position in range(genome_length):
	current_coverage += genome_change[position]
	print(current_coverage)

