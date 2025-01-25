from flask import Flask, render_template, request
from datetime import datetime
from fuzzy import fuzzyfikasi_stok, fuzzyfikasi_permintaan, rule_base, defuzzyfikasi, kategori_produksi
from diagram import create_fuzzy_plot, create_fuzzy_permin, create_fuzzy_output_plot

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('home.html')

@app.route('/fuzzy', methods=['GET' ,'POST'])
def fuzzy():
    if request.method == 'POST':
        jumlah_stok = request.form['stok']
        permintaan = request.form['permintaan']

        # Fuzzyfikasi
        fuzzy_stok = fuzzyfikasi_stok(int(jumlah_stok))
        fuzzy_permintaan = fuzzyfikasi_permintaan(int(permintaan))
        
        stok_grafik = create_fuzzy_plot(int(jumlah_stok), fuzzy_stok)
        permintaan_grafik = create_fuzzy_permin(int(permintaan), fuzzy_permintaan)

        # Rule Base
        rules = rule_base(fuzzy_stok, fuzzy_permintaan)

        # Defuzzyfikasi
        produksi = defuzzyfikasi(rules)
        plot_hasil = create_fuzzy_output_plot(produksi)
        
        kategori = kategori_produksi(produksi)

        return render_template('fuzzy.html', jumlah_stok = jumlah_stok,
                               permintaan = permintaan,
                               fuzzy_stok = fuzzy_stok,
                               fuzzy_permintaan = fuzzy_permintaan,
                               rules = rules,
                               produksi = produksi,
                               kategori = kategori,
                               stok_grafik = stok_grafik,
                               permintaan_grafik = permintaan_grafik,
                               plot_hasil=plot_hasil)
    else:
        return render_template('fuzzy.html', fuzzy_stok='', fuzzy_permintaan = '')
    
if __name__ == "__main__":
    app.run(debug=True)
