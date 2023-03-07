#! /usr/bin/python3

# List below last taken from https://docs.aws.amazon.com/general/latest/gr/rande.html on 2023-03-07
# Could be extracted from https://www.aws-services.info/regions.html in the future
regionDict = {
    "af-south-1": {"continent": "Africa", "city": "Cape Town"},
    "ap-east-1": {"continent": "Asia", "city": "Hongkong"},
    "ap-northeast-1": {"continent": "Asia", "city": "Tokyo"},
    "ap-northeast-2": {"continent": "Asia", "city": "Seoul"},
    "ap-northeast-3": {"continent": "Asia", "city": "Osaka"},
    "ap-south-1": {"continent": "Asia", "city": "Mumbai"},
    "ap-south-2": {"continent": "Asia", "city": "Hyderabad"},
    "ap-southeast-1": {"continent": "Asia", "city": "Singapore"},
    "ap-southeast-2": {"continent": "Asia", "city": "Sydney"},
    "ap-southeast-3": {"continent": "Asia", "city": "Jakarta"},
    "ap-southeast-4": {"continent": "Asia", "city": "Melborne"},
    "ca-central-1": {"continent": "Canada", "city": "Central"},
    "cn-north-1": {"continent": "China", "city": "Beijing"},
    "cn-northwest-1": {"continent": "China", "city": "Ningxia"},
    "eu-central-1": {"continent": "EU", "city": "Frankfurt"},
    "eu-central-2": {"continent": "EU", "city": "Zurich"},
    "eu-north-1": {"continent": "EU", "city": "Stockholm"},
    "eu-south-1": {"continent": "EU", "city": "Milan"},
    "eu-south-2": {"continent": "EU", "city": "Zaragoza (Spain)"},
    "eu-west-1": {"continent": "EU", "city": "Ireland"},
    "eu-west-2": {"continent": "EU", "city": "London"},
    "eu-west-3": {"continent": "EU", "city": "Paris"},
    "me-central-1": {"continent": "Middle", "city": "UAE"},
    "me-south-1": {"continent": "Middle", "city": "Bahrain"},
    "sa-east-1": {
        "continent": "South",
        "city": "Sao Paulo",
    },
    "us-east-1": {"continent": "US", "city": "N. Virginia"},
    "us-east-2": {"continent": "US", "city": "Ohio"},
    "us-gov-east-1": {
        "continent": "USGOV",
        "city": "US GovCloud East",
    },
    "us-gov-west-1": {
        "continent": "USGOV",
        "city": "US GovCloud West",
    },
    "us-west-1": {"continent": "US", "city": "N. California"},
    "us-west-2": {"continent": "US", "city": "Oregon"},
}

import sys

QUERY = sys.argv[1]

retCount = 0
if QUERY == "all":
    retItems = {regionCode: regionInfo for regionCode, regionInfo in regionDict.items()}
else:
    retItems = {
        regionCode: regionInfo
        for regionCode, regionInfo in regionDict.items()
        if QUERY.lower() in str(regionCode).lower()
        or QUERY.lower() in str(regionInfo["city"]).lower()
    }

xmlString = """<?xml version="1.0"?><items>"""
for item in retItems:
    xmlString += f"""<item uid="{item}" arg="{item}" valid="YES" autocomplete="{item}" type="file">"""
    xmlString += f"""<title>{item}</title>"""
    xmlString += f"""<subtitle>{retItems[item]['city']}, {retItems[item]['continent']}</subtitle>"""
    xmlString += """</item>"""
xmlString += """</items>"""
print(xmlString)
