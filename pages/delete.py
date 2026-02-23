# pages/delete.py

from flask import Blueprint, flash, redirect, url_for

delete_bp = Blueprint("delete", __name__)


@delete_bp.route("/delete/<int:pad_id>")
def delete_page(pad_id):

    # Redireciona para a página inicial
    flash('Pad deletado com sucesso!', 'success')
    return redirect(url_for('home.home_page'))
