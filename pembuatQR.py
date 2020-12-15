def create_db(info: dict) -> str:
    ''' Create db if it is not already created '''
    from tinydb import TinyDB, Query
    import os
    if os.stat('db') == 0:
        db = TinyDB('db/links.json')
        db.insert(info)
        return f'\nBerjaya mencipta DB\n'
    else:
        return f'\nDB sudah ada\n'

def create_qr(info: dict) -> str:
    ''' Create and save QR code from information given'''
    import qrcode
    img = qrcode.make(info['Link']) # menghasilkan qr code
    nama_hasilan = '_'.join(info['Link'].split('.')) + '.png' # nama hasilan
    img.save('created_qr_imgs'+'/'+nama_hasilan)
    return f'\nQR imej \'{nama_hasilan}\' disimpan\n'

def insert_db(info: dict) -> str:
    ''' Query and insert object if it is not in db '''
    from tinydb import TinyDB, Query
    db = TinyDB('db/links.json')
    Jalinan = Query()
    if info['Link'] != db.search(Jalinan.Link == info['Link']):
        return f'\n\'{info["Link"]}\' sudah berada didalam DB\n'
    db.insert(info)
    return f'\nBerjaya menyimpan maklumat \'{info["Link"]}\'\n'

def read_qr_image(filename: str) -> str:
    import cv2
    img = cv2.imread('created_qr_imgs'+'/'+filename)
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(img)
    return data

if __name__ == "__main__":
    # contoh data
    data = {'Link':'thepythoncode.com', 'Category': 'Software', 'Description':'Cool python tutorial website'}
    print(create_db(data))
    print(create_qr(data))
    print(insert_db(data))
    print(read_qr_image('_'.join(data['Link'].split('.'))+'.png'))