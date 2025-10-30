import os
# Enter path here
path = "C:/Users/trevo/TkDocs/Code/secure-sight"
accepted_extensions = [".js", ".ts", ".java", ".py", ".tsx", "."]

for file in os.listdir(path):
    if os.path.isdir(file):
        print("Hello")


class LineCounter:
    # Hidden Selections:
    # RA: Read Allowed Extensions
    # RP: Read Path
    # D: Load default values

    def __init__(self):
        self.allowed_extensions = []
        self.path = ""
        self.count = 0

    def start_dialog(self):
        print("//////////////////////////////////")
        print("//////Welcome To LineCounter//////")
        print("//////////////////////////////////")

        while True:
            selection = input("Enter: P for Path A for Allowed Extensions, C to begin Counting or E to Exit\n")
            selection = selection.upper()
            if selection == 'P':
                self.set_path() 
            elif selection == 'A':
                self.set_allowed()
            elif selection == 'C':
                if len(self.allowed_extensions) != 0:
                    if len(self.path) != 0:
                       print("Beginning Count...") # Count 
                       self.countLines(self.path)
                       print("Final Count: " + str(self.count))
                    else: 
                        print("Please use P to enter a valid path.")
                        continue  
                else:
                    print("Please use A to enter valid allowed extensions")  
            elif selection == "RP":
                print(self.path)
            elif selection == "RA":
                print(self.allowed_extensions)
            elif selection == "D":
                self.allowed_extensions = [".txt"]
                self.path = "C:/Users/trevo/TkDocs/Misc/"
                print("Defaults Loaded!")
            elif selection == 'E':
                print("See ya!")
                break
            else:
                print("Please Enter a Valid Selection")
                print("Your selection: " + selection)


    def set_path(self):
        path = input("Please enter your file/folder path\n")
        self.path = path

    def set_allowed(self):
        allowed_extensions = []
        selection = ''
        while selection != 'E':
            selection = input("Enter a file extension to be included in the count\n")
            if selection == 'E':
                break
            elif len(selection) == 0:
                print("Please select a valid file extension")
                continue
            else:
                allowed_extensions.append(selection)
        self.allowed_extensions = allowed_extensions
    
    def countLines(self, file):
        # Might only work in root folder
        if os.path.isdir(file):
            for f in os.listdir(file):
                self.countLines(self.path+"/"+f)
        else:
            if os.path.isfile(file):
                print("Hey, Im a file!")
                if file[file.index('.'):] in self.allowed_extensions:
                    with open(file) as open_file:
                        for line in open_file:
                            print(line)
                            self.count+=1
                else:
                    print("Invalid file extension")