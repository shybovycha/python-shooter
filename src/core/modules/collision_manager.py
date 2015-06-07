class CollisionManager(object):
    """
        Class, managing all the collisions between Entities.
    """

    entities = []

    @classmethod
    def register(self, entity):
        """
            Add entity to be handled by collision manager.
        """

        self.entities.append(entity)

    @classmethod
    def unregister(self, entity):
        """
            Remove entity from collisions managing.
        """

        if entity in self.entities:
            self.entities.remove(entity)

    @classmethod
    def update(self):
        """
            Handles collisions between **different** entities.
            E. g., we entity can not collide with itself.
            Collision handler will be called on both entities collided.
        """

        for entity1 in self.entities:
            for entity2 in self.entities:
                if entity1 == entity2:
                    continue

                if entity1.check_collision(entity2):
                    entity1.on_hit_entity(entity2)
                    entity2.on_hit_entity(entity1)
