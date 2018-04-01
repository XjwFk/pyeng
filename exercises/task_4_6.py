# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_route = ospf_route.split()
key_set = ['Protocol:', 'Prefix:', 'AD/Metric:', 'Next-Hop:', 'Last update:', 'Outbound Interface:']
#result = {key: [] for key in key_set}
#result = dict.fromkeys(key_set)
ospf_route[0] = 'OSPF'
ospf_route[2] = ospf_route[2].strip('[]')
ospf_route[3] = ospf_route[4].strip(',')
ospf_route[4] = ospf_route[5].strip(',')
ospf_route[5] = ospf_route[6]

for i in range(6):
	print('{0:25}{1:15}'.format(key_set[i],ospf_route[i]))
#print(result)