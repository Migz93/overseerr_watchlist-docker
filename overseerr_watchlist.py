import logging
from flask import Flask, request, Response
from plexapi.myplex import MyPlexAccount

logging.basicConfig(filename="/config/overseerr_watchlist.log", level=logging.INFO,
                    format="%(asctime)s: %(message)s")

#Copy config file from /config folder into /app folder
import os
os.system('cp /config/overseerr_watchlist_config.py /app/overseerr_watchlist_config.py')  
#Import config from file
import overseerr_watchlist_config

username = overseerr_watchlist_config.username
plex_token = overseerr_watchlist_config.plex_token
overseerr_users = overseerr_watchlist_config.overseerr_users

#Create printLog function
def printLog(*args, **kwargs):
    print(*args, **kwargs)
    logging.info(*args, **kwargs)

printLog("-----Starting Up-----")
account = MyPlexAccount(username=username, token=plex_token)
printLog(f"Plex account is, {account}.")


app = Flask(__name__)
@app.route('/overseerr', methods=['POST'])
def return_response():
    data = request.json
    printLog("----------------------")
    printLog("Request from Overseerr received, data:")
    printLog(data)
    username = data["requestedBy_username"]
    if username in overseerr_users:
        printLog(f"Request from {username}, progressing.")
        title = data["subject"]
        printLog(f"Title is: {title}.")
        tmdb = data["tmdbId"]
        printLog(f"TMDB ID is: {tmdb}.")
        media_type = data["media_type"]
        search = account.searchDiscover(title, libtype=media_type)
        for result in search:
            printLog("Looping through search results.")
            for guid in result.guids:
                if tmdb in guid.id:
                    printLog("Matched TMDB ID.")
                    printLog(result)
                    printLog(guid.id)
                    printLog("Adding to Plex watchlist")
                    account.addToWatchlist(result)

    return Response(status=200)
if __name__ == "__main__": app.run(host='0.0.0.0', port=5005)