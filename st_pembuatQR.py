import streamlit as st
from PembuatQR import cipta_imej_qr, insert_to_db, baca_imej_qr

st.title('Bookmarking QR way')

colCiptaQR, colImej = st.beta_columns(2)

with colCiptaQR:
    st.header('Ruangan untuk cipta QR bookmark')
    the_link = st.text_input('Masukkan link:')
    the_kategori = st.text_input('Masukkan kategori link:')
    the_deskripsi = st.text_area('Masukkan deskripsi link:')
    info = {'Link':the_link, 'Kategori':the_kategori, 'Deskripsi':the_deskripsi}
    if the_link and the_kategori and the_deskripsi:
        def cipta_tmplate(info):
            st.write(cipta_imej_qr(info))
            st.write(insert_to_db(info))
            with colImej:
                st.header('QR bookmark dicipta')
                nama_hasilan = '_'.join(info['Link'].split('.')) + '.png'
                st.image('created_qr_imgs/'+nama_hasilan, caption=f'QR bookmark untuk {the_link}')
        mencipta = st.button('Cipta')
        if mencipta:
            cipta_tmplate(info)
    else:
        st.write('Masukkan informasi untuk mencipta QR bookmark')
        with colImej:
            st.header('Tiada imej dicipta')
