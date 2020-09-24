from common.ny_cab_data_exception import ApiException
from model import db


def get_trip_count(medallion=None, pickup_date=None):
    try:
        result_list = []

        if medallion is None:
            result = db.engine.execute("""select  medallion,date(pickup_datetime) as pickup_date, count(medallion) as total_trips from cab_trip_data
                                        group by medallion,date(pickup_datetime) """)
            for row in result:
                result_list.append(dict(row))

        elif medallion is not None and pickup_date is None:

            result = db.engine.execute("""select  medallion,date(pickup_datetime) as pickup_date, count(medallion)  as total_trips from cab_trip_data
                                        where medallion = '{medallion}'
                                    group by medallion,date(pickup_datetime)""".format(medallion=medallion))
            if result.rowcount > 0:
                for row in result:
                    result_list.append(dict(row))
            else:
                result_list.append({"medallion": medallion, "pickup_date": '', "total_trips": 0})

        elif medallion is not None and pickup_date is not None:

            result = db.engine.execute("""select  medallion,date(pickup_datetime) as pickup_date, count(medallion)  as total_trips from cab_trip_data
                                        where medallion in ('{medallion}')  and date(pickup_datetime) = date('{pickup_date}') 
                                        group by medallion,date(pickup_datetime)""".format(
                medallion=medallion,
                pickup_date=pickup_date))
            if result.rowcount > 0:
                for row in result:
                    result_list.append(dict(row))
            else:
                result_list.append({"medallion": medallion, "pickup_date": pickup_date, "total_trips": 0})
        return result_list
    except Exception as e:
        raise ApiException("Exception in Get trip data from Database")
