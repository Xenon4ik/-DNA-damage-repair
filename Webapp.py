from flask import Flask, render_template, request
from build_plot import Plot

app = Flask(__name__) 


@app.route('/') 
def entry_page() -> 'html': 
    return render_template('main.html') 

@app.route('/plot', methods=['GET', 'POST'])
def plot_page() -> 'html': 
    dosetxt = request.form['dose']
    dose = int(dosetxt) 
    Plot(dose)
    return render_template('plot.html', dose=dose)

app.run()