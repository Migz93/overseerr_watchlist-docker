# Overseerr Watchlist
[![Docker Image CI](https://github.com/Migz93/overseerr_watchlist-docker/actions/workflows/main.yml/badge.svg)](https://github.com/Migz93/overseerr_watchlist-docker/actions/workflows/main.yml)  
Docker container that will receive webhooks from Overseerr and then add requests from specified user accounts to your Plex watchlist by searching Plex Discover.

# Config Setup
* Download `overseerr_watchlist_config.py.example` manually.
* Fill out options within `overseerr_watchlist_config.py.example`
* Rename `overseerr_watchlist_config.py.example` to `overseerr_watchlist_config.py`
* Mount directory with `overseerr_watchlist_config.py` as `/config` for container.

# Overseerr Setup
You need to configure the Overseerr webhook to point to the IP that this docker is running on, at port 5005.  
You also need to change the "JSON Payload" that Overseerr sends to have "subject, media_type, tmdbId & requestedBy_username" in the root of the request.  
Here's an example of my JSON Payload from Overseerr:
```yaml
{
    "notification_type": "{{notification_type}}",
    "event": "{{event}}",
    "subject": "{{subject}}",
    "message": "{{message}}",
    "media_type": "{{media_type}}",
    "tmdbId": "{{media_tmdbid}}",
    "tvdbId": "{{media_tvdbid}}",
    "requestedBy_username": "{{requestedBy_username}}"
}
```

# Docker Command
```bash
docker run -d \
  --name overseerr_watchlist \
  -v /path/to/config/dir:/config \
  -p 5005:5005/tcp \
  miguel1993/overseerr_watchlist
```

# Versions
* 31/08/2022 - Initial release.  

# Credits
https://python-plexapi.readthedocs.io/en/latest/introduction.html  
https://towardsdatascience.com/intro-to-webhooks-and-how-to-receive-them-with-python-d5f6dd634476

# Notes
Plex Discover is not as full a source of information as for example Trakt. So there is a chance with less popular media that Plex Discover does not have it, which would mean this script would be unable to add it to your watchlist.

Test
