# hello everyone this is group project here

import numpy as np
import matplotlib.pyplot as plt
from abc import ABC,abstractmethod

import sqlite3
import hashlib
from cryptography.fernet import Fernet
import matplotlib.pyplot as plt

# Initialize the database
def initialize_db():
    conn = sqlite3.connect('messages.db')
    c = conn.cursor()
    
    # Create messages table
    c.execute('''CREATE TABLE IF NOT EXISTS messages
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  sender TEXT NOT NULL,
                  receiver TEXT NOT NULL,
                  message TEXT NOT NULL,
                  status TEXT DEFAULT 'Unread',
                  read_timestamp TEXT,
                  sent_timestamp TEXT DEFAULT CURRENT_TIMESTAMP)''')
    
    # Create users table
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  username TEXT UNIQUE NOT NULL,
                  password TEXT NOT NULL)''')
    
    # Create blocked_users table
    c.execute('''CREATE TABLE IF NOT EXISTS blocked_users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  blocker TEXT NOT NULL,
                  blocked TEXT NOT NULL)''')
    
    # Create drafts table
    c.execute('''CREATE TABLE IF NOT EXISTS drafts
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  sender TEXT NOT NULL,
                  receiver TEXT NOT NULL,
                  message TEXT NOT NULL)''')
    
    conn.commit()
    conn.close()

def initial_page(self):
    print("--------------------Login Page--------------------")
    print("1. Sign up")
    print("2. Login")
    print("3. Exit")
    
    choice = input("Enter choice : ")

    if(choice == 1):
    
    elif(choice == 2):
        
    elif(choice == 3):
        # exit