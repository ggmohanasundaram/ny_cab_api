from model.cab_trip_queries import get_trip_count
from . import db


class CabTripDataModel(db.Model):
    __tablename__ = 'cab_trip_data'

    medallion = db.Column(db.Text, primary_key=True)
    hack_license = db.Column(db.Text, nullable=True)
    vendor_id = db.Column(db.Text, nullable=True)
    rate_code = db.Column(db.Integer, nullable=True)
    store_and_fwd_flag = db.Column(db.Text, nullable=True)
    pickup_datetime = db.Column(db.DateTime)
    dropoff_datetime = db.Column(db.DateTime)
    passenger_count = db.Column(db.Integer, nullable=True)
    trip_time_in_secs = db.Column(db.Float, nullable=True)
    trip_distance = db.Column(db.Float, nullable=True)

    @staticmethod
    def get_all_trips():
        return CabTripDataModel.query.all()

    @staticmethod
    def get_cab_trips(medallion):
        return CabTripDataModel.query.get(medallion)

    @staticmethod
    def get_total_trips(medallion, data):
        return get_trip_count(medallion, data)
