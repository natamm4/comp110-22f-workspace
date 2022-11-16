"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730557757"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other: Point) -> int:
        """Returns distance between Point (called on by method) and another Point (parameter)."""
        length: int = sqrt(((other.x - self.x) ** 2 + (other.y - self.y) ** 2))
        return length


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def tick(self) -> None:
        """Reassign the object's location attribute the result of adding the self object's location with its direction. Hint: Look at the add method."""
        self.location = self.location.add(self.direction)
        if self.is_infected() is True:
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()

    def contract_disease(self) -> None:
        """Assign INFECTED to sickness attribute of Cell."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """True if Cell is vulnerable."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False

    def is_infected(self) -> bool:
        """True if Cell is infected."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False

    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_vulnerable() is True:
            return "gray"
        if self.is_infected() is True:
            return "red"
        if self.is_immune() is True:
            return "blue"

    def contact_with(self, other: Cell) -> None:
        """When two Cells make contact, if one is infected and the other is vulnerable, then the other should become infected."""
        if self.is_infected() is True and other.is_vulnerable() is True:
            other.contract_disease()
        if self.is_vulnerable() is True and other.is_infected() is True:
            self.contract_disease()

    def immunize(self) -> None:
        """Assigns the constant IMMUNE to the sickness attribute of the Cell."""
        self.sickness = constants.IMMUNE

    def is_immune(self) -> bool:
        """Returns True when the Cell's sickness is equal to IMMUNE."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infections: int, immunes: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []
        if infections >= cells or infections <= 0:
            raise ValueError("Some number of the Cell objects must begin infected.")
        if immunes >= cells or (immunes + infections) > cells or immunes < 0:
            raise ValueError("Number of immune cells exceeds number of Cell objects.")
        
        for _ in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
        for cell in range(infections):
            self.population[cell].sickness = 1
        for cell in range(immunes):
            self.population[cell].sickness = -1

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for cell in self.population:
            if cell.is_infected():
                return False
        return True

    def check_contacts(self) -> None:
        """Compare the distance between every pair of cells. If any distance is less than CELL_RADIUS, call Cell#contact_with on one of the cells."""
        for cell in self.population:
            next: int = self.population.index(cell) + 1
            for i in range(next, (len(self.population) - 1)):
                length: int = cell.location.distance(self.population[i].location)
                if length < constants.CELL_RADIUS:
                    cell.contact_with(self.population[i])
