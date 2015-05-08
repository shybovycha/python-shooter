class CollisionManager(object):
    entities = []

    @classmethod
    def register(klass, entity):
        klass.entities.append(entity)

    @classmethod
    def unregister(klass, entity):
        klass.entities.remove(entity)

    @classmethod
    def update(klass):
        for entity1 in klass.entities:
            for entity2 in klass.entities:
                if entity1 == entity2:
                    continue

                if entity1.check_collision(entity2):
                    entity1.on_hit_entity(entity2)
                    entity2.on_hit_entity(entity1)
