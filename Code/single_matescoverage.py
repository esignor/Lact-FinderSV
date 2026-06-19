#!/usr/bin/env python3
import sys

if len(sys.argv) == 1:
	print("Syntax: " + sys.argv[0] + " file.sam genomelength")
	exit()

# initialize genome_change variable as a list constituted by 0 with length = genomelength
genome_length = int(sys.argv[2])
genome_change = [0]*genome_length


sam_file = open(sys.argv[1]) # open sam file and read each line not starting with @ 
for line in sam_file:
	if line[0] == '@':
		continue

	fields = line.split("\t")   # makes a list of individual tab-separated fields
	if ((int(fields[1]) & 12) == 8):   # == 8 for mate unmapped
		starting_read_position = int(fields[3])
		read_length = 100
		end_read_position = int(fields[3]) + read_length

		# increment start position by one
		genome_change[starting_read_position] += 1 
		# decrement end position by one
		genome_change[end_read_position + read_length] -= 1 
sam_file.close()

	
# print genomic profile as a wiggle file
print("fixedStep chrom=genome start=1 step=1 span=1")
current_coverage = 0
# cicle over all positions of the genome
for position in range(genome_length): 
	current_coverage += genome_change[position] 
	print(current_coverage)

