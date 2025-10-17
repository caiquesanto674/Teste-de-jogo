from dataclasses import dataclass

@dataclass(frozen=True)
class Position:
    x: int
    y: int

class GameMap:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = {}

    def add_entity(self, entity, position: Position):
        self.grid[position] = entity
        entity.position = position

    def move_entity(self, entity, new_position: Position):
        old_position = entity.position
        if old_position in self.grid:
            del self.grid[old_position]
        self.grid[new_position] = entity
        entity.position = new_position

    def get_distance(self, pos1: Position, pos2: Position) -> float:
        return ((pos1.x - pos2.x) ** 2 + (pos1.y - pos2.y) ** 2) ** 0.5