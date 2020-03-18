import graphene
# from graphql import GraphQLError

from graphene_django.types import DjangoObjectType
from collegeapp.models import University, Student


class StudentType(DjangoObjectType):
    class Meta:
        model = Student


class UniversityType(DjangoObjectType):
    class Meta:
        model = University


class Query(object):
    students = graphene.List(StudentType)
    universities = graphene.List(UniversityType)
    student = graphene.Field(StudentType, id=graphene.Int())
    university = graphene.Field(UniversityType, id=graphene.Int())

    def resolve_students(self, info, **kwargs):
        return Student.objects.all()

    def  resolve_universities(self, info, **kwargs):
        return University.objects.all()

    def resolve_student(self, info, **kwargs):
        id =  kwargs.get('id')

        if id is not None:
            return Student.objects.get(pk=id)
        
        return None

    def resolve_university(self, info, **kwargs):
        id = kwargs.get('id')

        if id  is not None:
            return University.objects.get(pk=id)

        return None


# mutations
#shows which fields used to change data
class StudentInput(graphene.InputObjectType):
    id = graphene.ID()
    first_name = graphene.String()
    last_name = graphene.String()

class UniversityInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()


#creating mutations for create  data
#class CreateStudent(graphene.Mutation):
