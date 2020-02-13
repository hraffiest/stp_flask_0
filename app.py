from flask import Flask, render_template 	# сперва подключим модуль
import data  # sample date from file
app = Flask(__name__) 	# объявим экземпляр фласка


@app.route('/')
def main():
    return render_template('index.html', title='Stepik Travel', departures=data.departures, tour=data.tours)


@app.route('/departure/<departure>')
def show_daparture(departure):
    return render_template('departure.html', title=departure, departure=departure)


@app.route('/tour/<int:id_tour>')
def show_tour(id_tour):
    tour = data.tours[id_tour]
    from_town = data.departures[tour["departure"]]
    # correct typo for 'ночь/и/ей'
    nights = tour['nights']
    if nights == 1:
        nights = '1 ночь'
    elif 4 >= nights % 10 >= 1:
        nights = '{} ночи'.format(nights)
    else:
        nights = '{} ночей'.format(nights)

    return render_template('tour.html', title=tour['title'], tour=tour, departures=from_town, nights=nights)


if __name__ == '__main__':
    app.run(port=4999, debug=True)
