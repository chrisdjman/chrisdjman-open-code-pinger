import socket
print (" ---------------------------------- ")
print (" ---WELCOME TO CHRISDJMAN PINGER--- ")
print (" ---------------------------------- ")
print ("                                    ")
print ("                                    ")
adrs = input("Enter the website address : ")
print("")
print("IP of the entered host is ",socket.gethostbyname(adrs))


input("press enter to exit")