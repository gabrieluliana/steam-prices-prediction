from steam_dataframe import SteamGameData
import sys


print(sys.argv[1])
steam_gamedata = SteamGameData(sys.argv[1])

# print(steam_gamedata.raw_df)
# print(steam_gamedata.raw_attributes)

steam_gamedata.process_attributes()
steam_gamedata.df.to_csv("steam_processed.csv")

    

