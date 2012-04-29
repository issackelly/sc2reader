###This class holds all variable information between versions!
###These are codes, times, minerals, gas, and supply
class version(object):

	class Thrash():
		thrash = [0x72a3, 0x72a0, 0x72a1, 0x4b40, 0x72a4, 0x2aa0, 0x6c00, 0x72a6, 0x5601]
		#['0x10ba0', '0x144a2', '0x15d09', '0x72a5', '0x128a6', '0x72a8', '0x128a4', '0x128a3', '0x162a0', '0x128a0', '0x7ba2', '0x103a0', '0x7ca0', '0x147a3', '0x147a0', '0x147a1', '0x10da0', '0x147a4', '0x147a5', '0x11ba9', '0x13d00', '0x26a0', '0x5b41', '0x11ba0', '0x11ba1', '0x11ba3', '0x11ba4', '0x16f40', '0x11ba6', '0x11ba7', '0x1fa0e', '0x11bab', '0x4ba0', '0x10aa0', '0x106a1', '0x37a0', '0x26a1', '0x128a5', '0x26a3', '0x72a9', '0x6240', '0x7000', '0x175a0', '0x178a0', '0x104a1', '0x6f00', '0x128a9', '0x17ba0', '0x72ab', '0x3140', '0x158a0', '0x72aa', '0x72af', '0x72ad', '0x15c01', '0x128af', '0x128ae', '0x128ad', '0x17aa0', '0x128aa', '0x159a0', '0x128a8', '0x106a0', '0x14f01', '0x14442', '0x5940', '0x1840e', '0x2640', '0x10821', '0x6c61', '0x10620', '0x14ba0', '0x17da0', '0x108a0', '0x13c00', '0x11baa', '0x17801', '0x11bac', '0x11bad', '0x11bae', '0x14422', '0x7b42']

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
		cancel = { "code" : 0x006b00}

	class TerranBuilding():
		halt_build = { "code" : 0x007001}

	class Research():
		cancel = { "code" : 0x006c00}  # Generic ESC cancel
		cancel_unit = { "code" : 0x006b00}  # Cancel + build id

	class Production():
		set_rally_point = { "code" : 0x005720}
		set_rally_target = { "code" : 0x005720}
		cancel = { "code" : 0x006b00}  # Generic ESC cancel
		cancel_unit = { "code" : 0x006b00}  # Cancel + build id

	class SCV():
		code = 0x004901
		gather_resources = { "code" : 0x006840}
		return_cargo = { "code" : 0x006801}
		toggle_auto_repair = { "code" : 0x007100}
		repair = { "code" : 0x007140}
		halt = { "code" : 0x00f20e}
		command_center = { "code" : 0x007220, "min" : 400, "gas" : 0, "time" : 100}
		supply_depot = { "code" : 0x007221, "min" : 100, "gas" : 0, "time" : 30}
		barracks = { "code" : 0x007223, "min" : 150, "gas" : 0 , "time" : 60}
		engineering_bay = { "code" : 0x007224, "min" : 125, "gas" : 0, "time" : 35}
		missle_turret = { "code" : 0x007225, "min" : 100, "gas" : 0, "time" : 25}
		bunker = { "code" : 0x007226, "min" : 100, "gas" : 0, "time" : 35}
		refinery = { "code" : 0x007242, "min" : 75, "gas" : 0, "time" : 30}
		sensor_tower = { "code" : 0x007228, "min" : 125, "gas" : 100, "time" : 25}
		ghost_academy = { "code" : 0x007229, "min" : 150, "gas" : 50, "time" : 40}
		factory = { "code" : 0x00722a, "min" : 150, "gas" : 100, "time" : 60}
		starport = { "code" : 0x00722b, "min" : 150, "gas" : 100, "time" : 50}
		armory = { "code" : 0x00722d, "min" : 150, "gas" : 100, "time" : 65}
		fusion_core = { "code" : 0x00722f, "min" : 150, "gas" : 150, "time" : 65}

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
		toggle_auto_repair = { "code" : 0x003900}
		repair = { "code" : 0x003940}

	class Marine():
		code = 0x004c01
		use_stim_pack_mixed = { "code" : 0x007400}

	class Marauder():
		code = 0x004f01
		use_stim_pack_mixed = { "code" : 0x007400}
		use_stim_pack = { "code" : 0x006100}

	class Ghost():
		code = 0x004e01
		cloak_on = { "code" : 0x007500}
		cloak_off = { "code" : 0x007501}
		nuke_start = { "code" : 0x015f20}
		nuke_cancel = { "code" : 0x015f01}
		hold_fire = { "code" : 0x003200}
		weapons_free = { "code" : 0x003300}
		emp_round = { "code" : 0x016220}
		sniper_round = { "code" : 0x007640}

	class SiegeTank():
		code = 0x003c01
		seige_mode_on = { "code" : 0x007800}
		seige_mode_off = { "code" : 0x007900}
		class Sieged():
			code = 0x3d01

	class Reaper():
		code = 0x004d01

	class Hellion():
		code = 0x005101

	class Thor():
		code = 0x005001
		strike_cannons = { "code" : 0x006340}

	class Viking():
		code = 0x003e01
		assault_mode_on = { "code" : 0x007e00}
		assault_mode_off = { "code" : 0x007f00}
		class Assault():
			code = 0x3f01

	class Medivac():
		code = 0x005201
		unload_all = { "code" : 0x007b22 }
		unload_all_moving = { "code" : "UA.UNLOAD_ALL,U.MEDIVAC"}
		unload_unit = { "code" : 0x007b63}
		load_unit = { "code" : 0x007b40}
		toggle_auto_heal = { "code" : 0x007700}
		heal = { "code" : 0x020803}

	class Raven():
		code = 0x005401
		auto_turret = { "code" : 0x017b20}
		point_defence_drone = { "code" : 0x003e20}
		seeker_missle = { "code" : 0x004a40}

	class AutoTurret():
		code = 0x003b01

	class PointDefenceDrone():
		code = 0x002501

	class Banshee():
		code = 0x005301
		cloak_on = { "code" : 0x007a00}
		cloak_off = { "code" : 0x007a01 }

	class Battlecruiser():
		code = 0x005501
		yamato_cannon = { "code" : 0x007d40}

	class TerranMain():
		set_rally_point = { "code" : 0x005920}
		set_rally_target = { "code" : 0x005920}
		train_scv = { "code" : 0x010c00, "min" : 50, "gas" : 0, "time" : 17}

	class CommandCenter():
		code = 0x002d01
		lift_up = { "code" : 0x010200}
		lift_down = { "code" : 0x010320}
		unload_all = { "code" : 0x010101 }
		unload_unit = { "code" : 0x010163}
		load_unit = { "code" : 0x010104}
		upgradeto_orbital_command = { "code" : 0x015400, "min" : 150, "gas" : 0, "time" : 35}
		upgradeto_orbital_command_cancel = { "code" : 0x015401}
		upgradeto_planetary_fortress = { "code" : 0x014f00, "min" : 150, "gas" : 150, "time" : 50}
		upgradeto_planetary_fortress_cancel = { "code" : 0x030f01}
		class Flying():
			code = 0x004001

	class OrbitalCommand():
		code = 0x00a001
		lift_up = { "code" : 0x015700	}
		lift_down = { "code" : 0x015820}
		mule_target = { "code" :0x004b20}
		mule_location = { "code" :0x004b20}
		extra_supply = { "code" : 0x004b40}
		scanner_sweep = { "code" :0x007c20}
		class Flying():
			code = 0x00a201

	class PlanetaryFortress():
		code = 0x009e01
		cancel_pf = { "code" : 0x012e00}  #????

	class SupplyDepot():
		code = 0x002e01
		lower_supply = { "code" : 0x010e00}
		raise_supply = { "code" : 0x010f00}
		class Lowered():
			code = 0x004b01

	class EngineeringBay():
		code = 0x003101
		hisec_auto_tracking = { "code" : 0x011300, "min" : 100, "gas" : 100, "time" : 80}
		building_armor = { "code" : 0x011301, "min" : 150, "gas" : 150, "time" : 140}
		inftantry_weapons_1 = { "code" : 0x011302, "min" : 100, "gas" : 100, "time" : 160}
		inftantry_weapons_2 = { "code" : 0x011303, "min" : 175, "gas" : 175, "time" : 190}
		inftantry_weapons_3 = { "code" : 0x011304, "min" : 250, "gas" : 250, "time" : 220}
		neosteel_frame = { "code" :  0x011305, "min" : 100, "gas" : 100, "time" : 110}
		inftantry_armor_1 = { "code" :0x011306, "min" : 100, "gas" : 100, "time" : 160}
		inftantry_armor_2 = { "code" :0x011307, "min" : 175, "gas" : 175, "time" : 190}
		inftantry_armor_3 = { "code" :0x011308, "min" : 250, "gas" : 250, "time" : 220}

	class GhostAcademy():
		code = 0x003501
		arm_silo_w_nuke = { "code" : 0x011500, "min" : 100, "gas" : 100, "time" : 60}
		personal_cloaking = { "code" : 0x011900, "min" : 150, "gas" : 150, "time" : 120}
		moebius_reactor = { "code" : 0x011901, "min" : 100, "gas" : 100, "time" : 80}

	class FusionCore():
		code = 0x003a01
		yamato_cannon = { "code" : 0x015c00, "min" : 150, "gas" : 150, "time" : 60}

	class Bunker():
		code = 0x003301
		salvage = { "code" : 0x016100}
		stimpack = { "code" : 0x017000}
		unload_all = { "code" : 0x010001}
		unload_unit = { "code" : 0x010063}
		load_unit = { "code" : 0x20020}

	class Armory():
		code = 0x003901
		vehicle_plating_1 = { "code" :0x011a02, "min" : 100, "gas" : 100, "time" : 160}
		vehicle_plating_2 = { "code" : 0x011a03,  "min" : 175, "gas" : 175, "time" : 190}
		vehicle_plating_3 = { "code" : 0x011a04, "min" : 250, "gas" : 250, "time" : 220}
		vehicle_weapons_1 = { "code" : 0x011a05, "min" : 100, "gas" : 100, "time" : 160}
		vehicle_weapons_2 = { "code" : 0x011a06, "min" : 175, "gas" : 175, "time" : 190}
		vehicle_weapons_3 = { "code" : 0x011a07, "min" : 250, "gas" : 250, "time" : 220}
		ship_plating_1 = { "code" : 0x011a08, "min" : 100, "gas" : 100, "time" : 160}
		ship_plating_2 = { "code" : 0x011a09, "min" : 175, "gas" : 175, "time" : 190}
		ship_plating_3 = { "code" : 0x011a0a, "min" : 250, "gas" : 250, "time" : 220}
		ship_weapons_1 = { "code" : 0x011a0b, "min" : 100, "gas" : 100, "time" : 160}
		ship_weapons_2 = { "code" : 0x011a0c, "min" : 175, "gas" : 175, "time" : 190}
		ship_weapons_3 = { "code" : 0x011a0d, "min" : 250, "gas" : 250, "time" : 220}


	class Barracks():
		code = 0x003001
		marine = { "code" : 0x011000, "min" : 50, "gas" : 0, "time" : 25}
		reaper = { "code" : 0x011001, "min" : 50, "gas" : 50, "time" : 45}
		ghost = { "code" : 0x011002, "min" : 150, "gas" : 150, "time" : 40}
		marauder = { "code" : 0x011003, "min" : 100, "gas" : 25, "time" : 30}

		lift_up = { "code" : 0x010500}
		lift_down = { "code" : 0x010d20}

		addon_techlab = { "code" : 0x010400 ,"min" : 50, "gas" : 25, "time" : 25}
		addon_techlab_move = { "code" : 0x010420,"min" : 50, "gas" : 25, "time" : 25}
		addon_techlab_cancel = { "code" : 0x02c406}

		addon_reactor = { "code" : 0x010401,"min" : 50, "gas" : 50, "time" : 50}
		addon_reactor_move = { "code" : 0x010421,"min" : 50, "gas" : 50, "time" : 50}
		addon_reactor_cancel = { "code" : 0x02c406}

		class Techlab():
			code = 0x004101
			nitropacks = { "code" : 0x011403, "min" : 50, "gas" : 50, "time" : 100}
			stimpack = { "code" : 0x011600, "min" : 100, "gas" : 100, "time" : 140}
			combat_shield = { "code" : 0x011601, "min" : 100, "gas" : 100, "time" : 110}
			concussive_shells = { "code" : 0x011602, "min" : 50, "gas" : 50, "time" : 60}

			cancel_research = { "code" : 0x012f00}
			cancel_specific_research = { "code" : 0x012f31}

		class Reactor():
			code = 0x4201

		class Flying():
			code = 0x004a01

	class Factory():
		code = 0x003601
		lift_up = { "code" : 0x010700}
		lift_down = { "code" : 0x010a20}

		addon_techlab = { "code" : 0x010600,"min" : 50, "gas" : 25, "time" : 25}
		addon_techlab_move = { "code" : 0x010600,"min" : 50, "gas" : 25, "time" : 25}
		addon_techlab_cancel = { "code" : 0x2c606}

		addon_reactor = { "code" : 0x010601,"min" : 50, "gas" : 50, "time" : 50}
		addon_reactor_move = { "code" : 0x010601,"min" : 50, "gas" : 50, "time" : 50}
		addon_reactor_cancel = { "code" : 0x02c606}

		seige_tank = { "code" : 0x011101}
		thor = { "code" : 0x011104}
		hellion = { "code" : 0x011105}

		class Techlab():
			code = 0x004301
			siege_tech = { "code" : 0x011700, "min" : 100, "gas" : 100, "time" : 80}
			infernal_preignighter = { "code" : 0x011701, "min" : 150, "gas" : 150, "time" : 110}
			strike_cannon = { "code" : 0x011702, "min" : 150, "gas" : 150, "time" : 110}

			cancel_research = { "code" : 0x012f00}
			cancel_specific_research = { "code" : 0x012f31}

		class Reactor():
			code = 0x4401

		class Flying():
			code = 0x004701

	class Starport():
		code = 0x003701
		lift_up = { "code" : 0x010900}
		lift_down = { "code" : 0x010b20}

		addon_techlab = { "code" : 0x010800,"min" : 50, "gas" : 25, "time" : 25}
		addon_techlab_move = { "code" : 0x010800,"min" : 50, "gas" : 25, "time" : 25}
		addon_techlab_cancel = { "code" : 0x02806}

		addon_reactor = { "code" : 0x010801,"min" : 50, "gas" : 50, "time" : 50}
		addon_reactor_move = { "code" : 0x010801,"min" : 50, "gas" : 50, "time" : 50}
		addon_reactor_cancel = { "code" : 0x02806}

		medivac = { "code" : 0x011200}
		banshee = { "code" : 0x011201}
		raven = { "code" : 0x011202}
		battlecruiser = { "code" : 0x011203}
		viking = { "code" : 0x011204}

		class Techlab():
			code = 0x004501
			cloaking_field = { "code" : 0x011800, "min" : 200, "gas" : 200, "time" : 110}
			caduceus_reactor = { "code" : 0x011802, "min" : 100, "gas" : 100, "time" : 80}
			corvid_reactor = { "code" : 0x011803, "min" : 150, "gas" : 150, "time" : 110}
			seeker_missle = { "code" : 0x011806,  "min" : 150, "gas" : 150, "time" : 110}
			durable_materials = { "code" : 0x011807, "min" : 150, "gas" : 150, "time" : 110}

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
		return_cargo = { "code" : 0x006901}
		gather_resources = {"code" : 0x006940}
		nexus = { "code" : 0x011b20, "min" : 400, "gas" : 0, "time" : 100}
		pylon = { "code" : 0x011b21, "min" : 100, "gas" : 0, "time" : 25}
		gateway = { "code" : 0x011b23, "min" : 150, "gas" : 0, "time" : 65}
		forge = { "code" : 0x011b24, "min" : 150, "gas" : 0, "time" : 45}
		fleet_beacon = { "code" : 0x011b25, "min" : 300, "gas" : 200, "time" : 60}
		twilight_council = { "code" : 0x011b26, "min" : 150, "gas" : 100, "time" : 50}
		photon_cannon = { "code" : 0x011b27, "min" : 150, "gas" : 0, "time" : 40}
		assimilator = { "code" : 0x011b42, "min" : 100, "gas" : 0, "time" : 30}
		stargate = { "code" : 0x011b29,  "min" : 150, "gas" : 150, "time" : 60}
		templar_archives = { "code" : 0x011b2a, "min" : 150, "gas" : 200, "time" : 50}
		dark_shrine = { "code" : 0x011b2b, "min" : 100, "gas" : 250, "time" : 100}
		robotics_bay = { "code" : 0x011b2c, "min" : 200, "gas" : 200, "time" : 65}
		robotics_facility = { "code" : 0x011b2d, "min" : 200, "gas" : 100, "time" : 65}
		cybernetics_core = { "code" : 0x011b2e, "min" : 150, "gas" : 0, "time" : 50}

	class Zealot():
		code = 0x006501

	class Stalker():
		code = 0x006601
		blink = { "code" : 0x014b20}

	class Sentry():
		code = 0x006901
		hallucinate_archon = { "code" : 0x003f00}
		hallucinate_colossus = { "code" : 0x004000}
		hallucinate_high_templar = { "code" : 0x004100}
		hallucinate_immortal = { "code" : 0x004200}
		hallucinate_phoenix = { "code" : 0x004300}
		hallucinate_probe = { "code" : 0x004400}
		hallucinate_stalker = { "code" : 0x004500}
		hallucinate_void_ray = { "code" : 0x004600}
		hallucinate_warp_prism = { "code" : 0x004700}
		hallucinate_zealot = { "code" : 0x004800}
		guardian_shield = { "code" : 0x003800}
		force_field = { "code" : 0x015920}

	class HighTemplar():
		code = 0x006701
		psionic_storm = { "code" : 0x012120}
		feedback = { "code" : 0x003c40}
		merge_into_archon = { "code" : 0x017c00}

	class DarkTemplar():
		code = 0x006801
		merge_into_archon = { "code" : 0x017c00}

	class Archon():
		code = 0x00a801

	class WarpPrism():
		code = 0x006d01
		unload_all = { "code" : 0x011c22}
		unload_all_moving = { "code" : 0x011c42}
		unload_unit = { "code" : 0x011c63}
		load_unit = { "code" : 0x011c40}
		phase_mode = { "code" : 0x015a00}
		transport_mode = { "code" : 0x015b00}
		class Phasing():
			code = 0x00a401

	class Voidray():
		code = 0x006c01

	class Pheonix():
		code = 0x006a01
		gravitation_beam_on = { "code" : 0x004c40}

	class Colossus():
		code = 0x001d01

	class Carrier():
		code = 0x006b01
		interceptor = { "code" : 0x012400}

	class Observer():
		code = 0x006e01

	class Mothership():
		code = 0x002401
		vortex = { "code" : 0x016320}
		mass_recall = { "code" : 0x003d20}

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
		probe = { "code" : 0x012000,  "min" : 50, "gas" : 0, "time" : 17}
		mothership = { "code" : 0x003b00, "min" : 400, "gas" : 400, "time" : 160 }
		chronoboost = { "code" : 0x006540}
		set_rally_point = { "code" : 0x005a20}
		set_rally_target = { "code" : 0x005a20}

	class Gateway():
		code = 0x005a01
		zealot = { "code" : 0x011d00, "min" : 100, "gas" : 0, "time" : 38}
		stalker = { "code" : 0x011d01, "min" : 125, "gas" : 50, "time" : 42}
		high_templar = { "code" : 0x011d03,  "min" : 50, "gas" : 150, "time" : 55}
		dark_templar = { "code" : 0x011d04, "min" : 125, "gas" : 125, "time" : 55}
		sentry = { "code" : 0x011d05, "min" : 50, "gas" : 100, "time" : 42}
		to_warpgate = {"code" : 0x015500}
		class WarpGate():
			code = 0x00a101
			warp_zealot = { "code" : 0x014720, "min" : 100, "gas" : 0, "time" : 5}
			warp_stalker = { "code" : 0x014721, "min" : 125, "gas" : 50, "time" : 5}
			warp_high_templar = { "code" : 0x014723, "min" : 50, "gas" : 150, "time" : 5}
			warp_dark_templar = { "code" : 0x014724, "min" : 125, "gas" : 125, "time" : 5}
			warp_sentry = { "code" : 0x014725, "min" : 50, "gas" : 100, "time" : 5}
			to_gateway = {"code" : 0x015600}

	class Forge():
		code = 0x005b01
		ground_weapons_1 = { "code" : 0x012500, "min" : 100, "gas" : 100, "time" : 160}
		ground_weapons_2 = { "code" : 0x012501, "min" : 175, "gas" : 175, "time" : 190}
		ground_weapons_3 = { "code" : 0x012502, "min" : 250, "gas" : 250, "time" : 220}
		ground_armour_1 = { "code" : 0x012503, "min" : 100, "gas" : 100, "time" : 160}
		ground_armour_2 = { "code" : 0x012504, "min" : 175, "gas" : 175, "time" : 190}
		ground_armour_3 = { "code" : 0x012505, "min" : 250, "gas" : 250, "time" : 220}
		shield_1 = { "code" : 0x012506, "min" : 200, "gas" : 200, "time" : 160}
		shield_2 = { "code" : 0x012507, "min" : 300, "gas" : 300, "time" : 190}
		shield_3 = { "code" : 0x012508, "min" : 400, "gas" : 400, "time" : 220}


	class CyberneticsCore():
		code = 0x006401
		air_weapons_1 = { "code" : 0x015d00, "min" : 100, "gas" : 100, "time" : 160}
		air_weapons_2 = { "code" : 0x015d01, "min" : 175, "gas" : 175, "time" : 190}
		air_weapons_3 = { "code" : 0x015d02, "min" : 250, "gas" : 250, "time" : 220}
		air_armour_1 = { "code" : 0x015d03,  "min" : 150, "gas" : 150, "time" : 160}
		air_armour_2 = { "code" : 0x015d04, "min" : 225, "gas" : 225, "time" : 190}
		air_armour_3 = { "code" : 0x015d05,"min" : 300, "gas" : 300, "time" : 220}
		warpgate = { "code" : 0x015d06,  "min" : 50, "gas" : 50, "time" : 140}
		hallucination = { "code" : 0x015d07, "min" : 100, "gas" : 100, "time" : 80}


	class RoboticsFacility():
		code = 0x006301
		warp_prism = { "code" : 0x011f00, "min" : 200, "gas" : 0, "time" : 50}
		observer = { "code" : 0x011f01, "min" : 25, "gas" : 75, "time" : 40}
		colossus = { "code" : 0x011f02, "min" : 300, "gas" : 200, "time" : 75}
		immortal = { "code" : 0x011f03, "min" : 250, "gas" : 100, "time" : 55}


	class Stargate():
		code = 0x005f01
		pheonix = { "code" : 0x011e00, "min" : 150, "gas" : 100, "time" : 35}
		carrier = { "code" : 0x011e02, "min" : 350, "gas" : 250, "time" : 120}
		voidray = { "code" : 0x011e04, "min" : 250, "gas" : 150, "time" : 60}

	class DarkShrine():
		code = 0x006101

	class TwilightCouncil():
		code = 0x005d01
		charge = { "code" : 0x015e00, "min" : 200, "gas" : 200, "time" : 140}
		blink = { "code" : 0x015e01,  "min" : 150, "gas" : 100, "time" : 110}


	class FleetBeacon():
		code = 0x005c01
		gavitation_catapault = { "code" : 0x003601, "min" : 150, "gas" : 150, "time" : 80} #Graviton Catapult',


	class TemplarArchive():
		code = 0x006001
		psi_storm = { "code" : 0x012704, "min" : 200, "gas" : 200, "time" : 110}


	class RoboticsBay():
		code = 0x006201
		grav_booster = { "code" : 0x012601,  "min" : 100, "gas" : 100, "time" : 80}
		grav_drive = { "code" : 0x012602, "min" : 100, "gas" : 100, "time" : 80}
		thermal_lance = { "code" : 0x012605, "min" : 200, "gas" : 200, "time" : 140}


	 # # # # # # # # # # # # # # # # # # # # #
	 # # Zerg
	 # # # # # # # # # # # # # # # # # # # # #

	class Larva():
		code = 0x00b101
		drone = { "code" : 0x013200, "min" : 50, "gas" : 0, "time" : 17}
		zergling = { "code" : 0x013201,  "min" : 50, "gas" : 0, "time" : 24}
		overlord = { "code" : 0x013202, "min" : 100, "gas" : 0, "time" : 25}
		hydralisk = { "code" : 0x013203, "min" : 100, "gas" : 50, "time" : 33}
		mutalisk = { "code" : 0x013204, "min" : 100, "gas" : 100, "time" : 33}
		ultralisk = { "code" : 0x013206, "min" : 300, "gas" : 200, "time" : 70}
		roach = { "code" : 0x013209, "min" : 75, "gas" : 25, "time" : 27}
		infestor = { "code" : 0x01320a, "min" : 100, "gas" : 150, "time" : 50}
		corrupter = { "code" : 0x01320b, "min" : 150, "gas" : 150, "time" : 40}


	class Egg():
		code = 0x008301
		cancel = { "code" : "UA.CANCEL_BANELING_MORPHING,U.ZERGLING"} #Cancel',


	class Drone():
		code = 0x008401
		gather_resources = { "code" : 0x012920} #Gather Resources (Zerg)',
		return_cargo = { "code" : 0x012901} #Return cargo',
		burrow = { "code" : 0x013600} #Burrow',
		unburrow = { "code" : 0x013700}

		hatchery = { "code" : 0x012820, "min" : 300, "gas" : 0, "time" : 100}
		spawning_pool = { "code" : 0x012823, "min" : 200, "gas" : 0, "time" : 65}
		evolution_chamber = { "code" : 0x012824, "min" : 75, "gas" : 0, "time" : 35}
		hydra_den = { "code" : 0x012825,  "min" : 100, "gas" : 100, "time" : 40}
		spire = { "code" : 0x012826, "min" : 200, "gas" : 200, "time" : 100}
		ultralisk_cavern = { "code" : 0x012827, "min" : 150, "gas" : 200, "time" : 65}
		extractor = { "code" : 0x012842, "min" : 25, "gas" : 0, "time" : 30}
		infestation_pit = { "code" : 0x012828,  "min" : 100, "gas" : 100, "time" : 50}
		nydus_network= { "code" : 0x012829, "min" : 150, "gas" : 200, "time" : 50}
		baneling_nest = { "code" : 0x01282a, "min" : 100, "gas" : 50, "time" : 60}
		roach_warren = { "code" : 0x01282d, "min" : 150, "gas" : 0, "time" : 55}
		spine_crawler = { "code" : 0x01282e, "min" : 100, "gas" : 0, "time" : 50}
		spore_crawler = { "code" : 0x01282f, "min" : 75, "gas" : 0, "time" : 30}

		class Burrowed():
			code = 0x009001

	class Queen():
		code = 0x009a01
		burrow = { "code" : 0x014800} #Burrow',
		unburrow = { "code" : 0x014900}
		creep_tumor = { "code" : 0x017520} #Creep Tumor',
		larva = { "code" : 0x006040} #Larva',
		transfuse = { "code" : 0x016640} #Transfuse',
		class Burrowed():
			code = 0x009901

	class Mutalisk():
		code = 0x008801

	class Zergling():
		code = 0x008501
		burrow = { "code" : 0x013c00} #Burrow',
		unburrow = { "code" : 0x013d00}
		baneling = { "code" : 0x003a00, "min" : 25, "gas" : 25, "time" : 20}

		class BanelingCocoon():
			code = 0x002201
			cancel_baneling = { "code" : "UA.CANCEL_BANELING_MORPHING,U.ZERGLING"}

		class Burrowed():
			code = 0x009301

	class Baneling():
		code = 0x002301
		burrow = { "code" : 0x013400} #Burrow',
		unburrow = { "code" : 0x013500}
		explode = { "code" : 0x003500} #Explode',
		attack_structure = { "code" : 0x005d00} #Attack Structure'
		class Burrowed():
			code = 0x008f01

	class Roach():
		code = 0x008a01
		burrow = { "code" : 0x013a00} #Burrow',
		unburrow = { "code" : 0x013b00}
		class Burrowed():
			code = 0x009201


	class Hydralisk():
		code = 0x008701
		burrow = { "code" : 0x013800} #Burrow',
		unburrow = { "code" : 0x013900}
		class Burrowed():
			code = 0x009101

	class Infestor():
		code = 0x008b01
		burrow = { "code" : 0x014c00} #Burrow',
		unburrow = { "code" : 0x014d00}

		fungal_growth = { "code" : 0x003720} #Fungal Growth',
		infested_terran = { "code" : 0x005e20} #Infested Terran',
		neural_parasite = { "code" : 0x005f40}
		class Burrowed():
			code = 0x009b01

	class Ultralisk():
		code = 0x008901
		burrow = { "code" : 0x015200} #Burrow',
		unburrow = { "code" : 0x015300}
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
		corruption = { "code" : 0x003100} #Corruption',
		broodlord = { "code" : 0x013300, "min" : 150, "gas" : 150, "time" : 34}

		class BroodlordCocoon():
			code = 0x008d01
			cancel_broodlord = { "code" : 0x023301}

		class Broodlord():
			code = 0x008e01

	class Broodling():
		code = 0x00d001

	class Overlord():
		code = 0x008601
		unload_all = { "code" : 0x014422}
		unload_all_moving = { "code" : 0x014401}
		unload_unit = { "code" : 0x014463}
		load_unit = { "code" : 0x014404}
		creep = { "code" : 0x017400} #Generate Creep',
		cancel_creep = { "code" : 0x017401} #Stop generating Creep',
		unload_at = { "code" : 0x014401} #Unload all at',

		overseer = { "code" : 0x014e00, "min" : 50, "gas" : 100, "time" : 17}
		cancel_overseer = { "code" : 0x014e01}

		class OverseerCocoon():
			code = 0x009c01

	class Overseer():
		code = 0x009d01
		changling = { "code" : 0x005000} #Changeling',
		contaminate = { "code" : 0x020340} #Contaminate',

	class Changeling():
		code = 0x002601

	class NydusWorm():
		code = 0x00a901
		unload_all = { "code" : 0x014a01}
		unload_unit = { "code" : 0x014a63}
		load_unit = { "code" : 0x014a40}

	class SpineCrawler(Building, Attacker):
		code = 0x007e01
		uproot = { "code" : 0x017600}
		root = { "code" : 0x017820}
		cancel_root = { "code" : 0x33901}
		class Uprooted():
			code = 0x00a601

	class SporeCrawler(Building, Attacker):
		code = 0x007f01
		uproot = { "code" : 0x017700}
		root = { "code" : 0x017920}
		cancel_root = { "code" : 0x033901}
		class Uprooted():
			code = 0x00a701
	class Extractor():
		code = 0x007401

	class ZergMain(Production, Research):
		worker_rally_point = { "code" : 0x005b21} #Set worker rally point',
		worker_rally_target = { "code" : 0x005b21} #Set worker rally target',
		unit_rally_point = { "code" : 0x005b20} #Set unit rally point',
		unit_rally_target = { "code" : 0x005b20} #Set unit rally target',

		queen = { "code" : 0x016400, "min" : 150, "gas" : 0, "time" : 50}
		evolve_burrow = { "code" : 0x012e03, "min" : 100, "gas" : 100, "time" : 100}
		evolve_carapace = { "code" : 0x012e01, "min" : 100, "gas" : 100, "time" : 60}
		evolve_ventral_sacs = { "code" : 0x012e02, "min" : 200, "gas" : 200, "time" : 130}


	class Hatchery():
		code = 0x007201
		lair = { "code" : 0x012b00, "min" : 150, "gas" : 100, "time" : 80}
		cancel_lair = { "code" : 0x012b01}

	class Lair():
		code = 0x008001
		hive = { "code" : 0x012c00, "min" : 200, "gas" : 150, "time" : 100}
		cancel_hive = { "code" : 0x012c01}

	class Hive():
		code = 0x008101

	class SpawningPool():
		code = 0x007501
		adrenal_glands = { "code" : 0x012f00, "min" : 200, "gas" : 200, "time" : 130}
		metabolic_boost = { "code" : 0x012f01, "min" : 100, "gas" : 100, "time" : 110}


	class EvolutionChamber():
		code = 0x007601
		melee_attack_1 = { "code" : 0x012a00, "min" : 100, "gas" : 100, "time" : 160}
		melee_attack_2 = { "code" : 0x012a01, "min" : 150, "gas" : 150, "time" : 190}
		melee_attack_3 = { "code" : 0x012a02, "min" : 200, "gas" : 200, "time" : 200}
		ground_carapace_1 = { "code" : 0x012a03, "min" : 150, "gas" : 150, "time" : 160}
		ground_carapace_2 = { "code" : 0x012a04, "min" : 225, "gas" : 225, "time" : 190}
		ground_carapace_3 = { "code" : 0x012a05, "min" : 300, "gas" : 300, "time" : 220}
		missile_attack_1 = { "code" : 0x012a06, "min" : 100, "gas" : 100, "time" : 160}
		missile_attack_2 = { "code" : 0x012a07, "min" : 150, "gas" : 150, "time" : 190}
		missile_attack_3 = { "code" : 0x012a08, "min" : 200, "gas" : 200, "time" : 220}


	class RoachWarren():
		code = 0x007d01
		glial_recon = { "code" : 0x005c01, "min" : 100, "gas" : 100, "time" : 110} #Evolve Glial Reconstitution',
		tunneling_claws = { "code" : 0x005c02, "min" : 150, "gas" : 150, "time" : 110} #Evolve Tunneling Claws',


	class BanelingNest():
		code = 0x007c01
		centrifugal_hooks = { "code" : 0x015100, "min" : 150, "gas" : 150, "time" : 110}

	class CreepTumor():
		code = 0x007301
		class Burrowed():
			code = 0x00a501
			creep_tumor = { "code" : 0x017a20}
			cancel_creep_tumor = { "code" : 0x3fa06}

	class HydraliskDen():
		code = 0x007701
		grooved_spines = { "code" : 0x013002, "min" : 150, "gas" : 150, "time" : 80}


	class InfestationPit():
		code = 0x007a01
		pathogen_glands = { "code" : 0x015002, "min" : 150, "gas" : 150, "time" : 80}
		neural_parasite = { "code" : 0x015003,  "min" : 150, "gas" : 150, "time" : 110}


	class NydusNetwork():
		code = 0x007b01
		unload_all = { "code" : 0x014a01}
		unload_unit = { "code" : 0x014a63}
		load_unit = { "code" : 0x014a40}
		nydus= { "code" : 0x017d20,"min" : 100, "gas" : 100, "time" : 20}


	class Spire():
		code = 0x007801
		flyer_attack_1 = { "code" : 0x013100, "min" : 100, "gas" : 100, "time" : 160}
		flyer_attack_2 = { "code" : 0x013101, "min" : 175, "gas" : 175, "time" : 190}
		flyer_attack_3 = { "code" : 0x013102,  "min" : 250, "gas" : 250, "time" : 220}
		flyer_carapace_1 = { "code" : 0x013103, "min" : 150, "gas" : 150, "time" : 160}
		flyer_carapace_2 = { "code" : 0x013104, "min" : 225, "gas" : 225, "time" : 190}
		flyer_carapace_3 = { "code" : 0x013105, "min" : 300, "gas" : 300, "time" : 220}
		greater_spire = { "code" : 0x012d00, "min" : 100, "gas" : 150, "time" : 100}
		cancel_greater_spire = { "code" : 0x012d01 }
		class GreaterSpire():
			code = 0x008201

	class UltraliskCavern():
		code = 0x007901
		chitinous = { "code" : 0x006602, "min" : 150, "gas" : 150, "time" : 110}


