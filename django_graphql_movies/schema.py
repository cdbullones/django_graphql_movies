import graphene
import graphql_jwt
import graphql_social_auth
import movies.schema
import users.schema

class Query(users.schema.Query, movies.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

class Mutation(users.schema.Mutation, movies.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    social_auth = graphql_social_auth.SocialAuthJWT.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)