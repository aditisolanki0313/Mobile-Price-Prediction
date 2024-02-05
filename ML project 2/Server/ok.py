import json
import pickle
import numpy as np 

__Name = None
__data_columns = None
__model = None

def get_estimated_price(Name, Battery_mAh, Camera_MP, Storage_GB_RAM,Storage_GB_ROM,Display_cm):
    try:
        loc_index = __data_columns.index(Name.lower())
    except:
        loc_index = -1

    x_input = np.zeros(len(__data_columns))

    x_input[0] = Battery_mAh
    x_input[1] = Camera_MP
    x_input[2] = Storage_GB_RAM
    x_input[3] = Storage_GB_ROM
    x_input[4] = Display_cm
   
    if loc_index >= 0:
        x_input[loc_index] = 1

    return round(__model.predict([x_input])[0],2)

def load_saved_art():
    print("loading saved art...start")
    global __data_columns
    global __Name

    with open("server/art/mobile.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __Name = __data_columns[3:]
    
    global __model
    if __model is None:
        with open ("server/art/mobile_price.pickle", 'rb') as f:
            __model = pickle.load(f)
        print("loading saved art...done")

    #     with open('your_model_file.pkl', 'rb') as f:
    # __model = pickle.load(f, encoding='latin1')

def get_mobile_name():
    return __Name

def get_data_columns():
    return __data_columns

if __name__ == "__main__":
    load_saved_art()
    print(get_mobile_name())
    print(get_estimated_price('alcatel 3x (black, 32 gb)', 1000, 15,12,58,43))