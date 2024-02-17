from config import Config
import hashlib, pathlib, pickle, os, time, json, subprocess
class Game():
    def __init__(self):
        self.path = Config.path+'/savegames'
        self.files = {'files': {}}
    def setdata(self):
        for (dirpath, dirnames, filenames) in os.walk(self.path):
            for filename in filenames:
                if not filename.endswith('.baronysave'):
                    print(f'Skipping for {filename}')
                    continue
                with open(self.path+'/'+filename) as f:
                    parsed = json.loads(f.read())
                print(f"Backup for {filename}")
                self.files['files'][filename] = {}
                self.files['files'][filename]['data'] = parsed
        print(f'Detected {len(self.files["files"])} saves, awaiting file changes ')
    
    def backup(self, path, save):
        for index, player in enumerate(self.files["files"][save]["data"]['players']):
            if player['stats']['maxHP'] != 0:
                self.files["files"][save]["data"]['players'][index]['stats']['MP'] = self.files["files"][save]["data"]['players'][index]['stats']['maxMP']
                self.files["files"][save]["data"]['players'][index]['stats']['HP'] = self.files["files"][save]["data"]['players'][index]['stats']['maxHP']
                self.files["files"][save]["data"]['players'][index]['stats']['HUNGER'] = 1000
                print(f"Restored HP, MP and hunger for player {index+1}")
        with open(path, 'w') as f:
            json.dump(self.files["files"][save]["data"], f, indent=4)
        print(f"Successfully backed up {path}! Remember to go back to main menu to restart.")

    def checkchange(self):
        self.setdata()
        while True:
            dirs = [i for i in self.files['files'].keys()]
            for i in dirs:
                path=self.path+'/'+i
                try:
                    with open(path, 'r') as f:
                        parsed = json.loads(f.read())
                    if parsed != self.files['files'][i]['data']:
                        with open(path) as f:
                            parsed = json.loads(f.read())
                        self.files['files'][i]['data'] = parsed
                        print("Dungeon progress detected, saving progress!")
                    else:
                        pass
                    for (dirpath, dirnames, filenames) in os.walk(self.path):
                        if len([i for i in filenames if i.endswith('.baronysave')]) > len([i for i in self.files['files'].keys() if i.endswith('.baronysave')]):
                            self.files = {'files': {}}
                            self.setdata()
                except FileNotFoundError:
                    self.backup(path=path, save=i)
            time.sleep(0.75)
m = Game()
m.checkchange()