###This class holds all variable information between versions!
###These are codes, times, minerals, gas, and supply
class version(object):
	
	class Thrash():
		thrash = []
		
	class DataObject():
		right_click = { "code" : 0x3700 }
		right_click_in_fog = { "code" : 0x5700 }

	class Moveable():
		stop = { "code" : 0x002400}
		hold = { "code" : 0x002602}
		move = { "code" : 0x002610}
		patrol = { "code" : 0x002611}
		follow = { "code" : 0x002610}

	class Attacker():
		attack_move = { "code" : 0x002a10}
		attack_object = { "code" : 0x002a10}

	class Supporter():
		scan_move = { "code" : 0x002613}  # attack move for units without attack
		scan_target = { "code" : 0x002613}  # attack move for units without attack

	class Building():
		cancel = { "code" : 0x13000}

	class TerranBuilding():
		halt_build = { "code" : 0x013001}

	class Research():
		cancel = { "code" : 0x012c00}  # Generic ESC cancel
		cancel_unit = { "code" : 0x012c31}  # Cancel + build id

	class Production():
		set_rally_point = { "code" : 0x011710}
		set_rally_target = { "code" : 0x011720}
		cancel = { "code" : 0x012c00}  # Generic ESC cancel
		cancel_unit = { "code" : 0x012c31}  # Cancel + build id
		
	class SCV():
		code = 0x004901
		gather_resources = { "code" : 0x012820}
		return_cargo = { "code" : 0x012801}
		toggle_auto_repair = { "code" : 0x013100}
		repair = { "code" : 0x013120}
		halt = { "code" : 0x01f206}
		command_center = { "code" : 0x013210, "min" : 400, "gas" : 0, "time" : 100}
		supply_depot = { "code" : 0x013211, "min" : 100, "gas" : 0, "time" : 30}
		barracks = { "code" : 0x013213, "min" : 150, "gas" : 0 , "time" : 60}
		engineering_bay = { "code" : 0x013214, "min" : 125, "gas" : 0, "time" : 35}
		missle_turret = { "code" : 0x013215, "min" : 100, "gas" : 0, "time" : 25}
		bunker = { "code" : 0x013216, "min" : 100, "gas" : 0, "time" : 35}
		refinery = { "code" : 0x013222, "min" : 75, "gas" : 0, "time" : 30}
		sensor_tower = { "code" : 0x017210, "min" : 125, "gas" : 100, "time" : 25}
		ghost_academy = { "code" : 0x017211, "min" : 150, "gas" : 50, "time" : 40}
		factory = { "code" : 0x017212, "min" : 150, "gas" : 100, "time" : 60}
		starport = { "code" : 0x017213, "min" : 150, "gas" : 100, "time" : 50}
		armory = { "code" : 0x017215, "min" : 150, "gas" : 100, "time" : 65}
		fusion_core = { "code" : 0x017217, "min" : 150, "gas" : 150, "time" : 65}
	
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
		repair = { "code" : 0x003920}

	class Marine():
		code = 0x004c01
		use_stim_pack_mixed = { "code" : 0x013400}

	class Marauder():
		code = 0x004f01
		use_stim_pack_mixed = { "code" : 0x013400}
		use_stim_pack = { "code" : 0x012100}

	class Ghost():
		code = 0x004e01
		cloak_on = { "code" : 0x013500}
		cloak_off = { "code" : 0x013501}
		nuke_start = { "code" : 0x031f10}
		nuke_cancel = { "code" : 0x031f01}
		hold_fire = { "code" : 0x003200}
		weapons_free = { "code" : 0x003300}
		emp_round = { "code" : 0x032210}
		sniper_round = { "code" : 0x013620}

	class SiegeTank():
		code = 0x003d01
		seige_mode_on = { "code" : 0x013800}
		seige_mode_off = { "code" : 0x013900}

	class Reaper():
		code = 0x004d01
	
	class Hellion():
		code = 0x005101
		
	class Thor():
		code = 0x005001
		strike_cannons = { "code" : 0x012320}

	class Viking():
		code = 0x003e01
		assault_mode_on = { "code" : 0x013e00}
		assault_mode_off = { "code" : 0x013f00}

	class Medivac():
		code = 0x005201
		unload_all = { "code" : 0x013b12 }
		unload_all_moving = { "code" : 0x013b22}
		unload_unit = { "code" : 0x013b33}
		load_unit = { "code" : 0x013b20}
		toggle_auto_heal = { "code" : 0x013700}
		heal = { "code" : 0x020803}

	class Raven():
		code = 0x005401
		auto_turret = { "code" : 0x033b10}
		point_defence_drone = { "code" : 0x003e10}
		seeker_missle = { "code" : 0x010a20}

	class AutoTurret():
		code = 0x003b01
		
	class PointDefenceDrone():
		code = 0x002501
		
	class Banshee():
		code = 0x005301
		cloak_on = { "code" : 0x013a00}
		cloak_off = { "code" : 0x013a01 }

	class Battlecruiser():
		code = 0x005501
		yamato_cannon = { "code" : 0x013d20}

	class TerranMain():
		set_rally_point = { "code" : 0x011910}
		set_rally_target = { "code" : 0x011910}
		train_scv = { "code" : 0x020c00, "min" : 50, "gas" : 0, "time" : 17}

	class CommandCenter():
		code = 0x002d01
		lift_up = { "code" : 0x020200}
		lift_down = { "code" : 0x020310}
		unload_all = { "code" : 0x020101 }
		unload_unit = { "code" : 0x020133}
		load_unit = { "code" : 0x020104}
		upgradeto_orbital_command = { "code" : 0x031400, "min" : 150, "gas" : 0, "time" : 35}
		upgradeto_orbital_command_cancel = { "code" : 0x031401}
		upgradeto_planetary_fortress = { "code" : 0x030f00, "min" : 150, "gas" : 150, "time" : 50}
		upgradeto_planetary_fortress_cancel = { "code" : 0x030f01}
		class Flying():
			code = 0x004001
			
	class OrbitalCommand():
		code = 0x00a001
		lift_up = { "code" : 0x031700	}
		lift_down = { "code" : 0x031810}
		mule_target = { "code" :0x010b10}
		mule_location = { "code" :0x010b10}
		extra_supply = { "code" : 0x012220}
		scanner_sweep = { "code" :0x013c10}
		class Flying():
			code = 0x00a201
			
	class PlanetaryFortress():
		code = 0x009e01
		cancel_pf = { "code" : 0x012e00}  #????

	class SupplyDepot():
		code = 0x002e01
		lower_supply = { "code" : 0x020e00}
		raise_supply = { "code" : 0x020f00}
		class Lowered():
			code = 0x004b01

	class EngineeringBay():
		code = 0x003101
		hisec_auto_tracking = { "code" : 0x021300, "min" : 100, "gas" : 100, "time" : 80}
		building_armor = { "code" : 0x021301, "min" : 150, "gas" : 150, "time" : 140}
		inftantry_weapons_1 = { "code" : 0x021302, "min" : 100, "gas" : 100, "time" : 160}
		inftantry_weapons_2 = { "code" : 0x021303, "min" : 175, "gas" : 175, "time" : 190}
		inftantry_weapons_3 = { "code" : 0x021304, "min" : 250, "gas" : 250, "time" : 220}
		neosteel_frame = { "code" :  0x021305, "min" : 100, "gas" : 100, "time" : 110}
		inftantry_armor_1 = { "code" :0x021306, "min" : 100, "gas" : 100, "time" : 160}
		inftantry_armor_2 = { "code" :0x021307, "min" : 175, "gas" : 175, "time" : 190}
		inftantry_armor_3 = { "code" :0x025300, "min" : 250, "gas" : 250, "time" : 220}

	class GhostAcademy():
		code = 0x003501
		arm_silo_w_nuke = { "code" : 0x021500, "min" : 100, "gas" : 100, "time" : 60}
		personal_cloaking = { "code" : 0x021900, "min" : 150, "gas" : 150, "time" : 120}
		moebius_reactor = { "code" : 0x021901, "min" : 100, "gas" : 100, "time" : 80}

	class FusionCore():
		code = 0x003a01
		yamato_cannon = { "code" : 0x031c00, "min" : 150, "gas" : 150, "time" : 60}

	class Bunker():
		code = 0x003301
		salvage = { "code" : 0x032100}
		stimpack = { "code" : 0x033000}
		unload_all = { "code" : 0x020001}
		unload_unit = { "code" : 0x020033}
		load_unit = { "code" : 0x20020}

	class Armory():
		code = 0x003901
		vehicle_plating_1 = { "code" :0x021a02, "min" : 100, "gas" : 100, "time" : 160}
		vehicle_plating_2 = { "code" : 0x021a03,  "min" : 175, "gas" : 175, "time" : 190}
		vehicle_plating_3 = { "code" : 0x021a04, "min" : 250, "gas" : 250, "time" : 220}
		vehicle_weapons_1 = { "code" : 0x021a05, "min" : 100, "gas" : 100, "time" : 160}
		vehicle_weapons_2 = { "code" : 0x021a06, "min" : 175, "gas" : 175, "time" : 190}
		vehicle_weapons_3 = { "code" : 0x021a07, "min" : 250, "gas" : 250, "time" : 220}
		ship_plating_1 = { "code" : 0x025a00, "min" : 100, "gas" : 100, "time" : 160}
		ship_plating_2 = { "code" : 0x025a01, "min" : 175, "gas" : 175, "time" : 190}
		ship_plating_3 = { "code" : 0x025a02, "min" : 250, "gas" : 250, "time" : 220}
		ship_weapons_1 = { "code" : 0x025a03, "min" : 100, "gas" : 100, "time" : 160}
		ship_weapons_2 = { "code" : 0x025a04, "min" : 175, "gas" : 175, "time" : 190}
		ship_weapons_3 = { "code" : 0x025a05, "min" : 250, "gas" : 250, "time" : 220}

	
	class Barracks():
		code = 0x003001
		marine = { "code" : 0x021000, "min" : 50, "gas" : 0, "time" : 25}
		reaper = { "code" : 0x021001, "min" : 50, "gas" : 50, "time" : 45}
		ghost = { "code" : 0x021002, "min" : 150, "gas" : 150, "time" : 40}
		marauder = { "code" : 0x021003, "min" : 100, "gas" : 25, "time" : 30}
		
		lift_up = { "code" : 0x020500}
		lift_down = { "code" : 0x020d10}
	
		addon_techlab = { "code" : 0x020400 ,"min" : 50, "gas" : 25, "time" : 25}
		addon_techlab_move = { "code" : 0x020400,"min" : 50, "gas" : 25, "time" : 25}
		addon_techlab_cancel = { "code" : 0x02c406}

		addon_reactor = { "code" : 0x020401,"min" : 50, "gas" : 50, "time" : 50}
		addon_reactor_move = { "code" : 0x020401,"min" : 50, "gas" : 50, "time" : 50}
		addon_reactor_cancel = { "code" : 0x02c406}

		class Techlab():
			code = 0x004101
			nitropacks = { "code" : 0x021403, "min" : 50, "gas" : 50, "time" : 100}
			stimpack = { "code" : 0x021600, "min" : 100, "gas" : 100, "time" : 140}
			combat_shield = { "code" : 0x021601, "min" : 100, "gas" : 100, "time" : 110}
			concussive_shells = { "code" : 0x021602, "min" : 50, "gas" : 50, "time" : 60}
			
			cancel_research = { "code" : 0x012f00}
			cancel_specific_research = { "code" : 0x012f31}

		class Reactor():
			code = 0x4201

		class Flying():
			code = 0x004a01

	class Factory():
		code = 0x003601 
		lift_up = { "code" : 0x020700}
		lift_down = { "code" : 0x020a10}

		addon_techlab = { "code" : 0x020600,"min" : 50, "gas" : 25, "time" : 25}
		addon_techlab_move = { "code" : 0x020600,"min" : 50, "gas" : 25, "time" : 25}
		addon_techlab_cancel = { "code" : 0x2c606}

		addon_reactor = { "code" : 0x020601,"min" : 50, "gas" : 50, "time" : 50}
		addon_reactor_move = { "code" : 0x020601,"min" : 50, "gas" : 50, "time" : 50}
		addon_reactor_cancel = { "code" : 0x02c606}

		seige_tank = { "code" : 0x021101}
		thor = { "code" : 0x021104}
		hellion = { "code" : 0x021105}

		class Techlab():
			code = 0x004301
			siege_tech = { "code" : 0x021700, "min" : 100, "gas" : 100, "time" : 80}
			infernal_preignighter = { "code" : 0x021701, "min" : 150, "gas" : 150, "time" : 110}
			strike_cannon = { "code" : 0x021702, "min" : 150, "gas" : 150, "time" : 110}
			
			cancel_research = { "code" : 0x012f00}
			cancel_specific_research = { "code" : 0x012f31}

		class Reactor():
			code = 0x4401

		class Flying():
			code = 0x004701

	class Starport():
		code = 0x003701
		lift_up = { "code" : 0x020900}
		lift_down = { "code" : 0x020b10}

		addon_techlab = { "code" : 0x020800,"min" : 50, "gas" : 25, "time" : 25}
		addon_techlab_move = { "code" : 0x020800,"min" : 50, "gas" : 25, "time" : 25}
		addon_techlab_cancel = { "code" : 0x02806}

		addon_reactor = { "code" : 0x020801,"min" : 50, "gas" : 50, "time" : 50}
		addon_reactor_move = { "code" : 0x020801,"min" : 50, "gas" : 50, "time" : 50}
		addon_reactor_cancel = { "code" : 0x02806}

		medivac = { "code" : 0x021200}
		banshee = { "code" : 0x021201}
		raven = { "code" : 0x021202}
		battlecruiser = { "code" : 0x021203}
		viking = { "code" : 0x021204}

		class Techlab():
			code = 0x004501
			cloaking_field = { "code" : 0x021800, "min" : 200, "gas" : 200, "time" : 110}
			caduceus_reactor = { "code" : 0x021802, "min" : 100, "gas" : 100, "time" : 80}
			corvid_reactor = { "code" : 0x021803, "min" : 150, "gas" : 150, "time" : 110}
			seeker_missle = { "code" : 0x021806,  "min" : 150, "gas" : 150, "time" : 110}
			durable_materials = { "code" : 0x021807, "min" : 150, "gas" : 150, "time" : 110}
			
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
		return_cargo = { "code" : 0x012901}
		gather_resources = {"code" : 0x012920}
		nexus = { "code" : 0x021b10, "min" : 400, "gas" : 0, "time" : 100}
		pylon = { "code" : 0x021b11, "min" : 100, "gas" : 0, "time" : 25}
		gateway = { "code" : 0x021b13, "min" : 150, "gas" : 0, "time" : 65}
		forge = { "code" : 0x021b14, "min" : 150, "gas" : 0, "time" : 45}
		fleet_beacon = { "code" : 0x021b15, "min" : 300, "gas" : 200, "time" : 60}
		twilight_council = { "code" : 0x021b16, "min" : 150, "gas" : 100, "time" : 50}
		photon_cannon = { "code" : 0x021b17, "min" : 150, "gas" : 0, "time" : 40}
		assimilator = { "code" : 0x021b22, "min" : 100, "gas" : 0, "time" : 30}
		stargate = { "code" : 0x025b11,  "min" : 150, "gas" : 150, "time" : 60}
		templar_archives = { "code" : 0x025b12, "min" : 150, "gas" : 200, "time" : 50}
		dark_shrine = { "code" : 0x025b13, "min" : 100, "gas" : 250, "time" : 100}
		robotics_bay = { "code" : 0x025b14, "min" : 200, "gas" : 200, "time" : 65}
		robotics_facility = { "code" : 0x025b15, "min" : 200, "gas" : 100, "time" : 65}
		cybernetics_core = { "code" : 0x025b16, "min" : 150, "gas" : 0, "time" : 50}

	class Zealot():
		code = 0x006501
		
	class Stalker():
		code = 0x006601
		blink = { "code" : 0x030b10}

	class Sentry():
		code = 0x006901
		hallucinate_archon = { "code" : 0x003f00}
		hallucinate_colossus = { "code" : 0x010000}
		hallucinate_high_templar = { "code" : 0x010100}
		hallucinate_immortal = { "code" : 0x010200}
		hallucinate_phoenix = { "code" : 0x010300}
		hallucinate_probe = { "code" : 0x010400}
		hallucinate_stalker = { "code" : 0x010500}
		hallucinate_void_ray = { "code" : 0x010600}
		hallucinate_warp_prism = { "code" : 0x010700}
		hallucinate_zealot = { "code" : 0x010800}
		guardian_shield = { "code" : 0x003800}
		force_field = { "code" : 0x031910}
	
	class HighTemplar():
		code = 0x006701
		psionic_storm = { "code" : 0x022110}
		feedback = { "code" : 0x003c20}
		merge_into_archon = { "code" : 0x033c00}

	class DarkTemplar():
		code = 0x006801
		merge_into_archon = { "code" : 0x033c00}

	class Archon():
		code = 0x00a801

	class WarpPrism():
		code = 0x006d01
		unload_all = { "code" : 0x021c12}
		unload_all_moving = { "code" : 0x021c22}
		unload_unit = { "code" : 0x021c33}
		load_unit = { "code" : 0x021c20}
		phase_mode = { "code" : 0x031a00}
		transport_mode = { "code" : 0x031b00}
		class Phasing():
			code = 0x00a401

	class Voidray():
		code = 0x006c01
		
	class Pheonix():
		code = 0x006a01
		gravitation_beam_on = { "code" : 0x010c20}

	class Colossus():
		code = 0x001d01 
		
	class Carrier():
		code = 0x006b01
		interceptor = { "code" : 0x022400}

	class Observer():
		code = 0x006e01
	
	class Mothership():
		code = 0x002401
		vortex = { "code" : 0x032310}
		mass_recall = { "code" : 0x003d10}

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
		probe = { "code" : 0x022000,  "min" : 50, "gas" : 0, "time" : 17}
		mothership = { "code" : 0x003b00, "min" : 400, "gas" : 400, "time" : 160 }
		chronoboost = { "code" : 0x012520}
		set_rally_point = { "code" : 0x011a10}
		set_rally_target = { "code" : 0x011a10}

	class Gateway():
		code = 0x005a01
		zealot = { "code" : 0x021d00, "min" : 100, "gas" : 0, "time" : 38}
		stalker = { "code" : 0x021d01, "min" : 125, "gas" : 50, "time" : 42}
		high_templar = { "code" : 0x021d03,  "min" : 50, "gas" : 150, "time" : 55}
		dark_templar = { "code" : 0x021d04, "min" : 125, "gas" : 125, "time" : 55}
		sentry = { "code" : 0x021d05, "min" : 50, "gas" : 100, "time" : 42}
		to_warpgate = {"code" : 0x031500}
		class WarpGate():
			code = 0x00a101
			warp_zealot = { "code" : 0x030710, "min" : 100, "gas" : 0, "time" : 5}
			warp_stalker = { "code" : 0x030711, "min" : 125, "gas" : 50, "time" : 5}
			warp_high_templar = { "code" : 0x030713, "min" : 50, "gas" : 150, "time" : 5}
			warp_dark_templar = { "code" : 0x030714, "min" : 125, "gas" : 125, "time" : 5}
			warp_sentry = { "code" : 0x030715, "min" : 50, "gas" : 100, "time" : 5}
			to_gateway = {"code" : 0x031600}

	class Forge():
		code = 0x005b01
		ground_weapons_1 = { "code" : 0x022500, "min" : 100, "gas" : 100, "time" : 160}
		ground_weapons_2 = { "code" : 0x022501, "min" : 175, "gas" : 175, "time" : 190}
		ground_weapons_3 = { "code" : 0x022502, "min" : 250, "gas" : 250, "time" : 220}
		ground_armour_1 = { "code" : 0x022503, "min" : 100, "gas" : 100, "time" : 160}
		ground_armour_2 = { "code" : 0x022504, "min" : 175, "gas" : 175, "time" : 190}
		ground_armour_3 = { "code" : 0x022505, "min" : 250, "gas" : 250, "time" : 220}
		shield_1 = { "code" : 0x022506, "min" : 200, "gas" : 200, "time" : 160}
		shield_2 = { "code" : 0x022507, "min" : 300, "gas" : 300, "time" : 190}
		shield_3 = { "code" : 0x026500, "min" : 400, "gas" : 400, "time" : 220}


	class CyberneticsCore():
		code = 0x006401
		air_weapons_1 = { "code" : 0x031d00, "min" : 100, "gas" : 100, "time" : 160}
		air_weapons_2 = { "code" : 0x031d01, "min" : 175, "gas" : 175, "time" : 190}
		air_weapons_3 = { "code" : 0x031d02, "min" : 250, "gas" : 250, "time" : 220}
		air_armour_1 = { "code" : 0x031d03,  "min" : 150, "gas" : 150, "time" : 160}
		air_armour_2 = { "code" : 0x031d04, "min" : 225, "gas" : 225, "time" : 190}
		air_armour_3 = { "code" : 0x031d05,"min" : 300, "gas" : 300, "time" : 220}
		warpgate = { "code" : 0x031d06,  "min" : 50, "gas" : 50, "time" : 140}
		hallucination = { "code" : 0x035d01, "min" : 100, "gas" : 100, "time" : 80}


	class RoboticsFacility():
		code = 0x006301
		warp_prism = { "code" : 0x021f00, "min" : 200, "gas" : 0, "time" : 50}
		observer = { "code" : 0x021f01, "min" : 25, "gas" : 75, "time" : 40}
		colossus = { "code" : 0x021f02, "min" : 300, "gas" : 200, "time" : 75}
		immortal = { "code" : 0x021f03, "min" : 250, "gas" : 100, "time" : 55}


	class Stargate():
		code = 0x005f01
		pheonix = { "code" : 0x021e00, "min" : 150, "gas" : 100, "time" : 35}
		carrier = { "code" : 0x021e02, "min" : 350, "gas" : 250, "time" : 120}
		voidray = { "code" : 0x021e04, "min" : 250, "gas" : 150, "time" : 60}

	class DarkShrine():
		code = 0x006101
		
	class TwilightCouncil():
		code = 0x005d01
		charge = { "code" : 0x031e00, "min" : 200, "gas" : 200, "time" : 140}
		blink = { "code" : 0x031e01,  "min" : 150, "gas" : 100, "time" : 110}


	class FleetBeacon():
		code = 0x005c01
		gavitation_catapault = { "code" : 0x003601, "min" : 150, "gas" : 150, "time" : 80} #Graviton Catapult',


	class TemplarArchive():
		code = 0x006001
		psi_storm = { "code" : 0x022704, "min" : 200, "gas" : 200, "time" : 110}


	class RoboticsBay():
		code = 0x006201
		grav_booster = { "code" : 0x022601,  "min" : 100, "gas" : 100, "time" : 80}
		grav_drive = { "code" : 0x022602, "min" : 100, "gas" : 100, "time" : 80}
		thermal_lance = { "code" : 0x022605, "min" : 200, "gas" : 200, "time" : 140}


	 # # # # # # # # # # # # # # # # # # # # #
	 # # Zerg
	 # # # # # # # # # # # # # # # # # # # # #

	class Larva():
		code = 0x00b101
		drone = { "code" : 0x023200, "min" : 50, "gas" : 0, "time" : 17}
		zergling = { "code" : 0x023201,  "min" : 50, "gas" : 0, "time" : 24}
		overlord = { "code" : 0x023202, "min" : 100, "gas" : 0, "time" : 25}
		hydralisk = { "code" : 0x023203, "min" : 100, "gas" : 50, "time" : 33}
		mutalisk = { "code" : 0x023204, "min" : 100, "gas" : 100, "time" : 33}
		ultralisk = { "code" : 0x023206, "min" : 300, "gas" : 200, "time" : 70}
		roach = { "code" : 0x027201, "min" : 75, "gas" : 25, "time" : 27}
		infestor = { "code" : 0x027202, "min" : 100, "gas" : 150, "time" : 50}
		corrupter = { "code" : 0x027203, "min" : 150, "gas" : 150, "time" : 40}


	class Egg():
		code = 0x008301
		cancel = { "code" : 0x012b00} #Cancel',


	class Drone():
		code = 0x008401
		gather_resources = { "code" : 0x022920} #Gather Resources (Zerg)',
		return_cargo = { "code" : 0x022901} #Return cargo',
		burrow = { "code" : 0x023600} #Burrow',
		unburrow = { "code" : 0x023700}
		
		hatchery = { "code" : 0x022810, "min" : 300, "gas" : 0, "time" : 100}
		spawning_pool = { "code" : 0x022813, "min" : 200, "gas" : 0, "time" : 65}
		evolution_chamber = { "code" : 0x022814, "min" : 75, "gas" : 0, "time" : 35}
		hydra_den = { "code" : 0x022815,  "min" : 100, "gas" : 100, "time" : 40}
		spire = { "code" : 0x022816, "min" : 200, "gas" : 200, "time" : 100}
		ultralisk_cavern = { "code" : 0x022817, "min" : 150, "gas" : 200, "time" : 65}
		extractor = { "code" : 0x022822, "min" : 25, "gas" : 0, "time" : 30}
		infestation_pit = { "code" : 0x026810,  "min" : 100, "gas" : 100, "time" : 50}
		nydus_network= { "code" : 0x026811, "min" : 150, "gas" : 200, "time" : 50}
		baneling_nest = { "code" : 0x026812, "min" : 100, "gas" : 50, "time" : 60}
		roach_warren = { "code" : 0x026815, "min" : 150, "gas" : 0, "time" : 55}
		spine_crawler = { "code" : 0x026816, "min" : 100, "gas" : 0, "time" : 50}
		spore_crawler = { "code" : 0x026817, "min" : 75, "gas" : 0, "time" : 30}
		
		class Burrowed():
			code = 0x009001

	class Queen():
		code = 0x009a01
		burrow = { "code" : 0x030800} #Burrow',
		unburrow = { "code" : 0x030900}
		creep_tumor = { "code" : 0x033510} #Creep Tumor',
		larva = { "code" : 0x012020} #Larva',
		transfuse = { "code" : 0x032620} #Transfuse',
		class Burrowed():
			code = 0x009901

	class Mutalisk():
		code = 0x008801
		
	class Zergling():
		code = 0x008501
		burrow = { "code" : 0x023c00} #Burrow',
		unburrow = { "code" : 0x023d00}
		baneling = { "code" : 0x003a00, "min" : 25, "gas" : 25, "time" : 20}
		
		class BanelingCocoon():
			code = 0x002201
			cancel_baneling = { "code" : 0x012b00}
			
		class Burrowed():
			code = 0x009301

	class Baneling():
		code = 0x002301
		burrow = { "code" : 0x023400} #Burrow',
		unburrow = { "code" : 0x023500}
		explode = { "code" : 0x003500} #Explode',
		attack_structure = { "code" : 0x011d00} #Attack Structure'
		class Burrowed():
			code = 0x008f01

	class Roach():
		code = 0x008a01
		burrow = { "code" : 0x023a00} #Burrow',
		unburrow = { "code" : 0x023b00}
		class Burrowed():
			code = 0x009201
			

	class Hydralisk():
		code = 0x008701
		burrow = { "code" : 0x023800} #Burrow',
		unburrow = { "code" : 0x023900}
		class Burrowed():
			code = 0x009101 
			
	class Infestor():
		code = 0x008b01
		burrow = { "code" : 0x030c00} #Burrow',
		unburrow = { "code" : 0x030d00}

		fungal_growth = { "code" : 0x003710} #Fungal Growth',
		infested_terran = { "code" : 0x011e10} #Infested Terran',
		neural_parasite = { "code" : 0x011f20}
		class Burrowed():
			code = 0x009b01 

	class Ultralisk():
		code = 0x008901
		burrow = { "code" : 0x031200} #Burrow',
		unburrow = { "code" : 0x031300}
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
		corruption = { "code" : 0x003120} #Corruption',
		broodlord = { "code" : 0x023300, "min" : 150, "gas" : 150, "time" : 34}
		
		class BroodlordCocoon():
			code = 0x008d01
			cancel_broodlord = { "code" : 0x023301}
			
		class Broodlord():
			code = 0x008e01

	class Broodling():
		code = 0x00d001
		
	class Overlord():
		code = 0x008601
		unload_all = { "code" : 0x030412}
		unload_all_moving = { "code" : 0x030401}
		unload_unit = { "code" : 0x030433}
		load_unit = { "code" : 0x030404}
		creep = { "code" : 0x033400} #Generate Creep',
		cancel_creep = { "code" : 0x033401} #Stop generating Creep',
		unload_at = { "code" : 0x030401} #Unload all at',
		
		overseer = { "code" : 0x030e00, "min" : 50, "gas" : 100, "time" : 17}
		cancel_overseer = { "code" : 0x030e01}
		
		class OverseerCocoon():
			code = 0x009c01
			
	class Overseer():
		code = 0x009d01
		changling = { "code" : 0x011000} #Changeling',
		contaminate = { "code" : 0x040320} #Contaminate',

	class Changeling():
		code = 0x002601

	class NydusWorm():
		code = 0x00a901
		unload_all = { "code" : 0x030a01}
		unload_unit = { "code" : 0x030a33}
		load_unit = { "code" : 0x030a20}

	class SpineCrawler(Building, Attacker):
		code = 0x007e01
		uproot = { "code" : 0x033600}
		root = { "code" : 0x033810}
		cancel_root = { "code" : 0x33901}
		class Uprooted():
			code = 0x00a601

	class SporeCrawler(Building, Attacker):
		code = 0x007f01
		uproot = { "code" : 0x033700}
		root = { "code" : 0x033910}
		cancel_root = { "code" : 0x033901}
		class Uprooted():
			code = 0x00a701
	class Extractor():
		code = 0x007401
		
	class ZergMain(Production, Research):
		worker_rally_point = { "code" : 0x011b11} #Set worker rally point',
		worker_rally_target = { "code" : 0x011b11} #Set worker rally target',
		unit_rally_point = { "code" : 0x011b10} #Set unit rally point',
		unit_rally_target = { "code" : 0x011b10} #Set unit rally target',
		
		queen = { "code" : 0x032400, "min" : 150, "gas" : 0, "time" : 50}
		evolve_burrow = { "code" : 0x022e03, "min" : 100, "gas" : 100, "time" : 100}
		evolve_carapace = { "code" : 0x022e01, "min" : 100, "gas" : 100, "time" : 60}
		evolve_ventral_sacs = { "code" : 0x022e02, "min" : 200, "gas" : 200, "time" : 130}


	class Hatchery():
		code = 0x007201
		lair = { "code" : 0x022b00, "min" : 150, "gas" : 100, "time" : 80}
		cancel_lair = { "code" : 0x022b01}
	
	class Lair():
		code = 0x008001
		hive = { "code" : 0x022c00, "min" : 200, "gas" : 150, "time" : 100}
		cancel_hive = { "code" : 0x022c01}

	class Hive():
		code = 0x008101

	class SpawningPool():
		code = 0x007501
		adrenal_glands = { "code" : 0x022f00, "min" : 200, "gas" : 200, "time" : 130}
		metabolic_boost = { "code" : 0x022f01, "min" : 100, "gas" : 100, "time" : 110}


	class EvolutionChamber():
		code = 0x007601
		melee_attack_1 = { "code" : 0x022a00, "min" : 100, "gas" : 100, "time" : 160}
		melee_attack_2 = { "code" : 0x022a01, "min" : 150, "gas" : 150, "time" : 190}
		melee_attack_3 = { "code" : 0x022a02, "min" : 200, "gas" : 200, "time" : 200}
		ground_carapace_1 = { "code" : 0x022a03, "min" : 150, "gas" : 150, "time" : 160}
		ground_carapace_2 = { "code" : 0x022a04, "min" : 225, "gas" : 225, "time" : 190}
		ground_carapace_3 = { "code" : 0x022a05, "min" : 300, "gas" : 300, "time" : 220}
		missile_attack_1 = { "code" : 0x022a06, "min" : 100, "gas" : 100, "time" : 160}
		missile_attack_2 = { "code" : 0x022a07, "min" : 150, "gas" : 150, "time" : 190}
		missile_attack_3 = { "code" : 0x026a00, "min" : 200, "gas" : 200, "time" : 220}


	class RoachWarren():
		code = 0x007d01
		glial_recon = { "code" : 0x011c01, "min" : 100, "gas" : 100, "time" : 110} #Evolve Glial Reconstitution',
		tunneling_claws = { "code" : 0x011c02, "min" : 150, "gas" : 150, "time" : 110} #Evolve Tunneling Claws',


	class BanelingNest():
		code = 0x007c01
		centrifugal_hooks = { "code" : 0x031100, "min" : 150, "gas" : 150, "time" : 110}

	class CreepTumor():
		code = 0x007301
		class Burrowed():
			code = 0x00a501
			creep_tumor = { "code" : 0x033a10}
			cancel_creep_tumor = { "code" : 0x3fa06}

	class HydraliskDen():
		code = 0x007701
		grooved_spines = { "code" : 0x023002, "min" : 150, "gas" : 150, "time" : 80}


	class InfestationPit():
		code = 0x007a01
		pathogen_glands = { "code" : 0x031002, "min" : 150, "gas" : 150, "time" : 80}
		neural_parasite = { "code" : 0x031003,  "min" : 150, "gas" : 150, "time" : 110}


	class NydusNetwork():
		code = 0x007b01
		unload_all = { "code" : 0x030a01}
		unload_unit = { "code" : 0x030a33}
		load_unit = { "code" : 0x030a20}
		nydus= { "code" : 0x033d10,"min" : 100, "gas" : 100, "time" : 20}


	class Spire():
		code = 0x007801
		flyer_attack_1 = { "code" : 0x023100, "min" : 100, "gas" : 100, "time" : 160}
		flyer_attack_2 = { "code" : 0x023101, "min" : 175, "gas" : 175, "time" : 190}
		flyer_attack_3 = { "code" : 0x023102,  "min" : 250, "gas" : 250, "time" : 220}
		flyer_carapace_1 = { "code" : 0x023103, "min" : 150, "gas" : 150, "time" : 160}
		flyer_carapace_2 = { "code" : 0x023104, "min" : 225, "gas" : 225, "time" : 190}
		flyer_carapace_3 = { "code" : 0x023105, "min" : 300, "gas" : 300, "time" : 220}
		greater_spire = { "code" : 0x022d00, "min" : 100, "gas" : 150, "time" : 100}
		cancel_greater_spire = { "code" : 0x022d01 }
		class GreaterSpire():
			code = 0x008201

	class UltraliskCavern():
		code = 0x007901
		chitinous = { "code" : 0x012602, "min" : 150, "gas" : 150, "time" : 110}
		

