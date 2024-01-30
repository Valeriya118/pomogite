from flask import Blueprint, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Email, EqualTo

views = Blueprint('views', __name__)

class PurchaseForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    last_name = StringField('Фамилия', validators=[DataRequired()])
    phone = StringField('Телефон', validators=[DataRequired()])
    address = StringField('Адрес', validators=[DataRequired()])
    card_number = StringField('Номер карты', validators=[DataRequired()])
    expiration_date = StringField('Срок действия', validators=[DataRequired()])
    cvv = StringField('CVV', validators=[DataRequired()])
    submit = SubmitField('Подтвердить')

@views.route('/')
@views.route('/page1.html')
def home():
    form = PurchaseForm()
    if form.validate_on_submit():
        pass
    return render_template("page1.html", form=form)



@views.route('/page15.html')
def page15():
    form = PurchaseForm()
    if form.validate_on_submit():
        pass
    return render_template("page15.html", form=form)

@views.route('/page2.html')
def page2():
    form = PurchaseForm()
    if form.validate_on_submit():
        pass
    return render_template("page2.html", form=form)

@views.route('/page3.html')
def page3():
    form = PurchaseForm()
    if form.validate_on_submit():
        pass
    return render_template("page3.html", form=form)

@views.route('/page4.html')
def page4():
    form = PurchaseForm()
    if form.validate_on_submit():
        pass
    return render_template("page4.html", form=form)

@views.route('/page5.html')
def page5():
    form = PurchaseForm()
    if form.validate_on_submit():
        pass
    return render_template("page5.html", form=form)

@views.route('/page6.html')
def page6():
    form = PurchaseForm()
    if form.validate_on_submit():
        pass
    return render_template("page6.html", form=form)

@views.route('/page7.html')
def page7():
    form = PurchaseForm()
    if form.validate_on_submit():
        pass
    return render_template("page7.html", form=form)

@views.route('/page8.html')
def page8():
    form = PurchaseForm()
    if form.validate_on_submit():
        pass
    return render_template("page8.html", form=form)

@views.route('/page9.html')
def page9():
    form = PurchaseForm()
    if form.validate_on_submit():
        pass
    return render_template("page9.html", form=form)

@views.route('/page10.html')
def page10():
    form = PurchaseForm()
    if form.validate_on_submit():
        pass
    return render_template("page10.html", form=form)

@views.route('/page11.html')
def page11():
    form = PurchaseForm()
    if form.validate_on_submit():
        pass
    return render_template("page11.html", form=form)

@views.route('/page12.html')
def page12():
    form = PurchaseForm()
    if form.validate_on_submit():
        pass
    return render_template("page12.html", form=form)

@views.route('/page13.html')
def page13():
    form = PurchaseForm()
    if form.validate_on_submit():
        pass
    return render_template("page13.html", form=form)

@views.route('/page14.html')
def page14():
    form = PurchaseForm()
    if form.validate_on_submit():
        pass
    return render_template("page14.html", form=form)

@views.route('/page16.html')
def page16():
    form = PurchaseForm()
    if form.validate_on_submit():
        pass
    return render_template("page16.html", form=form)

@views.route('/page17.html', methods=['GET', 'POST'])
def page17():
    form = PurchaseForm()
    if form.validate_on_submit():
        flash('Form submitted successfully!', 'success')
        return redirect(url_for('home'))  # Redirect to the home page after submission

    return render_template('page17.html', form=form)

@views.route('/page18.html')
def page18():
    form = MyForm()
    if form.validate_on_submit():
        pass
    return render_template("page18.html", form=form)


