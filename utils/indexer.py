import csv
import os

languages = [
        'pl_PL',
        'zh_CN',
        'ja_JP',
        'vi_VN',
        'es_ES'
        ]

translation_map = dict()

abs_path = '../electrum/locale/'

for lang in languages:
    po_path = abs_path + lang + '/electrum.po'
    print(po_path)
    with open(po_path, "r") as po_file:
        read_entry = False
        idx = ''
        for line in po_file:
            if ('gui/qt' in line  or 'ledger' in line) and 'lightning' not in line:
                read_entry = True
            if "msgid" in line and read_entry:
                idx = line.strip()[7:-1]
            if 'msgstr' in line and read_entry:
                if idx not in translation_map.keys():
                    translation_map[idx]=[]
                translation_map[idx].append(line.strip()[8:-1])
                read_next_line = False
                idx = ''


with open("res.csv", 'w') as output:
    writer = csv.writer(output)
    for i in range(10):
        writer.writerow([])
    for key in translation_map.keys():
        row = translation_map[key]
        row.insert(0, key)
        writer.writerow(row)
    