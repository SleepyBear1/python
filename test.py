from sys import exit                                                                            
import sys,re,os                                                                                                                                            
def startMenu():                                                                                
    global userApps,userPasswords,userPincode,userName,userEmail                                
    clr()                                                                                    
    sys.tracebacklimit=0                                                                       
    print("Welcome to Key Safe".center(40, ' ')+"\n"+"-"*40+"")                            
    print("Enter the number of the desired function:\n\n",                                 
          "1)  Login With existing Account\n",                                          
          "2)  Create new Account\n",                                                   
          "3)  Information\n",                                                             
          "4)  Exit\n")                                                                    
    while True:                                                                           
        try:                                                                                   
            userChoice=int(input(" - "))                                                        
            if userChoice in range(1,5):                                                        
                break                                                                           
            else:                                                                               
                print("Please only enter numbers on the menu!")                                 
        except ValueError:                                                                      
            print("Please only enter numbers on the menu!")                                     
    if userChoice == 1:                                                                         
        userLogin()                                                                             
    if userChoice == 2:                                                                         
        clr()                                                                                   
        userNameChange()                                                                        
        print("Greetings, "+userName+".")                                                       
        userEmailChange()                                                                       
        userPincodeChange()                                                                     
        emailData=(userEmail.split("@")[1]).split(".")[0].capitalize()                          
        userApps=[str(emailData),'Code avengers','Python turtle']                               
        userPasswords=['undefined','undefined','undefined']                                     
        exportData()                                                                            
        print("-"*60,"\nYour account has been created, "+userName+"!","\nYour Login Email:",userEmail,"\nYour Pincode:",userPincode,"\nYou have been given 3 default apps: \n\t- "+emailData.capitalize()+"\n\t- Code Avengers\n\t- Python Turtle\nThe default passwords for these are: 'undefined'\nYou can change this in the 'Change an existing password' menu setting\n\nEnjoy!\n"+"-"*60,"\n"*2) 
        mainMenu()                                                                              
    if userChoice == 3:                                                                         
        clr()                                                                                   
        print("Welcome To Key Safe".center(60," ")+"\n"+"-"*60+"\n"+"\n\tKey Safe is a password storing programme developed\n"+"\tin Python. In this programme I added functionality\n"+"\tto View/Add/Change/Remove Apps and their\n"+"\tpasswords.  I have tried to make this programme\n"+"\teasy to use.\n"+"\n\tIn the numbered Menus, simply type the number of\n"+"\tthe desired function you want to access.\n"+"\n\t- Josh")
        input("\nPress ENTER to continue...")                                                   
        startMenu()                                                                             
    if userChoice == 4:                                                                         
        clr()                                                                                   
        endProgram(str("Thank you! Have a good day!\nClosing..."))                              

def encrypt(txt):                                                                               
    encrypted = ''                                                                              
    for i in txt:                                                                               
        c = ord(i)+5                                                                            
        if ord(i) != c:                                                                         
            b = chr(c)                                                                          
            encrypted += b                                                                      
    encrypted=str(encrypted.replace("\\","
    encrypted=str(encrypted.replace("|","%"))                                                   
    return encrypted                                                                            

def decrypt(txt):                                                                               
    txt.replace('
    txt.replace('%','|')                                                                        
    decrypted = ''                                                                              
    for x in txt:                                                                               
        c = ord(x)-5                                                                            
        if ord(x) != c:                                                                         
            b = chr(c)                                                                          
            decrypted += b                                                                      
    return decrypted                                                                            

def endProgram(reason="Closing..."):                                                            
    global userPincode,userEmail                                                                
    print(reason)                                                                               
    userPincode=""                                                                              
    userEmail=""                                                                                
    exit(0)                                                                                     

def clr():                                                                                      
    print("\n"*50)                                                                              
    return ''                                                                                   

def userPincodeChange():                                                                        
    global userPincode                                                                          
    while True:                                                                                 
        print("Your new Pincode must:\n\t- Be longer than 8 characters\n\t- Contain at least 1 Lowercase letter\n\t- Contain at least 1 Uppercase letter\n\t- Contain at least 1 number\n") 
        userPincode= input("Input your pincode: \n - ")                                         
        if len(userPincode) <= 7 :                                                              
            clr()                                                                               
            print("Must be at least 8 characters\n")                                            
        if ' ' in userPincode:                                                                  
            clr()                                                                               
            print("Must not contain spaces!\n")                                                 
        if len(userPincode) >= 20:                                                              
            clr()                                                                               
            print("Must be shorter than 20 characters\n")                                       
        if not re.search("[a-z]",userPincode):                                                  
            clr()                                                                               
            print("Must contain lowercase\n")                                                   
        if not re.search("[0-9]",userPincode):                                                  
            clr()                                                                               
            print("Must contain a number\n")                                                    
        if not re.search("[A-Z]",userPincode):                                                  
            clr()                                                                               
            print("Must contain a least 1 uppercase\n")                                         
        if len(userPincode) > 6 and len(userPincode) < 20 and re.search("[A-Za-z0-9]",userPincode) and not ' ' in userPincode: 
            clr()                                                                               
            return                                                                              
        else:                                                                                   
            clr()                                                                               
            print("Please make sure your new pincode follows the rules.")                 

def userDelete():                                                                               
    menuAsk("WARNING:  THIS ACTION CANNOT BE UNDONE!\nAre you sure you want to delete this account?\n!") 
    if outcome == True:                                                                         
        os.remove(encrypt(re.sub('[0-9]+', '', userEmail))+".txt")                              
        endProgram("Account terminated")                                                        
    else:                                                                                       
        clr()                                                                                   
        print("Action Cancelled!\n\nReturning to menu...")                                      
        mainMenu()                                                                              

def menuAsk(msg="\nWould you like to return to the menu? (Yes or No)"):                         
    while True:                                                                                 
        global Polar,outcome                                                                    
        print(msg)                                                                              
        Polar=str(input(" - ")).lower()                                                         
        if 'y' in Polar:                                                                        
            outcome=True                                                                        
            return outcome                                                                      
        if 'n' in Polar:                                                                        
            outcome=False                                                                       
            return outcome                                                                      
        else:                                                                                   
            print("Please enter either Yes or No")                                              
            continue                                                                            

def importData():                                                                               
    global userApps,userPasswords,userPincode,fileName,userName                                 
    userPincode=decrypt(fileName[1])                                                            
    userName=decrypt(fileName[2])                                                               
    userApps=[]                                                                                 
    userPasswords=[]                                                                            
    fileName=list(fileName)                                                                     
    for app in range(0,len((fileName[3]).split(","))):                                          
        userApps.append(decrypt((fileName[3]).split(",")[app]))                                 
    for password in range(0,len((fileName[4]).split(","))):                                     
        userPasswords.append(decrypt((fileName[4]).split(",")[password]))                       

def exportData():                                                                               
    fileName=open(encrypt(re.sub('[0-9]+', '', userEmail))+".txt","w+")                         
    fileName.write("{}\n{}\n{}\n".format(encrypt(userEmail),encrypt(userPincode),encrypt(userName))) 
    for i in range(0,len(userApps)):                                                            
        if i == (len(userApps)-1):                                                              
            fileName.write("{}".format(encrypt(userApps[i])))                                   
        else:                                                                                   
            fileName.write("{}".format(encrypt(userApps[i]))+",")                              
    fileName.write("\n")                                                                        
    for i in range(0,len(userPasswords)):                                                       
        if i == (len(userPasswords)-1):                                                         
            ending=""                                                                           
        else:                                                                                   
            ending=","                                                                          
        fileName.write("{}".format(encrypt(userPasswords[i]))+ending)                           
    fileName.close()                                                                            
    
def passwordFind():                                                                             
    global userApps,userPasswords                                                               
    while True:                                                                                 
        clr()                                                                                   
        print("Displaying",len(userApps),"Apps/Websites")                                       
        print("".ljust(10)+"App:".ljust(22)+"Password:\n")                                      
        for index in range(0,len(userApps)):                                                    
            print("".ljust(10)+userApps[index].ljust(20)+"\t"+"*"*len(userPasswords[index]))    
        userChoice=str(input("\nType 'All' to display all Apps/websites and their Passwords.\nWhat Website/App would you like to find the password for: ")).capitalize()
        if userChoice == "All":                                                                 
            clr()                                                                               
            print("Displaying all Apps/Websites and their Passwords.")                          
            print("".ljust(10)+"App:".ljust(22)+"Password:\n")                                  
            for index in range(0,len(userApps)):                                                
                print("".ljust(10)+userApps[index].ljust(20)+"\t"+userPasswords[index])         
            menuAsk()                                                                           
            if outcome == True:                                                                 
                clr()                                                                           
                mainMenu()                                                                      
            else:                                                                               
                continue                                                                        
        if userChoice in userApps:                                                              
            clr()                                                                               
            print("".ljust(10)+"App:".ljust(22)+"Password:\n")                                  
            print("".ljust(10)+str(userApps[userApps.index(userChoice)]).ljust(22)+str(userPasswords[userApps.index(userChoice)])) 
            menuAsk()                                                                           
            if outcome == True:                                                                 
                clr()                                                                           
                mainMenu()                                                                      
            else:                                                                               
                continue                                                                        
        if not userChoice in userApps:                                                          
            clr()                                                                               
            print("\n"+userChoice,"does not seem to exist. Would you like to add it? (Yes or No)") 
            menuAsk("")                                                                         
            if outcome == True:                                                                 
                addApp(str(userChoice))                                                         
                menuAsk()                                                                       
                if outcome == True:                                                             
                    clr()                                                                       
                    mainMenu()                                                                  
                else:                                                                           
                    continue                                                                    
            else:                                                                               
                menuAsk()                                                                       
                if outcome == True:                                                             
                    clr()                                                                       
                    mainMenu()                                                                  
                else:                                                                           
                    continue                                                                    

def passwordChange():                                                                           
    global userPasswords                                                                        
    clr()                                                                                       
    print("Please enter the number for the password you want to change:")                       
    print("".ljust(10)+"App:".ljust(22)+"Password:\n")                                          
    for i in range(0,len(userApps)):                                                            
        print("".ljust(5),"{}".format(i+1)+").",userApps[i].ljust(20)+"\t"+"*"*len(userPasswords[i])) 
    print("\n      {}). Cancel".format(i+2))                                                    
    while True:                                                                                 
        try:                                                                                    
            userChoice=int(input(" - "))                                                        
            if userChoice in range(1,len(userApps)+1):                                          
                while True:                                                                     
                    print("\rEnter the new password for", userApps[userChoice-1]+":")           
                    newChoice=str(input(" - "))                                                 
                    if len(newChoice) >= 4:                                                     
                        userPasswords[userChoice-1]=newChoice                                   
                        exportData()                                                            
                        clr()                                                                   
                        print("Password Sucessfully Changed! Returning to Menu...\n")           
                        mainMenu()                                                              
                    else:                                                                       
                        print("It is recommended that you new password is longer than 4 characters!") 
                        continue                                                                
            if userChoice == (len(userApps)+1):                                                 
                clr()                                                                           
                print("Returning to menu...\n\n")                                               
                mainMenu()                                                                      
            else:                                                                               
                print("Please only enter numbers on the menu")                                  
        except ValueError:                                                                      
            print("Try Again! Please only enter numbers on the menu!")                          

def removeApp():                                                                                
    global userPasswords,userApps                                                               
    clr()                                                                                       
    print("Please state the number for the app you want to remove:")                            
    print("".ljust(10)+"App:".ljust(22)+"\n")                                                   
    for i in range(0,len(userApps)):                                                            
        print("".ljust(5),"{}".format(i+1)+").",userApps[i].ljust(20))                          
    print("\n      {}). Cancel".format(i+2))                                                    
    while True:                                                                                 
        try:                                                                                    
            userChoice=int(input(" - "))                                                        
            if userChoice in range(1,len(userApps)+1):                                          
                del userApps[userChoice-1]                                                      
                del userPasswords[userChoice-1]                                                 
                clr()                                                                           
                print("App & Password Removed!\nReturning to menu...\n\n")                      
                mainMenu()                                                                      
            if userChoice == (len(userApps)+1):                                                 
                clr()                                                                           
                print("Returning to menu...\n\n")                                               
                mainMenu()                                                                      
            else:                                                                               
                print("Please only enter numbers on the menu")                                  
        except ValueError:                                                                      
            print("Try Again! Please only enter numbers on the menu!")                          

def addApp(new=""):                                                                             
    global userApps,userPasswords                                                               
    if new != "":                                                                               
        clr()                                                                                   
        while True:                                                                             
            print("Please enter a password for "+new+":")                                       
            dataPassword=str(input(" - "))                                                      
            if len(dataPassword) > 4:                                                           
                userApps.append(new)                                                            
                userPasswords.append(dataPassword)                                              
                clr()                                                                           
                print("App/Website Added!\n\tApp:\t\tPassword:\n\n\t"+new+"".ljust(22)+("*"*len(dataPassword))) 
                break                                                                           
            else:                                                                               
                clr()                                                                           
                print("Try Again!\n\nIt is recommended that your password is more than 4 characters!")  
    else:                                                                                       
        clr()                                                                                   
        while True:                                                                             
            print("Please enter the name of the Website/App:")                                  
            userInput=str(input(" - ")).capitalize()                                            
            if userInput == "Cancel":                                                           
                clr()                                                                           
                mainMenu()                                                                      
            if len(userInput) > 1:                                                              
                userApps.append(userInput)                                                      
                clr()                                                                           
                while True:                                                                     
                    print("Please enter the password for "+userInput+":")                       
                    userChoice= str(input(" - "))                                               
                    if len(userChoice) > 4:                                                     
                        userPasswords.append(userChoice)                                        
                        break                                                                   
                    else:                                                                       
                        print("Try Again!\n\nIt is recommended that your password is more than 4 characters!") 
                        continue                                                                
                clr()                                                                           
                print("App/Website Added!\n\tApp:\t\tPassword:\n\n\t"+userInput+"".ljust(10)+("*"*len(userChoice))) 
                menuAsk("Would you like to add another app: (Yes or No)")                       
                if outcome == True:                                                             
                    continue                                                                    
                else:                                                                           
                    clr()                                                                       
                    print("Returning to menu!\n")                                               
                    exportData()                                                                
                    mainMenu()                                                                  
            else:                                                                               
                clr()                                                                           
                print("Try Again!\n\nInput can not be left empty!")                             

def userLogin():                                                                                
    global fileName,userEmail,userPincode                                                       
    attempts= 3                                                                                 
    while attempts > 0:                                                                         
        try:                                                                                    
            userEmail=str(input("Please enter your existing Email address: ")).lower()          
            clr()                                                                               
            if re.match(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", userEmail):        
                fileName=open(encrypt(re.sub('[0-9]+', '', userEmail))+".txt","r").read().split()
                if decrypt(fileName[0]) == userEmail:                                           
                    break                                                                       
                else:                                                                           
                    print("\nIncorrect email address")                                          
            else:                                                                               
                print("Invalid Email address\n")                                                
                attempts-=1                                                                     
                if attempts == 0:                                                               
                    endProgram(str("\n"*3+"Too many attempts! The program will now exit."))     
                continue                                                                        
        except FileNotFoundError:                                                               
            print("This Email address ("+userEmail+") does not exist!\n")                       
            attempts-=1                                                                         
            if attempts == 0:                                                                   
                endProgram("Too many attempts! The program will now exit.")                     
            pass                                                                                
    attempts= 3                                                                                 
    clr()                                                                                       
    while attempts > 0:                                                                         
        print("Email Entered: "+userEmail)                                                      
        userPincode=str(input("Please enter your Pincode: "))                                   
        if decrypt(fileName[1]) == userPincode:                                                 
            importData()                                                                        
            clr()                                                                               
            mainMenu()                                                                          
        else:                                                                                   
            clr()                                                                               
            print("Incorrent pin!\n")                                                           
            attempts-=1                                                                         
            if attempts == 1:                                                                   
                    print("\r\rContinuing to enter the incorrect Pincode will cause the program to close.\n") 
            if attempts == 0:                                                                   
                clr()                                                                           
                endProgram("Too many attempts! The program will now exit.")                     

def userEmailChange():                                                                          
    global userEmail                                                                            
    while True:                                                                                 
        newEmail=str(input("Please enter your new Email address: ")).lower()                    
        if re.match(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", newEmail):             
            if os.path.isfile(encrypt(re.sub('[0-9]+', '', newEmail))+".txt"):                  
                clr()                                                                           
                print("This user already exists! Try again!\n")                                 
            else:                                                                               
                try:                                                                            
                    if len(userPincode) > 7:                                                    
                        os.remove(encrypt(re.sub('[0-9]+', '', userEmail))+".txt")              
                        userEmail= newEmail                                                     
                        exportData()                                                            
                        clr()                                                                   
                        print("Your login email is now:",userEmail,"\n")                        
                        mainMenu()                                                              
                    else:                                                                       
                        userEmail= newEmail                                                     
                        return                                                                  
                except NameError:                                                               
                    userEmail= newEmail                                                         
                    return                                                                      
        else:                                                                                   
            clr()                                                                               
            print("Invalid Email Address!\n")                                                   
    
def userNameChange():                                                                           
    global userName                                                                             
    while True:                                                                                 
        userName= input("Please enter your first name: ").capitalize()                          
        if len(userName) > 15:                                                                  
            clr()                                                                               
            print("Error! Maximum 15 characters allowed!\n")                                    
            continue                                                                            
        if len(userName) < 2:                                                                   
            clr()                                                                               
            print("Error! Must have at least 2 characters!\n")                                  
            continue                                                                            
        if not re.match("^[a-z,A-Z]*$", userName):                                              
            clr()                                                                               
            print("Error! Only the letters a-z are allowed!\n")                                 
            continue                                                                            
        if len(userName) <15 and len(userName) >= 2 and re.match("^[a-z,A-Z]*$", userName):     
            clr()                                                                               
            break                                                                               
        else:                                                                                   
            print("Please enter a valid first name...\n")                                       
            continue                                                                            
    return                                                                                      
    
def userOptions():                                                                              
    print("Account options for:",userName,"\nEnter the number of the desired function:\n\n\t",  
          "1)  Change Login Pincode\t(Currently: "+"*"*len(userPincode)+")\n\t",                
          "2)  View Login Pincode\n\t",                                                         
          "3)  Change Login Email address\t(Currently: "+userEmail+")\n\t",                     
          "4)  Change Display Name\t(Currently: "+userName+")\n\t",                             
          "5)  Delete Account\n\n\t",                                                           
          "6)  Return to menu\n")                                                               
    while True:                                                                                 
        try:                                                                                    
            userChoice=int(input(" - "))                                                        
            if userChoice in range(1,7):                                                        
                break                                                                           
            else:                                                                               
                print("Please only enter numbers on the menu!")                                 
        except ValueError:                                                                      
            print("Please only enter numbers on the menu!")                                     
    if userChoice == 1:                                                                         
        clr()                                                                                   
        userPincodeChange()                                                                     
        print("Your pincode has been updated to:",userPincode)                                  
        exportData()                                                                            
        userOptions()                                                                           
    if userChoice == 2:                                                                         
        clr()                                                                                   
        print("\nYour Login Pincode:",userPincode,"\n")                                         
        userOptions()                                                                           
    if userChoice == 3:                                                                         
        userEmailChange()                                                                       
        print("Your email has been changed to:",userEmail)                                      
    if userChoice == 4:                                                                         
        userNameChange()                                                                        
        print("Your name has been changed to: "+userName+".\n\nReturning to menu...\n")         
        mainMenu()                                                                              
    if userChoice == 5:                                                                         
        userDelete()                                                                            
    if userChoice == 6:                                                                         
        clr()                                                                                   
        mainMenu()                                                                              
        
def mainMenu():                                                                                 
    print("Key Safe Main Menu".center(60, ' ')+"\n"+"-"*60+"\n")                                
    print("Logged in user:",userName+"\n"+                                                      
          "You have",len(userApps),"apps\n"                                                     
          "Enter the number of the desired function:\n\n",                                      
          "1)  Find the password for an existing Website/App\n",                                
          "2)  Add new Website/App and new password for it\n",                                  
          "3)  Change an existing password for an existing Website/App\n",                      
          "4)  Remove an existing App/Website\n",                                               
          "5)  Account Options\n",                                                              
          "6)  Exit\n")                                                                         
    while True:                                                                                 
        try:                                                                                    
            userChoice=int(input(" - "))                                                        
            if userChoice in range(1,7):                                                        
                break                                                                           
            else:                                                                               
                print("Please only enter numbers on the menu!")                                 
        except ValueError:                                                                      
            print("Please only enter numbers on the menu!")                                     
    if userChoice == 1:                                                                         
        passwordFind()                                                                          
    if userChoice == 2:                                                                         
        addApp()                                                                                
    if userChoice == 3:                                                                         
        passwordChange()                                                                        
    if userChoice == 4:                                                                         
        if len(userApps) == 2:                                                                  
            clr()                                                                               
            print("You must have at least 3 apps before you can remove an app.\n")              
            mainMenu()                                                                          
        else:                                                                                   
            removeApp()                                                                         
    if userChoice == 5:                                                                         
        clr()                                                                                   
        userOptions()                                                                           
    if userChoice == 6:                                                                         
        clr()                                                                                   
        exportData()                                                                            
        endProgram(str("Thank you,"+userName+"! Have a Good Day!\nClosing..."))                 

startMenu()                                                                                     