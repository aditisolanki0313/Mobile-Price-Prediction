from flask import Flask, request, jsonify

import ok

app = Flask(__name__)



@app.route('/get_mobile_name', methods = ['GET'])
def get_mobile_name():
    response = jsonify({
        'Name': ok.get_mobile_name()
    })
    response.headers.add('Access-control-allow-origin', '*') 
    return response

@app.route('/predict_Price', methods= ['POST'])

def predict_Price():
    Name = request.form['Name']
    Battery_mAh = int(request.form['Battery_mAh'])
    Camera_MP = int(request.form['Camera_MP'])
    Storage_GB_RAM = int(request.form['Storage_GB_RAM'])
    Storage_GB_ROM = int(request.form['Storage_GB_ROM'])
    Display_cm = int(request.form['Display_cm'])

    response = jsonify({
        'estimated_Price': ok.get_estimated_Price(Name, Battery_mAh, Camera_MP, Storage_GB_RAM,Storage_GB_ROM,Display_cm)
    })
    response.headers.add('Access-control-allow-origin', '*')
    return response


if __name__ == "__main__":
    print("starting python flask server for mobile price prediction...")
    ok.load_saved_art()
    app.run()
