#!/bin/python3
# -*- encoding:utf-8 -*-

'''
Two functions for kaiju2table outputname
get_top_rela(): only print taxon names with relative abundance larger than 2% (can be changed)
get_rela(): print all taxon names
'''

import sys

def get_top_rela(kaiju_out):
	with open(kaiju_out,'r') as infile:
		rela = {}
		for line in infile:
			rela[line.split('\t')[4][:-1]] = line.split('\t')[1]
		rela.pop('taxon_name')
		rela.pop('unclassified')
		#print(rela)
		top_rela = {}
		others = 0
		for taxon in rela:
			if float(rela[taxon]) < 2 and taxon !='Viruses' and taxon !='cannot be assigned to a (non-viral) phylum': #change 'phylum' to whatever taxon rank you need
				others = others + float(rela[taxon])
			elif taxon =='cannot be assigned to a (non-viral) phylum': #change 'phylum' to whatever taxon rank you need
				top_rela['Unassigned'] = float(rela[taxon])
			elif taxon =='Viruses':
				top_rela['Viruses'] = float(rela[taxon])
			else:
				top_rela[taxon] = float(rela[taxon])
		top_rela['Others'] = others

	return top_rela

def get_rela(kaiju_out, rela_out):
	with open(kaiju_out,'r') as infile:
		rela = {}
		for line in infile:
			rela[line.split('\t')[4][:-1]] = line.split('\t')[1]
		rela.pop('taxon_name')
		rela.pop('unclassified')
		rela['Unassigned'] = rela.pop('cannot be assigned to a (non-viral) phylum') #change 'phylum' to whatever taxon rank you need
	with open(rela_out, 'w') as outfile:
		outfile.write('taxon_name'+'\t'+'Percent'+'\n')
		for key in rela:
			outfile.write(key+'\t'+rela[key]+'\n')

#inputname='1A.kaiju.phylum.summary.out'
#outputname='1A.kaiju.phylum.txt'
inputname=sys.argv[1]
outputname=sys.argv[2]
get_rela(inputname,outputname)