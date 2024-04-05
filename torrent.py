import hashlib
import time
from bcoding import bdecode, bencode

def read_torrent_file(torrent_file_path):
    with open(torrent_file_path, 'rb') as f:
        torrent_data =bdecode(f.read())

    return torrent_data

def generate_peer_id():
    seed = str(time.time())
    return hashlib.sha1(seed.encode('utf-8')).digest()

def calculate_info_hash(torrent_data):
    # Chuyển dữ liệu torrent thành chuỗi byte
    torrent_bytes = bencode(torrent_data['info'])
    # Tính toán băm SHA-1
    info_hash = hashlib.sha1(torrent_bytes).digest()
    return info_hash