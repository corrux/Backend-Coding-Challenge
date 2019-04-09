from flask import Flask
import pymongo


app = Flask(__name__)


@app.route('/excavator_operating_hours_since_last_maintenance', methods=['GET'])
def get_hours_since_last_maintenance():
    return None


@app.route('/excavator_average_fuel_rate_past_24h', methods=['GET'])
def get_average_guel_rate_past_24h():
    return None


@app.route('/excavator_last_10_CAN_messages', methods=['GET'])
def get_last_10_CAN_messages():
    return None


@app.route('/excavator_operational', methods=['GET'])
def get_operational_status():
    return None
