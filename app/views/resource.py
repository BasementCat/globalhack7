from flask import Blueprint, url_for, redirect, render_template, flash, g
from flask_login import login_required

from app.models.common import Resource
from flask import Blueprint, render_template, g, current_app, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user
from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, FileField, HiddenField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from flask_babel import gettext

from wtforms.widgets import TextArea

from app.main import db
from app.models.common import User, Category, PRIMARY_ROLE, USER_RESOURCE_TYPES
from app.lib.constants import *


app = Blueprint('resource', __name__)


class ResourceForm(Form):
    name = StringField(LABELS['name'])
    category = QuerySelectField(LABELS['category'], query_factory=lambda: Category.query.filter(Category.parent != None), get_label='name')
    quantity_available = StringField(LABELS['quantity'], default=1)
    quantity_needed = StringField(LABELS['quantity'], default=1)
    description = StringField(LABELS['description'], widget=TextArea())
    type = HiddenField(LABELS['type'])
    picture = FileField(LABELS["picture"], description=HELP["picture"])
    submit = SubmitField(LABELS['submit_create'])


@app.route('/<id>', methods=['GET', 'POST'])
@login_required
def detail_view(id=None):
    if id == 'new':
        return 'Not Implemented Yet'
    resource = Resource.query.get(id)
    if not resource:
        flash(gettext('No resource found.'), 'warning')
        return redirect(url_for('index.index', lang_code=g.lang_code))

    show_request_btn = True
    resource_requested = False
    if current_user.is_authenticated():
        if current_user.id == resource.user_id:
            show_request_btn = False
            resource_requested = resource.requested

    return render_template('resource_detail.jinja.html', resource=resource, show_request_btn=show_request_btn, resource_requested=resource_requested)


@app.route('/create', methods=['GET', 'POST'])
def resource_create():
    if not current_user.is_authenticated():
        flash(ERROR_MESSAGES['not_logged_in'], "warning")
        return redirect(url_for('index.index'))

    default_data = {}
    if request.args.get('cat_id'):
        default_data['category'] = Category.query.get(int(request.args['cat_id']))
    if request.args.get('name'):
        default_data['name'] = request.args['name']
    if request.args.get('type'):
        default_data['type'] = request.args['type']

    form = ResourceForm(data=default_data)

    if request.args.get('type') == 'NEED':
        del form.quantity_available
    else:
        del form.quantity_needed

    if form.validate_on_submit():
        new_resource = Resource(
            name=form.name.data,
            category=form.category.data,
            description=form.description.data,
            fulfilled=False,
            quantity_needed=form.quantity_needed.data if form.type.data == 'NEED' else 0,
            quantity_available=form.quantity_available.data if form.type.data == 'HAVE' else 0,
            type=form.type.data,
            user_id=current_user.id
        )
        db.session.add(new_resource)
        db.session.commit()
        new_resource.picture = form.picture.data
        db.session.add(new_resource)
        db.session.commit()
        flash(GENERAL_MESSAGES['resource_save_success'], "success")
        return redirect(url_for('index.index'))
    return render_template('resource_editor.jinja.html', name=request.args.get('name'), form=form)


@app.route('/request/', methods=['GET', 'POST'])
def resource_request():
    resource = Resource.query.get(request.args.get('resource_id'))
    if resource:
        resource.requested = 1
        db.session.add(resource)
        db.session.commit()
        flash(GENERAL_MESSAGES['resource_requested'], "success")
    else:
        flash(GENERAL_MESSAGES['resource_requested'], "error")
    return redirect(url_for('index.index'))


@app.route('/request_fulfilled/', methods=['GET', 'POST'])
def resource_request_fulfilled():
    resource = Resource.query.get(request.args.get('resource_id'))
    if resource:
        resource.fulfilled = 1
        db.session.add(resource)
        db.session.commit()
        flash(GENERAL_MESSAGES['resource_fulfilled'], "success")
    else:
        flash(GENERAL_MESSAGES['resource_not_requested'], "error")
    return redirect(url_for('index.index'))
