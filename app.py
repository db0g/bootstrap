from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def col_raw_border():
    return render_template('pages/col_row_border.html')

@app.route('/width_height')
def width_height():
    return render_template('pages/width_height.html')

@app.route('/alert_modal')
def alert_modal():
    return render_template('pages/alert_modal.html')

if (__name__) == '__main__':
    app.run(debug=True)

