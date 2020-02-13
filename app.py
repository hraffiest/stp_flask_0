from flask import Flask, render_template, request  # сперва подключим модуль
import data  # sample date from file
app = Flask(__name__) 	# объявим экземпляр фласка


@app.route('/')
def main():
    return render_template('index.html',
                           title='Stepik Travel',
                           departures=data.departures,
                           tour=data.tours)


@app.route('/departure/<departure>')
def show_daparture(departure):
    from_town = data.departures[departure]
    # this will be a dict with tours for this departure
    tours_dict = dict()
    for key, value in data.tours.items():
        if value['departure'] == departure:
            tours_dict[key] = value
    # count of tours for this departure
    print(tours_dict.values())
    counter = len(tours_dict)
    if counter == 1:
        counter = 'Найден 1 тур'
    elif counter == 11:
        counter = 'Найдено {} туров'.format(counter)
    elif 4 >= counter % 10 >= 1:
        counter = 'Найдено {} тура'.format(counter)
    else:
        counter = 'Найдено {} туров'.format(counter)
    return render_template('departure.html',
                           departure=departure,
                           departures=data.departures,
                           from_town=from_town,
                           tours=tours_dict,
                           counter=counter)



@app.route('/tour/<int:id_tour>')
def show_tour(id_tour):
    tour = data.tours[id_tour]
    from_town = data.departures[tour["departure"]]
    # correct typo for 'ночь/и/ей'
    nights = tour['nights']
    if nights == 1:
        nights = '1 ночь'
    elif nights == 11:
        nights = '{} ночей'.format(nights)
    elif 4 >= nights % 10 >= 1:
        nights = '{} ночи'.format(nights)
    else:
        nights = '{} ночей'.format(nights)

    return render_template('tour.html',
                           title=tour['title'],
                           tour=tour,
                           from_town=from_town,
                           nights=nights,
                           departures=data.departures)


if __name__ == '__main__':
    app.run(port=4999, debug=True)
