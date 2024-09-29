import sqlite3

# Database setup
conn = sqlite3.connect('feedback.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS feedback (user_input TEXT, response TEXT, user_feedback TEXT)''')
conn.commit()
conn.close()
