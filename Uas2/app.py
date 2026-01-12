from flask import Flask, render_template, request, redirect
from utils import *

app = Flask(__name__)

# ================= MENU UTAMA =================
@app.route("/", methods=["GET", "POST"])
def menu():
    if request.method == "POST":
        p = request.form["pilihan"]

        if p in ["2", "3", "4", "5"] and not biodata_lengkap():
            return redirect("/peringatan")

        return {
            "1": redirect("/biodata"),
            "2": redirect("/sks"),
            "3": redirect("/nilai"),
            "4": redirect("/lihat-nilai"),
            "5": redirect("/ip")
        }.get(p, redirect("/"))

    return render_template("menu.html")

# ================= BIODATA MENU =================
@app.route("/biodata", methods=["GET", "POST"])
def biodata_menu():
    if request.method == "POST":
        p = request.form["pilihan"]
        if p == "1":
            return redirect("/biodata/input")
        elif p == "2":
            return redirect("/biodata/lihat")
    return render_template("biodata_menu.html")

# ================= INPUT BIODATA =================
@app.route("/biodata/input", methods=["GET", "POST"])
def biodata_input():
    if request.method == "POST":
        biodata["nama"] = request.form["nama"]
        biodata["nim"] = request.form["nim"]
        return redirect("/biodata")
    return render_template("biodata_input.html")

# ================= LIHAT BIODATA =================
@app.route("/biodata/lihat")
def biodata_lihat():
    return render_template("biodata_lihat.html", biodata=biodata)

# ================= SKS =================
@app.route("/sks", methods=["GET", "POST"])
def sks():
    if request.method == "POST":
        sks_list.clear()
        sks_list.extend(map(int, request.form["sks"].split()))
        return redirect("/")
    return render_template("sks.html")

# ================= INPUT NILAI =================
@app.route("/nilai", methods=["GET", "POST"])
def nilai():
    if request.method == "POST":
        nilai_list.clear()
        jenis = request.form["jenis"]
        data = request.form["nilai"].split()

        if jenis == "angka":
            for n in data:
                nilai_list.append(konversi_nilai_ke_bobot(int(n)))
        else:
            for h in data:
                nilai_list.append(konversi_huruf_ke_bobot(h))

        return redirect("/")
    return render_template("nilai.html")

# ================= LIHAT NILAI =================
@app.route("/lihat-nilai")
def lihat_nilai():
    return render_template("lihat_nilai.html",
                           biodata=biodata,
                           nilai=nilai_list)

# ================= IP =================
@app.route("/ip")
def ip():
    if not sks_list or not nilai_list:
        return redirect("/")

    total = sum(s * n for s, n in zip(sks_list, nilai_list))
    ipk = round(total / sum(sks_list), 2)

    return render_template("ip.html",
                           biodata=biodata,
                           ip=ipk)

# ================= PERINGATAN =================
@app.route("/peringatan")
def peringatan():
    return render_template("peringatan.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)