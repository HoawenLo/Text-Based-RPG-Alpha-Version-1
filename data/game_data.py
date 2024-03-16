from .items.item_data import item_database, item_utils
from .locations.all_locations import locations_database
from .player_mechanics.player_mechanics import Player

game_data = {"items":item_database, "locations":locations_database, "player":Player}

item_utils = item_utils
