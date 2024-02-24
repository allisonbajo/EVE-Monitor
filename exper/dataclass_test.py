import json
from dataclasses import dataclass


@dataclass
class Blueprint:
    name: str
    outcome: str
    output: int
    materials: object

    @classmethod
    def from_json(cls, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        
        return cls(**data)


class Mineral:
    name: str
    region: str


if __name__ == '__main__':
    print('Load Blueprint')
    blueprint = Blueprint.from_json('./data/Blueprint 17482.json')
    print(blueprint.materials)
    for mineral in blueprint.materials['minerals']:
        print(mineral)

    #blueprint.output()