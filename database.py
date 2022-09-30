#from ast import Delete
from ctypes import sizeof
import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine import connection
#from datetime import datetime
from cassandra.cqlengine.management import sync_table
from cassandra.cqlengine.models import Model
from cassandra.cluster import Cluster
from collections import namedtuple


# Connection
  
cassandraHost = '192.168.56.1'
cluster = Cluster([cassandraHost], port=9042)
session=cluster.connect()

#Vytvareni keyspace a tabulek
#session.execute("""DROP KEYSPACE IF EXISTS uois""")
session.execute("""CREATE KEYSPACE IF NOT EXISTS uois WITH REPLICATION = { 'class' : 'NetworkTopologyStrategy', 'datacenter1' : 3 };""")
session.set_keyspace('uois') 
session.execute("CREATE TABLE IF NOT EXISTS groups (id int PRIMARY KEY, name text, groupType text, members list<text>)")
session.execute("CREATE TABLE IF NOT EXISTS users (id int PRIMARY KEY, name text, surname text)")
session.execute("CREATE TABLE IF NOT EXISTS groupTypes (id int PRIMARY KEY, name text)")
session.execute("CREATE TABLE IF NOT EXISTS roleTypes (id int PRIMARY KEY, name text)")
session.execute("CREATE TABLE IF NOT EXISTS memberships (id int PRIMARY KEY, roleType text, group text)")



connection.setup([cassandraHost], "uois", protocol_version=3)


#Fuknce pro provadeni CRUD operaci v databazi
class Person():
    def Create(id,name,surname):
        session.execute("INSERT INTO users (id, name, surname) VALUES (%s, %s,%s)", (id, name, surname))
    def Delete(id):
        session.execute("DELETE FROM users WHERE id=%s",(id, ))
    def Update(id,name,surname):
        session.execute("UPDATE users SET name=%s, surname=%s WHERE id=%s",(name, surname,id, ) )
class Group_D():
    def Create(id,name,groupType):
        session.execute("INSERT INTO groups (id, name, groupType) VALUES (%s, %s, %s)", (id, name, groupType))
    def Delete(id):
        session.execute("DELETE FROM groups WHERE id=%s",(id, ))
    def Update(id,name,surname):
        session.execute("UPDATE groups SET name=%s, groupType=%s WHERE id=%s",(name, surname,id, ))
class Group_Type_D():
    def Create(id,name):
        session.execute("INSERT INTO groupTypes (id, name) VALUES (%s, %s)", (id, name))
    def Delete(id):
        session.execute("DELETE FROM groupTypes WHERE id=%s",(id, ))
    def Update(id,name):
        session.execute("UPDATE groupTypes SET name=%s WHERE id=%s",(name, id, ))
class Role_Type_D():
    def Create(id,name):
        session.execute("INSERT INTO roleTypes (id, name) VALUES (%s, %s)", (id, name))
    def Delete(id):
        session.execute("DELETE FROM roleTypes WHERE id=%s",(id, ))
    def Update(id,name):
        session.execute("UPDATE roleTypes SET name=%s WHERE id=%s",(name, id, ))
class Membership_D():
    def Create(id,roleType,group):
        session.execute("INSERT INTO memberships (id, roleType, group) VALUES (%s, %s,%s)", (id, roleType,group))
    def Delete(id):
        session.execute("DELETE FROM memberships WHERE id=%s",(id, ))
    def Update(id,roleType,group):
        session.execute("UPDATE memberships SET roleType=%s, group=%s WHERE id=%s",(roleType, group, id, ))


#Vytvoreni pocatecnich dat
"""
Person.Create(1,"Jakub","Smejkal")
Person.Create(2,"Josef","Vondra")
Group_D.Create(1,"23-5KB","1")
Group_D.Create(2,"24-5KB","1")
Group_D.Create(3,"25-5KB","1")
Group_Type_D.Create(1, "UNOB")
Group_Type_D.Create(2, "StalStav")
Role_Type_D.Create(1, "Admin")
Role_Type_D.Create(2, "Student")
Membership_D.Create(1,"1","1")
Membership_D.Create(2,"2","2")

Person.Delete(2)
Group_D.Delete(3)
Group_Type_D.Delete(2)
Role_Type_D.Delete(2)
Membership_D.Delete(2)

Person.Update(1,"Ondra","Ondru")
Group_D.Update(1,"21-5KB","2")
Group_Type_D.Update(1, "CVUT")
Role_Type_D.Update(1, "SuperAdmin")
Membership_D.Update(1,"3","3")
"""







#Users
#Session CQL command
rows = session.execute('SELECT id, name, surname FROM users')

#Namedtuple pro ukladani uzivatelu do listu
allusers = namedtuple("allusers",['id','name','surname'])
listusers=[]

#Ukladani uzivatelu do listu a jejich vypisovani 
for row in rows:
    print("usr: ", row.id, row.name, row.surname)
    listusers.append(allusers(row.id, row.name, row.surname))
    
#Groups
rows = session.execute('SELECT id, name, groupType FROM groups')
allgroups = namedtuple("allgroups",['id','name','groupType'])
listgroups=[]

for row in rows:
    print("grp: ", row.id, row.name, row.grouptype)
    listgroups.append(allgroups(row.id, row.name, row.grouptype))

#GroupType 
rows = session.execute('SELECT id, name FROM groupTypes')
for row in rows:
    print("grptype: ", row.id, row.name)

#RoleType
rows = session.execute('SELECT id, name FROM roleTypes')
for row in rows:
    print("roletype: ", row.id, row.name)

#Membership
rows = session.execute('SELECT id, roletype, group FROM memberships')
for row in rows:
    print("membership: ", row.id, row.roletype, row.group)







