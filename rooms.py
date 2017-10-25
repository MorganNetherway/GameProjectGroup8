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
        "description": "The tale of the Trojan Horse is well known. Betrayal is a common theme throughout history and myth. It appears you've found the one thing that you can always trust with your life: A sword.",
        "items": [item_sword],
        "action": "special_well"
    },
    "room_3": {
        "name": "CORRIDOR OF CHAOS ",
        "description": "The hallway shifts and turns dangerously, twisting into shapes that cut deep into your mind. Fortunately, the hallway appears too small for the Minotaur to fit through. However, a second ago you were walking on the ceiling, so who can be sure? The primogeniture of nothingness, Chaos was the first thing to exist. Perhaps this is the true center of the Labyrinth?",
        "items": "[item_gate_12_key]",
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
        "items": [item_diary_3],
        "action": None
    },
    "room_6": {
        "name": "TOMB OF THUNDER",
        "description": "You can hear thunder faintly booming in the distance. The calling card of Zeus, it's said that wherever the heavenly, sonorous rumblings occur, he swiftly follows. Maybe it represents his blessing? Maybe its his anger at the twisted, treacherous dealings that have happened here? Interpreting the will of the divine is a difficult task. Then again, so is slaying the Minotaur.",
        "items": [item_spear],
        "action": None
    },
    "room_7": {
        "name": "THE BASILISK NEST",
        "description": "When a rooster incubates an egg hatched by a snake, a Basilisk is born. A creature so cruel that it can kill merely with its baleful gaze. Stones crack under its foul breath, and plants wither upon its horrible touch. It only makes sense that such a horrible thing would reside in the Minotaur's prison. Maybe it was placed here as a guard, as surely if any creature could kill the Minotaur it would be this. This room, however, is as unassuming and regular as the Labyrinths halls. It appears to be empty.",
        "items": [item_scroll_attack],
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
        "items": [item_diary_4, item_scroll_speed],
        "action": None
    },
    "room_10": {
        "name": "MEDUSA’S CHAMBERS",
        "description": "Medusa the deadly gorgon, with serpents as locks of hair, and a stare with the ability to turn people to stone was beheaded by the demigod son of Zeus, called Perseus. Athena, goddess of wisdom and war, then placed the head of Medusa on her shield, as the ultimate defence from her enemies. However it was stolen by King Minos, through Poseidon who felt pity for the king after ruining his life as well as being the natural rival of Athena. Minos placed the head in the Labyrinth in the hope that one day the Minotaur or travellers would stumble across it and turn to stone. The room is filled with statues of your journeying predecessors. \n""",
        "items": [item_diary_5],
        "action": None
    },
    "room_11": {
        "name": "THE ROOM OF THE TITANS",
        "description": """The predecessors of the generation of the Olympian deities, were the Titans. Kronos, father of Zeus, Hades and Poseidon, was overthrown by his children just as he had overthrown his father, lord of the sky, Uranus. However the Titans seek revenge from Olympian gods, and King Minos’ vengeful nature agreed him to house the spirit of Kronos, in this chamber of the Labyrinth, where not even the gods could imagine he was hiding. Beware traveller, Kronos is the lord of time, and even setting foot in thisber without paying homage to the Titan would be foolish, as you could be trapped in a time loop within the deadly maze for eternity, not dying and simply being cham devoured by the Minotaur over and over till the end of time itself \n""",
        "items": "",
        "action": None
    },
    "room_12": {
        "name": "WAR ROOM",
        "description": """This room contains a bust of the god Ares, with a scroll contained in his mouth. Ares is the God of War. Not well liked in either Olympus or Earth, he has to resort to resort to more nefarious methods to keep followers. Basking in the chaos of battle, he approved of King Minos' Labyrinth, although rather wanted the Minotaur to be used as a living weapon. This room is dedicated to Ares; take up his blessing and you will be able to fight for longer. \n""",
        "items": [item_scroll_health, item_gate_11_key],
        "action": None
    },
    "room_13": {
        "name": "HOLE TO THE UNDERWORLD",
        "description": """Poseidon played a cruel joke on King Minos by making his wife fall in love with a Cretan Bull, however his brother Hades, Lord of the Underworld granted King Minos a favour by creating a direct fall for travellers who enter the Labyrinth straight to the underworld. Beware travellers, it is a literal pit that leads you to hell and if you ended up in the Labyrinth you will likely be devoured by the three headed dog of Hades, Cerberus or walk the Asphodel fields of punishment for eternity. \n""",
        "items": [item_diary_2],
        "action": None
    },
    "room_14": {
        "name": "TREASURE CHAMBER",
        "description": """Due to the appearance and ferocity of the beast, everyone forgets the fact that the Minotaur itself is half human. Humans crave wealth and power, every being that the half bull half man has devoured, all their personal possessions and gold have been stored as a trophy cabinet in the Labyrinth. King Minos himself has not forgotten to appease his half son by ladening the room with the finest antiquities fit for the gods themselves. A harsh light comes from above, and the treasure betrays an even more blinding glow. It seems unguarded, but your instincts tell you otherwise. When has wealth ever been easy to obtain? \n""",
        "items": [item_shield, item_gate_6_key],
        "action": None
    }
       "room_15": {
        "name": "Burial Chamber",
        "description": """A tiny burial chamber, with 2 main tombs. On one of the tombs is a hook for a key""",
        "items": [item_scroll_health],
        "description": """A tiny burial chamber, with 2 main tombs. On one of the tombs is a hook for a key""",
      }

