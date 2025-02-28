from tkinter import *

class TowerOfHanoi:
	def __init__(self):
		self.poles = {"1": [], "2": [], "3": []}
		self.disks = []
		self.num_disks = len(self.poles) * 2 - 1
		self.initialize_game()
		# self.GUI()
		self.get_pole_input()
		
	def GUI(self):
		window = Tk()
		window.geometry("1080x780")
		window.mainloop()
	
	def initialize_game(self):
		# Initializing disks
		for i in range(self.num_disks):
			i += 1
			self.disks.append(i)
		
		# Putting the disks on pole number 1
		self.poles["1"] = self.disks
  		# Disks are numbered from 1 - n(disks) from small to big
		# Default is that all the disks are on pole 1 
		# And the destination pole is pole 3
		# The first value(0) of a disk is the highest disk on the pole 	
  
	def get_pole_input(self):
		selected_pole_1 = input("Enter the pole you want to pick a disk from: ")
		selected_pole_2 = input("Enter the pole you want to put the disk on: ")
		if selected_pole_1 not in self.poles.keys() or selected_pole_2 not in self.poles.keys():
			print("Invalid pole number")
   
		self.move_disk(selected_pole_1, selected_pole_2)

	def move_disk(self, selected_pole_1, selected_pole_2):
		# Check if the move is valid
		if len(self.poles[selected_pole_1]) == 0:
			print("There is no disk on the selected pole")
			return
 
		if len(self.poles[selected_pole_2]) == 0:
			self.poles[selected_pole_2].append(self.poles[selected_pole_1].pop())
			return
 
# Create an instance of the game in Python
game = TowerOfHanoi()
