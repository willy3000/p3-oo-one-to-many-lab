class Pet:
    pass

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Invalid pet: must be an instance of Pet")
        self._pets.append(pet)
        pet.set_owner(self)

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)

class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        if pet_type not in self.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}")
        self.owner = owner
        if owner:
            owner.add_pet(self)

    def set_owner(self, owner):
        self.owner = owner