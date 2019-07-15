import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model

class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class Query(graphene.ObjectType):
    user = graphene.Field(UserType)
    users = graphene.List(UserType)

    def resolve_users(self, info):
        return get_user_model().objects.all()

    def resolve_user(self, info):
        user = info.context.user

        if user.is_anonymous:
            raise Exception('Not logged!')
        return user

class UserInput(graphene.InputObjectType):
    username = graphene.String()
    password = graphene.String()
    email = graphene.String()


class CreateUser(graphene.Mutation):
    class Arguments:
        input = UserInput(required=True)

    ok = graphene.Boolean()
    user = graphene.Field(UserType)

    def mutate(self, info, input):
        print("INPUT: " + str(input.email))
        ok = True
        user_instance = get_user_model()(
            username=input["username"],
            email=input["email"]
        )
        user_instance.set_password(input["password"])
        user_instance.save()

        return CreateUser(ok=ok, user=user_instance)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()