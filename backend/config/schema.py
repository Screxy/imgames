import graphene
import apps.users.schema
import apps.rooms.schema
import apps.organizations.schema
import apps.flows.schema


class Query(apps.users.schema.Query, apps.rooms.schema.Query, apps.organizations.schema.Query, apps.flows.schema.Query, graphene.ObjectType):
    pass


class Mutation(apps.users.schema.Mutation, apps.rooms.schema.Mutation, apps.organizations.schema.Mutation, apps.flows.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
