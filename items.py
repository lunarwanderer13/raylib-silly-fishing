from pyray import Color

class ItemRarity:
    def __init__(self, name: str, color: Color) -> None:
        self.name: str = name
        self.color: Color = color

class Item:
    item_type: str = "item"
    item_colors: list[Color] = [
        Color(72, 64, 71),
        Color(99, 83, 73),
        Color(63, 81, 49),
        Color(53, 95, 120),
        Color(119, 34, 26),
        Color(201, 113, 44),
        Color(209, 176, 68),
        Color(208, 208, 208),
    ]
    item_rarities: list[ItemRarity] = [
        ItemRarity("Junk", item_colors[0]),
        ItemRarity("Common", item_colors[1]),
        ItemRarity("Uncommon", item_colors[2]),
        ItemRarity("Rare", item_colors[3]),
        ItemRarity("Very Rare", item_colors[4]),
        ItemRarity("Epic", item_colors[5]),
        ItemRarity("Legendary", item_colors[6]),
        ItemRarity("Godly", item_colors[7]),
    ]

    def __init__(self, item_id: int, item_name: str, item_description: str, item_rarity: ItemRarity | str, item_properties: dict[str, str] | None = None) -> None:
        self.item_id: int = item_id
        self.item_name: str = item_name
        self.item_description: str = item_description
        self.item_properties: dict[str, str] = item_properties or {}

        if isinstance(item_rarity, ItemRarity):
            self.item_rarity: ItemRarity = item_rarity
        else:
            self.item_rarity: ItemRarity = next((v for v in self.item_rarities if v.name == item_rarity), self.item_rarities[0])

class Tool(Item):
    item_type: str = "tool"
    tool_tiers: list[str] = [
        "Old",
        "Beginner's",
        "Novice's",
        "Adept's",
        "Expert's",
        "Master's",
        "Grandmaster's",
        "Elder's",
    ]

    def __init__(self, item_id: int, item_name: str, item_description: str, item_tier: int, item_properties: dict[str, str] | None = None) -> None:
        self.item_tier: str = self.tool_tiers[item_tier - 1]
        super().__init__(item_id, f"{self.item_tier} {item_name}", item_description, self.item_rarities[item_tier], item_properties or {})

    def use(self) -> None:
        print(f"Used {self.item_name}")

class Rod(Tool):
    item_type: str = "rod"

    def __init__(self, item_id: int, item_description: str, item_tier: int, item_properties: dict[str, str] | None = None) -> None:
        super().__init__(item_id, self.item_type.capitalize(), item_description, item_tier, item_properties or {})

    def use(self) -> None:
        pass

class Bait(Tool):
    item_type: str = "bait"

    def __init__(self, item_id: int, item_description: str, item_tier: int, item_properties: dict[str, str] | None = None) -> None:
        super().__init__(item_id, self.item_type.capitalize(), item_description, item_tier, item_properties or {})

    def use(self) -> None:
        pass

class Fish(Item):
    item_type: str = "fish"

item_index: list[Item] = [
    Item(0,
         "The Guide",
         "A guide passed through generations of fishermen, now in your hands.",
         "Very Rare",
         {
             "unsellable": "Unsellable",
         }),
    Rod(1,
        "An old, dusty stick with some string tied to it.",
        1,
         {
             "catch_strength": "0.50",
             "catch_speed": "0.50",
             "equippable": "Equippable",
             "unsellable": "Unsellable",
         }),
    Rod(2,
        "A worn down rod with some cracks and tape on it.",
        2,
         {
             "catch_strength": "0.75",
             "catch_speed": "0.75",
             "equippable": "Equippable",
             "unsellable": "Unsellable",
         }),
    Rod(3,
        "A basic rod, gets the job done.",
        3,
         {
             "catch_strength": "1.00",
             "catch_speed": "1.00",
             "equippable": "Equippable",
             "unsellable": "Unsellable",
         }),
    Rod(4,
        "A decent rod, nothing special.",
        4,
         {
             "catch_strength": "1.25",
             "catch_speed": "1.25",
             "equippable": "Equippable",
             "unsellable": "Unsellable",
         }),
    Rod(5,
        "A nice rod, bends easily.",
        5,
         {
             "catch_strength": "1.50",
             "catch_speed": "1.50",
             "equippable": "Equippable",
             "unsellable": "Unsellable",
         }),
    Rod(6,
        "A great rod, looks brand new.",
        6,
         {
             "catch_strength": "1.75",
             "catch_speed": "1.75",
             "equippable": "Equippable",
             "unsellable": "Unsellable",
         }),
    Rod(7,
        "An amazing rod, both looks and feels great.",
        7,
         {
             "catch_strength": "2.00",
             "catch_speed": "2.00",
             "equippable": "Equippable",
             "unsellable": "Unsellable",
         }),
    Rod(8,
        "A rod only known from legends and myths, made from the remains of a huge ocean creature.",
        8,
         {
             "catch_strength": "2.50",
             "catch_speed": "2.50",
             "equippable": "Equippable",
             "unsellable": "Unsellable",
         }),
    Bait(9,
         "A bunch of old worms bound together.",
         1,
         {
             "catch_rate": "1.10",
             "catch_value": "1.10",
             "uses_left": "5",
             "equippable": "Equippable",
             "unsellable": "Unsellable",
         }),
    Bait(10,
         "A half-empty can of dead worms.",
         2,
         {
             "catch_rate": "1.20",
             "catch_value": "1.20",
             "uses_left": "10",
             "equippable": "Equippable",
             "unsellable": "Unsellable",
         }),
    Bait(11,
         "A small box full of tiny worms and random veggies.",
         3,
         {
             "catch_rate": "1.30",
             "catch_value": "1.30",
             "uses_left": "25",
             "equippable": "Equippable",
             "unsellable": "Unsellable",
         }),
    Bait(12,
         "A plastic plate with red worms.",
         4,
         {
             "catch_rate": "1.40",
             "catch_value": "1.40",
             "uses_left": "50",
             "equippable": "Equippable",
             "unsellable": "Unsellable",
         }),
    Bait(13,
         "A metal box filled with all kinds of worms.",
         5,
         {
             "catch_rate": "1.50",
             "catch_value": "1.50",
             "uses_left": "75",
             "equippable": "Equippable",
             "unsellable": "Unsellable",
         }),
    Bait(14,
         "A bucket with both all kinds of worms and veggies, kinda heavy.",
         6,
         {
             "catch_rate": "1.60",
             "catch_value": "1.60",
             "uses_left": "100",
             "equippable": "Equippable",
             "unsellable": "Unsellable",
         }),
    Bait(15,
         "A small fridge filled with all kinds of amateur and professional bait.",
         7,
         {
             "catch_rate": "1.80",
             "catch_value": "1.80",
             "uses_left": "500",
             "equippable": "Equippable",
             "unsellable": "Unsellable",
         }),
    Bait(16,
         "A bottomless can filled with algae and small fish from the ocean floor, mostly undiscovered species.",
         8,
         {
             "catch_rate": "2.00",
             "catch_value": "2.00",
             "uses_left": "-1",
             "equippable": "Equippable",
             "unsellable": "Unsellable",
         }),
]
