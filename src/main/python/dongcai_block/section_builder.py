#encoding=utf-8
import datetime
def section_build_stock(source):
    dest = {}

    date_now = datetime.datetime.now()
    block_data = {
                    "ClassId": "00451", 
                 
                    "SysCode":"行业板块",
                    "SectionNameH":"房地产",
                    "SectionName":"房地产",
                    "PlateCode":"DH00451", 
                    "SectionLevel": "0",
                    "MarketCode": "DH",
                    "StockCode":"600639",
                    "StockShortName":"浦东金桥",
                    "Obj":"SH600639",
                    "bzzb":1,
    }
    SysCodeSwitch = {
                    'DD':1001,
                    'DG':1002,
                    'DH':1003,
    }
    
    dest["ClassId"] = source["SysCode"][2:]
    dest["SysCode"] = SysCodeSwitch[source["SysCode"][:2]]
    dest["SectionNameH"] = source["TypeName"]
    dest["SectionName"] = source["TypeName"]
    dest["PlateCode"] = source["SysCode"]
    dest["SectionLevel"] = 1
    dest["MarketCode"] = source["Code"][:2]
    dest["StockCode"] = source["Code"][2:]
    dest["Obj"] = source["Code"]
    # dest["StockShortName"] = source["Name"]
    dest["bzzb"] = 1
    dest["UpdateDateTime"] = date_now - datetime.timedelta(hours=8)

    # dest["ClassId"] = source["Name"]
    # dest["ClassId"] = source["Name"]
    # dest["ClassId"] = source["Name"]


    return dest



def section_build(source, gps):
    dest = {}

    date_now = datetime.datetime.now()
    block_data = {
                "ClassId": "00498",
                "SysCode":"概念板块", 
                "SectionLevel": "0",
                "PlateCode":"DG00498",
                "SectionNameH":"AB股",
                "SectionName":"AB股",
                "gps":0, 
                "ComputerType":1,    
                "ShortCode":"A"
    }
    SysCodeSwitch = {
                    'DD':1001,
                    'DG':1002,
                    'DH':1003,
    }
    
    
    dest["ClassId"] = source["SysCode"][2:]
    dest["SysCode"] = SysCodeSwitch[source["SysCode"][:2]]
    dest["SectionLevel"] = 1
    dest["PlateCode"] = source["SysCode"]
    dest["SectionNameH"] = source["TypeName"]
    dest["SectionName"] = source["TypeName"]

    dest["gps"] = gps

    dest["ComputerType"] = 1
    dest["UpdateDateTime"] = date_now - datetime.timedelta(hours=8)
    # dest["ShortCode"] =  source["TypeZm"]    
    
    

    # dest["ClassId"] = source["Name"]
    # dest["ClassId"] = source["Name"]
    # dest["ClassId"] = source["Name"]


    return dest