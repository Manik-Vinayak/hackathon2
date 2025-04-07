from flask import Blueprint, request, redirect, render_template, url_for
import sqlite3
import os
from werkzeug.utils import secure_filename

item_bp = Blueprint('items', __name__)

DB_PATH = 'database.db'

# Ensure database and table exist
def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_name TEXT,
                description TEXT,
                status TEXT,
                image TEXT,
                urn TEXT
            )
        ''')
init_db()

@item_bp.route('/submit', methods=['POST'])
def submit_item():
    name = request.form['student_name']
    description = request.form['description']
    status = request.form['status']
    urn = request.form['urn']

    image_file = request.files['image']
    image_filename = None
    if image_file and image_file.filename != '':
        image_filename = secure_filename(image_file.filename)
        image_path = os.path.join('static/uploads', image_filename)
        image_file.save(image_path)

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('INSERT INTO items (student_name, description, status, image, urn) VALUES (?, ?, ?, ?, ?)',
                     (name, description, status, image_filename, urn))

    return redirect(url_for('items.show_items'))

@item_bp.route('/items')
def show_items():
    with sqlite3.connect(DB_PATH) as conn:
        items = conn.execute('SELECT * FROM items').fetchall()
    return render_template('items.html', items=items)

@item_bp.route('/claim', methods=['POST'])
def claim_item():
    # For now, just simulate claim action
    item_id = request.form['item_id']
    claimant_name = request.form['claimant_name']
    claimant_urn = request.form['claimant_urn']
    print(f"Claim received for Item ID {item_id} by {claimant_name} ({claimant_urn})")
    return redirect(url_for('items.show_items'))
