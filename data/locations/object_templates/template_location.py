# template location

class Location():

    def __init__(self):
        
        self.all_areas = {}

    def create_area(self, area_name, move_areas, quests, interactions, npcs):
        """Create a new area within a location. The new area will be an attribute
        of the Location class.
        
        Args:
            area_name: The name of area as a string.
            move_areas: A list of the areas that can be moved to.
            quests: A list of the quests available in the area.
            interactions: A list of the interactions available in the area.
            npcs: A list of the npcs available in the area.
            
        Returns:
            None"""
        
        if not isinstance(area_name, str):
            raise TypeError(f"Input area_name is not string datatype, area_name is type {type(area_name)}.")
        if not isinstance(move_areas, list):
            raise TypeError(f"Input move_areas is not list datatype, move_areas is type {type(move_areas)}.")
        if not isinstance(quests, list):
            raise TypeError(f"Input quests is not list datatype, quests is type {type(quests)}.")
        if not isinstance(interactions, list):
            raise TypeError(f"Input interactions is not list datatype, interactions is type {type(interactions)}.")
        if not isinstance(npcs, list):
            raise TypeError(f"Input npcs is not list datatype, npcs is type {type(npcs)}.")
        if len(interactions) > 5:
            raise ValueError(f"Length of interactions is greater than 5. Length of interactions is {len(interactions)}.")

        interactions_front = ["Available interactions: "]
        interactions_template = interactions_front + interactions

        area_data = {"areas":move_areas,
                     "quests":quests, 
                     "interactions":interactions_template, 
                     "npcs":npcs}
        
        setattr(self, area_name, area_data)
        area_val = getattr(self, area_name)
        self.add_area_to_master(area_val, area_name)
    
    def add_area_to_master(self, area_val, area_name):
        """Add an area to the all_areas dictionary which contains a dictionary to access
        all areas in a location.
        
        Args:
            area_val: The area data as an attribute of the location class.
            area_name: The name of the area as a string.
            
        Returns:
            None"""

        self.all_areas[area_name] = area_val

