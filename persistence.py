#I want to create a script that allows for the persistence of a software on a machine

#Useful libraries that I would be working with
try:
    import os
    import winreg
    import sys
except Exception as e:
    print(f"An error occurred in imported libraries due to [{e}]")


#Declaring the class 
class Hiraishin:
    def __init__(self):
        self.checkReg()
    
    #This function helps add the program to the registry
    def addReg(self):
        try:
            address = sys.argv[0] 
            for id, i in enumerate(sys.argv[0]):
                if i == ".":
                    filename = sys.argv[0][:id]
                    filename = os.path.basename(filename).title()
                    #print(filename)
            reg_hkey = winreg.HKEY_CURRENT_USER
            key = winreg.OpenKey(reg_hkey, r'Software\Microsoft\Windows\CurrentVersion\Run', 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, f'{filename}', 0, winreg.REG_SZ, address)
            winreg.CloseKey(key)
        except:
            pass
    
    #This function helps check if the program is in the registry
    def checkReg(self):
        try:
            reg_hkey = winreg.HKEY_CURRENT_USER
            key = winreg.OpenKey(reg_hkey, r'Software\Microsoft\Windows\CurrentVersion\Run', 0, winreg.KEY_READ)
            index = 0
            while True:
                v = winreg.EnumValue(key, index)
                if f'{filename}' not in v:
                    index += 1
                    continue
                return True
        except:
            winreg.CloseKey(key)
            self.addReg()



if __name__ == "__main__":
    print("PERSISTENCE \n")

    persistence = Hiraishin()

    print("Executed successfully!!")
