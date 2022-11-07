import os


def JSONtoTSV(JSONfile, TSVfile):
    with open(JSONfile, encoding='utf-8') as file:
        JSON = file.readlines()[1:-1]

    for i in range(len(JSON)):
        JSON[i] = JSON[i].replace('  ', '')
        JSON[i] = JSON[i].replace('\n', '')
        JSON[i] = JSON[i].replace(',', '')
    
    TSV = []
    TSVheadline = []

    if '"table":' in JSON[0]:
        if '"rows":' in JSON[1]:
            rows = []
            while '{' in JSON:
                row = JSON[JSON.index('{')+1:JSON.index('}')]
                JSON = JSON[JSON.index('}')+1:]
                rows.append(row)
            for row in rows:
                TSVline = ''
                for i in range(len(row)):
                    row[i] = row[i].replace('"', '')
                    row[i] = row[i].split(': ')
                    if len(row) > len(TSVheadline):
                        TSVheadline.append(row[i][0])
                    TSVline += row[i][1] + '\t'.expandtabs()
                TSVline = TSVline[:-1]+'\n'
                TSV.append(TSVline)
            TSVheadline = '\t'.join(TSVheadline).expandtabs()
            TSV = [TSVheadline+'\n'] + TSV

            with open(TSVfile, 'w', encoding='utf-8') as newfile:
                newfile.writelines(TSV)
        elif '"columns":' in JSON[1]:
            pass
        else:
            print("Wrong table format in JSON")
    else:
        print("There is no table in JSON")

def main():
    os.chdir(r"C:\Users\Roma\Desktop\Lab4")
    JSONfile = r'C:\Users\Roma\Desktop\Lab4\schedule.json'
    TSVfile = r'C:\Users\Roma\Desktop\Lab4\schedule.tsv'
    JSONtoTSV(JSONfile, TSVfile)

if __name__ == "__main__":
    main()