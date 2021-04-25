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


def serialize(obj):
    return json.dumps(obj, default=my_enc, sort_keys=True)
