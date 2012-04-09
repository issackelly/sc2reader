import json
import os
import logging

abilities = {}
objects = {}

def create_class(base, obj):
    return type(str(obj['vid']), (base,), obj)

class Base(object):
    def __str__(self):
        return self.title
    def __repr__(self):
        return "<'%(title)s'>" % {
                      "title": self.title if self.title else self.vid if self.vid else self.__class__.__bases__[0].__name__
                      }

def create_package(filename):
    with open(filename, "rb") as f:
        package = {}
        current = json.load(f)

        # Create ability templates
        moveable_abilities = current["moveable_abilities"]
        attacker_abilities = current["attacker_abilities"]

        # Create our base objects
        Object = create_default("Object", current["object_defaults"])
        Ability = create_default("Ability", current["ability_defaults"])

        package["default"] = [Object, Ability]

        # Create all the Objects
        objects, t_objects = create_multiple(Object, current["objects"])

        for key, obj in objects.iteritems():
            if obj.moveable and obj.attacker:
                obj.abilities.extend(Object.abilities + moveable_abilities + attacker_abilities)
            elif obj.moveable:
                obj.abilities.extend(Object.abilities + moveable_abilities)
            elif obj.attacker:
                obj.abilities.extend(Object.abilities + attacker_abilities)
            else:
                obj.abilities.extend(Object.abilities)
        # Create all the Abilities
        abilities, t_abilities = create_multiple(Ability, current["abilities"])

        # Create references to objects
        for obj in abilities.itervalues():
            if obj.build_unit:
                try:
                    obj.build_unit = t_objects[obj.build_unit]
                except KeyError:
                    logging.debug("Missing unit: %s", obj.build_unit)

        # Create references to abilities
        for obj in objects.itervalues():
            for i, ability in enumerate(obj.abilities):
                if (ability in ["RightClickTarget", "RightClickLocation"]):
                    continue
                try:
                    obj.abilities[i] = t_abilities[ability]
                except KeyError:
                    logging.debug("Missing ability: %s", ability)
        del t_abilities, t_objects
        # Check for unused abilities and objects if debugging is enabled
        if (logging.getLogger().level == logging.DEBUG):
            import sys
            for obj in abilities.itervalues():
                if sys.getrefcount(obj) <= 4:
                    logging.debug("Unused ability: %s", obj)

        package["objects"] = objects
        package["abilities"] = abilities
        return package

def create_default(name, obj):
    return type(name, (Base,), obj)

def create_class(base, obj):
    try:
        return type(str(obj["vid"]), (base,), obj)
    except KeyError:
        print obj

def create_multiple_x(base, dictionary):
    return [create_class(base, obj) for key, obj in dictionary.iteritems()]

def create_multiple(base, dictionary):
    result, temp = {}, {}
    for key, obj in dictionary.iteritems():
        if key in result:
            print "Duplicate key " + key
        obj = create_class(base, obj)
        try:
            obj.code = int(key)
        except:
            obj.code = key
        result[obj.code] = obj
        temp[obj.vid] = obj
    return result, temp

def test(dir="sc2reader/new_data/"):
    logging.getLogger().setLevel(logging.DEBUG)
    p = []
    for filename in ["v12.json", "v13.json", "v14.json", "v133.json", "v142.json"]:
        print "Starting: " + filename
        p.append(create_package(os.path.join(dir, filename)))
    return p
