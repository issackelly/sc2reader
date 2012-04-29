# TODO: Handle Cancels better
# TODO: Handle transport abilities (load, unload) better. Need disambiguation.
# TODO: There are other disambigution problems, Gather Resources for example
# TODO: Handle build addon in target location ability better
# TODO: Add hallucinated units, resources, critters, destructibles, and alt changeling forms
# TODO: Map Hallucination to Hallucinated equivalents
# TODO: Add attacker and mover flags in, probably via big sets
#
# There are probably more issues here...

import json, re
from sc2reader import graham_data

# Ordered Dicts preserver serialized key-value order
# for readability and ease if editing (via grouping)
from collections import OrderedDict

def fix_name(name):
    name = ''.join(word[0].upper()+word[1:] for word in name.split('_'))
    # I know this is terrible, but it was easy
    name = name.replace('ResearchArmSilo','ArmSilo')
    return name

protoss_units = set(['Probe','Zealot','Stalker','Sentry','HighTemplar','DarkTemplar','Archon','WarpPrism','WarpPrismPhasing','Voidray','Pheonix','Colossus','Carrier','Intercepter','Observer','Mothership','Immortal','Pylon','Assimilator','PhotonCannon','Nexus','Gateway','WarpGate','Forge','CyberneticsCore','RoboticsFacility','RoboticsBay','Stargate','DarkShrine','TwilightCouncil','FleetBeacon','TemplarArchives'])
terran_units = set(['SCV','SensorTower','MissileTurret','Refinery','Techlab','Reactor','MULE','Marine','Marauder','Ghost','SiegeTank','SiegeTankSieged','Reaper','Hellion','Thor','Viking','VikingAssault','Medivac','Raven','AutoTurret','PointDefenceDrone','Banshee','Battlecruiser','CommandCenter','CommandCenterFlying','OrbitalCommand','OrbitalCommandFlying','PlanetaryFortress','SupplyDepot','SupplyDepotLowered','EngineeringBay','GhostAcademy','FusionCore','Bunker','Armory','Barracks','BarracksTechlab','BarracksReactor','BarracksFlying','Factory','FactoryTechlab','FactoryReactor','FactoryFlying','Starport','StarportTechlab','StarportReactor','StarportFlying'])
zerg_units = set(['Larva','Egg','Drone','DroneBurrowed','Queen','QueenBurrowed','Mutalisk','Zergling','ZerglingBurrowed','ZerglingBanelingCocoon','Baneling','BanelingBurrowed','Roach','RoachBurrowed','Hydralisk','HydraliskBurrowed','Changeling','Infestor','InfestorBurrowed','Ultralisk','UltraliskBurrowed','InfestedTerran','InfestedTerranBurrowed','InfestedTerranEgg','Corruptor','CurruptorBroodlord','CorruptorBroodlordCocoon','Broodling','Overlord','Overseer','OverlordOverseerCocoon','Changeling','NydusWorm','SpineCrawler','SpineCrawlerUprooted','SporeCrawler','SporeCrawlerUprooted','Extractor','Hatchery','Lair','Hive','SpawningPool','EvolutionChamber','RoachWarren','BanelingNest','CreepTumor','CreepTumorBurrowed','HydraliskDen','InfestationPit','NydusNetwork','Spire','GreaterSpire','UltraliskCavern'])

buildings = set(['Pylon','Assimilator','PhotonCannon','Nexus','Gateway','WarpGate','Forge','CyberneticsCore','RoboticsFacility','RoboticsBay','Stargate','DarkShrine','TwilightCouncil','FleetBeacon','TemplarArchives','SensorTower','MissileTurret','Refinery','Techlab','Reactor','CommandCenter','CommandCenterFlying','OrbitalCommand','OrbitalCommandFlying','PlanetaryFortress','SupplyDepot','SupplyDepotLowered','EngineeringBay','GhostAcademy','FusionCore','Bunker','Armory','Barracks','BarracksTechlab','BarracksReactor','BarracksFlying','Factory','FactoryTechlab','FactoryReactor','FactoryFlying','Starport','StarportTechlab','StarportReactor','StarportFlying','NydusWorm','SpineCrawler','SpineCrawlerUprooted','SporeCrawler','SporeCrawlerUprooted','Extractor','Hatchery','Lair','Hive','SpawningPool','EvolutionChamber','RoachWarren','BanelingNest','HydraliskDen','InfestationPit','NydusNetwork','Spire','GreaterSpire','UltraliskCavern'])
research_buildings = set(['EngineeringBay','GhostAcademy','FusionCore','Armory','Forge','CyberneticsCore','TwilightCouncil','FleetBeacon','TemplarArchives','RoboticsBay','EvolutionChamber','SpawningPool','RoachWarren','BanelingNest','HydraliskDen','InfestationPit','Spire','GreaterSpire','UltraliskCavern','BarracksTechlab','StarportTechlab','FactoryTechlab','Hatchery','Lair','Hive'])
main_buildings = set(["CommandCenter","Nexus","Hatchery","Lair","Hive","OrbitalCommand","OrbitalCommandFlying","CommandCenterFlying","PlanetaryFortress"])

non_zerg_bio = set(['Zealot','DarkTemplar','HighTemplar','SCV','Marine','Marauder','Reaper','Ghost'])

attackers = ((protoss_units | terran_units | zerg_units) - buildings - set(['Infestor','InfestorBurrowed','HighTemplar','WarpPrism','WarpPrismPhasing','Medivac','Overlord','Overseer','Observer','Raven','Changeling','MULE','ZerglingBurrowed','UltraliskBurrowed','HydraliskBurrowed','QueenBurrowed','DroneBurrowed'])) | set(['SpineCrawler','SporeCrawler','Bunker','PhotonCannon','MissileTurret'])
moveables = ((protoss_units | terran_units | zerg_units) - buildings - set(['WarpPrismPhasing','BanelingBurrowed','ZerglingBurrowed','UltraliskBurrowed','HydraliskBurrowed','QueenBurrowed','DroneBurrowed','SiegeTankSieged'])) | set (['SporeCrawlerUprooted','SpineCrawlerUprooted','FactoryFlying','StarportFlying','BarracksFlying','CommandCenterFlying','OrbitalCommandFlying'])

def add_abilities(out, unit, unit_name=None):

    for key, item in unit.abilities.iteritems():

        if hasattr(item, "code"):
            add_unit(out, item, unit_name+'_'+key)

        elif "code" in item:
            if item['name'][:11]=='right_click':
                continue

            ability_name = fix_name(item['name'])

            if ability_name == 'ArmSiloWNuke':
                ability_name = 'ArmSilo'
            elif ability_name != 'WarpPrism' and ability_name[:4] == 'Warp':
                ability_name = 'WarpIn'+ability_name[4:]

            ability = OrderedDict(
                uid=ability_name,
                vid=ability_name,
                title=ability_name
            )

            if re.search('Burrow|Unburrow|Land|Lift|Uproot|Root|Addon|Load|Unload|Gather',ability_name):
                ability_name += unit_name
                ability['vid'] = ability_name

            if 'gas' in item:
                ability['gas'] = item['gas']
            if 'min' in item:
                ability['minerals'] = item['min']
            if 'time' in item:
                ability['build_time'] = item['time']
            if 'supply' in item:
                ability['supply'] = item['supply']

            if ability_name[:10] == "RightClick":
                prefix = ''

            elif re.search('hallucinate', ability_name.lower()):
                ability['energy'] = 100
                ability['build'] = True
                ability['build_unit'] = ability_name[11:]

            elif re.search('cancel', ability_name.lower()):
                ability['cancel'] = True

            elif unit_name in set(research_buildings) and ability_name[:4]!="Halt":
                ability['research'] = True
                prefix = "Research" if unit_name not in zerg_units else "Evolve"
                ability_name = prefix+ability['uid']
                ability['uid'] = prefix+ability['uid']
                ability['vid'] = prefix+ability['vid']
                ability['title'] = prefix+" "+ability['title']

            elif set(item.keys()) & set(['gas','min','time','supply']):
                ability['build'] = True
                ability['build_unit'] = ability_name
                if unit_name == 'WarpGate':
                    prefix = 'WarpIn'
                elif unit_name == 'Probe':
                    prefix = 'WarpIn'
                elif unit_name in ('Larva','Drone','Zergling','Overlord','Corruptor','Hatchery','Lair') :
                    prefix = 'MorphTo'
                elif unit_name in ('Barracks','CommandCenter','OrbitalCommand','PlanetaryFortress'):
                    if ability_name[:9] == 'UpgradeTo':
                        prefix = ''
                        ability['build_unit'] = ability_name[9:]
                    elif ability_name[:5] == 'Addon':
                        prefix = 'Build'
                        ability['build_unit'] = ability_name[5:]
                    else:
                        prefix = 'Train'
                else:
                    prefix = 'Build'

                ability_name = prefix+ability['uid']
                ability['uid'] = prefix+ability['uid']
                ability['vid'] = prefix+ability['vid']
                ability['title'] = prefix+" "+ability['title']

            elif ability_name == 'Changeling':
                ability['energy'] = 50
                ability['build'] = True
                ability['build_unit'] = 'Changeling'
                prefix = 'Spawn'
                ability_name = prefix+ability['uid']
                ability['uid'] = prefix+ability['uid']
                ability['vid'] = prefix+ability['vid']
                ability['title'] = prefix+" "+ability['title']

            ability['title'] = ' '.join(re.findall('[A-Z]+[a-z]*[0-9]?',ability['title']))
            code = item['code'] or sum(ord(a) for a in str(ability_name))*-1
            out['abilities'][code] = ability

            if hasattr(unit, "code"):
                out['objects'][unit.code]['abilities'].append(ability_name)

        else:
            print "Skipped "+str(key)

def add_unit(out, unit, name=None):
    name = fix_name(name or unit.__name__)
    if name == 'GatewayWarpGate':
        name = 'WarpGate'
    elif name == 'SpireGreaterSpire':
        name = 'GreaterSpire'

    name_parts = re.findall('[A-Z]+[a-z]*',name)
    if name_parts[-1] == 'Cocoon':
        title = ''.join(name_parts[1:])
    else:
        title = ''.join(name_parts)

    d = OrderedDict(
        uid=re.sub('Burrowed|Flying|Lowered|Uprooted|Sieged|Assault|Phasing|Cocoon','',name),
        vid=name,
        title=title
    )

    if name in terran_units:
        d['race'] = 'Terran'
    elif name in protoss_units:
        d['race'] = 'Protoss'
    elif name in zerg_units:
        d['race'] = 'Zerg'
    else:
        d['race'] = 'Neutral'

    if name in (zerg_units - buildings) | non_zerg_bio:
        d['biological'] = True

    if name in ((terran_units & buildings) | ((terran_units|protoss_units)-non_zerg_bio) | set(['SCV'])):
        d['mechanical'] = True

    if name in set(['Queen','HighTemplar','Ghost','Infestor','Sentry','DarkTemplar','Mothership','WarpPrism','Archon']):
        d['psionic'] = True

    # Can't be both even though colosus is targeted as both
    if name in set(['Overlord','Overseer','Corruptor','Broodlord','Mothership','Voidray','WarpPrism','WarpPrismPhasing','Pheonix','Observer','Carrier','Intercepter','Mutalisk','CorruptorBroodlordCocoon','OverlordOverseerCocoon','Medivac','Viking','Battlecruiser','Raven','Banshee','PointDefenceDrone', 'CommandCenterFlying','OrbitalCommandFlying','BarracksFlying','FactoryFlying','StarportFlying']):
        d['air'] = True
    elif name in (zerg_units | protoss_units | terran_units):
        d['ground'] = True

    if name in buildings:
        d['structure'] = True

    if name in set(['Colossus','Ultralisk','Broodlord','Thor','Mothership','Battlecruiser','Archon','Carrier']):
        d['massive'] = True

    if name in set(['SCV','MULE','Probe','Drone']):
        d['worker'] = True

    if name in main_buildings | set(['Gateway','WarpGate','Stargate','RoboticsFacility','Barracks','BarracksFlying','Factory','FactoryFlying','Starport','StarportFlying']):
        d['production'] = True

    if name in research_buildings:
        d['research'] = True

    if name in main_buildings:
        d['main'] = True

    if name in attackers:
        d['attacker'] = True

    if name in moveables:
        d['moveable'] = True

    d['abilities']=list()
    out['objects'][unit.code] = d
    add_abilities(out, unit, name)


def transform(version):
    out = OrderedDict(
            attacker_abilities = [ "attack_move", "attack_object", "stop" ],
            moveable_abilities = [ "move", "patrol", "stop", "follow", "hold"],

            object_defaults = OrderedDict(
                    uid = "",
                    vid = "",
                    title = "",

                    race = "Neutral",
                    mechanical = False,
                    biological = False,
                    psionic = False,
                    air = False,
                    ground = False,
                    structure = False,
                    massive = False,

                    worker = False,
                    production = False,
                    research = False,
                    main = False,

                    attacker = False,
                    moveable = False,

                    abilities = ["RightClickLocation", "RightClickTarget"]
                ),

            ability_defaults = OrderedDict(
                    uid = "",
                    vid = "",
                    title = "",

                    minerals = 0,
                    gas = 0,
                    food = 0,
                    energy = 0,
                    cooldown = 0,

                    target = [], # location, bio, mechanical, structure, flying, ground
                        target_player = [], # self, enemy, ally,

                    research = False,
                    cancel = False,

                    build = False,
                        build_unit = "",
                        build_time = 0,
                        build_queue = 0,
                ),

            objects = dict(),
            abilities = dict()
        )

    # Revert ability code to its internal value
    for code, ability in version.abilities.iteritems():
        ability['code'] = code

    # Cycle through all the registered units
    for unit in version.types.values():
        add_unit(out, unit)

    return out

for version in ["v142","v14","v133","v13","v12"]:
    with open('sc2reader/new_data/'+version+'.json', 'w') as f:
        json.dump(transform(getattr(graham_data, version)), f, indent=4)