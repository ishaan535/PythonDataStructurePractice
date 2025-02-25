print("Ishaan Sarkar")
dict = { 'name': 'Ishaan Sarkar', 'School': 'Christ Church School'}
tup = ('Ishaan Sarkar', 18)
print(dict)
print(tup)
fileName = input("File name: ")
fileNameStr =fileName.split(".")

fileType = {'type': 'json', 'content': '', }
def process_xml():
    print("XML file successfully processed")

def process_json():
    print("JSON file successfully processed")

def process_csv():
    print("CSV file successfully processed")

match fileType:
    case {'type': 'xml', 'content': '', }: process_xml()
    case {'type': 'json', 'content': '', }: process_json()
    case {'type': 'csv', 'content': '', }: process_csv()
    case _: raise ValueError("File not supported.")
