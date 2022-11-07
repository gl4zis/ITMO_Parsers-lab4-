import json
import yaml
import os

def JSONtoYAML(JSONfile, YAMLfile):
    with open(JSONfile, encoding='utf-8') as jsonfile:
        data = json.load(jsonfile)
    with open(YAMLfile, 'w', encoding='utf-8') as yamlfile:
        data = yaml.dump(data, allow_unicode=True).replace('\n\n', '\n').replace('\'', '')
        yamlfile.write(data)

def main():
    os.chdir(r"C:\Users\Roma\Desktop\Lab4")
    JSONfile = r'C:\Users\Roma\Desktop\Lab4\schedule.json'
    YAMLfile = r'C:\Users\Roma\Desktop\Lab4\schedule.yaml'
    JSONtoYAML(JSONfile, YAMLfile)

if __name__ == "__main__":
    main()