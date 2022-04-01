import graphene
import apps.users.schema
import apps.rooms.schema
import apps.organizations.schema
import apps.flows.schema
import apps.computed.schema


class Query(apps.users.schema.Query, apps.rooms.schema.Query, apps.organizations.schema.Query, apps.flows.schema.Query, apps.computed.schema.Query, graphene.ObjectType):
    pass


class Mutation(apps.users.schema.Mutation, apps.rooms.schema.Mutation, apps.organizations.schema.Mutation, apps.flows.schema.Mutation, graphene.ObjectType):
    pass


class Subscription(apps.rooms.schema.Subscription):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation,
                         subscription=Subscription)
