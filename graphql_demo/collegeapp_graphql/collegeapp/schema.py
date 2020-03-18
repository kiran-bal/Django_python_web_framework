import graphene
from graphql import GraphQLError
from graphene_django.types import DjangoObjectType
from collegeapp.models import University, Student

# Type creation for student class
class StudentType(DjangoObjectType):
    class Meta:
        model = Student

# Type creation for University Class
class UniversityType(DjangoObjectType):
    class Meta:
        model = University


class Query(object):
    """ Creating Query class which helps to query students and university
        as whole or seperately using  id of the class. variables defined
        below  will be the keywords used to query in graphiql interface
        and followed  by functions to resolve each query
    """
    students = graphene.List(StudentType)
    universities = graphene.List(UniversityType)
    student = graphene.Field(StudentType, id=graphene.Int())
    university = graphene.Field(UniversityType, id=graphene.Int())

    def resolve_students(self, info, **kwargs):
        return Student.objects.all()

    def resolve_universities(self, info, **kwargs):
        return University.objects.all()

    def resolve_student(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Student.objects.get(pk=id)
        return None

    def resolve_university(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return University.objects.get(pk=id)
        return None


## Mutations starts here ##
class UniversityInput(graphene.InputObjectType):
    """Defines which variables used to change data"""
    id = graphene.ID()
    name = graphene.String()


class StudentInput(graphene.InputObjectType):
    """Defines which variables used to change data"""
    id = graphene.ID()
    first_name = graphene.String()
    last_name = graphene.String()
    university = graphene.List(UniversityInput)


# creating mutations for creating and updating
class CreateUniversity(graphene.Mutation):
    """ Class to add new University data in the model"""
    class Arguments:
        input = UniversityInput(required=True)

    ok = graphene.Boolean()
    university = graphene.Field(UniversityType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        university_instance = University(name=input.name)
        university_instance.save()
        return CreateUniversity(ok=ok, university=university_instance)


class UpdateUniversity(graphene.Mutation):
    """ Class to update existing University data
        in the model using id
    """
    class Arguments:
        id = graphene.Int(required=True)
        input = UniversityInput(required=True)

    ok = graphene.Boolean()
    university = graphene.Field(UniversityType)

    @staticmethod
    def mutate(self, info, id, input=None):
        ok = False
        university_instance = University.objects.get(pk=id)
        if university_instance:
            ok = True
            university_instance.name = input.name
            university_instance.save()
            return UpdateUniversity(ok=ok, university=university_instance)
        return UpdateUniversity(ok=ok, university=None)


# reflecting the changes
class Mutation(graphene.ObjectType):
    """ Class to create mutations and update the models"""
    create_university = CreateUniversity.Field()
    update_university = UpdateUniversity.Field()

## Mutations ends here ##
