import argparse
import core.core_logger as cl

"""
This file is the starting point of the complete Amersfoort script
"""

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Aanpassen van folder structuur.")
    parser.add_argument('--gemeente', required=True, help="Naam van de gemeente die verwerkt wordt")
    args = parser.parse_args()

    # Import the correct mapping
    try:
        mm = __import__("mapping.mapping_" + args.gemeente.lower(), fromlist=['startMapping'])
    except ModuleNotFoundError:
        print(f"De correcte mapping kon niet worden gevonden.")
        exit()  # Stop execution of the script

    # Initialize a new log file
    cl.initLog(args.gemeente.lower())

    try:
        mm.startMapping()
    except AttributeError:
        print(f"De functie 'startMapping' kon niet worden gevonden in de mapping module.")
        exit()  # Stop execution of the script


    print("Stop met de uitvoering van het hoofdscript...")