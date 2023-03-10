from pprint import pprint

BEGIN = 'BEGIN:VCARD'
END = 'END:VCARD'


# 传入一个vard文件返回字典列表
def read_vcf(vcf_file):
    vcf_list = []
    with open(vcf_file, 'r', encoding='utf-8') as f:
        # 每条数据由BEGIN和END标志包围，里面的数据是键值对使用:分割
        # 读取每条数据
        for line in f:
            # 如果是BEGIN，开始读取数据
            if line.startswith(BEGIN):
                vcf = {}
                # 读取每条数据的每一行
                for line in f:
                    # 如果是END，结束读取数据
                    if line.startswith(END):
                        break
                    # 如果不是END，读取键值对
                    else:
                        key, value = line.strip().split(':')
                        vcf[key] = value
                vcf_list.append(vcf)

    return vcf_list


# 传入一个字典列表返回vard文件
def write_vcf(vcf_list, fn):
    with open(fn, 'w', encoding='utf-8') as f:
        for vcf in vcf_list:
            f.write(BEGIN + '\n')
            for key, value in vcf.items():
                f.write(key + ':' + value + '\n')
            f.write(END + '\n')


vcf_list = read_vcf('v.vcf')


def to_sql(vcf):
    # 'ADR;TYPE=HOME;CHARSET=UTF-8', -> 'adr'
    # 'FN', -> 'name'
    # 'N',
    # 'NOTE;CHARSET=UTF-8', -> 'note'
    # 'TEL;TYPE=CELL', -> 'tel'
    # 'TEL;TYPE=CELL;TYPE=PREF', -> 'tel'
    adr = vcf.get('ADR;TYPE=HOME;CHARSET=UTF-8', 'NULL')
    if adr != 'NULL':
        adr = "'" + adr + "'"
    name = vcf.get('FN', 'NULL')
    if name != 'NULL':
        name = "'" + name + "'"
    note = vcf.get('NOTE;CHARSET=UTF-8', 'NULL')
    if note != 'NULL':
        note = "'" + note + "'"
    tel = vcf.get('TEL;TYPE=CELL', 'NULL')
    tel2 = vcf.get('TEL;TYPE=CELL;TYPE=PREF', 'NULL')
    if tel2 != 'NULL':
        tel = tel + ';' + tel2
    if tel.startswith('NULL;'):
        tel = tel[5:]

    return f"INSERT INTO t_privacy (name, tel, adr, note) VALUES ({name}, '{tel}', {adr}, {note});\n"


f = open('in.sql', 'w', encoding='utf-8')
# keyset = set()
for vcf in vcf_list:
    # keyset.update(vcf.keys())
    f.write(to_sql(vcf))


f.close()
# pprint(keyset)

# sp = []
# other = []
# for vcf in vcf_list:
#     # 如果包含EMAIL;TYPE=WORK
#     if 'EMAIL;TYPE=WORK' in vcf:
#         sp.append(vcf)
#     else:
#         other.append(vcf)
# write_vcf(sp, 'sp.vcf')
# write_vcf(other, 'v.vcf')
