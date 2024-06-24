import json

# basic data loader for local json writing

class DataLoader:
    def __init__(self, file_Path: str, data: any = None):
        self.file_Path = file_Path
        self.data = data
    
    def read_Json(self):
        try:
            with open(self.file_Path, "r") as f:
                self.data = json.load(f)
            print("Successfully read data from", self.file_Path)
        except FileNotFoundError:
            print("File not found:", self.file_Path)
            self.data = {}  

    def traverse_Nested_Json(self, keys: list):
        nested_Key = self.data
        for key in keys:
            nested_Key = nested_Key[key]

        return nested_Key

    def append_Json(self, new_Object: dict, keys: list):
        nested_Key = self.traverse_Nested_Json(keys)

        nested_Key.append(new_Object)
        print(f'New {keys[-1][:len(keys[-1]) - 1]} created.')

    def save_Json(self):
        with open(self.file_Path, "w") as f:
            json.dump(self.data, f, indent=2) 
        print("Successfully wrote data to", self.file_Path)

    def display_Json(self, keys: list):
        nested_Key = self.traverse_Nested_Json(keys)

        for idx, item in enumerate(nested_Key):
            print(f'{idx + 1}:')
            for k, v in item.items():
                print(f'{k}: {v}')
            print()