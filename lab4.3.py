import re
import os

def JSONtoYAML(JSONfile, YAMLfile):
    with open(JSONfile, encoding='utf-8') as file:
        JSON = file.readlines()[1:-1]

    YAMLdoc = []
    linestart = ''
    masstaples = False
    maslevel = 0
    level = 0
    for i in JSON:
        YAMLline = ''
        line = re.findall(r'(?<=\s)[\{\}\[\]\"].*', i)
        if len(line) > 0:
            line = line[0]
        else:
            line = ''
        keys = re.findall(r'(?<=\").+(?=\":)', line)
        values = re.findall(r'\s\".*\"', line)
        if len(keys) > 0:
            YAMLline = linestart + keys[0] + ':'
            if len(values) == 0:
                values = re.findall(r'\s[0-9\.]+[\s,]', line)
                if len(values) == 0:
                    values = re.findall(r'(?:true|false)', line)
                    if len(values) == 0:
                        YAMLdoc.append(YAMLline+'\n')
                    else:
                        YAMLdoc.append(YAMLline+' '+values[0]+'\n')
                else:
                        YAMLdoc.append(YAMLline+values[0]+'\n')
            else:
                if len(values[0]) == 3:
                    YAMLline += " ''"
                    YAMLdoc.append(YAMLline+'\n')
                else:
                    value = values[0][2:-1]
                    if value.find('\\n') > -1:
                        YAMLline += ' |\n'
                        YAMLdoc.append(YAMLline)
                        value = value.split('\\n')
                        for i in value:
                            YAMLdoc.append(' '*2*(level+1) + i + '\n')
                    else:
                        YAMLdoc.append(YAMLline+' '+value+'\n')
        if masstaples and level == maslevel:
            linestart = ' '*2*(level-1) + '- '
        else:
            linestart = ' '*2*level
        if '{' in line:
            level += 1
            linestart = '  '+linestart
        if '[' in line:
            masstaples = True
            level += 1
            maslevel = level
            linestart = '  '+linestart
        if '}' in line:
            level -= 1
            linestart = linestart[2:]
        if ']' in line:
            masstaples = False
            maslevel = 0
            level -= 1
            linestart = linestart[2:]
        #if YAMLline != '':
         #   YAMLdoc.append(YAMLline + '\n')

    with open(YAMLfile, 'w', encoding='utf-8') as newFile:
        newFile.writelines(YAMLdoc)



def main():
    os.chdir(r"C:\Users\Roma\Desktop\Lab4")
    JSONfile = r'C:\Users\Roma\Desktop\Lab4\schedule.json'
    YAMLfile = r'C:\Users\Roma\Desktop\Lab4\schedule.yaml'
    JSONtoYAML(JSONfile, YAMLfile)

if __name__ == "__main__":
    main()