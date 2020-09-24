import datetime

from flask import Blueprint, json, Response, request
from flask_api_cache.api_cache import ApiCache

from common.ny_cab_data_exception import ApiException
from model.CabTripData import CabTripDataModel

trip_details_api = Blueprint('tripdetails', __name__)


@trip_details_api.route('/', methods=['GET'])
@ApiCache(expired_time=30)
def get_trip_counts():
    try:
        date = request.args.get('date', default=None, type=str)
        if date is not None:
            try:
                datetime.datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                return build_response({"Error": ' Date Format should be %Y-%m-%d'}, 400)
        medallion = request.args.get('medallion', default=None, type=str)
        response = CabTripDataModel.get_total_trips(medallion, date)
        return build_response(response, 200)
    except ApiException as e:
        return build_response("""{Error : DB Error}""", 500)

    except Exception as e:
        return build_response("""{Error : Server Error}""", 500)


def build_response(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
