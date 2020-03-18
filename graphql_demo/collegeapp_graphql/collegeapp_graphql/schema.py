import graphene

import collegeapp.schema

class Query(collegeapp.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)