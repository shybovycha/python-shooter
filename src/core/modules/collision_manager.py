class CollisionManager(object):
    """
        Class, managing all the collisions between Entities.
    """

    entities = []

    @classmethod
    def clear(cls):
        """
            Resets collisions
        """

        cls.entities = []

    @classmethod
    def register(cls, entity):
        """
            Add entity to be handled by collision manager.
        """

        cls.entities.append(entity)

    @classmethod
    def unregister(cls, entity):
        """
            Remove entity from collisions managing.
        """

        if entity in cls.entities:
            cls.entities.remove(entity)

    @classmethod
    def update(cls):
        """
            Handles collisions between **different** entities.
            E. g., we entity can not collide with itself.
            Collision handler will be called on both entities collided.
        """

        for entity1 in cls.entities:
            for entity2 in cls.entities:
                if entity1 == entity2:
                    continue

                if entity1.check_collision(entity2):
                    entity1.on_hit_entity(entity2)
                    entity2.on_hit_entity(entity1)
