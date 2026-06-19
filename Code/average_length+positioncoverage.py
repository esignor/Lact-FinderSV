#!/usr/bin/env python3
import sys

if len(sys.argv) == 1:
	print("Syntax: " + sys.argv[0] + " file.sam genomelength max_fragment_size")
	exit()

# initialize genome_change variable as a list constituted by 0 with length = genomelength
genome_length = int(sys.argv[2])
genome_change = [0]*genome_length
sum_fragments_change = [0]*genome_length
max_fragment_size = int(sys.argv[3])

sam_file = open(sys.argv[1])   # open sam file and read each line not starting with @
for line in sam_file:
	if line[0] == '@': 
		continue
## same phycoverage.py
	fields = line.split("\t")   # makes a list of individual tab-separated fields
	if ((int(fields[1]) & 12) == 0):  # both flags unset indicates that both segments map
		if((int(fields[8]) > 0) and (int(fields[8]) < max_fragment_size)):
			starting_read_position = int(fields[3]) 
			read_length = 100 
			end_read_position = int(fields[7]) + read_length
			# increment start position by one
			genome_change[starting_read_position] += 1
			# decrement end position by one
			genome_change[end_read_position] -= 1
## adding respect phycoverage.py			
			# for each position computation the sum of the fragments
			# sum_fragments_change
			# increment start position by fragment size
			sum_fragments_change[starting_read_position] += int(fields[8]) # is fragment size (TLEN)
			# decrement end position
			sum_fragments_change[end_read_position] -= int(fields[8]) 
sam_file.close()
	
# print genomic profile as a wiggle file
# print("fixedStep chrom=genome start=1 step=1 span=1")
current_coverage = 0
current_sum = 0 # for do a means of fragments length
# cicle over all positions of the genome
for position in range(genome_length):
	current_coverage += genome_change[position] 
	current_sum += sum_fragments_change[position]
	# division for 0, preserve base position information
	if(current_coverage > 0):
		print(position, current_sum/current_coverage) # divide the fragment length for phycoverage => length of fragments of a certain base area X / fragments number of a certain base area X
	else:
	# region reference genome unmapped, preserve base postion information
		print(position, -1)
