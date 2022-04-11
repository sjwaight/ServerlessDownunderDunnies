import logging
import json
import mysql.connector
import os

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:

    postcode = req.route_params.get('postcode')

    if postcode and len(postcode) == 4 and postcode.isdigit():

        #MYSQL Connection
        cnx = mysql.connector.connect(user=os.environ["dunnydbuser"], password=os.environ["dunnydbsecret"],
                            host=os.environ["dunnydbhost"],
                            database=os.environ["dunnydbname"])
        #Query
        cursor = cnx.cursor()
        query = ("SELECT name, address1, town FROM toilets "
        "WHERE postcode=" + postcode)
        cursor.execute(query)
        resultRow = ""
        for (name, address1, town) in cursor:
            resultRow = resultRow + json.dumps({'name' : name, 'address1': address1, 'town': town}) + ","
        resultRow = resultRow.rstrip(",")
        cursor.close()
        cnx.close()
        returnData = "[" + resultRow + "]"

        return func.HttpResponse(returnData)

    else:
        return func.HttpResponse(
             "INVALID input",
             status_code=400
        )