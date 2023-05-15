import string
import mysql.connector
import random
import base64
from PIL import Image
import io


def sqlQuery(query):
    conn = mysql.connector.connect(user='MasterAdmin19', password='Ro5?dLz$MP!j9tB9',
                                   host='rds-mysql-cps4951.c4bnum2utzbm.us-east-1.rds.amazonaws.com',
                                   database='Testing')
    cursor = conn.cursor()

    cursor.execute(query)

    result = []
    for x in cursor:
        result.append(x)

    conn.commit()
    cursor.close()
    conn.close()

    return result


def randomString():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(100))
    return password


def menuQuery(query):
    conn = mysql.connector.connect(user='MasterAdmin19', password='Ro5?dLz$MP!j9tB9',
                                   host='rds-mysql-cps4951.c4bnum2utzbm.us-east-1.rds.amazonaws.com',
                                   database='Testing')
    cursor = conn.cursor()

    cursor.execute(query)

    result = []
    for x in cursor:
        result.append(x)

    conn.commit()
    cursor.close()
    conn.close()

    return result


def imageQuery(query, number):
    conn = mysql.connector.connect(user='MasterAdmin19', password='Ro5?dLz$MP!j9tB9',
                                   host='rds-mysql-cps4951.c4bnum2utzbm.us-east-1.rds.amazonaws.com',
                                   database='Testing')
    cursor = conn.cursor()

    cursor.execute(query)

    blobs = []
    for x in cursor:
        blobs.append(x)

    if number == 1:
        num = 1
        for y in blobs:
            binary_data = y[0]
            with open("G:/My Drive/Restaurant_app/static/assets/" + str(num) + ".png", "wb") as file:
                file.write(binary_data)
            num += 1
        return blobs

    if number == 2:
        num = 1
        for y in blobs:
            binary_data = y[0]
            with open("G:/My Drive/Restaurant_app/static/assets/" + str(num + 3) + ".png", "wb") as file:
                file.write(binary_data)
            num += 1
        return blobs

    if number == 3:
        num = 1
        for y in blobs:
            binary_data = y[0]
            with open("G:/My Drive/Restaurant_app/static/assets/" + str(num + 6) + ".png", "wb") as file:
                file.write(binary_data)
            num += 1
        return blobs
