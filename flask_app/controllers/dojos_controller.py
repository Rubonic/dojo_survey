from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojo import Dojo


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():

    print('PPPPPPPPPPPPPPPPPPPPPP')
    if not Dojo.validate_dojo(request.form):
        print('DDDDDDDDDDDDDDDDDDDDDDD')
        return redirect('/')

    data = {
        'name' : request.form['name'],
        'location' : request.form['location'],
        'language' : request.form['language'],
        'comment' : request.form['comment'],
        'created_at' : 'NOW()',
        'updated_at' : 'NOW()'
    }


    ninja = Dojo.create(data)


    return redirect(f'/result/{ninja}')


@app.route('/result/<int:id>')
def result(id):
    data = {
        'id' : id
    }
    ninja = Dojo.get_ninja(data)
    print(f'+++++++++++++++++++++++++++++++++++++++dojo {ninja}')

    return render_template('result.html', ninja = ninja)