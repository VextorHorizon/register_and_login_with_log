# 🐍 Easy Python Register and Login System with Log

A beginner-friendly Python script for a simple login and registration system using text files for storing credentials and logging login attempts. No external libraries required — just pure Python.

## 🚀 Features

- ✅ User registration with username and password
- 🔐 Login system with up to 5 attempts
- 📝 Logs every login attempt (success or failure) into `login.log`
- 📂 Credentials saved in `user_data.txt` as plain text
- ⚡ Simple logic using `dict`, `with open`, `.split()`, `.strip()`, and conditional statements

## 📁 File Structure

easy-python-register-and-login-system-with-log/
├── main.py # The main Python script
├── user_data.txt # Stores usernames and passwords (plaintext)
├── login.log # Logs login success and failures with timestamp
└── README.md # You’re reading it


## 🧠 Ideal For

- Beginners learning Python with practical projects
- Students starting to explore backend logic or cybersecurity basics
- Anyone looking for a clean, minimal login system as a foundation

## ⚙️ How It Works

- On registration: Appends `username,password` to `user_data.txt`
- On login: Reads `user_data.txt`, compares credentials, and logs the result to `login.log`
- Users have up to 5 login attempts before lockout

## 🔒 Note

This is **not secure for production** — passwords are stored in plain text for learning purposes. You can upgrade it with password hashing (`hashlib`) later.

## 👨‍💻 Developer

- **VextorHorizon**  

---

