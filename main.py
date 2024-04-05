import sys
import tracker
import torrent

def main():
    filepath = sys.argv[1]
    torrent_data = torrent.read_torrent_file(filepath)
    peers = tracker.get_peers_from_tracker(torrent_data)    

    
    print(peers)
    print(torrent_data["announce"])


main()


