import requests

from bcoding import bdecode, bencode
import logging

import torrent


def get_peers_from_tracker(torrent_data):
    tracker_url = torrent_data['announce']
    info_hash = torrent.calculate_info_hash(torrent_data=torrent_data)
    peer_id = torrent.generate_peer_id()
    port = 6881
    uploaded = 0
    downloaded = 0
    left = torrent_data['info']['length']

    params = {
        'info_hash': info_hash,
        'peer_id': peer_id,
        'port': port,
        'uploaded': uploaded,
        'downloaded': downloaded,
        'left': left,
        'event': 'started'
    }

    try:
        answer_tracker = requests.get(tracker_url, params=params, timeout=5)
        response_data = bdecode(answer_tracker.content)
        peer_list = response_data.get('peers', [])
        peers_info = []

        for peer in peer_list:
            ip = peer.get('ip')
            port = peer.get('port')
            if ip and port:
                peers_info.append({'ip': ip, 'port': port})
        
        return peers_info
        
    except Exception as e:
            logging.exception("HTTP scraping failed: %s" % e.__str__())
    


