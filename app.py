from flask import Flask, render_template 	# сперва подключим модуль
import data  # sample date from file
app = Flask(__name__) 	# объявим экземпляр фласка


@app.route('/')
def main():
    return render_template('index.html', title='Stepik Travel')


@app.route('/departure/<departure>')
def show_daparture(departure):
    return render_template('departure.html', title=departure, departure=departure)


@app.route('/tour/<id_tour>')
def show_tour(id_tour):
    tour = None
    for i in data.tours:
        # compare url with title from data.py
        if data.tours[i]['title'].lower() == ' '.join(id_tour.split('-')).lower():
            tour = data.tours[i]
    # why here i see the problem "Local variable 'tour' might be referenced before assignment" ???
    if tour is not None:
        return render_template('tour.html', title=data.title, tour=tour)
    else:
        return '404'


if __name__ == '__main__':
    app.run(port=4999, debug=True)
