import  json
import  pprint

pp = pprint.PrettyPrinter(indent = 4)

FilePath = 'C:\\Users\\Condes\\Dropbox\\Apps\\Reporter-App\\2014-03-07-reporter-export.json'

if FilePath:
    file = open(FilePath)
    data = json.load(file)



pp.pprint(data)