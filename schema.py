#from database import Person,Osoba,Group,Skupina,GroupType,TypSkupiny,RoleType,TypRole,Membership,Clenstvi
#from graphene import ObjectType, Schema, String, Int, Field, List

from unicodedata import name
import graphene
from graphene import ObjectType, String, Field, List, Int
from database import Person,Group_D,Group_Type_D,Role_Type_D,Membership_D
import uuid
from collections import namedtuple
from database import listusers, allusers, listgroups, allgroups

#resolver pro vypsani vsech uzivatelu
class AllUsers(ObjectType):
	id = Int()
	name = String()
	surname = String()

	def resolve_id(allusers,info):
		return allusers.id

	def resolve_name(allusers,info):
		return allusers.name

	def resolve_surname(allusers,info):
		return allusers.surname

#resolver pro vypsani vsech skupin
class AllGroups(ObjectType):
	id = Int()
	name = String()
	groupType = String()

	def resolve_id(allgroups,info):
		return allgroups.id

	def resolve_name(allgroups,info):
		return allgroups.name

	def resolve_groupType(allgroups,info):
		return allgroups.groupType
	

#modely
class User(graphene.ObjectType):
	id = graphene.Int()
	name = graphene.String()
	surname=graphene.String()

class Group(graphene.ObjectType):
	id = graphene.Int()
	name = graphene.String()
	groupType = graphene.String()

class GroupType(graphene.ObjectType):
	id = graphene.Int()
	name = graphene.String()

class RoleType(graphene.ObjectType):
	id = graphene.Int()
	name = graphene.String()

class Membership(graphene.ObjectType):
	id = graphene.Int()
	roleType = graphene.String()
	group = graphene.String()



	
#Queries 
class Query(graphene.ObjectType):
	users=graphene.List(User,first=graphene.Int())
	all_users=List(AllUsers)
	all_groups=List(AllGroups)

	def resolve_all_users(root,info):
		
		return listusers

	def resolve_all_groups(root,info):
		
		return listgroups

	def resolve_users(self,info,first):
		return [
			User(name='Pavel',surname='Vomacka',age='22')
		][:first]

# Mutations
class CreateUser(graphene.Mutation):
	class Arguments:
		id=graphene.Int()
		name = graphene.String()
		surname=graphene.String()
		

	uzivatel = graphene.Field(User)

	def mutate(self,info,id,name,surname):
		uzivatel = User(name)
		Person.Create(id,name,surname)
		return CreateUser(uzivatel=uzivatel)

class CreateGroup(graphene.Mutation):
	class Arguments:
		id=graphene.Int()
		name = graphene.String()
		groupType=graphene.String()
		

	skupina = graphene.Field(Group)

	def mutate(self,info,id,name,groupType):
		skupina = Group(name)
		Group_D.Create(id,name,groupType)
		return CreateGroup(skupina=skupina)

class CreateGroupType(graphene.Mutation):
	class Arguments:
		id=graphene.Int()
		name = graphene.String()
		

	typskupiny = graphene.Field(GroupType)

	def mutate(self,info,id,name):
		typskupiny = GroupType(name)
		Group_Type_D.Create(id,name)
		return CreateGroupType(typskupiny=typskupiny)

class CreateRoleType(graphene.Mutation):
	class Arguments:
		id=graphene.Int()
		name = graphene.String()
		

	typrole = graphene.Field(RoleType)

	def mutate(self,info,id,name):
		typrole = RoleType(name)
		Role_Type_D.Create(id,name)
		return CreateRoleType(typrole=typrole)

class CreateMembership(graphene.Mutation):
	class Arguments:
		id=graphene.Int()
		roleType = graphene.String()
		group = graphene.String()
		

	clenstvi = graphene.Field(Membership)

	def mutate(self,info,id,roleType,group):
		clenstvi = Membership(name)
		Membership_D.Create(id,roleType,group)
		return CreateMembership(clenstvi=clenstvi)

class UpdateUser(graphene.Mutation):
	class Arguments:
		id=graphene.Int()
		name = graphene.String()
		surname=graphene.String()

	uzivatel = graphene.Field(User)

	def mutate(self,info,id,name,surname):
		uzivatel=User(name)
		Person.Update(id,name,surname)
		return UpdateUser(uzivatel=uzivatel)

class UpdateGroup(graphene.Mutation):
	class Arguments:
		id=graphene.Int()
		name = graphene.String()
		groupType=graphene.String()
		

	skupina = graphene.Field(Group)

	def mutate(self,info,id,name,groupType):
		skupina = Group(name)
		Group_D.Update(id,name,groupType)
		return UpdateGroup(skupina=skupina)

class UpdateGroupType(graphene.Mutation):
	class Arguments:
		id=graphene.Int()
		name = graphene.String()
		

	typskupiny = graphene.Field(GroupType)

	def mutate(self,info,id,name):
		typskupiny = GroupType(name)
		Group_Type_D.Update(id,name)
		return UpdateGroupType(typskupiny=typskupiny)

class UpdateRoleType(graphene.Mutation):
	class Arguments:
		id=graphene.Int()
		name = graphene.String()
		

	typrole = graphene.Field(RoleType)

	def mutate(self,info,id,name):
		typrole = RoleType(name)
		Role_Type_D.Update(id,name)
		return UpdateRoleType(typrole=typrole)

class UpdateMembership(graphene.Mutation):
	class Arguments:
		id=graphene.Int()
		roleType = graphene.String()
		group = graphene.String()
		

	clenstvi = graphene.Field(Membership)

	def mutate(self,info,id,roleType,group):
		clenstvi = Membership(name)
		Membership_D.Update(id,roleType,group)
		return UpdateMembership(clenstvi=clenstvi)

class DeleteUser(graphene.Mutation):
	class Arguments:
		id=graphene.Int()

	uzivatel = graphene.Field(User)

	def mutate(self,info,id,):
		uzivatel=User(name)
		Person.Delete(id)
		return DeleteUser(uzivatel=uzivatel)

class DeleteGroup(graphene.Mutation):
	class Arguments:
		id=graphene.Int()
		
	skupina = graphene.Field(Group)

	def mutate(self,info,id):
		skupina = Group(name)
		Group_D.Delete(id)
		return DeleteGroup(skupina=skupina)

class DeleteGroupType(graphene.Mutation):
	class Arguments:
		id=graphene.Int()
		
	typskupiny = graphene.Field(GroupType)

	def mutate(self,info,id):
		typskupiny = GroupType(name)
		Group_Type_D.Delete(id)
		return DeleteGroupType(typskupiny=typskupiny)

class DeleteRoleType(graphene.Mutation):
	class Arguments:
		id=graphene.Int()
	
	typrole = graphene.Field(RoleType)

	def mutate(self,info,id):
		typrole = RoleType(name)
		Role_Type_D.Delete(id)
		return DeleteRoleType(typrole=typrole)

class DeleteMembership(graphene.Mutation):
	class Arguments:
		id=graphene.Int()

	clenstvi = graphene.Field(Membership)

	def mutate(self,info,id):
		clenstvi = Membership(name)
		Membership_D.Delete(id)
		return DeleteMembership(clenstvi=clenstvi)


class Mutations(graphene.ObjectType):
	create_user = CreateUser.Field()
	create_group = CreateGroup.Field()
	create_group_type=CreateGroupType.Field()
	create_role_type=CreateRoleType.Field()
	create_membership=CreateMembership.Field()
	update_user = UpdateUser.Field()
	update_group = UpdateGroup.Field()
	update_group_type=UpdateGroupType.Field()
	update_role_type=UpdateRoleType.Field()
	update_membership=UpdateMembership.Field()
	delete_user = DeleteUser.Field()
	delete_group=DeleteGroup.Field()
	delete_group_type=DeleteGroupType.Field()
	delete_role_type=DeleteRoleType.Field()
	delete_membership=DeleteMembership.Field()
schema = graphene.Schema(query=Query, mutation=Mutations)



