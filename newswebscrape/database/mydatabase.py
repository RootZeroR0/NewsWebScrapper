import sqlite3

conn = sqlite3.connect('mynews.db')
curr = conn.cursor()

curr.execute("""
                create table abpananda_tb(
                    id integer,
                    heading text,
                    title text,
                    description text,
                    date text
                )
                """)

conn.commit()
conn.close()