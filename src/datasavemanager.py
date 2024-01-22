import pickle
import os
from Config.datasavenames import DATASAVENAMES

class DataSaveManager():
    playerData = {}

    @classmethod
    def dump(cls):
        try:
            with open('playerdata.pkl', 'wb') as f:
                pickle.dump(cls.playerData, f)
        except Exception as e:
            raise e
        
    @classmethod
    def load(cls):
        try:
            with open('playerdata.pkl', 'rb') as f:
                return pickle.load(f)
        except Exception as e:
            raise e

    @classmethod
    def init(cls):
        if os.path.exists('playerdata.pkl') and os.path.getsize('playerdata.pkl') > 0:
            cls.playerData = cls.load()         

        for datasavename, datasavedefaultvalue in DATASAVENAMES.items():
            if not datasavename in cls.playerData:
                cls.playerData[datasavename] = datasavedefaultvalue

    @classmethod
    def get(cls, data_name):
        if not data_name in cls.playerData:
            raise Exception("f{data_name} does not exist in DATASAVENAMES")
        return cls.playerData[data_name]

    @classmethod
    def update(cls, data_name, value):
        if not data_name in cls.playerData:
            raise Exception("f{data_name} does not exist in DATASAVENAMES")
        try:
            cls.playerData[data_name] = value
            cls.dump()
        except Exception as e:
            raise e

if __name__ == "__main__":
    DataSaveManager.init()
    print(DataSaveManager.get("Highscore"))
    DataSaveManager.update("Highscore", 20)
    print(DataSaveManager.get("Highscore"))