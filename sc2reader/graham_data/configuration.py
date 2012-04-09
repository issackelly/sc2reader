def Wrapped(func):
    def _wrapper(*args, **kwargs):
        def get_class(cls):
            func(cls, *args, **kwargs)
            return cls
        return get_class
    return _wrapper

class SC2Object(object):
    name = "No Object"
    id = 0x0


###TYPES:
#    click
#    rally
#    action
#    cancel
#    build
#    upgrade
#    spell
#    train
#    morph
#    changestate
def Data(conf):

    def Add(clazz, types, abilities):
        types[clazz.code] = clazz
        for k,v in clazz.abilities.items():
            abilities[k] = v

    def AddAll(clazzes, types, abilities):
        for clazz in clazzes:
            Add(clazz,types,abilities)

    def DataObject(clazz):
        def __init__(self,id,frame=""):
            self.id = id
            self.frame = frame

        def visit(self,frame,player,object_type=None):
            pass

        def __str__(self):
            return self.__class__.__name__

        clazz.__init__ = __init__
        clazz.visit = visit
        clazz.__str__ = __str__

        clazz.abilities[conf.DataObject.right_click["code"]]  = {"code" : 1 , "code" :53, "type" : "click" , "name" : "right_click"}
        clazz.abilities[conf.DataObject.right_click_in_fog["code"]]  = {"code" :54, "type" : "click" , "name" : "right_click_fog"}
        return clazz

    def Moveable(clazz):
        clazz.abilities[conf.Moveable.stop["code"]]  = {"code" :58, "type" : "action" , "name" : "stop"}
        clazz.abilities[conf.Moveable.hold["code"]]  = {"code" :59, "type" : "action" , "name" : "hold"}
        clazz.abilities[conf.Moveable.move["code"]]= {"code" :60, "type" : "action" , "name" : "move"}
        clazz.abilities[conf.Moveable.patrol["code"]]  = {"code" :61, "type" : "action" , "name" : "patrol"}
        clazz.abilities[conf.Moveable.follow["code"]]  = {"code" :62, "type" : "action" , "name" : "follow"}
        return clazz

    def Attacker(clazz):
        clazz.abilities[conf.Moveable.stop["code"]]  = {"code" :58, "type" : "action" , "name" : "stop"}
        clazz.abilities[conf.Attacker.attack_move["code"]]  = {"code" :66, "type" : "action" , "name" : "attack_move"}
        clazz.abilities[conf.Attacker.attack_object["code"]]  = {"code" :67, "type" : "action" , "name" : "attack_object"}
        return clazz

    def Worker(clazz):
        return clazz


    def Supporter(clazz):
        clazz.abilities[conf.Supporter.scan_move["code"]]  = {"code" :75, "type" : "action" , "name" : "scan_move"}
        clazz.abilities[conf.Supporter.scan_target["code"]]  = {"code" :76, "type" : "action" , "name" : "scan_target"}
        return clazz

    def Building(clazz):
        clazz.abilities[conf.Building.cancel["code"]]  = {"code" :80, "type" : "cancel" , "name" : "cancel_building"}
        return clazz

    def TerranBuilding(clazz):
        clazz.abilities[conf.TerranBuilding.halt_build["code"]]  = {"code" :84, "type" : "cancel" , "name" : "halt_building"}
        return clazz

    def Research(clazz):
        clazz.abilities[conf.Research.cancel["code"]]  = {"code" :88, "type" : "cancel" , "name" : "cancel"}
        clazz.abilities[conf.Research.cancel_unit["code"]]  = {"code" :89, "type" : "cancel" , "name" : "cancel_unit"}
        return clazz

    def Production(clazz):
        clazz.abilities[conf.Production.set_rally_point["code"]]  = {"code" :93, "type" : "rally" , "name" : "set_rally_point"}
        clazz.abilities[conf.Production.set_rally_target["code"]]  = {"code" :94, "type" : "rally" , "name" : "set_rally_target"}
        clazz.abilities[conf.Production.cancel["code"]]  = {"code" :95, "type" : "cancel" , "name" : "cancel"}
        clazz.abilities[conf.Production.cancel_unit["code"]]  = {"code" :96, "type" : "cancel" , "name" : "cancel_unit"}
        return clazz

    def addObject(abilities,datamap,icode,atype,name):
        res = {"code":icode,"type":atype,"name":name}
        if "min" in datamap:
            res["min"] = datamap["min"]
        if "gas" in datamap:
            res["gas"] = datamap["gas"]
        if "time" in datamap:
            res["time"] = datamap["time"]
        if "supply" in datamap:
            res["supply"] = datamap["supply"]
        abilities[datamap["code"]] = res

    class data:
        internalcodes = {}

        @classmethod
        def internalObject(self,code):
            return self.internalcodes[code]

        version = conf
        data_objects = {}
        types = {}
        abilities = {}

        for t in conf.Thrash.thrash:
            abilities[t] = {"code" :111, "type" : "thrash", "name" : "thrash"}

        @classmethod
        def type(self, type_code):
            return self.types[type_code]

        @classmethod
        def ability(self, ability_code):
                return self.abilities[ability_code] if ability_code in self.abilities.keys() else {"code" :119, "type" : "UNKNOWN", "name" : "UNKNOWN"}
        ###############Terran Units
        @Attacker
        @Worker
        @Moveable
        @DataObject
        class SCV():
            abilities = {}
            code = conf.SCV.code
            addObject(abilities,conf.SCV.gather_resources,129, "action" , "gather_resources")
            addObject(abilities,conf.SCV.return_cargo,130,  "action" ,  "return_cargo")
            addObject(abilities,conf.SCV.toggle_auto_repair,131,  "action" ,  "toggle_auto_repair")
            addObject(abilities,conf.SCV.repair,132,  "action" ,  "repair")
            addObject(abilities,conf.SCV.halt,133,  "action" ,  " halt_construction")
            addObject(abilities,conf.SCV.command_center,134,  "build" ,  "command_center")
            addObject(abilities,conf.SCV.supply_depot,135,  "build",  "supply_depot")
            addObject(abilities,conf.SCV.barracks,136,  "build" ,  "barracks")
            addObject(abilities,conf.SCV.engineering_bay,137,  "build" ,  "engineering_bay")
            addObject(abilities,conf.SCV.missle_turret,138,  "build" ,  "missile_turret")
            addObject(abilities,conf.SCV.bunker,139,  "build" ,  "bunker")
            addObject(abilities,conf.SCV.refinery,140,  "build" ,  "refinery")
            addObject(abilities,conf.SCV.sensor_tower,141,  "build" ,  "sensor_tower")
            addObject(abilities,conf.SCV.ghost_academy,142,  "build" ,  "ghost_academy")
            addObject(abilities,conf.SCV.factory,143,  "build" ,  "factory")
            addObject(abilities,conf.SCV.starport,144,  "build" ,  "starport")
            addObject(abilities,conf.SCV.armory,145,  "build" ,  "armory")
            addObject(abilities,conf.SCV.fusion_core,146,  "build" ,  "fusion_core")

        @Attacker
        @Worker
        @Moveable
        @DataObject
        class MULE():
            abilities = {}
            code = conf.MULE.code
            addObject(abilities,conf.MULE.toggle_auto_repair,155,  "action" ,  "auto_repair")
            addObject(abilities,conf.MULE.repair,156,  "action" ,  "repair")

        @Attacker
        @Moveable
        @DataObject
        class Marine():
            abilities = {}
            code = conf.Marine.code
            addObject(abilities,conf.Marine.use_stim_pack_mixed,164,  "action" ,  "stim_pack_mixed")

        @Attacker
        @Moveable
        @DataObject
        class Marauder():
            abilities = {}
            code = conf.Marauder.code
            addObject(abilities,conf.Marauder.use_stim_pack_mixed,172,  "action" ,  "stim_pack")
            addObject(abilities,conf.Marauder.use_stim_pack,173,  "action" ,  "stim_pack_mixed")

        @Attacker
        @Moveable
        @DataObject
        class Reaper():
            abilities = {}
            code = conf.Reaper.code

        @Attacker
        @Moveable
        @DataObject
        class Ghost():
            abilities = {}
            code = conf.Ghost.code
            addObject(abilities,conf.Ghost.cloak_on,181,  "action" ,  "cloak")
            addObject(abilities,conf.Ghost.cloak_off,182,  "action" ,  "uncloak")
            addObject(abilities,conf.Ghost.nuke_start,183,  "action" ,  "nuke")
            addObject(abilities,conf.Ghost.nuke_cancel,184,  "action" ,  "cancel_nuke")
            addObject(abilities,conf.Ghost.hold_fire,185,  "action" ,  "hold_fire")
            addObject(abilities,conf.Ghost.weapons_free,186,  "action" ,  "weapons_free")
            addObject(abilities,conf.Ghost.emp_round,187,  "action" ,  "EMP_Round")
            addObject(abilities,conf.Ghost.sniper_round,188,  "action" ,  "sniper_round")

        @Attacker
        @Moveable
        @DataObject
        class SiegeTank():
            abilities = {}
            code = conf.SiegeTank.code
            addObject(abilities,conf.SiegeTank.seige_mode_on,196,  "changestate" ,  "siege_mode")
            addObject(abilities,conf.SiegeTank.seige_mode_off,197,  "changestate" ,  "tank_mode")

        @Attacker
        @Moveable
        @DataObject
        class Thor():
            abilities = {}
            code = conf.Thor.code
            addObject(abilities,conf.Thor.strike_cannons,205,  "action" ,  "strike_cannons")

        @Attacker
        @Moveable
        @DataObject
        class Viking():
            abilities = {}
            code = conf.Viking.code
            addObject(abilities,conf.Viking.assault_mode_on,213,  "changestate" ,  "assault_mode")
            addObject(abilities,conf.Viking.assault_mode_off,214,  "changestate" ,  "fighter_mode")

        @Attacker
        @Moveable
        @DataObject
        class Medivac():
            abilities = {}
            code = conf.Medivac.code
            addObject(abilities,conf.Medivac.unload_all,222,  "action" ,  "unload_all")
            addObject(abilities,conf.Medivac.unload_all_moving,223,  "action" ,  "unload_all_moving")
            addObject(abilities,conf.Medivac.unload_unit,224,  "action" ,  "unload_unit")
            addObject(abilities,conf.Medivac.load_unit,225,  "action" ,  "load_unit")
            addObject(abilities,conf.Medivac.toggle_auto_heal,226,  "action",  "toggle_auto_heal")
            addObject(abilities,conf.Medivac.heal,227,  "action" ,  "heal")

        @Moveable
        @DataObject
        class Raven():
            abilities = {}
            code = conf.Raven.code
            addObject(abilities,conf.Raven.auto_turret,234,  "action" ,  "build_auto_turret")
            addObject(abilities,conf.Raven.point_defence_drone,235,  "action" ,  "build_point_defence_drone")
            addObject(abilities,conf.Raven.seeker_missle,236,  "action" ,  "seeker_missle")

        @Attacker
        @Moveable
        @DataObject
        class Banshee():
            abilities = {}
            code = conf.Banshee.code
            addObject(abilities,conf.Banshee.cloak_on,244,  "action" ,  "cloak")
            addObject(abilities,conf.Banshee.cloak_off,245,  "action" ,  "uncloak")

        @Attacker
        @Moveable
        @DataObject
        class Battlecruiser():
            abilities = {}
            code = conf.Battlecruiser.code
            addObject(abilities,conf.Battlecruiser.yamato_cannon,253,  "action" ,  "yamato_cannon")



        AddAll([SCV,MULE,Marine,Marauder,Reaper,Ghost,SiegeTank,Thor,Viking,Medivac,Raven,Banshee,Battlecruiser],types,abilities)

        ##### Terran Buildings
        def TerranMain(clazz):
            Building(clazz)
            addObject(clazz.abilities,conf.TerranMain.set_rally_point,262,  "rally" ,  "set_rally_point")
            addObject(clazz.abilities,conf.TerranMain.set_rally_target,263,  "rally" ,  "set_rally_target")
            addObject(clazz.abilities,conf.TerranMain.train_scv,264,  "train" ,  "SCV")
            return clazz

        @TerranBuilding
        @DataObject
        class SupplyDepot():
            abilities = {}
            code = conf.SupplyDepot.code
            addObject(abilities,conf.SupplyDepot.lower_supply,272,  "changestate" ,  "lower")
            addObject(abilities,conf.SupplyDepot.raise_supply,273,  "changestate" ,  "raise")

        @TerranBuilding
        @DataObject
        class Refinery():
            abilities = {}
            code = conf.Refinery.code

        @TerranBuilding
        @DataObject
        class Bunker():
            abilities = {}
            code = conf.Bunker.code
            addObject(abilities,conf.Bunker.salvage,280,  "action" ,  "salvage")
            addObject(abilities,conf.Bunker.stimpack,281,  "action" ,  "stimpack")
            addObject(abilities,conf.Bunker.unload_all,282,  "action" ,  "unload_all")
            addObject(abilities,conf.Bunker.unload_unit,283,  "action" ,  "unload_unit")
            addObject(abilities,conf.Bunker.load_unit,284,  "action" ,  "load")

        @Attacker
        @TerranBuilding
        @DataObject
        class MissileTurret():
            abilities = {}
            code = conf.MissileTurret.code

        @TerranBuilding
        @DataObject
        class SensorTower():
            abilities = {}
            code = conf.SensorTower.code

        @Production
        @TerranBuilding
        @TerranMain
        @DataObject
        class CommandCenter(SC2Object):
            abilities = {}
            code = conf.CommandCenter.code
            addObject(abilities,conf.CommandCenter.lift_up,294,  "action" ,  "lift")

            addObject(abilities,conf.CommandCenter.unload_all,296,  "action" ,  "unload_all")
            addObject(abilities,conf.CommandCenter.unload_unit,297,  "action" ,  "unload")
            addObject(abilities,conf.CommandCenter.load_unit,298,  "action" ,  "load")
            addObject(abilities,conf.CommandCenter.upgradeto_orbital_command,299,  "morph" ,  "upgrade_to_orbital_command")
            addObject(abilities,conf.CommandCenter.upgradeto_orbital_command_cancel,300,  "cancel" ,  "upgrade_to_orbital_command_cancel")
            addObject(abilities,conf.CommandCenter.upgradeto_planetary_fortress,301,  "morph" ,  "upgrade_to_planetary_fortress")
            addObject(abilities,conf.CommandCenter.upgradeto_planetary_fortress_cancel,302,  "cancel" ,  "upgrade_to_planetary_fortress_cancel")

            class Flying():
                code = conf.CommandCenter.Flying.code
                abilities = {}
                addObject(abilities,conf.CommandCenter.lift_down,295,  "action" ,  "land")

        @Production
        @TerranBuilding
        @TerranMain
        @DataObject
        class OrbitalCommand(SC2Object):
            abilities = {}
            code = conf.OrbitalCommand.code
            addObject(abilities,conf.OrbitalCommand.lift_up,313,  "action" ,  "lift")

            addObject(abilities,conf.OrbitalCommand.mule_target,315,  "train" ,  "calldown_mule_target")
            addObject(abilities,conf.OrbitalCommand.mule_location,316,  "train" ,  "calldown_mule_location")
            addObject(abilities,conf.OrbitalCommand.extra_supply,317,  "build" ,  "calldown_extra_supplies")
            addObject(abilities,conf.OrbitalCommand.scanner_sweep,318,  "spell" ,  "scanner_sweep")

            class Flying():
                code = conf.OrbitalCommand.Flying.code
                abilities = {}
                addObject(abilities,conf.OrbitalCommand.lift_down,314,  "action" ,  "land")

        @Production
        @TerranBuilding
        @TerranMain
        @DataObject
        class PlanetaryFortress():
            abilities = {}
            code = conf.PlanetaryFortress.code

        @Research
        @TerranBuilding
        @DataObject
        class EngineeringBay(SC2Object):
            abilities = {}
            code = conf.EngineeringBay.code
            addObject(abilities,conf.EngineeringBay.hisec_auto_tracking,328,  "upgrade" ,  "hisec_auto_tracking")
            addObject(abilities,conf.EngineeringBay.building_armor,329,  "upgrade" ,  "building_armor")
            addObject(abilities,conf.EngineeringBay.inftantry_weapons_1,330,  "upgrade" ,  "infantry_weapons_1")
            addObject(abilities,conf.EngineeringBay.inftantry_weapons_2,331,  "upgrade" ,  "infantry_weapons_2")
            addObject(abilities,conf.EngineeringBay.inftantry_weapons_3,332,  "upgrade" ,  "infantry_weapons_3")
            addObject(abilities,conf.EngineeringBay.neosteel_frame,333,  "upgrade" ,  "neosteel_frame")
            addObject(abilities,conf.EngineeringBay.inftantry_armor_1,334,  "upgrade" ,  "infantry_armor_1")
            addObject(abilities,conf.EngineeringBay.inftantry_armor_2,335,  "upgrade" ,  "infantry_armor_2")
            addObject(abilities,conf.EngineeringBay.inftantry_armor_3,336,  "upgrade" ,  "infantry_armor_3")

        @Research
        @TerranBuilding
        @DataObject
        class GhostAcademy(SC2Object):
            abilities = {}
            code = conf.GhostAcademy.code
            addObject(abilities,conf.GhostAcademy.arm_silo_w_nuke,344,  "train" ,  "arm_silo_with_nuke")
            addObject(abilities,conf.GhostAcademy.personal_cloaking,345,  "upgrade" ,  "personal_cloaking")
            addObject(abilities,conf.GhostAcademy.moebius_reactor,346,  "upgrade" ,  "moebius_reactor")

        @Research
        @TerranBuilding
        @DataObject
        class FusionCore(SC2Object):
            abilities = {}
            code = conf.FusionCore.code
            addObject(abilities,conf.FusionCore.yamato_cannon,354,  "upgrade" ,  "yamato_cannon")


        @Research
        @TerranBuilding
        @DataObject
        class Armory(SC2Object):
            abilities = {}
            code = conf.Armory.code
            addObject(abilities,conf.Armory.vehicle_plating_1,363,  "upgrade" ,  "vehicle_plating_1")
            addObject(abilities,conf.Armory.vehicle_plating_2,364,  "upgrade" ,  "vehicle_plating_2")
            addObject(abilities,conf.Armory.vehicle_plating_3,365,  "upgrade" ,  "vehicle_plating_3")
            addObject(abilities,conf.Armory.vehicle_weapons_1,366,  "upgrade" ,  "vehicle_weapons_1")
            addObject(abilities,conf.Armory.vehicle_weapons_2,367,  "upgrade" ,  "vehicle_weapons_2")
            addObject(abilities,conf.Armory.vehicle_weapons_3,368,  "upgrade" ,  "vehicle_weapons_3")
            addObject(abilities,conf.Armory.ship_plating_1,369,  "upgrade" ,  "ship_plating_1")
            addObject(abilities,conf.Armory.ship_plating_2,370,  "upgrade" ,  "ship_plating_2")
            addObject(abilities,conf.Armory.ship_plating_3,371,  "upgrade" ,  "ship_plating_3")
            addObject(abilities,conf.Armory.ship_weapons_1,372,  "upgrade" ,  "ship_weapons_1")
            addObject(abilities,conf.Armory.ship_weapons_2,373,  "upgrade" ,  "ship_weapons_2")
            addObject(abilities,conf.Armory.ship_weapons_3,374,  "upgrade" ,  "ship_weapons_3")

        @Production
        @TerranBuilding
        @DataObject
        class Barracks(SC2Object):
            abilities = {}
            code = conf.Barracks.code
            addObject(abilities,conf.Barracks.marine,382,  "train" ,  "marine")
            addObject(abilities,conf.Barracks.reaper,383,  "train" ,  "reaper")
            addObject(abilities,conf.Barracks.ghost,384,  "train" ,  "ghost")
            addObject(abilities,conf.Barracks.marauder,385,  "train" ,  "marauder")

            addObject(abilities,conf.Barracks.lift_up,387,  "action" ,  "lift")

            addObject(abilities,conf.Barracks.addon_techlab,390,  "build" ,  "techlab")
            addObject(abilities,conf.Barracks.addon_techlab_cancel,392,  "cancel" ,  "cancel_techlab")

            addObject(abilities,conf.Barracks.addon_reactor,394,  "build" ,  "reactor")
            addObject(abilities,conf.Barracks.addon_reactor_cancel,396,  "cancel" ,  "cancel_reactor")

            @Research
            @TerranBuilding
            @DataObject
            class Techlab(SC2Object):
                abilities = {}
                code = conf.Barracks.Techlab.code
                addObject(abilities,conf.Barracks.Techlab.nitropacks,404,  "upgrade" ,  "nitropacks")
                addObject(abilities,conf.Barracks.Techlab.stimpack,405,  "upgrade" ,  "stimpack")
                addObject(abilities,conf.Barracks.Techlab.combat_shield,406,  "upgrade" ,  "combat_shield")
                addObject(abilities,conf.Barracks.Techlab.concussive_shells,407,  "upgrade" ,  "concussive_shells")

                addObject(abilities,conf.Barracks.Techlab.cancel_research,409,  "cancel" ,  "cancel_research")
                addObject(abilities,conf.Barracks.Techlab.cancel_specific_research,410,  "cancel" ,  "cancel_specific_research")

            class Reactor(SC2Object):
                code = conf.Barracks.Reactor.code

            class Flying(SC2Object):
                abilities = {}
                addObject(abilities,conf.Barracks.lift_down,388,  "action" ,  "land")
                addObject(abilities,conf.Barracks.addon_techlab_move,390,  "build" ,  "techlab_move")
                addObject(abilities,conf.Barracks.addon_reactor_move,394,  "build" ,  "reactor_move")
                code = conf.Barracks.Flying.code

        @Production
        @TerranBuilding
        @DataObject
        class Factory(SC2Object):
            abilities = {}
            code = conf.Factory.code

            addObject(abilities,conf.Factory.seige_tank,425,  "train" ,  "seige_tank")
            addObject(abilities,conf.Factory.thor,426,  "train" ,  "thor")
            addObject(abilities,conf.Factory.hellion,427,  "train" ,  "hellion")

            addObject(abilities,conf.Factory.lift_up,429,  "action" ,  "lift")

            addObject(abilities,conf.Factory.addon_techlab,432,  "build" ,  "techlab")
            addObject(abilities,conf.Factory.addon_techlab_cancel,434,  "cancel" ,  "cancel_techlab")

            addObject(abilities,conf.Factory.addon_reactor,436,  "build" ,  "reactor")
            addObject(abilities,conf.Factory.addon_reactor_cancel,438,  "cancel" ,  "cancel_reactor")


            @Research
            @TerranBuilding
            @DataObject
            class Techlab(SC2Object):
                abilities = {}
                code = conf.Factory.Techlab.code
                addObject(abilities,conf.Factory.Techlab.siege_tech,447,  "upgrade" ,  "siege_tech")
                addObject(abilities,conf.Factory.Techlab.infernal_preignighter,448,  "upgrade" ,  "infernal_preignighter")
                addObject(abilities,conf.Factory.Techlab.strike_cannon,449,  "upgrade" ,  "strike_cannon")

                addObject(abilities,conf.Factory.Techlab.cancel_research,451,  "cancel" ,  "cancel_research")
                addObject(abilities,conf.Factory.Techlab.cancel_specific_research,452,  "cancel" ,  "cancel_specific_research")

            class Reactor(SC2Object):
                code = conf.Factory.Reactor.code

            class Flying(SC2Object):
                abilities = {}
                code = conf.Factory.Flying.code
                addObject(abilities,conf.Factory.lift_down,430,  "action" ,  "land")
                addObject(abilities,conf.Factory.addon_reactor_move,436,  "build" ,  "reactor_move")
                addObject(abilities,conf.Factory.addon_techlab_move,432,  "build" ,  "techlab_move")

        @Production
        @TerranBuilding
        @DataObject
        class Starport(SC2Object):
            abilities = {}
            code = conf.Starport.code

            addObject(abilities,conf.Starport.medivac,466,  "train" ,  "medivac")
            addObject(abilities,conf.Starport.banshee,467,  "train" ,  "banshee")
            addObject(abilities,conf.Starport.raven,468,  "train" ,  "raven")
            addObject(abilities,conf.Starport.battlecruiser,469,  "train" ,  "battlecruiser")
            addObject(abilities,conf.Starport.viking,470,  "train" ,  "viking")

            addObject(abilities,conf.Starport.lift_up,473,  "action" ,  "lift")

            addObject(abilities,conf.Starport.addon_techlab,476,  "build" ,  "techlab")
            addObject(abilities,conf.Starport.addon_techlab_cancel,478,  "cancel" ,  "cancel_techlab")

            addObject(abilities,conf.Starport.addon_reactor,480,  "build" ,  "reactor")
            addObject(abilities,conf.Starport.addon_reactor_cancel,482,  "cancel" ,  "cancel_reactor")


            @Research
            @TerranBuilding
            @DataObject
            class Techlab(SC2Object):
                abilities = {}
                code = conf.Starport.Techlab.code
                addObject(abilities,conf.Starport.Techlab.cloaking_field,491,  "upgrade" ,  "cloaking")
                addObject(abilities,conf.Starport.Techlab.caduceus_reactor,492,  "upgrade" ,  "caduceus")
                addObject(abilities,conf.Starport.Techlab.corvid_reactor,493,  "upgrade" ,  "corvid")
                addObject(abilities,conf.Starport.Techlab.seeker_missle,494,  "upgrade" ,  "seeker")
                addObject(abilities,conf.Starport.Techlab.durable_materials,495,  "upgrade" ,  "durable")

                addObject(abilities,conf.Starport.Techlab.cancel_research,497,  "cancel" ,  "cancel_research")
                addObject(abilities,conf.Starport.Techlab.cancel_specific_research,498,  "cancel" ,  "cancel_research")

            class Reactor(SC2Object):
                code = conf.Starport.Reactor.code

            class Flying(SC2Object):
                code = conf.Starport.Flying.code
                abilities = {}
                addObject(abilities,conf.Starport.lift_down,474,  "action" ,  "land")
                addObject(abilities,conf.Starport.addon_techlab_move,476,  "build" ,  "techlab_move")
                addObject(abilities,conf.Starport.addon_reactor_move,480,  "build" ,  "reactor_move")

        AddAll([SupplyDepot,Refinery,Bunker,CommandCenter,OrbitalCommand,PlanetaryFortress,Barracks,Factory,Starport,EngineeringBay,Armory,FusionCore,GhostAcademy,MissileTurret,SensorTower],types,abilities)

        ##Protoss Units
        @Attacker
        @Worker
        @Moveable
        @DataObject
        class Probe(SC2Object):
            code = conf.Probe.code
            abilities = {}
            addObject(abilities,conf.Probe.return_cargo,519,  "action" ,  "return_cargo")
            addObject(abilities,conf.Probe.gather_resources,520,  "action" ,  "gather_resources")
            addObject(abilities,conf.Probe.nexus,521,  "build" ,  "nexus")
            addObject(abilities,conf.Probe.pylon,522,  "build" ,  "pylon")
            addObject(abilities,conf.Probe.gateway,523,  "build" ,  "gateway")
            addObject(abilities,conf.Probe.forge,524,  "build" ,  "forge")
            addObject(abilities,conf.Probe.fleet_beacon,525,  "build" ,  "fleet_beacon")
            addObject(abilities,conf.Probe.twilight_council,526,  "build" ,  "twilight_council")
            addObject(abilities,conf.Probe.photon_cannon,527,  "build" ,  "photon_cannon")
            addObject(abilities,conf.Probe.assimilator,528,  "build" ,  "assimilator")
            addObject(abilities,conf.Probe.stargate,529,  "build" ,  "stargate")
            addObject(abilities,conf.Probe.templar_archives,530,  "build" ,  "templar_archives")
            addObject(abilities,conf.Probe.dark_shrine,531,  "build" ,  "dark_shrine")
            addObject(abilities,conf.Probe.robotics_bay,532,  "build" ,  "robotics_bay")
            addObject(abilities,conf.Probe.robotics_facility,533,  "build" ,  "robotics_facility")
            addObject(abilities,conf.Probe.cybernetics_core,534,  "build" ,  "cybernetics_core")

        @Attacker
        @Moveable
        @DataObject
        class Zealot():
            abilities = {}
            code = conf.Zealot.code

        @Attacker
        @Moveable
        @DataObject
        class Stalker():
            abilities = {}
            code = conf.Stalker.code
            addObject(abilities,conf.Stalker.blink,543,  "action" ,  "blink")

        @Attacker
        @Moveable
        @DataObject
        class Sentry():
            abilities = {}
            code = conf.Sentry.code
            addObject(abilities,conf.Sentry.hallucinate_archon,551,  "action" ,  "hallucinate_archon")
            addObject(abilities,conf.Sentry.hallucinate_colossus,552,  "action" ,  "hallucinate_colossus")
            addObject(abilities,conf.Sentry.hallucinate_high_templar,553,  "action" ,  "hallucinate_high_templar")
            addObject(abilities,conf.Sentry.hallucinate_immortal,554,  "action" ,  "hallucinate_immortal")
            addObject(abilities,conf.Sentry.hallucinate_phoenix,555,  "action" ,  "hallucinate_phoenix")
            addObject(abilities,conf.Sentry.hallucinate_probe,556,  "action" ,  "hallucinate_probe")
            addObject(abilities,conf.Sentry.hallucinate_stalker,557,  "action" ,  "hallucinate_stalker")
            addObject(abilities,conf.Sentry.hallucinate_void_ray,558,  "action" ,  "hallucinate_voidray")
            addObject(abilities,conf.Sentry.hallucinate_warp_prism,559,  "action" ,  "hallucinate_warp_prism")
            addObject(abilities,conf.Sentry.hallucinate_zealot,560,  "action" ,  "hallucinate_zealot")
            addObject(abilities,conf.Sentry.guardian_shield,561,  "action" ,  "guardian_shield")
            addObject(abilities,conf.Sentry.force_field,562,  "action" ,  "force_field")

        @Attacker
        @Moveable
        @DataObject
        class HighTemplar():
            abilities = {}
            code = conf.HighTemplar.code
            addObject(abilities,conf.HighTemplar.psionic_storm,570,  "action" ,  "psionic_storm")
            addObject(abilities,conf.HighTemplar.feedback,571,  "action" ,  "feedback")
            addObject(abilities,conf.HighTemplar.merge_into_archon,572,  "morph" ,  "merge_into_archon")

        @Attacker
        @Moveable
        @DataObject
        class DarkTemplar():
            abilities = {}
            code = conf.DarkTemplar.code
            addObject(abilities,conf.DarkTemplar.merge_into_archon,580,  "morph" ,  "merge_into_archon")

        @Attacker
        @Moveable
        @DataObject
        class Archon():
            abilities = {}
            code = conf.Archon.code

        @Attacker
        @Moveable
        @DataObject
        class Colossus():
            abilities = {}
            code = conf.Colossus.code

        @Moveable
        @DataObject
        class WarpPrism():
            abilities = {}
            code = conf.WarpPrism.code
            addObject(abilities,conf.WarpPrism.unload_all,587,  "action" ,  "unload_all")
            addObject(abilities,conf.WarpPrism.unload_all_moving,588,  "action" ,  "unload_all_moving")
            addObject(abilities,conf.WarpPrism.unload_unit,589,  "action" ,  "unload")
            addObject(abilities,conf.WarpPrism.load_unit,590,  "action" ,  "load")
            addObject(abilities,conf.WarpPrism.phase_mode,591,  "changestate" ,  "phase_mode")
            addObject(abilities,conf.WarpPrism.transport_mode,592,  "changestate" ,  "transport_mode")

        @Attacker
        @Moveable
        @DataObject
        class Immortal():
            abilities = {}
            code = conf.Immortal.code

        @Moveable
        @DataObject
        class Observer():
            abilities = {}
            code = conf.Observer.code

        @Moveable
        @Attacker
        @DataObject
        class Voidray():
            abilities = {}
            code = conf.Voidray.code

        @Attacker
        @Moveable
        @DataObject
        class Phoenix():
            abilities = {}
            code = conf.Pheonix.code
            addObject(abilities,conf.Pheonix.gravitation_beam_on,600,  "action" ,  "graviton_beam")

        @Attacker
        @Moveable
        @DataObject
        class Carrier():
            abilities = {}
            code = conf.Carrier.code
            addObject(abilities,conf.Carrier.interceptor,608,  "action" ,  "interceptor")

        @Attacker
        @Moveable
        @DataObject
        class Mothership():
            abilities = {}
            code = conf.Mothership.code
            addObject(abilities,conf.Mothership.vortex,616,  "action" ,  "vortex")
            addObject(abilities,conf.Mothership.mass_recall,617,  "action" ,  "mass_recall")

        AddAll([Probe,Zealot,Stalker,Sentry,HighTemplar,DarkTemplar,Archon,Colossus,Immortal,Observer,WarpPrism,Phoenix,Voidray,Carrier,Mothership],types,abilities)

        ###Protoss Buildings
        @Production
        @DataObject
        class Nexus(SC2Object):
            code = conf.Nexus.code
            abilities = {}
            addObject(abilities,conf.Nexus.probe,627,  "train" ,  "probe")
            addObject(abilities,conf.Nexus.mothership,628,  "train" ,  "mothership")
            addObject(abilities,conf.Nexus.chronoboost,629,  "spell" ,  "chronoboost")
            addObject(abilities,conf.Nexus.set_rally_point,630,  "rally" ,  "rally")
            addObject(abilities,conf.Nexus.set_rally_target,631,  "rally" ,  "rally")

        @DataObject
        class Pylon():
            abilities = {}
            code = conf.Pylon.code

        @DataObject
        class Assimilator():
            code = conf.Assimilator.code
            abilities = {}

        @Production
        @DataObject
        class Gateway(SC2Object):
            code = conf.Gateway.code
            abilities = {}
            addObject(abilities,conf.Gateway.zealot,638,  "train" ,  "zealot")
            addObject(abilities,conf.Gateway.stalker,639,  "train" ,  "stalker")
            addObject(abilities,conf.Gateway.high_templar,640,  "train" ,  "high_templar")
            addObject(abilities,conf.Gateway.dark_templar,641,  "train" ,  "dark_templar")
            addObject(abilities,conf.Gateway.sentry,642,  "train" ,  "sentry")
            addObject(abilities,conf.Gateway.to_warpgate,643,  "changestate" ,  "warp_mode")

        @Production
        @DataObject
        class WarpGate(SC2Object):
            code = conf.Gateway.WarpGate.code
            abilities = {}
            addObject(abilities,conf.Gateway.WarpGate.warp_zealot,638,  "train" ,  "zealot")
            addObject(abilities,conf.Gateway.WarpGate.warp_stalker,639,  "train" ,  "stalker")
            addObject(abilities,conf.Gateway.WarpGate.warp_high_templar,640,  "train" ,  "high_templar")
            addObject(abilities,conf.Gateway.WarpGate.warp_dark_templar,641,  "train" ,  "dark_templar")
            addObject(abilities,conf.Gateway.WarpGate.warp_sentry,642,  "train" ,  "sentry")
            addObject(abilities,conf.Gateway.WarpGate.to_gateway,655,  "changestate" ,  "gateway_mode")

        @Research
        @DataObject
        class Forge(SC2Object):
            code = conf.Forge.code
            abilities = {}
            addObject(abilities,conf.Forge.ground_weapons_1,662,  "upgrade" ,  "ground_weapons_1")
            addObject(abilities,conf.Forge.ground_weapons_2,663,  "upgrade" ,  "ground_weapons_2")
            addObject(abilities,conf.Forge.ground_weapons_3,664,  "upgrade" ,  "ground_weapons_3")
            addObject(abilities,conf.Forge.ground_armour_1,665,  "upgrade" ,  "ground_armor_1")
            addObject(abilities,conf.Forge.ground_armour_2,666,  "upgrade" ,  "ground_armor_2")
            addObject(abilities,conf.Forge.ground_armour_3,667,  "upgrade" ,  "ground_armor_3")
            addObject(abilities,conf.Forge.shield_1,668,  "upgrade" ,  "shield_1")
            addObject(abilities,conf.Forge.shield_2,669,  "upgrade" ,  "shield_2")
            addObject(abilities,conf.Forge.shield_3,670,  "upgrade" ,  "shield_3")

        @Attacker
        @DataObject
        class PhotonCannon():
            code = conf.PhotonCannon.code
            abilities = {}

        @Research
        @DataObject
        class CyberneticsCore(SC2Object):
            code = conf.CyberneticsCore.code
            abilities = {}
            addObject(abilities,conf.CyberneticsCore.air_weapons_1,677,  "upgrade" ,  "air_weapons_1")
            addObject(abilities,conf.CyberneticsCore.air_weapons_2,678,  "upgrade" ,  "air_weapons_2")
            addObject(abilities,conf.CyberneticsCore.air_weapons_3,679,  "upgrade" ,  "air_weapons_3")
            addObject(abilities,conf.CyberneticsCore.air_armour_1,680,  "upgrade" ,  "air_armor_1")
            addObject(abilities,conf.CyberneticsCore.air_armour_2,681,  "upgrade" ,  "air_armor_2")
            addObject(abilities,conf.CyberneticsCore.air_armour_3,682,  "upgrade" ,  "air_armor_3")
            addObject(abilities,conf.CyberneticsCore.warpgate,683,  "upgrade" ,  "warpgate")
            addObject(abilities,conf.CyberneticsCore.hallucination,684,  "upgrade" ,  "hallucination")


        @Production
        @DataObject
        class RoboticsFacility(SC2Object):
            code = conf.RoboticsFacility.code
            abilities = {}
            addObject(abilities,conf.RoboticsFacility.warp_prism,692,  "train" ,  "warp_prism")
            addObject(abilities,conf.RoboticsFacility.observer,693,  "train" ,  "observer")
            addObject(abilities,conf.RoboticsFacility.colossus,694,  "train" ,  "colossus")
            addObject(abilities,conf.RoboticsFacility.immortal,695,  "train" ,  "immortal")

        @Production
        @DataObject
        class Stargate(SC2Object):
            code = conf.Stargate.code
            abilities = {}
            addObject(abilities,conf.Stargate.pheonix,702,  "train" ,  "phoenix")
            addObject(abilities,conf.Stargate.carrier,703,  "train" ,  "carrier")
            addObject(abilities,conf.Stargate.voidray,704,  "train" ,  "voidray")

        @Research
        @DataObject
        class TwilightCouncil(SC2Object):
            code = conf.TwilightCouncil.code
            abilities = {}
            addObject(abilities,conf.TwilightCouncil.charge,710,  "upgrade" ,  "charge")
            addObject(abilities,conf.TwilightCouncil.blink,711,  "upgrade" ,  "blink")

        @Research
        @DataObject
        class FleetBeacon(SC2Object):
            code = conf.FleetBeacon.code
            abilities = {}
            addObject(abilities,conf.FleetBeacon.gavitation_catapault,718,  "upgrade" ,  "graviton_catapult")

        @Research
        @DataObject
        class TemplarArchives(SC2Object):
            abilities = {}
            code = conf.TemplarArchive.code
            addObject(abilities,conf.TemplarArchive.psi_storm,725,  "upgrade" ,  "psionic_storm")

        @DataObject
        class DarkShrine():
            abilities = {}
            code = conf.DarkShrine.code

        @Research
        @DataObject
        class RoboticsBay(SC2Object):
            code = conf.RoboticsBay.code
            abilities = {}
            addObject(abilities,conf.RoboticsBay.grav_booster,732,  "upgrade" ,  "booster")
            addObject(abilities,conf.RoboticsBay.grav_drive,733,  "upgrade" ,  "drive")
            addObject(abilities,conf.RoboticsBay.thermal_lance,734,  "upgrade" ,  "thermal_lance")

        AddAll([Nexus,Pylon,Assimilator,Gateway,WarpGate,Forge,CyberneticsCore, RoboticsFacility,Stargate,TwilightCouncil,FleetBeacon,TemplarArchives,DarkShrine,RoboticsBay,PhotonCannon],types,abilities)


        ###ZERG UNITS

        @DataObject
        class Larva(SC2Object):
            code = conf.Larva.code
            abilities = {}
            addObject(abilities,conf.Larva.drone,746,  "train" ,  "drone")
            addObject(abilities,conf.Larva.zergling,747,  "train" ,  "zergling")
            addObject(abilities,conf.Larva.overlord,748,  "train" ,  "overlord")
            addObject(abilities,conf.Larva.hydralisk,749,  "train" ,  "hydralisk")
            addObject(abilities,conf.Larva.mutalisk,750,  "train" ,  "mutalisk")
            addObject(abilities,conf.Larva.ultralisk,751,  "train" ,  "ultralisk")
            addObject(abilities,conf.Larva.roach,752,  "train" ,  "roach")
            addObject(abilities,conf.Larva.infestor,753,  "train" ,  "infestor")
            addObject(abilities,conf.Larva.corrupter,754,  "train" ,  "corruptor")

        @DataObject
        class Egg():
            code = conf.Egg.code
            abilities = {}
            addObject(abilities,conf.Egg.cancel,827,  "cancel" ,  "cancel egg")

        @Supporter
        @Moveable
        @DataObject
        class Overlord(SC2Object):
            code = conf.Overlord.code
            abilities = {}
            addObject(abilities,conf.Overlord.creep,814,  "spell" ,  "creep")
            addObject(abilities,conf.Overlord.cancel_creep,815,  "cancel" ,  "cancel_creep")

            addObject(abilities,conf.Overlord.overseer,817,  "morph" ,  "overseer")
            addObject(abilities,conf.Overlord.cancel_overseer,818,  "cancel" ,  "cancel_overseer")

            class OverseerCocoon(SC2Object):
                code = conf.Overlord.OverseerCocoon.code
                abilities = {}

        @Attacker
        @Moveable
        @DataObject
        class Overseer():
            code = conf.Overseer.code
            abilities = {}
            addObject(abilities,conf.Overseer.changling,899,  "action" ,  "changeling")
            addObject(abilities,conf.Overseer.contaminate,900,  "action" ,  "contaminate")

        @Moveable
        @DataObject
        class Changeling():
            abilities = {}
            code = conf.Changeling.code

        @Worker
        @Moveable
        @DataObject
        class Drone(SC2Object):
            code = conf.Drone.code
            abilities = {}
            addObject(abilities,conf.Drone.gather_resources,762,  "action" ,  "gather_resources")
            addObject(abilities,conf.Drone.return_cargo,763,  "action" ,  "return_cargo")
            addObject(abilities,conf.Drone.burrow,764,  "action" ,  "burrow")
            addObject(abilities,conf.Drone.unburrow,765,  "action" ,  "unburrow")

            addObject(abilities,conf.Drone.hatchery,767,  "build" ,  "hatchery")
            addObject(abilities,conf.Drone.spawning_pool,768,  "build" ,  "spawning_pool")
            addObject(abilities,conf.Drone.evolution_chamber,769,  "build" ,  "evolution_chamber")
            addObject(abilities,conf.Drone.hydra_den,770,  "build" ,  "hydralisk_den")
            addObject(abilities,conf.Drone.spire,771,  "build" ,  "spire")
            addObject(abilities,conf.Drone.ultralisk_cavern,772,  "build" ,  "ultralisk")
            addObject(abilities,conf.Drone.extractor,773,  "build" ,  "extractor")
            addObject(abilities,conf.Drone.infestation_pit,774,  "build" ,  "infestation_pit")
            addObject(abilities,conf.Drone.nydus_network,775,  "build" ,  "nydus_network")
            addObject(abilities,conf.Drone.baneling_nest,776,  "build" ,  "baneling_nest")
            addObject(abilities,conf.Drone.roach_warren,777,  "build" ,  "roach_warren")
            addObject(abilities,conf.Drone.spine_crawler,778,  "build" ,  "spine_crawler")
            addObject(abilities,conf.Drone.spore_crawler,779,  "build" ,  "spore_crawler")

        @Attacker
        @Moveable
        @DataObject
        class Zergling(SC2Object):
            code = conf.Zergling.code
            abilities = {}
            addObject(abilities,conf.Zergling.baneling,787,  "morph" ,  "baneling")
            class BanelingCocoon():
                code = conf.Zergling.BanelingCocoon.code
                abilities = {}
                addObject(abilities,conf.Zergling.BanelingCocoon.cancel_baneling,791,  "cancel" ,  "cancel_baneling")

        @Attacker
        @Moveable
        @DataObject
        class Baneling():
            code = conf.Baneling.code
            abilities = {}
            addObject(abilities,conf.Baneling.burrow,847,  "action" ,  "burrow")
            addObject(abilities,conf.Baneling.unburrow,848,  "action" ,  "unburrow")
            addObject(abilities,conf.Baneling.explode,849,  "action" ,  "explode")
            addObject(abilities,conf.Baneling.attack_structure,850,  "action" ,  "attack")

        @Attacker
        @Moveable
        @DataObject
        class Queen():
            code = conf.Queen.code
            abilities = {}
            addObject(abilities,conf.Queen.burrow,835,  "action" ,  "burrow")
            addObject(abilities,conf.Queen.unburrow,836,  "action" ,  "unburrow")
            addObject(abilities,conf.Queen.creep_tumor,837,  "action" ,  "creep")
            addObject(abilities,conf.Queen.larva,838,  "action" ,  "larva")
            addObject(abilities,conf.Queen.transfuse,839,  "action" ,  "transfuse")

        @Attacker
        @Moveable
        @DataObject
        class Roach():
            code = conf.Roach.code
            abilities = {}
            addObject(abilities,conf.Roach.burrow,858,  "action" ,  "burrow")
            addObject(abilities,conf.Roach.unburrow,859,  "action" ,  "unburrow")

        @Attacker
        @Moveable
        @DataObject
        class Hydralisk():
            code = conf.Hydralisk.code
            abilities = {}
            addObject(abilities,conf.Hydralisk.burrow,867,  "action" ,  "burrow")
            addObject(abilities,conf.Hydralisk.unburrow,868,  "action" ,  "unburrow")

        @Attacker
        @Moveable
        @DataObject
        class Infestor():
            code = conf.Infestor.code
            abilities = {}
            addObject(abilities,conf.Infestor.burrow,877,  "action" ,  "burrow")
            addObject(abilities,conf.Infestor.unburrow,878,  "action" ,  "unburrow")

            addObject(abilities,conf.Infestor.fungal_growth,880,  "action" ,  "fungal")
            addObject(abilities,conf.Infestor.infested_terran,881,  "action" ,  "infested")
            addObject(abilities,conf.Infestor.neural_parasite,882,  "action" ,  "neural")

        @Attacker
        @Moveable
        @DataObject
        class Mutalisk():
            abilities = {}
            code = conf.Mutalisk.code

        @Attacker
        @Moveable
        @DataObject
        class Corruptor(SC2Object):
            code = conf.Corruptor.code
            abilities = {}
            addObject(abilities,conf.Corruptor.broodlord,801,  "morph" ,  "broodlord")
            addObject(abilities,conf.Corruptor.corruption,802,  "action" ,  "corruption")
            class BroodlordCocoon(SC2Object):
                code = conf.Corruptor.BroodlordCocoon.code
                abilities = {}
                addObject(abilities,conf.Corruptor.BroodlordCocoon.cancel_broodlord,806,  "cencel" ,  "cancel_broodlord")

        @Attacker
        @Moveable
        @DataObject
        class Broodlord():
            code = conf.Corruptor.Broodlord.code
            abilities = {}

        @Attacker
        @Moveable
        @DataObject
        class Ultralisk():
            code = conf.Ultralisk.code
            abilities = {}
            addObject(abilities,conf.Ultralisk.burrow,890,  "action" ,  "burrow")
            addObject(abilities,conf.Ultralisk.unburrow,891,  "action" ,  "unburrow")


        AddAll([Changeling,Larva,Drone,Zergling,Corruptor,Broodlord,Overlord,Egg,Queen,Baneling,Roach,Hydralisk,Infestor,Ultralisk,Broodlord,Mutalisk,Overseer],types,abilities)

        ###ZERG Buildings
        def ZergMain(clazz):
            addObject(clazz.abilities,conf.ZergMain.worker_rally_point,908,  "rally" ,  "worker_rally")
            addObject(clazz.abilities,conf.ZergMain.worker_rally_target,909,  "rally" ,  "worker_rally")
            addObject(clazz.abilities,conf.ZergMain.unit_rally_point,910,  "rally" ,  "unit_rally")
            addObject(clazz.abilities,conf.ZergMain.unit_rally_target,911,  "rally" ,  "unit_rally")

            addObject(clazz.abilities,conf.ZergMain.queen,913,  "train" ,  "queen")
            addObject(clazz.abilities,conf.ZergMain.evolve_burrow,914,  "upgrade" ,  "burrow")
            addObject(clazz.abilities,conf.ZergMain.evolve_carapace,915,  "upgrade" ,  "carapace")
            addObject(clazz.abilities,conf.ZergMain.evolve_ventral_sacs,916,  "upgrade" ,  "ventral_sacs")
            return clazz

        @ZergMain
        @DataObject
        class Hatchery(SC2Object):
            code = conf.Hatchery.code
            abilities = {}
            addObject(abilities,conf.Hatchery.lair,924,  "morph" ,  "lair")
            addObject(abilities,conf.Hatchery.cancel_lair,925,  "cancel" ,  "cancel_lair")

        @ZergMain
        @DataObject
        class Lair(SC2Object):
            code = conf.Lair.code
            abilities = {}
            addObject(abilities,conf.Lair.hive,932,  "morph" ,  "hive")
            addObject(abilities,conf.Lair.cancel_hive,933,  "cancel" ,  "cancel_hive")

        @ZergMain
        @DataObject
        class Hive(SC2Object):
            code = conf.Hive.code
            abilities = {}

        @DataObject
        class Extractor():
            abilities = {}
            code = conf.Extractor.code

        @Research
        @DataObject
        class SpawningPool(SC2Object):
            code = conf.SpawningPool.code
            abilities = {}
            addObject(abilities,conf.SpawningPool.adrenal_glands,948,  "upgrade" ,  "adrenal_glands")
            addObject(abilities,conf.SpawningPool.metabolic_boost,949,  "upgrade" ,  "metabolic_boost")

        @Research
        @DataObject
        class EvolutionChamber(SC2Object):
            code = conf.EvolutionChamber.code
            abilities = {}
            addObject(abilities,conf.EvolutionChamber.melee_attack_1,956,  "upgrade" ,  "melee_attack_1")
            addObject(abilities,conf.EvolutionChamber.melee_attack_2,957,  "upgrade" ,  "melee_attack_2")
            addObject(abilities,conf.EvolutionChamber.melee_attack_3,958,  "upgrade" ,  "melee_attack_3")
            addObject(abilities,conf.EvolutionChamber.ground_carapace_1,959,  "upgrade" ,  "ground_carapace_1")
            addObject(abilities,conf.EvolutionChamber.ground_carapace_2,960,  "upgrade" ,  "ground_carapace_2")
            addObject(abilities,conf.EvolutionChamber.ground_carapace_3,961,  "upgrade" ,  "ground_carapace_3")
            addObject(abilities,conf.EvolutionChamber.missile_attack_1,962,  "upgrade" ,  "missile_attack_1")
            addObject(abilities,conf.EvolutionChamber.missile_attack_2,963,  "upgrade" ,  "missile_attack_2")
            addObject(abilities,conf.EvolutionChamber.missile_attack_3,964,  "upgrade" ,  "missile_attack_3")

        @Research
        @DataObject
        class RoachWarren(SC2Object):
            code = conf.RoachWarren.code
            abilities = {}
            addObject(abilities,conf.RoachWarren.glial_recon,971,  "upgrade" ,  "glial_recon")
            addObject(abilities,conf.RoachWarren.tunneling_claws,972,  "upgrade" ,  "tunneling_claws")

        @Research
        @DataObject
        class BanelingNest(SC2Object):
            code = conf.BanelingNest.code
            abilities = {}
            addObject(abilities,conf.BanelingNest.centrifugal_hooks,979,  "upgrade" ,  "centrifugal_hooks")

        @Research
        @DataObject
        class HydraliskDen(SC2Object):
            code = conf.HydraliskDen.code
            abilities = {}
            addObject(abilities,conf.HydraliskDen.grooved_spines,986,  "upgrade" ,  "grooved_spines")

        @Research
        @DataObject
        class InfestationPit(SC2Object):
            code = conf.InfestationPit.code
            abilities = {}
            addObject(abilities,conf.InfestationPit.pathogen_glands,993,  "upgrade" ,  "pathogen_glands")
            addObject(abilities,conf.InfestationPit.neural_parasite,994,  "upgrade" ,  "neural_parasite")

        @Research
        @DataObject
        class Spire(SC2Object):
            code = conf.Spire.code
            abilities = {}
            addObject(abilities,conf.Spire.flyer_attack_1,1001,  "upgrade" ,  "flyer_attack_1")
            addObject(abilities,conf.Spire.flyer_attack_2,1002,  "upgrade" ,  "flyer_attack_2")
            addObject(abilities,conf.Spire.flyer_attack_3,1003,  "upgrade" ,  "flyer_attack_3")
            addObject(abilities,conf.Spire.flyer_carapace_1,1004,  "upgrade" ,  "flyer_carapace_1")
            addObject(abilities,conf.Spire.flyer_carapace_2,1005,  "upgrade" ,  "flyer_carapace_2")
            addObject(abilities,conf.Spire.flyer_carapace_3,1006,  "upgrade" ,  "flyer_carapace_3")
            addObject(abilities,conf.Spire.greater_spire,1007,  "upgrade" ,  "greater_spire")
            addObject(abilities,conf.Spire.cancel_greater_spire,1008,  "upgrade" ,  "cancel_greater_spire")

        @Research
        @DataObject
        class GreaterSpire(Spire):
            code = conf.Spire.GreaterSpire.code

        @Research
        @DataObject
        class UltraliskCavern(SC2Object):
            code = conf.UltraliskCavern.code
            abilities = {}
            addObject(abilities,conf.UltraliskCavern.chitinous,1020,  "upgrade" ,  "chitinous")

        @DataObject
        class NydusWorm():
            code = conf.NydusWorm.code
            abilities = {}
            addObject(abilities,conf.NydusWorm.unload_all,1026,  "action" ,  "unload")
            addObject(abilities,conf.NydusWorm.unload_unit,1027,  "action" ,  "unload")
            addObject(abilities,conf.NydusWorm.load_unit,1028,  "action" ,  "load")

        @DataObject
        class NydusNetwork():
            code = conf.NydusNetwork.code
            abilities = {}
            addObject(abilities,conf.NydusNetwork.unload_all,1034,  "action" ,  "unload")
            addObject(abilities,conf.NydusNetwork.unload_unit,1035,  "action" ,  "unload")
            addObject(abilities,conf.NydusNetwork.load_unit,1036,  "action" ,  "load")
            addObject(abilities,conf.NydusNetwork.nydus,1037,  "build" ,  "nydus_worm")

        @DataObject
        class SpineCrawler():
            code = conf.SpineCrawler.code
            abilities = {}
            addObject(abilities,conf.SpineCrawler.uproot,1043,  "action" ,  "uproot")
            addObject(abilities,conf.SpineCrawler.root,1044,  "action" ,  "root")
            addObject(abilities,conf.SpineCrawler.cancel_root,1045,  "cancel" ,  "cancel_root")

        @DataObject
        class SporeCrawler():
            code = conf.SporeCrawler.code
            abilities = {}
            addObject(abilities,conf.SporeCrawler.uproot,1051,  "action" ,  "uproot")
            addObject(abilities,conf.SporeCrawler.root,1052,  "action" ,  "root")
            addObject(abilities,conf.SporeCrawler.cancel_root,1053,  "cancel" ,  "cancel_root")

        @DataObject
        class CreepTumor():
            code = conf.CreepTumor.code
            abilities = {}
            @DataObject
            class Burrowed():
                code = conf.CreepTumor.Burrowed.code
                abilities = {}
                addObject(abilities,conf.CreepTumor.Burrowed.creep_tumor,1063,  "action" ,  "creep")
                addObject(abilities,conf.CreepTumor.Burrowed.cancel_creep_tumor,1064,  "cancel" ,  "creep cancel")



        AddAll([Hatchery,Lair,Hive,SpawningPool, EvolutionChamber,
        RoachWarren,
        BanelingNest,
        HydraliskDen,
        InfestationPit,
        Spire,
        GreaterSpire,Extractor,
        UltraliskCavern,NydusWorm,NydusNetwork,SpineCrawler,SporeCrawler,CreepTumor,CreepTumor.Burrowed],types,abilities)

    for a in data.abilities.values():
        data.internalcodes[a["code"]] = a

    return data
