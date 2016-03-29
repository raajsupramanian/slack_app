__author__ = 'raajsupra'
import json
from urlparse import urlparse
import httplib2 as http
import MySQLdb


db = MySQLdb.connect("raajsupra.mysql.pythonanywhere-services.com", "raajsupra", "global123", "raajsupra$lta")
cursor = db.cursor()


def fetch_data(skip=0):

    headers = {'AccountKey': 'M5y5OziKjipQSgZz9oEjOw==',
               'UniqueUserID': 'ecea9859-a840-4723-a7ad-f875d739f1a5',
               'accept': 'application/json'}  # Request results in JSON

    # API parameters
    uri = 'http://datamall2.mytransport.sg/ltaodataservice/'  # Resource URL
    bus_arrival_path = 'BusArrival?'
    bus_stops = 'BusStops?$skip=%s' % skip
    # Query parameters
    params = {'skip':skip}
    # Build query string & specify type of API call
    target = urlparse(uri + bus_stops)
    method = 'GET'
    body = ''

    # Get handle to http
    h = http.Http()
    # Obtain results
    return h.request(
        target.geturl(),
        method,
        body,
        headers)


if __name__== "__main__":
    # Authent
    # ication parameters
    # Parse JSON to print
    skip = 0
    response, content = fetch_data()
    content = json.loads(content)
    data_list = content["value"]
    while response and response['status'] == '200' and len(data_list):
        if skip != 0:
            content = json.loads(content)
            data_list = content["value"]
        skip += 50
        print "Writing" + str(skip)
        for data in data_list:
            query = 'INSERT INTO bus_stops values ("{0:s}", "{1:s}", {2:f}, {3:f}, "{4:s}")'.format(
                data['BusStopCode'],
                data['Description'],
                data['Latitude'],
                data['Longitude'],
                data['RoadName'])
            print query
            cursor.execute(query)
            db.commit()
        response, content = fetch_data(skip)
    db.close()
