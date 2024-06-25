import studentdata
fileaddress=[]
logoaddress=[]
subjects=[]

def file():
    if len(fileaddress)!=0:
        return fileaddress
    else:
        with open("properties.txt",mode="r") as properties_file:
            properties_file.seek(0)
            length=studentdata.find_lines(properties_file)
            for i in range(length):
                line=properties_file.readline()
                properties_list=line.split(",")
                if properties_list[1]=="file\n":
                    fileaddress.append(properties_list[0])
                    return fileaddress
def logoFile():
    if len(logoaddress)!=0:
        return logoaddress
    else:
        with open("properties.txt",mode="r") as properties_file:
            properties_file.seek(0)
            length=studentdata.find_lines(properties_file)
            for i in range(length):
                line=properties_file.readline()
                properties_list=line.split(",")
                if properties_list[1]=="logofile":
                    logoaddress.append(properties_list[0])
                    return logoaddress
                
def sub():
    if len(subjects)!=0:
        return subjects
    else:
        with open("properties.txt",mode="r") as properties_file:
            properties_file.seek(0)
            length=studentdata.find_lines(properties_file)
            for i in range(length):
                line=properties_file.readline()
                properties_list=line.split(",")
                if properties_list[0]=="subjects":
                    properties_list.pop(0)
                    subjects.extend(properties_list)
                    return subjects
