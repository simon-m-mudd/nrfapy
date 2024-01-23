#=============================================================================
# Script to get a timeseries
#
# Authors:
#     Simon Mudd
#=============================================================================
#=============================================================================
# IMPORT MODULES
#=============================================================================


#from __future__ import print_function
import pandas as pd
import nrfapy
import sys

#=============================================================================
# This is just a welcome screen that is displayed if no arguments are provided.
#=============================================================================
def print_welcome():

    print("\n\n=======================================================================")
    print("Hello! I'm going to grab some data from opentopography.")
    print("You will need to tell me which directory to look in.")
    print("Use the -dir flag to define the working directory.")
    print("If you don't do this I will assume the data is in the same directory as this script.")
    print("You also need to tell me the prefix of the DEM you want to download")
    print("Use the -fname flag to designate a file prefix")
    print("For help type:")
    print("   lsdtt_grabopentopographydata -h\n")
    print("=======================================================================\n\n ")

#=============================================================================
# A little file parsing tool
#=============================================================================    
def add_csv_extension(filename):
    if not filename.endswith('.csv'):
        filename += '.csv'
    return filename    
    
    
#=============================================================================
# This is the main function that runs the whole thing
#=============================================================================
def main(args=None):

    if args is None:
        args = sys.argv[1:]    
    
    # If there are no arguments, send to the welcome screen
    if not len(sys.argv) > 1:
        full_paramfile = print_welcome()
        sys.exit()

    # Get the arguments
    import argparse
    parser = argparse.ArgumentParser()
    
    #==========================================================================
    # The location of the data files
    parser.add_argument("-id", "--id", type=int, help="The station ID. At the moment there is no error checking if this station exists.")
    parser.add_argument("-dt", "--data_type", type=str, help="The kind of data you want. Options are 'gdf', 'ndf', 'gmf', 'nmf', 'cdr', 'cdr-d', 'cmr', 'pot-stage', 'pot-flow','gauging-stage', 'gauging-flow','amax-stage', 'amax-flow' please see https://nrfa.ceh.ac.uk/data-formats-types")
    parser.add_argument("-of", "--out_file_name", type=str, help="The name of the output file.",default="nrfa_data.csv")

    args = parser.parse_args()
 
    if not args.id:
        print("WARNING! You haven't supplied your station ID. Please specify this with the flag '-id'")
        sys.exit()
        
    if not args.data_type:
        print("WARNING! You haven't supplied your data_type. Please specify this with the flag '-dt'")
        sys.exit()

    df = nrfapy.get_ts(args.id,args.data_type)
    
    
    args.out_file_name = add_csv_extension(args.out_file_name)
    print("I'm printing your timeseries to the file "+args.out_file_name)
    df.to_csv(args.out_file_name,index = False)
    




#=============================================================================
if __name__ == "__main__":
    main()

