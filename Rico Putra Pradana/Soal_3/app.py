from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/soal/pretest/')
def pretest():
    return jsonify({'nama':'mukidi',
                    'email':'mukidi@ai.astra.co.id',
                    'usia':'28 Tahun, 3 Bulan'})

if __name__ == '__main__':
    app.run(host='localhost', port=5000)