"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    # Class attribute: shared across all Alien instances to track total count
    total_aliens_created = 0

    def __init__(self, x_coordinate, y_coordinate):
        # Instance attributes: unique to each alien object
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

        # Use Alien.total_aliens_created (class attribute) not self.total_aliens_created
        # If we used self., it would create an instance attribute shadowing the class one
        Alien.total_aliens_created += 1

        # Health is per-instance, not shared (each alien has its own health)
        self.health = 3

    def hit(self):
        # Decrement this specific alien's health by 1
        # Note: Health can go below 0, which is valid per test requirements
        self.health -= 1

    def is_alive(self):
        # Returns True if health > 0, False otherwise (0 or negative)
        return self.health > 0

    def teleport(self, x, y):
        # Update coordinates to new position
        self.x_coordinate = x
        self.y_coordinate = y

    def collision_detection(self, other):
        # Stub method - to be implemented later
        # 'other' parameter accepts another object (likely another Alien)
        # Currently returns None as per requirements
        pass


def new_aliens_collection(positions):
    # List comprehension creates Alien objects from list of (x, y) tuples
    # Example: positions=[(1, 2), (3, 4)] creates [Alien(1, 2), Alien(3, 4)]
    return [Alien(x, y) for x, y in positions]
