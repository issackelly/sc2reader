###This class holds all variable information between versions!
###These are codes, times, minerals, gas, and supply
class version(object):
	
	class Thrash():
		thrash = [0x4c00, 0x3601,0x5ba0,0x5601,0x58a0,0x2aa0,0x5b00,0x6600, 0x2a00, 0x5800, 0x7302,0x3100,0x5c01, 0x7061,0x6100, 0x7c02]
		         #0x15e09,0x16700,0x14502,0x12902,
		
	class DataObject():
		right_click = { "code" : 0x3700 }
		right_click_in_fog = { "code" : 0x5700 }

	class Moveable():
		stop = { "code" : 0x002400}
		hold = { "code" : 0x002602}
		move = { "code" : 0x002620}
		patrol = { "code" : 0x002621}
		follow = { "code" : 0x002620}

	class Attacker():
		attack_move = { "code" : 0x002a20}
		attack_object = { "code" : 0x002a40}

	class Supporter():
		scan_move = { "code" : 0x002623}  # attack move for units without attack
		scan_target = { "code" : 0x002623}  # attack move for units without attack

	class Building():
		cancel = { "code" : 0x006d00}

	class TerranBuilding():
		halt_build = { "code" : 0x007101}

	class Research():
		cancel = { "code" : 0x006c00}  # Generic ESC cancel
		cancel_unit = { "code" : 0x007100}  # Cancel + build id

	class Production():
		set_rally_point = { "code" : 0x005820}
		set_rally_target = { "code" : 0x005840}
		cancel = { "code" : 0x006c00}  # Generic ESC cancel
		cancel_unit = { "code" : 0x006d61}  # Cancel + build id

	class SCV():
		code = 0x004901
		gather_resources = { "code" : 0x006940}
		return_cargo = { "code" : 0x006901}
		toggle_auto_repair = { "code" : 0x007200}
		repair = { "code" : 0x007240}
		halt = { "code" : 0x00f30e}
		command_center = { "code" : 0x007320, "min" : 400, "gas" : 0, "time" : 100}
		supply_depot = { "code" : 0x007321, "min" : 100, "gas" : 0, "time" : 30}
		barracks = { "code" : 0x007323, "min" : 150, "gas" : 0 , "time" : 60}
		engineering_bay = { "code" : 0x007324, "min" : 125, "gas" : 0, "time" : 35}
		missle_turret = { "code" : 0x007325, "min" : 100, "gas" : 0, "time" : 25}
		bunker = { "code" : 0x007326, "min" : 100, "gas" : 0, "time" : 35}
		refinery = { "code" : 0x007302, "min" : 75, "gas" : 0, "time" : 30}
		sensor_tower = { "code" : 0x007328, "min" : 125, "gas" : 100, "time" : 25}
		ghost_academy = { "code" : 0x007329, "min" : 150, "gas" : 50, "time" : 40}
		factory = { "code" : 0x00732a, "min" : 150, "gas" : 100, "time" : 60}
		starport = { "code" : 0x00732b, "min" : 150, "gas" : 100, "time" : 50}
		armory = { "code" : 0x00732d, "min" : 150, "gas" : 100, "time" : 65}
		fusion_core = { "code" : 0x00732f, "min" : 150, "gas" : 150, "time" : 65}
	
	class SensorTower():
		code = 0x003401
		
	class MissileTurret():
		code = 0x003201
		
	class Refinery():
		code = 0x002f01
	
	class TechLab():
		code = 0x001e01
	
	class Reactor():
		code = 0x001f01
		
	class MULE():
		code = 0x00b901
		toggle_auto_repair = { "code" : 0x003a00}
		repair = { "code" : 0x003a40}

	class Marine():
		code = 0x004c01
		use_stim_pack_mixed = { "code" : 0x007500}

	class Marauder():
		code = 0x004f01
		use_stim_pack_mixed = { "code" : 0x007500}
		use_stim_pack = { "code" : 0x006200}

	class Ghost():
		code = 0x004e01
		cloak_on = { "code" : 0x007600}
		cloak_off = { "code" : 0x007601}
		nuke_start = { "code" : 0x016020}
		nuke_cancel = { "code" : 0x016001}
		hold_fire = { "code" : 0x003300}
		weapons_free = { "code" : 0x003400}
		emp_round = { "code" : 0x016320}
		sniper_round = { "code" : 0x007740}

	class SiegeTank():
		code = 0x003d01
		seige_mode_on = { "code" : 0x007900}
		seige_mode_off = { "code" : 0x007a00}

	class Reaper():
		code = 0x004d01
	
	class Hellion():
		code = 0x005101
		
	class Thor():
		code = 0x005001
		strike_cannons = { "code" : 0x006440}

	class Viking():
		code = 0x003e01
		assault_mode_on = { "code" : 0x007f00}
		assault_mode_off = { "code" : 0x008000}

	class Medivac():
		code = 0x005201
		unload_all = { "code" : 0x007c22 }
		unload_all_moving = { "code" : "UA.UNLOAD_ALL,U.MEDIVAC"}
		unload_unit = { "code" : 0x007c63}
		load_unit = { "code" : 0x007c40}
		toggle_auto_heal = { "code" : 0x007800}
		heal = { "code" : 0x020803}

	class Raven():
		code = 0x005401
		auto_turret = { "code" : 0x017c20}
		point_defence_drone = { "code" : 0x003f20}
		seeker_missle = { "code" : 0x004b40}

	class AutoTurret():
		code = 0x003b01
		
	class PointDefenceDrone():
		code = 0x002501
		
	class Banshee():
		code = 0x005301
		cloak_on = { "code" : 0x007b00}
		cloak_off = { "code" : 0x007b01 }

	class Battlecruiser():
		code = 0x005501
		yamato_cannon = { "code" : 0x007e40}

	class TerranMain():
		set_rally_point = { "code" : 0x005a20}
		set_rally_target = { "code" : 0x005a20}
		train_scv = { "code" : 0x010d00, "min" : 50, "gas" : 0, "time" : 17, "supply" : 1}

	class CommandCenter():
		code = 0x002d01
		lift_up = { "code" : 0x010300}
		lift_down = { "code" : 0x010420}
		unload_all = { "code" : 0x010201 }
		unload_unit = { "code" : 0x010263}
		load_unit = { "code" : 0x010204}
		upgradeto_orbital_command = { "code" : 0x015500, "min" : 150, "gas" : 0, "time" : 35}
		upgradeto_orbital_command_cancel = { "code" : 0x015501}
		upgradeto_planetary_fortress = { "code" : 0x015000, "min" : 150, "gas" : 150, "time" : 50}
		upgradeto_planetary_fortress_cancel = { "code" : 0x030f01}
		class Flying():
			code = 0x004001
			
	class OrbitalCommand():
		code = 0x00a001
		lift_up = { "code" : 0x015800	}
		lift_down = { "code" : 0x015920}
		mule_target = { "code" :0x004c20}
		mule_location = { "code" :0x004c20}
		extra_supply = { "code" : 0x006340}
		scanner_sweep = { "code" :0x007d20}
		class Flying():
			code = 0x00a201
			
	class PlanetaryFortress():
		code = 0x009e01
		cancel_pf = { "code" : 0x012e00}  #????

	class SupplyDepot():
		code = 0x002e01
		lower_supply = { "code" : 0x010f00}
		raise_supply = { "code" : 0x011000}
		class Lowered():
			code = 0x004b01

	class EngineeringBay():
		code = 0x003101
		hisec_auto_tracking = { "code" : 0x011400, "min" : 100, "gas" : 100, "time" : 80}
		building_armor = { "code" : 0x011401, "min" : 150, "gas" : 150, "time" : 140}
		inftantry_weapons_1 = { "code" : 0x011402, "min" : 100, "gas" : 100, "time" : 160}
		inftantry_weapons_2 = { "code" : 0x011403, "min" : 175, "gas" : 175, "time" : 190}
		inftantry_weapons_3 = { "code" : 0x011404, "min" : 250, "gas" : 250, "time" : 220}
		neosteel_frame = { "code" :  0x011405, "min" : 100, "gas" : 100, "time" : 110}
		inftantry_armor_1 = { "code" :0x011406, "min" : 100, "gas" : 100, "time" : 160}
		inftantry_armor_2 = { "code" :0x011407, "min" : 175, "gas" : 175, "time" : 190}
		inftantry_armor_3 = { "code" :0x011408, "min" : 250, "gas" : 250, "time" : 220}

	class GhostAcademy():
		code = 0x003501
		arm_silo_w_nuke = { "code" : 0x011600, "min" : 100, "gas" : 100, "time" : 60}
		personal_cloaking = { "code" : 0x011a00, "min" : 150, "gas" : 150, "time" : 120}
		moebius_reactor = { "code" : 0x011a01, "min" : 100, "gas" : 100, "time" : 80}

	class FusionCore():
		code = 0x003a01
		yamato_cannon = { "code" : 0x015d00, "min" : 150, "gas" : 150, "time" : 60}

	class Bunker():
		code = 0x003301
		salvage = { "code" : 0x016200}
		stimpack = { "code" : 0x017100}
		unload_all = { "code" : 0x010101}
		unload_unit = { "code" : 0x010163}
		load_unit = { "code" : 0x20020}

	class Armory():
		code = 0x003901
		vehicle_plating_1 = { "code" :0x011b02, "min" : 100, "gas" : 100, "time" : 160}
		vehicle_plating_2 = { "code" : 0x011b03,  "min" : 175, "gas" : 175, "time" : 190}
		vehicle_plating_3 = { "code" : 0x011b04, "min" : 250, "gas" : 250, "time" : 220}
		vehicle_weapons_1 = { "code" : 0x011b05, "min" : 100, "gas" : 100, "time" : 160}
		vehicle_weapons_2 = { "code" : 0x011b06, "min" : 175, "gas" : 175, "time" : 190}
		vehicle_weapons_3 = { "code" : 0x011b07, "min" : 250, "gas" : 250, "time" : 220}
		ship_plating_1 = { "code" : 0x011b08, "min" : 100, "gas" : 100, "time" : 160}
		ship_plating_2 = { "code" : 0x011b09, "min" : 175, "gas" : 175, "time" : 190}
		ship_plating_3 = { "code" : 0x011b0a, "min" : 250, "gas" : 250, "time" : 220}
		ship_weapons_1 = { "code" : 0x011b0b, "min" : 100, "gas" : 100, "time" : 160}
		ship_weapons_2 = { "code" : 0x011b0c, "min" : 175, "gas" : 175, "time" : 190}
		ship_weapons_3 = { "code" : 0x011b0d, "min" : 250, "gas" : 250, "time" : 220}

	
	class Barracks():
		code = 0x003001
		marine = { "code" : 0x011100, "min" : 50, "gas" : 0, "time" : 25, "supply" : 1}
		reaper = { "code" : 0x011101, "min" : 50, "gas" : 50, "time" : 45, "supply" : 1}
		ghost = { "code" : 0x011102, "min" : 150, "gas" : 150, "time" : 40, "supply" : 2}
		marauder = { "code" : 0x011103, "min" : 100, "gas" : 25, "time" : 30, "supply" : 2}
		
		lift_up = { "code" : 0x010600}
		lift_down = { "code" : 0x010e20}
	
		addon_techlab = { "code" : 0x010500 ,"min" : 50, "gas" : 25, "time" : 25}
		addon_techlab_move = { "code" : 0x010520,"min" : 50, "gas" : 25, "time" : 25}
		addon_techlab_cancel = { "code" : 0x02c406}

		addon_reactor = { "code" : 0x010501,"min" : 50, "gas" : 50, "time" : 50}
		addon_reactor_move = { "code" : 0x010521,"min" : 50, "gas" : 50, "time" : 50}
		addon_reactor_cancel = { "code" : 0x02c406}

		class Techlab():
			code = 0x004101
			nitropacks = { "code" : 0x011503, "min" : 50, "gas" : 50, "time" : 100}
			stimpack = { "code" : 0x011700, "min" : 100, "gas" : 100, "time" : 140}
			combat_shield = { "code" : 0x011701, "min" : 100, "gas" : 100, "time" : 110}
			concussive_shells = { "code" : 0x011702, "min" : 50, "gas" : 50, "time" : 60}
			
			cancel_research = { "code" : 0x012f00}
			cancel_specific_research = { "code" : 0x012f31}

		class Reactor():
			code = 0x4201

		class Flying():
			code = 0x004a01

	class Factory():
		code = 0x003701 
		lift_up = { "code" : 0x010800}
		lift_down = { "code" : 0x010b20}

		addon_techlab = { "code" : 0x010700,"min" : 50, "gas" : 25, "time" : 25}
		addon_techlab_move = { "code" : 0x010720,"min" : 50, "gas" : 25, "time" : 25}
		addon_techlab_cancel = { "code" : 0x2c606}

		addon_reactor = { "code" : 0x010701,"min" : 50, "gas" : 50, "time" : 50}
		addon_reactor_move = { "code" : 0x010721,"min" : 50, "gas" : 50, "time" : 50}
		addon_reactor_cancel = { "code" : 0x02c606}

		seige_tank = { "code" : 0x011201, "min" : 150, "gas" : 125, "time" : 45, "supply" : 3}
		thor = { "code" : 0x011204, "min" : 300, "gas" : 200, "time" : 60, "supply" : 6}
		hellion = { "code" : 0x011205, "min" : 100, "gas" : 0, "time" : 30, "supply" : 2}

		class Techlab():
			code = 0x004301
			siege_tech = { "code" : 0x011800, "min" : 100, "gas" : 100, "time" : 80}
			infernal_preignighter = { "code" : 0x011801, "min" : 150, "gas" : 150, "time" : 110}
			strike_cannon = { "code" : 0x011802, "min" : 150, "gas" : 150, "time" : 110}
			
			cancel_research = { "code" : 0x012f00}
			cancel_specific_research = { "code" : 0x012f31}

		class Reactor():
			code = 0x4401

		class Flying():
			code = 0x004701

	class Starport():
		code = 0x003701
		lift_up = { "code" : 0x010a00}
		lift_down = { "code" : 0x010c20}

		addon_techlab = { "code" : 0x010900,"min" : 50, "gas" : 25, "time" : 25}
		addon_techlab_move = { "code" : 0x010920,"min" : 50, "gas" : 25, "time" : 25}
		addon_techlab_cancel = { "code" : 0x02806}

		addon_reactor = { "code" : 0x010901,"min" : 50, "gas" : 50, "time" : 50}
		addon_reactor_move = { "code" : 0x010921,"min" : 50, "gas" : 50, "time" : 50}
		addon_reactor_cancel = { "code" : 0x02806}

		medivac = { "code" : 0x011300, "min" : 100, "gas" : 100, "time" : 42, "supply" : 2}
		banshee = { "code" : 0x011301, "min" : 150, "gas" : 100, "time" : 60, "supply" : 3}
		raven = { "code" : 0x011302, "min" : 100, "gas" : 200, "time" : 60, "supply" : 2}
		battlecruiser = { "code" : 0x011303, "min" : 50, "gas" : 0, "time" : 25, "supply" : 1}
		viking = { "code" : 0x011304, "min" : 150, "gas" : 75, "time" : 42, "supply" : 2}
		
		class Techlab():
			code = 0x004501
			cloaking_field = { "code" : 0x011900, "min" : 200, "gas" : 200, "time" : 110}
			caduceus_reactor = { "code" : 0x011902, "min" : 100, "gas" : 100, "time" : 80}
			corvid_reactor = { "code" : 0x011903, "min" : 150, "gas" : 150, "time" : 110}
			seeker_missle = { "code" : 0x011906,  "min" : 150, "gas" : 150, "time" : 110}
			durable_materials = { "code" : 0x011907, "min" : 150, "gas" : 150, "time" : 110}
			
			cancel_research = { "code" : 0x012f00}
			cancel_specific_research = { "code" : 0x012f31}

		class Reactor():
			code = 0x4601

		class Flying():
			code = 0x004801

	 # # # # # # # # # # # # # # # # # # # # # # # # # # #
	 # # Protoss Units
	 # # # # # # # # # # # # # # # # # # # # # # # # # # #

	class Probe():
		code = 0x007001
		return_cargo = { "code" : 0x006a01}
		gather_resources = {"code" : 0x006a40}
		nexus = { "code" : 0x011c20, "min" : 400, "gas" : 0, "time" : 100}
		pylon = { "code" : 0x011c21, "min" : 100, "gas" : 0, "time" : 25}
		gateway = { "code" : 0x011c23, "min" : 150, "gas" : 0, "time" : 65}
		forge = { "code" : 0x011c24, "min" : 150, "gas" : 0, "time" : 45}
		fleet_beacon = { "code" : 0x011c25, "min" : 300, "gas" : 200, "time" : 60}
		twilight_council = { "code" : 0x011c26, "min" : 150, "gas" : 100, "time" : 50}
		photon_cannon = { "code" : 0x011c27, "min" : 150, "gas" : 0, "time" : 40}
		assimilator = { "code" : 0x011c02, "min" : 100, "gas" : 0, "time" : 30}
		stargate = { "code" : 0x011c29,  "min" : 150, "gas" : 150, "time" : 60}
		templar_archives = { "code" : 0x011c2a, "min" : 150, "gas" : 200, "time" : 50}
		dark_shrine = { "code" : 0x011c2b, "min" : 100, "gas" : 250, "time" : 100}
		robotics_bay = { "code" : 0x011c2c, "min" : 200, "gas" : 200, "time" : 65}
		robotics_facility = { "code" : 0x011c2d, "min" : 200, "gas" : 100, "time" : 65}
		cybernetics_core = { "code" : 0x011c2e, "min" : 150, "gas" : 0, "time" : 50}

	class Zealot():
		code = 0x006501
		
	class Stalker():
		code = 0x006601
		blink = { "code" : 0x014c20}

	class Sentry():
		code = 0x006901
		hallucinate_archon = { "code" : 0x004000}
		hallucinate_colossus = { "code" : 0x004100}
		hallucinate_high_templar = { "code" : 0x004200}
		hallucinate_immortal = { "code" : 0x004300}
		hallucinate_phoenix = { "code" : 0x004400}
		hallucinate_probe = { "code" : 0x004500}
		hallucinate_stalker = { "code" : 0x004600}
		hallucinate_void_ray = { "code" : 0x004700}
		hallucinate_warp_prism = { "code" : 0x004800}
		hallucinate_zealot = { "code" : 0x004900}
		guardian_shield = { "code" : 0x003900}
		force_field = { "code" : 0x015a20}
	
	class HighTemplar():
		code = 0x006701
		psionic_storm = { "code" : 0x012220}
		feedback = { "code" : 0x003d40}
		merge_into_archon = { "code" : 0x017d00}

	class DarkTemplar():
		code = 0x006801
		merge_into_archon = { "code" : 0x017d00}

	class Archon():
		code = 0x00a801

	class WarpPrism():
		code = 0x006d01
		unload_all = { "code" : 0x011d22}
		unload_all_moving = { "code" : 0x011d42}
		unload_unit = { "code" : 0x011d63}
		load_unit = { "code" : 0x011d40}
		phase_mode = { "code" : 0x015b00}
		transport_mode = { "code" : 0x015c00}
		class Phasing():
			code = 0x00a401

	class Voidray():
		code = 0x006c01
		
	class Pheonix():
		code = 0x006a01
		gravitation_beam_on = { "code" : 0x004d00}
		
	class Colossus():
		code = 0x001d01 
		
	class Carrier():
		code = 0x006b01
		interceptor = { "code" : 0x012500}

	class Observer():
		code = 0x006e01
	
	class Mothership():
		code = 0x002401
		vortex = { "code" : 0x016420}
		mass_recall = { "code" : 0x003e20}

	class Immortal():
		code = 0x006f01
		
	class Pylon():
		code = 0x005801
		
	class Assimilator():
		code = 0x005901 
	
	class PhotonCannon():
		code = 0x005e01
			
	class Nexus():
		code = 0x005701
		probe = { "code" : 0x012100,  "min" : 50, "gas" : 0, "time" : 17, "supply" : 1}
		mothership = { "code" : 0x003c00, "min" : 400, "gas" : 400, "time" : 160 , "supply" : 8}
		chronoboost = { "code" : 0x006640}
		set_rally_point = { "code" : 0x005b40}
		set_rally_target = { "code" : 0x005b20}

	class Gateway():
		code = 0x005a01
		zealot = { "code" : 0x011e00, "min" : 100, "gas" : 0, "time" : 38, "supply" : 2}
		stalker = { "code" : 0x011e01, "min" : 125, "gas" : 50, "time" : 42, "supply" : 2}
		high_templar = { "code" : 0x011e03,  "min" : 50, "gas" : 150, "time" : 55, "supply" : 2}
		dark_templar = { "code" : 0x011e04, "min" : 125, "gas" : 125, "time" : 55, "supply" : 2}
		sentry = { "code" : 0x011e05, "min" : 50, "gas" : 100, "time" : 42, "supply" : 2}
		to_warpgate = {"code" : 0x015600}
		class WarpGate():
			code = 0x00a101
			warp_zealot = { "code" : 0x014820, "min" : 100, "gas" : 0, "time" : 5, "supply" : 2}
			warp_stalker = { "code" : 0x014821, "min" : 125, "gas" : 50, "time" : 5, "supply" : 2}
			warp_high_templar = { "code" : 0x014823, "min" : 50, "gas" : 150, "time" : 5, "supply" : 2}
			warp_dark_templar = { "code" : 0x014824, "min" : 125, "gas" : 125, "time" : 5, "supply" : 2}
			warp_sentry = { "code" : 0x014825, "min" : 50, "gas" : 100, "time" : 5, "supply" : 2}
			to_gateway = {"code" : 0x015700}

	class Forge():
		code = 0x005b01
		ground_weapons_1 = { "code" : 0x012600, "min" : 100, "gas" : 100, "time" : 160}
		ground_weapons_2 = { "code" : 0x012601, "min" : 175, "gas" : 175, "time" : 190}
		ground_weapons_3 = { "code" : 0x012602, "min" : 250, "gas" : 250, "time" : 220}
		ground_armour_1 = { "code" : 0x012603, "min" : 100, "gas" : 100, "time" : 160}
		ground_armour_2 = { "code" : 0x012604, "min" : 175, "gas" : 175, "time" : 190}
		ground_armour_3 = { "code" : 0x012605, "min" : 250, "gas" : 250, "time" : 220}
		shield_1 = { "code" : 0x012606, "min" : 200, "gas" : 200, "time" : 160}
		shield_2 = { "code" : 0x012607, "min" : 300, "gas" : 300, "time" : 190}
		shield_3 = { "code" : 0x012608, "min" : 400, "gas" : 400, "time" : 220}


	class CyberneticsCore():
		code = 0x006401
		air_weapons_1 = { "code" : 0x015e00, "min" : 100, "gas" : 100, "time" : 160}
		air_weapons_2 = { "code" : 0x015e01, "min" : 175, "gas" : 175, "time" : 190}
		air_weapons_3 = { "code" : 0x015e02, "min" : 250, "gas" : 250, "time" : 220}
		air_armour_1 = { "code" : 0x015e03,  "min" : 150, "gas" : 150, "time" : 160}
		air_armour_2 = { "code" : 0x015e04, "min" : 225, "gas" : 225, "time" : 190}
		air_armour_3 = { "code" : 0x015e05,"min" : 300, "gas" : 300, "time" : 220}
		warpgate = { "code" : 0x015e06,  "min" : 50, "gas" : 50, "time" : 140}
		hallucination = { "code" : 0x015e07, "min" : 100, "gas" : 100, "time" : 80}


	class RoboticsFacility():
		code = 0x006301
		warp_prism = { "code" : 0x012000, "min" : 200, "gas" : 0, "time" : 50, "supply" : 2}
		observer = { "code" : 0x012001, "min" : 25, "gas" : 75, "time" : 40, "supply" : 1}
		colossus = { "code" : 0x012002, "min" : 300, "gas" : 200, "time" : 75, "supply" : 6}
		immortal = { "code" : 0x012003, "min" : 250, "gas" : 100, "time" : 55, "supply" : 4}


	class Stargate():
		code = 0x005f01
		pheonix = { "code" : 0x011f00, "min" : 150, "gas" : 100, "time" : 35, "supply" : 2}
		carrier = { "code" : 0x011f02, "min" : 350, "gas" : 250, "time" : 120, "supply" : 6}
		voidray = { "code" : 0x011f04, "min" : 250, "gas" : 150, "time" : 60, "supply" : 3}

	class DarkShrine():
		code = 0x006101
		
	class TwilightCouncil():
		code = 0x005d01
		charge = { "code" : 0x015f00, "min" : 200, "gas" : 200, "time" : 140}
		blink = { "code" : 0x015f01,  "min" : 150, "gas" : 100, "time" : 110}


	class FleetBeacon():
		code = 0x005c01
		gavitation_catapault = { "code" : 0x003701, "min" : 150, "gas" : 150, "time" : 80} #Graviton Catapult',


	class TemplarArchive():
		code = 0x006001
		psi_storm = { "code" : 0x012804, "min" : 200, "gas" : 200, "time" : 110}


	class RoboticsBay():
		code = 0x006201
		grav_booster = { "code" : 0x012701,  "min" : 100, "gas" : 100, "time" : 80}
		grav_drive = { "code" : 0x012702, "min" : 100, "gas" : 100, "time" : 80}
		thermal_lance = { "code" : 0x012705, "min" : 200, "gas" : 200, "time" : 140}


	 # # # # # # # # # # # # # # # # # # # # #
	 # # Zerg
	 # # # # # # # # # # # # # # # # # # # # #

	class Larva():
		code = 0x00b101
		drone = {"code" : 0x013300, "min" : 50, "gas" : 0, "time" : 17, "supply" : 1}
		zergling = { "code" : 0x013301,  "min" : 50, "gas" : 0, "time" : 24, "supply" : 1}
		overlord = { "code" : 0x013302, "min" : 100, "gas" : 0, "time" : 25}
		hydralisk = { "code" : 0x013303, "min" : 100, "gas" : 50, "time" : 33, "supply" : 2}
		mutalisk = { "code" : 0x013304, "min" : 100, "gas" : 100, "time" : 33, "supply" : 2}
		ultralisk = { "code" : 0x013306, "min" : 300, "gas" : 200, "time" : 70, "supply" : 6}
		roach = { "code" : 0x013309, "min" : 75, "gas" : 25, "time" : 27, "supply" : 2}
		infestor = { "code" : 0x01330a, "min" : 100, "gas" : 150, "time" : 50, "supply" : 2}
		corrupter = { "code" : 0x01330b, "min" : 150, "gas" : 150, "time" : 40, "supply" : 2}


	class Egg():
		code = 0x008301
		cancel = { "code" : "UA.CANCEL_BANELING_MORPHING,U.ZERGLING"} #Cancel',


	class Drone():
		code = 0x008401
		gather_resources = { "code" : 0x012a20} #Gather Resources (Zerg)',
		return_cargo = { "code" : 0x012a01} #Return cargo',
		burrow = { "code" : 0x013700} #Burrow',
		unburrow = { "code" : 0x013800}
		
		hatchery = { "code" : 0x012920, "min" : 300, "gas" : 0, "time" : 100, "supply" : -1}
		spawning_pool = { "code" : 0x012923, "min" : 200, "gas" : 0, "time" : 65, "supply" : -1}
		evolution_chamber = { "code" : 0x012924, "min" : 75, "gas" : 0, "time" : 35, "supply" : -1}
		hydra_den = { "code" : 0x012925,  "min" : 100, "gas" : 100, "time" : 40, "supply" : -1}
		spire = { "code" : 0x012926, "min" : 200, "gas" : 200, "time" : 100, "supply" : -1}
		ultralisk_cavern = { "code" : 0x012927, "min" : 150, "gas" : 200, "time" : 65, "supply" : -1}
		extractor = { "code" : 0x012902, "min" : 25, "gas" : 0, "time" : 30, "supply" : -1}
		infestation_pit = { "code" : 0x012928,  "min" : 100, "gas" : 100, "time" : 50, "supply" : -1}
		nydus_network= { "code" : 0x012929, "min" : 150, "gas" : 200, "time" : 50, "supply" : -1}
		baneling_nest = { "code" : 0x01292a, "min" : 100, "gas" : 50, "time" : 60, "supply" : -1}
		roach_warren = { "code" : 0x01292d, "min" : 150, "gas" : 0, "time" : 55, "supply" : -1}
		spine_crawler = { "code" : 0x01292e, "min" : 100, "gas" : 0, "time" : 50, "supply" : -1}
		spore_crawler = { "code" : 0x01292f, "min" : 75, "gas" : 0, "time" : 30, "supply" : -1}
		
		class Burrowed():
			code = 0x009001

	class Queen():
		code = 0x009a01
		burrow = { "code" : 0x014900} #Burrow',
		unburrow = { "code" : 0x014a00}
		creep_tumor = { "code" : 0x017620} #Creep Tumor',
		larva = { "code" : 0x006140} #Larva',
		transfuse = { "code" : 0x016740} #Transfuse',
		class Burrowed():
			code = 0x009901

	class Mutalisk():
		code = 0x008801
		
	class Zergling():
		code = 0x008501
		burrow = { "code" : 0x013d00} #Burrow',
		unburrow = { "code" : 0x013e00}
		baneling = { "code" : 0x003b00, "min" : 25, "gas" : 25, "time" : 20}
		
		class BanelingCocoon():
			code = 0x002201
			cancel_baneling = { "code" : 0x0}
			
		class Burrowed():
			code = 0x009301

	class Baneling():
		code = 0x002301
		burrow = { "code" : 0x013500} #Burrow',
		unburrow = { "code" : 0x013600}
		explode = { "code" : 0x003600} #Explode',
		attack_structure = { "code" : 0x005e00} #Attack Structure'
		class Burrowed():
			code = 0x008f01

	class Roach():
		code = 0x008a01
		burrow = { "code" : 0x013b00} #Burrow',
		unburrow = { "code" : 0x013c00}
		class Burrowed():
			code = 0x009201
			

	class Hydralisk():
		code = 0x008701
		burrow = { "code" : 0x013900} #Burrow',
		unburrow = { "code" : 0x013a00}
		class Burrowed():
			code = 0x009101 
			
	class Infestor():
		code = 0x008b01
		burrow = { "code" : 0x014d00} #Burrow',
		unburrow = { "code" : 0x014e00}

		fungal_growth = { "code" : 0x003820} #Fungal Growth',
		infested_terran = { "code" : 0x005f20} #Infested Terran',
		neural_parasite = { "code" : 0x006040}
		class Burrowed():
			code = 0x009b01 

	class Ultralisk():
		code = 0x008901
		burrow = { "code" : 0x015300} #Burrow',
		unburrow = { "code" : 0x015400}
		class Burrowed():
			code = 0x009f01

	class InfestedTerran():
		code = 0x002101
		class Burrowed():
			code = 0x009401
		class Egg():
			code = 0x00b001 

	class Corruptor():
		code = 0x008c01
		corruption = { "code" : 0x003200} #Corruption',
		broodlord = { "code" : 0x013400, "min" : 150, "gas" : 150, "time" : 34, "supply" : 2}
		
		class BroodlordCocoon():
			code = 0x008d01
			cancel_broodlord = { "code" : 0x023301}
			
		class Broodlord():
			code = 0x008e01

	class Broodling():
		code = 0x00d001
		
	class Overlord():
		code = 0x008601
		unload_all = { "code" : 0x014522}
		unload_all_moving = { "code" : 0x014501}
		unload_unit = { "code" : 0x014563}
		load_unit = { "code" : 0x014504}
		creep = { "code" : 0x017500} #Generate Creep',
		cancel_creep = { "code" : 0x017501} #Stop generating Creep',
		unload_at = { "code" : 0x014501} #Unload all at',
		
		overseer = { "code" : 0x014f00, "min" : 50, "gas" : 100, "time" : 17}
		cancel_overseer = { "code" : 0x014f01}
		
		class OverseerCocoon():
			code = 0x009c01
			
	class Overseer():
		code = 0x009d01
		changling = { "code" : 0x005100} #Changeling',
		contaminate = { "code" : 0x020440} #Contaminate',

	class Changeling():
		code = 0x002601

	class NydusWorm():
		code = 0x00a901
		unload_all = { "code" : 0x014b01}
		unload_unit = { "code" : 0x014b63}
		load_unit = { "code" : 0x014b40}

	class SpineCrawler(Building, Attacker):
		code = 0x007e01
		uproot = { "code" : 0x017700}
		root = { "code" : 0x017920}
		cancel_root = { "code" : 0x33901}
		class Uprooted():
			code = 0x00a601

	class SporeCrawler():
		code = 0x007f01
		uproot = { "code" : 0x017800}
		root = { "code" : 0x017a20}
		cancel_root = { "code" : 0x033901}
		class Uprooted():
			code = 0x00a701
	class Extractor():
		code = 0x007401
		
	class ZergMain():
		worker_rally_point = { "code" : 0x005c21} #Set worker rally point',
		worker_rally_target = { "code" : 0x005c21} #Set worker rally target',
		unit_rally_point = { "code" : 0x005c20} #Set unit rally point',
		unit_rally_target = { "code" : 0x005c20} #Set unit rally target',
		
		queen = { "code" : 0x016500, "min" : 150, "gas" : 0, "time" : 50, "supply" : 2}
		evolve_burrow = { "code" : 0x012f03, "min" : 100, "gas" : 100, "time" : 100}
		evolve_carapace = { "code" : 0x012f01, "min" : 100, "gas" : 100, "time" : 60}
		evolve_ventral_sacs = { "code" : 0x012f02, "min" : 200, "gas" : 200, "time" : 130}


	class Hatchery():
		code = 0x007201
		lair = { "code" : 0x012c00, "min" : 150, "gas" : 100, "time" : 80}
		cancel_lair = { "code" : 0x012c01}
	
	class Lair():
		code = 0x008001
		hive = { "code" : 0x012d00, "min" : 200, "gas" : 150, "time" : 100}
		cancel_hive = { "code" : 0x012d01}

	class Hive():
		code = 0x008101

	class SpawningPool():
		code = 0x007501
		adrenal_glands = { "code" : 0x013000, "min" : 200, "gas" : 200, "time" : 130}
		metabolic_boost = { "code" : 0x013001, "min" : 100, "gas" : 100, "time" : 110}


	class EvolutionChamber():
		code = 0x007601
		melee_attack_1 = { "code" : 0x012b00, "min" : 100, "gas" : 100, "time" : 160}
		melee_attack_2 = { "code" : 0x012b01, "min" : 150, "gas" : 150, "time" : 190}
		melee_attack_3 = { "code" : 0x012b02, "min" : 200, "gas" : 200, "time" : 200}
		ground_carapace_1 = { "code" : 0x012b03, "min" : 150, "gas" : 150, "time" : 160}
		ground_carapace_2 = { "code" : 0x012b04, "min" : 225, "gas" : 225, "time" : 190}
		ground_carapace_3 = { "code" : 0x012b05, "min" : 300, "gas" : 300, "time" : 220}
		missile_attack_1 = { "code" : 0x012b06, "min" : 100, "gas" : 100, "time" : 160}
		missile_attack_2 = { "code" : 0x012b07, "min" : 150, "gas" : 150, "time" : 190}
		missile_attack_3 = { "code" : 0x012b08, "min" : 200, "gas" : 200, "time" : 220}


	class RoachWarren():
		code = 0x007d01
		glial_recon = { "code" : 0x005d01, "min" : 100, "gas" : 100, "time" : 110} #Evolve Glial Reconstitution',
		tunneling_claws = { "code" : 0x005d02, "min" : 150, "gas" : 150, "time" : 110} #Evolve Tunneling Claws',


	class BanelingNest():
		code = 0x007c01
		centrifugal_hooks = { "code" : 0x015200, "min" : 150, "gas" : 150, "time" : 110}

	class CreepTumor():
		code = 0x007301
		class Burrowed():
			code = 0x00a501
			creep_tumor = { "code" : 0x017b20}
			cancel_creep_tumor = { "code" : 0x3fa06}

	class HydraliskDen():
		code = 0x007701
		grooved_spines = { "code" : 0x013102, "min" : 150, "gas" : 150, "time" : 80}


	class InfestationPit():
		code = 0x007a01
		pathogen_glands = { "code" : 0x015102, "min" : 150, "gas" : 150, "time" : 80}
		neural_parasite = { "code" : 0x015103,  "min" : 150, "gas" : 150, "time" : 110}


	class NydusNetwork():
		code = 0x007b01
		unload_all = { "code" : 0x014b01}
		unload_unit = { "code" : 0x014b63}
		load_unit = { "code" : 0x014b40}
		nydus= { "code" : 0x017e20,"min" : 100, "gas" : 100, "time" : 20}


	class Spire():
		code = 0x007801
		flyer_attack_1 = { "code" : 0x013200, "min" : 100, "gas" : 100, "time" : 160}
		flyer_attack_2 = { "code" : 0x013201, "min" : 175, "gas" : 175, "time" : 190}
		flyer_attack_3 = { "code" : 0x013202,  "min" : 250, "gas" : 250, "time" : 220}
		flyer_carapace_1 = { "code" : 0x013203, "min" : 150, "gas" : 150, "time" : 160}
		flyer_carapace_2 = { "code" : 0x013204, "min" : 225, "gas" : 225, "time" : 190}
		flyer_carapace_3 = { "code" : 0x013205, "min" : 300, "gas" : 300, "time" : 220}
		greater_spire = { "code" : 0x012e00, "min" : 100, "gas" : 150, "time" : 100}
		cancel_greater_spire = { "code" : 0x012e01 }
		class GreaterSpire():
			code = 0x008201

	class UltraliskCavern():
		code = 0x007901
		chitinous = { "code" : 0x006702, "min" : 150, "gas" : 150, "time" : 110}
		

