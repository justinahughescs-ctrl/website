import sqlite3

def read_stats():
	with open('data.txt', 'r') as file:
        	lines = file.readlines()
        	wins = int(lines[0].split(':')[1].strip())
        	losses = int(lines[1].split(':')[1].strip())
        	draws = int(lines[2].split(':')[1].strip())
        	return wins, losses, draws

def update_stats(account_id, wins, losses, draws):
	conn = sqlite3.connect('accounts.db')
	cursor = conn.cursor()

	cursor.execute("""UPDATE Stats SET wins = wins + ?, losses = losses + ?, draws = draws + ? WHERE account_id = (SELECT id FROM Accounts WHERE id = ?)""", (wins, losses, draws, account_id))
	
	conn.commit()
	conn.close()

wins, losses, draws = read_stats()
update_stats(1, wins, losses, draws) #throwing it all into the 1 account for now

