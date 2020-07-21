from tkinter import *
from PIL import ImageTk,Image
import random
playerWins = 0
robotWins = 0
userTies = 0
def rock():
    a = 1
    playGame(a)
def paper():
    a = 2
    playGame(a)
def scissors():
    a = 3
    playGame(a)
  
def playGame(a):
    global playerWins
    global robotWins
    global userTies
    b = random.randint(1,3)
    if(a == 1 and b == 1):
        desLabel['text'] = "The Robot Chose: Rock"  
        userTies = userTies + 1     
        tieLabel['text'] = "User Total Ties: " + str(userTies)  

        ex = Toplevel()
        canvas = Canvas(ex, width = 300, height = 300)  
        canvas.pack()  
        img = ImageTk.PhotoImage(Image.open("rock.png"))  
        canvas.create_image(20, 20, anchor = NW, image=img) 
        ex.mainloop()


        xe = Toplevel()
        canvas = Canvas(xe, width = 300, height = 300)  
        canvas.pack()  
        img = ImageTk.PhotoImage(Image.open("rock.png"))  
        canvas.create_image(20, 20, anchor = NW, image=img) 
        xe.mainloop()







    if(a == 1 and b == 2):
        desLabel['text'] = "The Robot Chose: Paper"
        robotWins = robotWins + 1
        losingLabel['text'] = "Robot Total Wins: " + str(robotWins)  



        ex = Toplevel()
        canvas = Canvas(ex, width = 300, height = 300)  
        canvas.pack()  
        img = ImageTk.PhotoImage(Image.open("rock.png"))  
        canvas.create_image(20, 20, anchor = NW, image=img) 
        ex.mainloop()


        xe = Toplevel()
        canvas = Canvas(xe, width = 300, height = 300)  
        canvas.pack()  
        img = ImageTk.PhotoImage(Image.open("paper.png"))  
        canvas.create_image(20, 20, anchor = NW, image=img) 
        xe.mainloop()





    if(a == 1 and b == 3):
        desLabel['text'] = "The Robot Chose: Scissors"
        playerWins = playerWins + 1
        winningLabel['text'] = "User Total Wins: " + str(playerWins)



        ex = Toplevel()
        canvas = Canvas(ex, width = 300, height = 300)  
        canvas.pack()  
        img = ImageTk.PhotoImage(Image.open("rock.png"))  
        canvas.create_image(20, 20, anchor = NW, image=img) 
        ex.mainloop()


        xe = Toplevel()
        canvas = Canvas(xe, width = 300, height = 300)  
        canvas.pack()  
        img = ImageTk.PhotoImage(Image.open("scissors.png"))  
        canvas.create_image(20, 20, anchor = NW, image=img) 
        xe.mainloop()



    if(a == 2 and b == 1):
        desLabel['text'] = "The Robot Chose: Rock"
        playerWins = playerWins + 1
        winningLabel['text'] = "User Total Wins: " + str(playerWins)



        ex = Toplevel()
        canvas = Canvas(ex, width = 300, height = 300)  
        canvas.pack()  
        img = ImageTk.PhotoImage(Image.open("paper.png"))  
        canvas.create_image(20, 20, anchor = NW, image=img) 
        


        xe = Toplevel()
        canvas = Canvas(xe, width = 300, height = 300)  
        canvas.pack()  
        img = ImageTk.PhotoImage(Image.open("rock.png"))  
        canvas.create_image(20, 20, anchor = NW, image=img) 
        ex.mainloop()
        xe.mainloop()





    if(a == 2 and b == 2):
        desLabel['text'] = "The Robot Chose: Paper"
        userTies = userTies + 1     
        tieLabel['text'] = "User Total Ties: " + str(userTies)  



        ex = Toplevel()
        canvas = Canvas(ex, width = 300, height = 300)  
        canvas.pack()  
        img = ImageTk.PhotoImage(Image.open("paper.png"))  
        canvas.create_image(20, 20, anchor = NW, image=img) 
        ex.mainloop()


        xe = Toplevel()
        canvas = Canvas(xe, width = 300, height = 300)  
        canvas.pack()  
        img = ImageTk.PhotoImage(Image.open("paper.png"))  
        canvas.create_image(20, 20, anchor = NW, image=img) 
        xe.mainloop()


    if(a == 2 and b == 3):
        desLabel['text'] = "The Robot Chose: Scissors"
        robotWins = robotWins + 1
        losingLabel['text'] = "Robot Total Wins: " + str(robotWins)  



        ex = Toplevel()
        canvas = Canvas(ex, width = 300, height = 300)  
        canvas.pack()  
        img = ImageTk.PhotoImage(Image.open("paper.png"))  
        canvas.create_image(20, 20, anchor = NW, image=img) 
        ex.mainloop()


        xe = Toplevel()
        canvas = Canvas(xe, width = 300, height = 300)  
        canvas.pack()  
        img = ImageTk.PhotoImage(Image.open("scissors.png"))  
        canvas.create_image(20, 20, anchor = NW, image=img) 
        xe.mainloop()




    if(a == 3 and b == 1):
        desLabel['text'] = "The Robot Chose: Rock"
        robotWins = robotWins + 1
        losingLabel['text'] = "Robot Total Wins: " + str(robotWins)  



        ex = Toplevel()
        canvas = Canvas(ex, width = 300, height = 300)  
        canvas.pack()  
        img = ImageTk.PhotoImage(Image.open("scissors.png"))  
        canvas.create_image(20, 20, anchor = NW, image=img) 
        ex.mainloop()


        xe = Toplevel()
        canvas = Canvas(xe, width = 300, height = 300)  
        canvas.pack()  
        img = ImageTk.PhotoImage(Image.open("rock.png"))  
        canvas.create_image(20, 20, anchor = NW, image=img) 
        xe.mainloop()



    if(a == 3 and b == 2):
        desLabel['text'] = "The Robot Chose: Paper"
        playerWins = playerWins + 1
        winningLabel['text'] = "User Total Wins: " + str(playerWins)


        ex = Toplevel()
        canvas = Canvas(ex, width = 300, height = 300)  
        canvas.pack()  
        img = ImageTk.PhotoImage(Image.open("scissors.png"))  
        canvas.create_image(20, 20, anchor = NW, image=img) 
        ex.mainloop()


        xe = Toplevel()
        canvas = Canvas(xe, width = 300, height = 300)  
        canvas.pack()  
        img = ImageTk.PhotoImage(Image.open("paper.png"))  
        canvas.create_image(20, 20, anchor = NW, image=img) 
        xe.mainloop()



    if(a == 3 and b == 3):
        desLabel['text'] = "The Robot Chose: Scissors"
        userTies = userTies + 1  
        tieLabel['text'] = "User Total Ties: " + str(userTies) 


        ex = Toplevel()
        canvas = Canvas(ex, width = 300, height = 300)  
        canvas.pack()  
        img = ImageTk.PhotoImage(Image.open("scissors.png"))  
        canvas.create_image(20, 20, anchor = NW, image=img) 
        ex.mainloop()


        xe = Toplevel()
        canvas = Canvas(xe, width = 300, height = 300)  
        canvas.pack()  
        img = ImageTk.PhotoImage(Image.open("scissors.png"))  
        canvas.create_image(20, 20, anchor = NW, image=img) 
        xe.mainloop()




            
def resetGame():
    global playerWins
    global robotWins
    global userTies
    playerWins = 0
    robotWins = 0
    userTies = 0
    winningLabel['text'] = "User Total Wins: " + str(playerWins)
    losingLabel['text'] = "Robot Total Wins: " + str(robotWins)  
    tieLabel['text'] = "User Total Ties: " + str(userTies)      
    desLabel['text'] = "The Robot Chose: "



chicken = " "
root = Tk()
root.title("Rock Paper Scissors")
root.geometry('500x300')
root.config(bg = 'White')

mainLabel= Label(root, text = "Rock Paper or Scissors?", fg = "black", font = "gothic 12 bold")

desLabel = Label(root,text ="The Robot Chose: " + chicken, fg = "black", font = "gothic 12 bold")

a = str(playerWins)
b = str(userTies)
c = str(robotWins)

winningLabel = Label(root, text = "User Total Wins: " + a, fg = "black", font = "gothic 12 bold")
tieLabel = Label(root, text = "User Total Ties: " + b, fg = "black", font = "gothic 12 bold")
losingLabel = Label(root, text = "Robot Total Wins: " + c, fg = "black", font = "gothic 12 bold")




buttonRock = Button(root, text = "Rock", bg = "Black", fg = "Black", font = "gothic 24 bold", command = lambda : rock())
buttonPaper = Button(root, text = "Paper", bg = "Black", fg = "Black", font = "gothic 24 bold", command = lambda : paper() )
buttonScissors = Button(root, text = "Scissors", bg = "Black", fg = "Black", font = "gothic 24 bold", command = lambda: scissors())
resetButton = Button(root,text = "Reset Score",bg = "Black", fg = "Black", font = "gothic 24 bold", command = lambda: resetGame())

mainLabel.grid(row = 0, column = 0)
buttonRock.grid(row = 3, column = 0)
buttonPaper.grid(row = 3, column = 1)
buttonScissors.grid(row = 3, column =2)
desLabel.grid(row = 4, column = 0)
winningLabel.grid(row = 5, column = 0)
tieLabel.grid(row = 6, column = 0)
losingLabel.grid(row = 7, column = 0)
resetButton.grid(row = 12, column = 1)





root.mainloop()
