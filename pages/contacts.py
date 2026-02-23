# pages\contacts.py

import sqlite3
from flask import Blueprint, flash, redirect, render_template, request, url_for
from config import DB
from utils.auth import get_user_by_uid

contacts_bp = Blueprint('contacts', __name__)


@contacts_bp.route("/contacts", methods=["GET", "POST"])
def contacts_page():

    user_uid = request.cookies.get('owner_uid')
    userdata = dict(get_user_by_uid(user_uid))

    conn = sqlite3.connect(DB['name'])
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    if not userdata:
        own_name = ""
        own_email = ""
    else:
        own_name = userdata['own_display_name']
        own_email = userdata['own_email']

    form = {
        "name": own_name,
        "email": own_email,
        "subject": "",
        "message": ""
    }

    if request.method == "POST":

        form = {
            "name": request.form.get("name", "").strip(),
            "email": request.form.get("email", "").strip(),
            "subject": request.form.get("subject", "").strip(),
            "message": request.form.get("message", "").strip(),
        }

        cursor.execute(
            "INSERT INTO contacts ( cnt_name, cnt_email, cnt_subject, cnt_message ) VALUES ( ?, ?, ?, ? )",
            (form["name"], form["email"], form["subject"], form["message"],)
        )

        conn.commit()
        conn.close()

        if cursor.rowcount == 1:
            form = {
                "name": own_name,
                "email": own_email,
                "subject": "",
                "message": ""
            }
            flash("Contato enviado com sucesso!", "success")
        else:
            flash(
                "Oooops! Não foi possível enviar o contato. Tente novamente...", "danger")

    return render_template(
        "contacts.html",
        form=form,
        page_title="Faça Contato"
    )
