from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db
from app.models import User, Achievement, UserAchievement, Habit
from app.forms import RegistrationForm, LoginForm, AddHabitForm, EditProfileForm
import requests
from werkzeug.urls import url_parse

# User loader function required by flask_login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Dashboard route to display user's habits and achievements
@app.route('/dashboard')
@login_required
def dashboard():
    habits = current_user.habits.all()
    achievements = Achievement.query.all()
    return render_template('dashboard.html', title='Dashboard', habits=habits, achievements=achievements)

# Route to add a new habit for the current user
@app.route('/add_habit', methods=['GET', 'POST'])
@login_required
def add_habit():
    form = AddHabitForm()
    if form.validate_on_submit():
        habit = Habit(name=form.name.data, description=form.description.data, user=current_user)
        db.session.add(habit)
        db.session.commit()
        flash('Your habit has been added!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('add_habit.html', title='Add Habit', form=form)

# Route to edit a habit for the current user
@app.route('/edit_habit/<int:habit_id>', methods=['GET', 'POST'])
@login_required
def edit_habit(habit_id):
    habit = Habit.query.get_or_404(habit_id)
    if habit.user != current_user:
        flash('You are not authorized to edit this habit.', 'danger')
        return redirect(url_for('dashboard'))
    form = AddHabitForm()
    if form.validate_on_submit():
        habit.name = form.name.data
        habit.description = form.description.data
        db.session.commit()
        flash('Your habit has been updated!', 'success')
        return redirect(url_for('dashboard'))
    elif request.method == 'GET':
        form.name.data = habit.name
        form.description.data = habit.description
    return render_template('add_habit.html', title='Edit Habit', form=form)

# Route to delete a habit for the current user
@app.route('/delete_habit/<int:habit_id>', methods=['POST'])
@login_required
def delete_habit(habit_id):
    habit = Habit.query.get_or_404(habit_id)
    if habit.user != current_user:
        flash('You are not authorized to delete this habit.', 'danger')
        return redirect(url_for('dashboard'))
    db.session.delete(habit)
    db.session.commit()
    flash('Your habit has been deleted!', 'success')
    return redirect(url_for('dashboard'))

# Route to edit user profile information
@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your profile has been updated!', 'success')
        return redirect(url_for('dashboard'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('edit_profile.html', title='Edit Profile', form=form)

# Route for handling achievements and sharing
@app.route('/share_achievement/<int:achievement_id>')
@login_required
def share_achievement(achievement_id):
    achievement = Achievement.query.get_or_404(achievement_id)
    if not achievement:
        flash('Achievement not found!', 'danger')
        return redirect(url_for('dashboard'))

    # Example of generating a shareable link
    share_link = f'http://example.com/share/{achievement_id}'

    # Example of posting to social media (Twitter in this example)
    try:
        twitter_api_endpoint = 'https://api.twitter.com/1.1/statuses/update.json'
        twitter_access_token = 'your_twitter_access_token_here'
        headers = {
            'Authorization': f'Bearer {twitter_access_token}',
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        }
        tweet_message = f'I achieved {achievement.name}! Check it out: {share_link}'
        tweet_data = {
            'status': tweet_message
        }
        response = requests.post(twitter_api_endpoint, headers=headers, data=tweet_data)
        response.raise_for_status()

        flash(f'Sharing {achievement.name} on Twitter!', 'success')
    except requests.exceptions.RequestException as e:
        flash(f'Error sharing {achievement.name} on Twitter: {str(e)}', 'danger')

    return redirect(url_for('dashboard'))

# Error handler for 404 errors
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

# Error handler for 500 errors
@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

# Additional routes and logic can be added as needed for your application
# Example: Implement routes for adding, editing, or deleting habits, managing user profile, etc.

