def proses_link(link) -> str:
    ''' Proses nama untuk QR imej'''
    to_change = ['.', '/', ':']
    return ''.join('_' if c in to_change else c for c in link) + '.png'

def cipta_db(info: dict) -> str:
    ''' Cipta db sekiranya belum ada '''
    from tinydb import TinyDB, Query
    import os
    if os.stat('db') == 0:
        db = TinyDB('db/links.json')
        db.insert(info)
        return f'\nBerjaya mencipta DB\n'
    else:
        return f'\nDB sudah ada\n'

def cipta_imej_qr(info: dict) -> str:
    ''' Cipta dan simpan QR imej berdasar info diberi'''
    import qrcode
    img = qrcode.make(info['Link']) # menghasilkan qr code
    nama_hasilan = proses_link(info['Link']) # nama hasilan
    img.save('created_qr_imgs'+'/'+nama_hasilan)
    return f'\nQR imej \'{nama_hasilan}\' disimpan\n'

def insert_to_db(info: dict) -> str:
    ''' Query and insert object if it is not in db '''
    from tinydb import TinyDB, Query
    db = TinyDB('db/links.json')
    Jalinan = Query()
    if db.search(Jalinan.Link == info['Link']):
        return f'\n\'{info["Link"]}\' sudah berada didalam DB\n'
    db.insert(info)
    return f'\nMaklumat \'{info["Link"]}\' disimpan\n'

def baca_imej_qr(filename: str) -> str:
    ''' Baca info daripada QR imej '''
    import cv2
    img = cv2.imread('created_qr_imgs'+'/'+filename)
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(img)
    return data

# if __name__ == "__main__":
#     # contoh data
#     data = {'Link':'thepythoncode.com', 'Kategori': 'Software', 'Deskripsi':'Cool python tutorial website'}
#     print(create_db(data))
#     print(create_qr(data))
#     print(insert_db(data))
#     print(read_qr_image('_'.join(data['Link'].split('.'))+'.png'))