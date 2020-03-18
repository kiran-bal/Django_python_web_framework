import graphene
import collegeapp.schema

# Importing the Query objects from inner schema
class Query(collegeapp.schema.Query, graphene.ObjectType):
    pass

# Importing the mutation objects from inner schema
class Mutation(collegeapp.schema.Mutation, graphene.ObjectType):
    pass


#Applying the inner schema to reference in the settings 
schema = graphene.Schema(query=Query, mutation=Mutation)
