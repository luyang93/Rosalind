#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : prtm.py
# @Date    : 2019-02-16
# @Author  : luyang(luyang@novogene.com)


def main():
    file = 'input/rosalind_prtm.txt'
    with open(file) as f:
        my_pro = f.readline().strip()
        mass = 0
        for i in my_pro:
            mass += mass_table[i]
    print(mass)


if __name__ == "__main__":
    mass_table = {'A': 71.03711, 'C': 103.00919, 'D': 115.02694, 'E': 129.04259, 'F': 147.06841, 'G': 57.02146, 'H': 137.05891, 'I': 113.08406, 'K': 128.09496, 'L': 113.08406, 'M': 131.04049, 'N': 114.04293, 'P': 97.05276, 'Q': 128.05858, 'R': 156.10111, 'S': 87.03203, 'T': 101.04768, 'V': 99.06841, 'W': 186.07931, 'Y': 163.06333}
    main()
