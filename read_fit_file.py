import sys
import colog
import fitparse
from fitparse.records import DefinitionMessage


fileToParse = sys.argv[1] if len(sys.argv) >= 2 else "tests/files/polartest.fit"


# Load the FIT file
fitfile = fitparse.FitFile(fileToParse)

print(colog.green("\n--------------------------------------------"))
print(colog.green("--- Welcome to that sick fit file parser ---"))
print(colog.green("--------------------------------------------\n"))

print(colog.blue("\tPre parse infos :"))
print("\t\tFile : "+colog.yellow(fitfile._file))
print("\t\tCheck CRC : "+colog.yellow(fitfile.check_crc))
print("\t\tCRC : "+colog.yellow(fitfile._crc))
print("\t\tProcessor : "+colog.yellow(fitfile._processor))
print("\t\tIs complete ? : "+colog.yellow(fitfile._complete))
print("\t\tMessages : "+colog.yellow(fitfile._messages))



print()
# We quiet the warning cause we know that coros uses custom messages and they are not greatly handled
fitfile.parse()
print()



print(colog.blue("\tAfter parse infos :"))
print("\t\tFile : "+colog.yellow(fitfile._file))
print("\t\tCheck CRC : "+colog.yellow(fitfile.check_crc))
print("\t\tCRC : "+colog.yellow(fitfile._crc))
print("\t\tProcessor : "+colog.yellow(fitfile._processor))
print("\t\tIs complete ? : "+colog.yellow(fitfile._complete))
print()
# print(colog.red("====================== SOME MESSAGES ======================"))

actividict = {
    "waypoints": [],
    "laps": [],
    "sessions": [],
    "activity": None
}

cpt = 0
msg_cpt = 0

# print(len(fitfile._messages))

for msg in fitfile._messages:
    cpt += 1
#     # print(cpt)
#     # print(msg)

#     # We check if the message is not an instance of DefinitionMessage (so it is a data message)
#     if not isinstance(msg, DefinitionMessage) :
#         # We get the key/values of the message

#         # print(msg_data)

#         msg_data = msg.get_values()
#         msg_data_keys = msg_data.keys()

#         print(msg_data)

#         # We check for the records (waypoints) and the minimal information needed
#         if msg.name == "record" and "position_lat" in msg_data_keys and "position_long" in msg_data_keys and "altitude" in msg_data_keys and "timestamp" in msg_data_keys:
#             # We append the waypoint to a waypoints list
#             actividict["waypoints"].append({
#                 "timestamp": msg_data["timestamp"],
#                 "lat": msg_data["position_lat"] / 11930465 if msg_data["position_lat"] != None else None,
#                 "lon": msg_data["position_long"] / 11930465 if msg_data["position_long"] != None else None,
#                 "altitude": msg_data["altitude"],
#                 "hr": msg_data["heart_rate"] if "heart_rate" in msg_data_keys else None,
#                 "cadence": msg_data["cadence"] if "cadence" in msg_data_keys else None
#             })

#         elif msg.name == "lap":
#             # We just push the lap data as it is, because it seems that there is no different defs
#             actividict["laps"].append(msg_data)
            

#         elif msg.name == "session":
#             # We just push the lap data as it is, because it seems that there is no different defs
#             actividict["sessions"].append(msg_data)
#             print([getattr(msg,attr) for attr in msg.__slots__][2])
#             print()

#         elif msg.name == "activity":
#             # according to fit documentations there must be only one activity record
#             # For multisport the activity will be tagged multisport and the sessions will tell the subsports
#             actividict["activity"] = msg_data
#             print(msg_data)
#         # print([getattr(msg,attr) for attr in msg.__slots__])
#         # print()


# activity = UploadedActivity()

# def _checkDictForVal(dataDict, keyName, valIfNone):
#     return dataDict[keyName] if keyName in dataDict.keys() else valIfNone

# # We check if there is only one session for the moment
# if len(actividict["sessions"]) == 1:
#     # We create a temp var for simplicity
#     actividata = actividict["sessions"][0]

#     print(actividata["total_timer_time"])

#     # And we fill the activity data
#     activity.StartTime = actividata["start_time"]
#     activity.EndTime = actividata["timestamp"]
#     activity.Type = ActivityType.Running
#     activity.Stats = ActivityStatistics(
#         distance=actividata["total_distance"], 
#         timer_time=actividata["total_timer_time"], 
#         avg_speed=actividata["avg_speed"], 
#         max_speed=actividata["max_speed"], 
#         avg_hr=actividata["avg_heart_rate"], 
#         max_hr=actividata["max_heart_rate"], 
#         avg_run_cadence=actividata["avg_running_cadence"], 
#         max_run_cadence=actividata["max_running_cadence"],
#         strides=_checkDictForVal(actividata,"total_strides",0),
#         kcal=actividata["total_calories"],
#         avg_temp=actividata["avg_temperature"],
#         avg_power=_checkDictForVal(actividata, "avg_power", None)
#     )
# else:
#     # TODO handle multipple sessions
#     raise NotImplementedError

# activity.Laps = [
#     # A bit like the SELECT SQL clause
#     Lap(
#         startTime=lapData["start_time"], 
#         endTime=lapData["timestamp"],
#         waypointList=[
#             # SELECT
#             Waypoint(
#                 timestamp=wp["timestamp"],
#                 location=Location(
#                     lat=wp["lat"],
#                     lon=wp["lon"],
#                     alt=wp["altitude"]
#                 ),manual
#                 hr=wp["hr"],
#                 runCadence=wp["cadence"]
#             )
#             # FROM actividict["waypoints"] as wp
#             for wp in actividict["waypoints"]
#             # WHERE the wp timestamp is between the lap start and end timestamps.
#             if (wp["timestamp"] >= lapData["start_time"] and wp["timestamp"] < lapData["timestamp"])
#         ]
#     )
#     # FROM actividict["laps"]
#     for lapData in actividict["laps"]
# ]

# # I set the GPS and the Stationary as they are mandatory for the Sanity Check to succeed. 
# activity.GPS=True
# activity.Stationary=False
# activity.CheckSanity()



# # self.TZ = tz
# # self.FallbackTZ = fallbackTz
# # self.Name = name
# # self.Notes = notes
# # self.Private = private
# # self.Stationary = stationary
# # self.GPS = gps
# # self.PrerenderedFormats = {}
# # self.Device = device

# print('\n'.join(actividict["sessions"][0].keys()))







    if cpt < 10000:
        if isinstance(msg, DefinitionMessage) :
            print("\nDef message N°"+colog.cyan(cpt)+" : "+colog.yellow(msg.name))
            print(colog.magenta("\t"+str([fd.name for fd in msg.field_defs])))
        # elif isinstance(msg, DataMessage):
        else:
            # if msg.name == "file_id" :
            msg_cpt += 1
            print("\nDATA message N°"+colog.cyan(cpt)+" : "+colog.yellow(msg.name))
            myvar = ["name: "+field["name"]+("\t\t\t" if 6+len(field["name"]) < 16 else "\t\t" if 6+len(field["name"]) < 24 else "\t")+"value: "+str(field["value"]) for field in msg.as_dict()["fields"] if field['name'].find("unknown_") == -1]
            print("\t"+"\n\t".join(myvar))
                # print([field for field in msg.as_dict()["fields"] if field['name'] == "cadence"])
                # print("\t\tStart: "+ str(msg.as_dict()["fields"][1]["value"])+ "\tEnd: "+str(msg.as_dict()["fields"][4]["value"]))
            
            # if msg.name == "record":
            #     print("\nDATA message N°"+colog.cyan(cpt)+" : "+colog.yellow(msg.name))
                # print(str(msg.as_dict()["fields"][11]["value"]))
            
                # rec_field_names_array = [field["name"] for field in msg.as_dict()["fields"]]
                # position_lat_in_array = [field["value"] for field in msg.as_dict()["fields"] if field["name"] == "position_lat"]
                # position_long_in_array = [field["value"] for field in msg.as_dict()["fields"] if field["name"] == "position_long"]
                # altitude_in_array = [field["value"] for field in msg.as_dict()["fields"] if field["name"] == "altitude"]
                # timestamp_in_array = [field["value"] for field in msg.as_dict()["fields"] if field["name"] == "timestamp"]
            #     # if "position_lat" in rec_field_names_array and "position_long" in rec_field_names_array:
            #     #     if not position_lat_in_array == [None] and not position_long_in_array == [None] :
            #     #         print("\t\tData message N°"+colog.cyan(cpt)+" : "+colog.yellow(msg.name))
            #     #         print("\t\t\tLat : "+colog.red(position_lat_in_array[0]))
            #     #         print("\t\t\tLong : "+colog.red(position_long_in_array[0]))
            #     #         # print("\t\t\tAltitude : "+colog.red(altitude_in_array[0] if not len(altitude_in_array) == 0 else None))
            #     #         print("\t\t\tTimestamp : "+colog.red(timestamp_in_array[0]))
            # if msg.name == "session" or msg.name == "lap" :#or msg.name == "event":
            #     print('\n'.join([str(field["name"])+" : "+str(field["value"]) for field in msg.as_dict()["fields"]]))
            #     # print(msg.get_values()["cadence"] if "cadence" in msg.get_values().keys() else None)
            #     # print(msg.get_values()["temp"])
            #     print()

                # print("position_lat" in rec_field_names_array)
                # for field in msg.as_dict()["fields"]:
                #     print(field["name"])
                # print("\t\tData name : "+colog.blue(msg.as_dict()["fields"]))

# print(msg_cpt)
# print(isinstance(fitfile._messages[0], DefinitionMessage))
# print(fitfile._messages[0].name)

# print("Messages : "+colog.yellow(fitfile._messages[0]))
# print("Messages : "+colog.yellow(fitfile._messages[1]))
# print("Messages : "+colog.yellow(fitfile._messages[2]))
# print("Messages : "+colog.yellow(fitfile._messages[3]))


print()


# with warnings.catch_warnings():
#     # warnings.simplefilter("error")
#     try:
#         messages = fitfile.messages
#     except UserWarning as err:
#         print("lol")


# messages = fitfile.messages



# warnings.filterwarnings('error')



# try:
#     messages = fitfile.messages
# except UserWarning as err:
#     warnings.filterwarnings('ignore')
#     messages = fitfile.messages
#     # if str(err).find("Message ") == 0:
#     #     print(messages)
#     pass

# try:
#     # fitfile.messages[0]
#     print("meh")
#     for message in fitfile.messages:
#         print("meh2")
#         if message.name != "record":
#             print(colog.red(message.name))
#             print(colog.green(message.get_values()))
#     # print("\t"+colog.blue(fitfile.messages[73].get_values()))
#     # print(colog.yellow(fitfile.messages[74]))
#     # print("\t"+colog.blue(fitfile.messages[74].get_values()))
#     # print(colog.yellow(fitfile.messages[75]))
#     # print("\t"+colog.blue(fitfile.messages[75].get_values()))

#     # print(colog.red("------------------- SEP -------------------"))

#     # print(colog.yellow(fitfile.messages[91]))
#     # print("\t"+colog.blue(fitfile.messages[91].get_values()))
#     # print(colog.yellow(fitfile.messages[92]))
#     # print("\t"+colog.blue(fitfile.messages[92].get_values()))
#     # print(colog.yellow(fitfile.messages[93]))
#     # print("\t"+colog.blue(fitfile.messages[93].get_values()))
# except UserWarning as err:
#     if str(err).find("Message ") == 0:
#         print("found somethin maaaaaan")
#     warnings.filterwarnings('ignore')
#     pass

# for message in fitfile.messages:
#     if message.name != "record":
#         print(colog.red(message.name))
#         print(colog.green(message.get_values()))

# print(colog.red(fitfile.get_messages("device_info")))
# # Iterate over all messages of type "record"
# # (other types include "device_info", "file_creator", "event", etc)
# for record in fitfile.get_messages("device_info"):

#     print(colog.green(record))

#     # Records can contain multiple pieces of data (ex: timestamp, latitude, longitude, etc)
#     for data in record:

#         # Print the name and value of the data (and the units if it has any)
#         if data.units:
#             print(" * {}: {} ({})".format(data.name, data.value, data.units))
#         else:
#             print(" * {}: {}".format(data.name, data.value))

#     print("---")
