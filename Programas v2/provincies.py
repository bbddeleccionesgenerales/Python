#-------------------------------------------------------------------------------
# Name:        módulo1
# Purpose:
#
# Author:      Manu
#
# Created:     14/03/2020
# Copyright:   (c) Manu 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

iimport zipfile
import os
import sys
import mysql.connector

rutazip = r'C:\Users\Manu\Desktop\Python\Zips\02197706_MESA.zip'
rutaunzip = r'C:\Users\Manu\Desktop\Python\Unzips\02197706_MESA.zip'
fileUnzip = r'C:\Users\Manu\Desktop\Python\Unzips\07027706.DAT'

dirActual = os.path.dirname(rutazip)
print(dirActual)
nomFitxerZip = '02197706_MESA.zip'
dirUnzip = os.path.dirname (rutaunzip )
pathFitxerZip = os.path.join(dirActual,nomFitxerZip)
print(dirUnzip)


with zipfile.ZipFile(pathFitxerZip,'r') as zipRef:
     zipRef.extractall(dirUnzip)

pathFitxer = fileUnzip

cnx = mysql.connector.connect(host='192.168.255.133',user='perepi',password='pastanaga',
      database='eleccions_generals2')
cursor = cnx.cursor()

try:
   with open (pathFitxer,'r') as fitxer:
       #cont = 0
       for linea in fitxer:

            if linea[11:13] != '99':
                llista = []
            #CD = (linea[8:14])
                llista.append(linea[14:64].strip())
                llista.append(linea[11:13])
                llista.append(linea[9:11])
                insert_provincies = ('INSERT INTO provincies (nom, codi_ine, comunitat_aut_id) VALUES (%s, %s, %s)')
                cursor.execute(insert_provincies, llista)
                #print(llista)
                #cont+=1
       #print(cont)

except OSError as e:
    print('Imposible abrir fichero ' + pathFitxer)

cnx.commit()
cursor.close()
cnx.close()
