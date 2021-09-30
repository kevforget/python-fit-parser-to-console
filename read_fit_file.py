import sys
import colog
import fitparse
from fitparse.records import DefinitionMessage


if len(sys.argv) >= 2:
    fileToParse = sys.argv[1]
else:
    print("Usage: python3 read_fit_file.py path/to/file.fit [fit_msg_type] [msg_display_number]")
    print("\tThe fit_msg_type correspond to fit message types in the garmin fit profile.")
    print("\t\tIt's optional but if filled it will show you only the desired msg type e.g. session")
    print("\tThe msg_display_number will show you the n firsts number of messages.")
    exit(1)

msg_type_filter = sys.argv[2] if len(sys.argv) >= 3 else None

desired_number_of_message = int(sys.argv[3]) if len(sys.argv) >= 4 else None

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
fitfile.parse()
print()

print(colog.blue("\tAfter parse infos :"))
print("\t\tFile : "+colog.yellow(fitfile._file))
print("\t\tCheck CRC : "+colog.yellow(fitfile.check_crc))
print("\t\tCRC : "+colog.yellow(fitfile._crc))
print("\t\tProcessor : "+colog.yellow(fitfile._processor))
print("\t\tIs complete ? : "+colog.yellow(fitfile._complete))
print()

cpt = 0
msg_cpt = 0

for msg in fitfile._messages:
    cpt += 1

    if desired_number_of_message != None and cpt > desired_number_of_message:
        print("Desired message printing limit reached exiting.")
        exit(0)

    if msg_type_filter != None and msg.name != msg_type_filter:
        continue

    if isinstance(msg, DefinitionMessage):
        print("\nDef message N°"+colog.cyan(cpt)+" : "+colog.yellow(msg.name))
        print(colog.magenta("\t"+str([fd.name for fd in msg.field_defs])))
    else:
        msg_cpt += 1
        print("\nDATA message N°"+colog.cyan(cpt)+" : "+colog.yellow(msg.name))
        myvar = ["name: "+field["name"]+("\t\t\t" if 6+len(field["name"]) < 16 else "\t\t" if 6+len(field["name"]) < 24 else "\t")+"value: "+str(field["value"]) for field in msg.as_dict()["fields"] if field['name'].find("unknown_") == -1]
        print("\t"+"\n\t".join(myvar))
           
print("\nReached end of messages, exiting\n")

