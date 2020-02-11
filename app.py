from flask import Flask, render_template 	# сперва подключим модуль
import data
app = Flask(__name__) 	# объявим экземпляр фласка


@app.route('/')
def main():
    return render_template('index.html', title='Stepik Travel')


@app.route('/departure/<departure>')
def show_daparture(departure):
    return render_template('departure.html', title=departure, departure=departure)


@app.route('/tour/<id_tour>')
def show_tour(id_tour):
    return render_template('tour.html', title=id_tour, tour=id_tour)


if __name__ == '__main__':
    app.run(port=4999, debug=True)
