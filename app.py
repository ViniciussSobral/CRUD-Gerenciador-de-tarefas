from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3 as sql

app=Flask(__name__)
app.secret_key="admin"

@app.route("/")
@app.route("/index")

def index():
    con = sql.connect("form_db.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("SELECT * FROM tarefas")
    data=cur.fetchall()
    return render_template ("index.html", datas=data)


@app.route("/add_tarefa", methods=["POST","GET"])
def add_tarefa():
    if request.method== "POST":
        titulo=request.form["titulo"]
        descricao=request.form["descricao"]
        data=request.form["data"]
        status=request.form["status"]
        con=sql.connect("form_db.db")
        cur=con.cursor()
        cur.execute("insert into tarefas(TITULO,DESCRIÇÃO,DATA,STATUS) values (?,?,?,?)",(titulo,descricao,data,status))
        con.commit()
        flash("Dados cadastrados","sucess")
        return redirect(url_for("index"))
    return render_template("add_tarefa.html")

@app.route("/edit_tarefa/<string:id>",methods=["POST","GET"])
def edit_tarefa(id):
    if request.method=="POST":
        titulo=request.form["titulo"]
        descricao=request.form["descricao"]
        data=request.form["data"]
        status=request.form["status"]  
        con=sql.connect("form_db.db")
        cur=con.cursor()
        cur.execute("update tarefas set TITULO=?,DESCRIÇÃO=?,DATA=?,STATUS=? where ID=?",(titulo,descricao,data,status,id))
        con.commit()
        flash("Dados atualizados","sucess")
        return redirect(url_for("index"))
    con=sql.connect("form_db.db")
    con.row_factory=sql.Row
    cur= con.cursor()
    cur.execute("SELECT * FROM tarefas where ID =?",(id,))
    data=cur.fetchone()
    return render_template("edit_tarefa.html",datas=data)

@app.route("/delete_tarefa/<string:id>",methods=["GET"])    
def delete_tarefa(id):
    con=sql.connect("form_db.db")
    cur=con.cursor()
    cur.execute("delete from tarefas where ID=? ",(id,))
    con.commit()
    flash("Dados deletados","warning")
    return redirect(url_for("index"))
if __name__=='__main__':
    
    app.run(debug=True)



