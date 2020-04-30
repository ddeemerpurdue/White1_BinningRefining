import os
import sys
import subprocess

file = sys.argv[1]
print('Reading in information file...')

with open(file) as f:
    line = f.readline().split('\t')
    if line[0].lower() == 'assembly':
        assembly = str(line[1].strip())
        print(f'Assembly location:\t{assembly}')
    else:
        print('Error, assembly line not formatted correctly.')
    line = f.readline().split('\t')
    if line[0] == 'abundance':
        abundance = str(line[1].strip())
        print(f'Abundance file location:\t{abundance}')
    elif line[0] == 'abund_list':
        abundance = line[1]
    else:
        print('Error: abundance file not formatted correctly.')
    line = f.readline().split('\t')
    if line[0] == 'output':
        output = str(line[1].strip())
        print(f'Output location:\t{output}')
    else:
        print('Error: output file not formatted correctly.')
print('Read in file information.')


print('Loading in modules...')
os.system('module load bioinfo')
os.system('module load MaxBin/2.2.3')
print('Modules successfully loaded in.')

subprocess.check_call(['run_MaxBin.pl', '-contig', assembly, '-abund',
                      abundance, '-out', output])

print('Finished!')