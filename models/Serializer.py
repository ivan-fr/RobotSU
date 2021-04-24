import json
import models.TerrainContinu
import models.Vecteur
import models.Robot
import models.Polygone

def my_enc(obj):
    dic = {k: v for k, v in obj.__dict__.items() if not k.startswith("_")}
    dic.update({"__class": obj.__class__.__name__})
    return dic


def my_hook(dic):
    if "__class" in dic:
        cls = dic.pop("__class")
        return eval(f"models.{cls}.{cls}")(**dic)
    return dic


def serialize(terrainContinu, robot):
    f = open("TC.json", "w")
    json.dump(terrainContinu, f, default=my_enc, indent=4, sort_keys=True)
    f.close()
    f = open("Robot.json", "w")
    json.dump(robot, f, default=my_enc, indent=4, sort_keys=True)
    f.close()


def deserialize(filename):
    return json.load(open(filename, "r"), object_hook=my_hook)
