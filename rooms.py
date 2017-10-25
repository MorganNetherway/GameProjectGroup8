from items import *
#########################################################################################################
#                Somebody needs to finish this ASAP. This isn't hard, just time consuming               #
#########################################################################################################
rooms = {
    "room_1": {
        "name": "GENESIS GARDEN",
        "description": '''This room is damp and humid, small flowers of red pushing through the carpet of viscera covering the floor. The air is almost suffocating. The Minotaur was born from Minos' wife bedding a bull. His appetite grew too fast, and he began to consume humans for sustenance. Locked away in the Labyrinth, the Minotaur still hungers. A cruel plague befell Athens as recompense for the murder of King Minos' son, the only cure being seven Athenian youths and seven Athenian maidens sacrificed, fated to being devoured by the Minotaur. Commit that sordid abominaiton to his final resting place, and put an end to all this.''',
        "items": "",
        "action": None
    },
    "room_2": {
        "name": "THE TROJAN HORSE",
        "description": "The bane of Troy.",
        "items": [item_sword],
        "action": "special_well"
    },
    "room_3": {
        "name": "CORRIDOR OF CHAOS ",
        "description": "Definitely no Minotaurs here.",
        "items": "",
        "action": None
    },
    "room_4": {
        "name": "WELL OF DELPHI",
        "description": "Built at the behest of the Pythia, this chamber divinely channels a presence from the Oracle of Delphi herself. Known as a giver of prophecies, her ecstatic ravings were translated by priests into holy poems. Unfortunately, there doesn't seem to be a priest in sight. Most considered the fallibility of the Pythia to be fact. How can the sacred be wrong? Perhaps we simply lack the knowledge to fully understand her.",
        "items": "",
        "action": None
    },
    "room_5": {
        "name": "MIDAS TOUCH",
        "description": "Don't touch anything you don't want turning into SOLID GOLD.",
        "items": "",
        "action": None
    },
    "room_6": {
        "name": "TOMB OF THUNDER",
        "description": "You can hear thunder faintly booming in the distance. The calling card of Zeus, it's said that wherever the heavenly, sonorous rumblings occur, he swiftly follows. Maybe it represents his blessing? Maybe its his anger at the twisted, treacherous dealings that have happened here? Interpreting the will of the divine is a difficult task. Then again, so is slaying the Minotaur.",
        "items": "",
        "action": None
    },
    "room_7": {
        "name": "THE BASILISK NEST",
        "description": "When a rooster incubates an egg hatched by a snake, a Basilisk is born. A creature so cruel that it can kill merely with its baleful gaze. Stones crack under its foul breath, and plants wither upon its horrible touch. It only makes sense that such a horrible thing would reside in the Minotaur's prison. Maybe it was placed here as a guard, as surely if any creature could kill the Minotaur it would be this. This room, however, is as unassuming and regular as the Labyrinths halls. It appears to be empty.",
        "items": "",
        "action": None
    },
    "room_8": {
        "name": "PROMETHEUS' LAIR",
        "description": "Prometheus was the Titan who created mankind, and our greatest ally. Avoiding the climactic Titanomachy, and therefore surviving the subsequent banishment of Titans to the depths of Tartarus, he lived to struggle against Zeus in future confrontations. He stole fire from Zeus after it was wrongfully taken from mankind, and in return was chained to a rock while an eagle came daily to eat his liver. As Prometheus is immortal, this lasted until the hero Heracles came and freed him. How King Minos obtained that rock is certainly a mystery.",
        "items": "",
        "action": None
    },
    "room_9": {
        "name": "SHRINE OF HYPERION",
        "description": "This room is covered in glittering, tiny dots, set across a darker, nearly black stone. Some believe in The Harmony of the Spheres, which is the idea that the cosmos are music. They give off a song that we can't pick up on, as we have heard it from birth. What, then, would that make the songs we sing? You listen closely, and notice the dots give off a slight noise, like the humming of a bee. ",
        "items": "",
        "action": None
    },
    "room_10": {
        "name": "MEDUSA’S CHAMBERS",
        "description": "Medusa the deadly gorgon, with serpents as locks of hair, and a stare with the ability to turn people to stone was beheaded by the demigod son of Zeus, called Perseus. Athena, goddess of wisdom and war, then placed the head of Medusa on her shield, as the ultimate defence from her enemies. However it was stolen by King Minos, through Poseidon who felt pity for the king after ruining his life as well as being the natural rival of Athena. Minos placed the head in the Labyrinth in the hope that one day the Minotaur or travellers would stumble across it and turn to stone. The room is filled with statues of your journeying predecessors. """,
        "items": "",
        "action": None
    },
    "room_11": {
        "name": "THE ROOM OF THE TITANS",
        "description": """The predecessors of the generation of the Olympian deities, were the Titans. Kronos, father of Zeus, Hades and Poseidon, was overthrown by his children just as he had overthrown his father, lord of the sky, Uranus. However the Titans seek revenge from Olympian gods, and King Minos’ vengeful nature agreed him to house the spirit of Kronos, in this chamber of the Labyrinth, where not even the gods could imagine he was hiding. Beware traveller, Kronos is the lord of time, and even setting foot in thisber without paying homage to the Titan would be foolish, as you could be trapped in a time loop within the deadly maze for eternity, not dying and simply being cham devoured by the Minotaur over and over till the end of time itself""",
        "items": "",
        "action": None
    },
    "room_12": {
        "name": "FOUNTAIN OF DELPHI",
        "description": """This chamber is an interesting one, one shall not pass without receiving a riddle from the prophecy giver the Oracle of Delphi herself. Beware traveller, she can hear your thoughts and play on your inner most secrets, physically you must be up to the task of beating the Minotaur, but mentally it is this chamber which you must overcome, stay clear of the green light and navigate carefully around the marble fountain, voices will be heard.""",
        "items": "",
        "action": None
    },
    "room_13": {
        "name": "HOLE TO THE UNDERWORLD",
        "description": """Poseidon played a cruel joke on King Minos by making his wife fall in love with a Cretan Bull, however his brother Hades, Lord of the Underworld granted King Minos a favour by creating a direct fall for travellers who enter the Labyrinth straight to the underworld. Beware travellers, it is a literal pit that leads you to hell and if you ended up in the Labyrinth you will likely be devoured by the three headed dog of Hades, Cerberus or walk the Asphodel fields of punishment for eternity.""",
        "items": "",
        "action": None
    },
    "room_14": {
        "name": "TREASURE CHAMBER",
        "description": """Due to the appearance and ferocity of the beast, everyone forgets the fact that the Minotaur itself is half human. Humans crave wealth and power, every being that the half bull half man has devoured, all their personal possessions and gold have been stored as a trophy cabinet in the Labyrinth. King Minos himself has not forgotten to appease his half son by ladening the room with the finest antiquities fit for the gods themselves. A harsh light comes from above, and the treasure betrays an even more blinding glow. It seems unguarded, but your instincts tell you otherwise. When has wealth ever been easy to obtain?""",
        "items": "",
        "action": None
    }
}

