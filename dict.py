import random 

p=0
d=0
snl={8:37,13:34,38:9,11:2,28:4,40:68,52:81,76:97,65:46,93:64,89:70}
def rolldice():
	return random.randint(1,6)

#get 1 or 6 on the dice to enter the game.
while True:
	r= input("press r to roll the dice,q to quit:")
	if r =='r':
		d = rolldice()
		print("you got ",d)

		if d ==6 or d == 1:
			print("congatulations, yore in the game!!")
			break
		else:
			print("you need to 6 or 1 to start.try again ")
	elif r == 'q':
			exit()
			while True:
				r= inout ("press r to roll the dice, q to quit:")
				if r =='r':
					d= rolldice()
					print("you got",d)
					p = p+d
					if p== 100:
						print("hurray! you won ")
						exit()
						if p>100:
							p = p-d
							print("you need to get ",100-p,"to reach home")
							print("youre new position is ",p)
							if p in snk:
								if p<snl[p]:
									print(" wow ,you got a ladder")
								else:
									print("oops you got swallowed by a snake")

									p = snl[p]
									print("move to",p)
							elif r =='q':
									exit()


							