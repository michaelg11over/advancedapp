# Program Name: Assignment5.py
# Course: IT3883/Section 3883
# Student Name: Michael Glover
# Assignment Number: Assignment 5
# Due Date: 04/22/2026
# Purpose:write a Python program to create and interact with a database
# Resources: Python sqlite3 documentation

import sqlite3

#connects file
conn = sqlite3.connect("temperature_readings.db")
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS TemperatureReadings")
cursor.execute("CREATE TABLE TemperatureReadings (ID INTEGER PRIMARY KEY AUTOINCREMENT, Days TEXT, Temps REAL)")

#Reads file
file = open("Friday_83_4.txt", "r")
for line in file:
    data = line.strip().split()
    cursor.execute("INSERT INTO TemperatureReadings (Days, Temps) VALUES (?, ?)", (data[0], float(data[1])))
file.close()
conn.commit()

#prints avgs
cursor.execute("SELECT AVG(Temps) FROM TemperatureReadings WHERE Days = 'Thursday'")
thursday_avg = cursor.fetchone()[0]

cursor.execute("SELECT AVG(Temps) FROM TemperatureReadings WHERE Days = 'Sunday'")
sunday_avg = cursor.fetchone()[0]

print(f"Thursday average temperature:   {thursday_avg:.2f}")
print(f"Sunday average temperature: {sunday_avg:.2f}")

conn.close()