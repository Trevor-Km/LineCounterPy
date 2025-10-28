import os
# Enter path here
path = "C:/Users/trevo/TkDocs/Code/secure-sight"
accepted_extensions = [".js", ".ts", ".java", ".py", ".tsx", "."]
for file in os.listdir(path):
    if os.path.isdir(file):
        print("Hello")



def countLines(file):
    count = 0
    if os.path.isdir(file):
        count += countLines(file)
    else:
        if os.path.isfile(file):
            if file[file.index('.'):] in accepted_extensions:
                print("Hello")