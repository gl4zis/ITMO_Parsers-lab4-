import os
import math

def staples(string):
    if '{' in string:
        return 'opendict'
    if '}' in string:
        return 'closedict'
    if '[' in string:
        return 'openarr'
    if ']' in string:
        return 'closearr'

def JSONtoYAML(JSONfile, YAMLfile):
    with open(JSONfile, encoding='utf-8') as file:
        JSON = file.readlines()[1:-1]

    YAML = []
    level = 0
    key = None
    value = None
    arrlevel = math.inf
    startline = ''
    for i in JSON:

        YAMLline = ''
        line = i.replace('  ', '').replace('\n', '')
        colonind = line.find(':')
        if colonind > -1:
            key = line[line.find('\"')+1: colonind-1]
            if type(value) == str:
                if arrlevel == level:
                    startline = ' '*2*(level - 1) + '- '
                else:
                    startline = ' '*2*level
            elif type(value) == dict:
                if level - arrlevel == 1:
                    startline = ' '*2*(level - 1) + '- '
                else:
                    startline = ' '*2*level
            YAMLline = startline + key + ':'
            line = line[colonind+2:]
        staple = staples(line)
        if staple != None:
            if staple == 'opendict':
                level += 1
                value = dict()
            elif staple == 'openarr':
                level += 1
                arrlevel = level
                value = []
            else:
                level -= 1
                value = None
        else:
            value = line.replace('\",', '').replace('\"', '')
            if value == '':
                value = "\'\'"
        if type(value) == str:
            if '\\n' in value:
                YAMLline += ' |\n'
                YAML.append(YAMLline)
                YAMLline = ''
                text = value.split('\\n')
                for i in text:
                    YAML.append(' '*2*(level+1)+i+'\n')
            else:
                YAMLline += ' '+value
        if YAMLline != '':
            YAML.append(YAMLline+'\n')

    with open(YAMLfile, 'w', encoding='utf-8') as newFile:
        newFile.writelines(YAML)  

def main():
    os.chdir(r"C:\Users\Roma\Desktop\Lab4")
    JSONfile = r'C:\Users\Roma\Desktop\Lab4\schedule.json'
    YAMLfile = r'C:\Users\Roma\Desktop\Lab4\schedule.yaml'
    JSONtoYAML(JSONfile, YAMLfile)

if __name__ == "__main__":
    main()