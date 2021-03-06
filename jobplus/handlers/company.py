from flask import Blueprint, render_template, flash, redirect, url_for, request, current_app
from flask_login import login_required, current_user

from jobplus.forms import CompanyProfileForm
from jobplus.models import User, Company

company = Blueprint('company', __name__, url_prefix='/company')


@company.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if not current_user.is_company:
        flash('您不是企业用户，无法登陆', 'warning')
        return redirect(url_for('font.admin_base.html'))
    form = CompanyProfileForm(obj=current_user.company_info)
    form.name.data = current_user.name
    form.email.data = current_user.email
    if form.validate_on_submit():
        form.updated_profile(current_user)
        flash('企业信息更新成功', 'success')
        return redirect(url_for('front.admin_base.html'))
    return render_template('company/profile.html', form=form)


@company.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    pagination = Company.query.order_by(Company.id).paginate(
        page=page,
        per_page=current_app.config['COMPANY_PER_PAGE'],
        error_out=False
    )
    return render_template('company/index.html', pagination=pagination)


@company.route('/<int:company_id>')
def detail(company_id):
    return 'company detail: {}'.format(company_id)
