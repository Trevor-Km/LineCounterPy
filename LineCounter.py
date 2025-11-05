import os

class LineCounter:
    # Hidden Selections:
    # RA: Read Allowed Extensions
    # RP: Read Path
    # D: Load default values
    # TODO: Add rankings based on project size
    def __init__(self):
        self.allowed_extensions = []
        self.ignored_directories = ["node_modules"]
        self.path = ""
        self.count = 0

    def start_dialog(self):
        print("//////////////////////////////////")
        print("//////Welcome To LineCounter//////")
        print("//////////////////////////////////")

        while True:
            self.count = 0
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
                       print("Final Line Count: " + str(self.count))
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
                self.allowed_extensions = [".tsx", ".java", ".ts", ".py"]
                self.path = "C:/Users/trevo/TkDocs/Code/secure-sight"
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
            selection = input("Enter a file extension to be included in the count or E to exit\n")
            if selection.capitalize() == 'E':
                break
            elif len(selection) == 0:
                print("Please select a valid file extension")
                continue
            else:
                if selection[0] != '.':
                    selection = '.' + selection
                allowed_extensions.append(selection)
        self.allowed_extensions = allowed_extensions
    
    def countLines(self, file):
        # Might only work in root folder
        if os.path.isdir(file):
            for f in os.listdir(file):
                if f not in self.ignored_directories:
                    self.countLines(file + '/' + f)
        else:
            if os.path.isfile(file):
                if '.' not in file:
                    return
                if file[file.index('.'):] in self.allowed_extensions:
                    print(file)
                    with open(file) as open_file:
                        for i in open_file:
                            self.count+=1
