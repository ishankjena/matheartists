import random
import math
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, url_for
from samila import GenerativeImage, Projection
from jinja2 import Template

# mathematical functions generate art
# projections: RECTILINEAR (default), POLAR, AITOFF, HAMMER, LAMBERT, MOLLWEIDE
# VALID_COLORS list stores supported colors
# color, bgcolor: rgb, rgba, color_name

def generate_art(func1, func2, p, color, bg_color):
    f1 = lambda x,y: eval(func1)
    f2 = lambda x,y: eval(func2)
    projection = eval("Projection."+p.upper())
    g = GenerativeImage(f1,f2)
    g.generate()
    g.plot(color=color, bgcolor=bg_color, projection=projection)
    g.seed
    plt.savefig("static/newimage.png")


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        func1 = request.form.get("func1")
        func2 = request.form.get("func2")
        proj = request.form.get("proj")
        clr = request.form.get("color")
        bgclr = request.form.get("bgcolor")
        print(func1)
        print(func2)
        print(proj)
        print(clr)
        print(bgclr)
        generate_art(func1, func2, proj, clr, bgclr)
        return render_template("index.html", image_name="newimage.png")
        
    return render_template("index.html", image_name="test.png")

if __name__ == '__main__':
    app.run(debug=True)