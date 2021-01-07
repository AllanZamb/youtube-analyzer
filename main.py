from yt_stats import YTstats

API_KEY = 'AIzaSyBR6LZViWi0dBCNfxt3TRbn-nxVuix0c_w'
channel_id = "UCvASv4hWCpTTbeEU67jkEzA"

yt = YTstats(API_KEY, channel_id)
yt.extract_all()
yt.dump()  # dumps to .json