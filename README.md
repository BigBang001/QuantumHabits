<h2 align="center">QuantumHabits - Where Small Steps Lead to Quantum Leaps in Personal Growth</h2>

<p align="center">
  <em>Welcome to QuantumHabits, where the subtle science of habit formation meets the transformative power of quantum leaps. By harnessing AI and gamification, QuantumHabits empowers users to achieve significant personal growth through small, consistent actions.</em>
</p><br><br>

### The Name: QuantumHabits

**Fun Fact:** Ever wondered how tiny particles can lead to significant changes in the universe? Similarly, QuantumHabits applies this principle to personal development. "Quantum" represents the profound impact achievable through incremental changes, while "Habits" underscores the focus on nurturing positive routines.

### Purpose

QuantumHabits aims to:

1. **Facilitate Personal Growth:** Guide users in setting and achieving meaningful goals through daily habit tracking and insightful analytics.
   
2. **Harness AI for Personalization:** Utilize decision tree classifiers to provide tailored recommendations, adapting to each user's unique habits and preferences.

3. **Gamify Habit Building:** Introduce badges and rewards to motivate users, making the journey towards personal improvement engaging and enjoyable.

4. **Visualize Progress:** Offer intuitive charts and graphs to visualize habit adherence and progress over time, fostering accountability and motivation.

### Key Features

- **Goal Setting and Tracking:** Enable users to define and monitor goals, receiving timely reminders to stay focused and motivated.
  
- **Personalized Recommendations:** Employ AI algorithms to analyze habits and offer personalized suggestions for continuous improvement.
  
- **Achievements and Rewards:** Gamify the experience with badges and rewards, celebrating milestones and consistent progress.
  
- **Secure Authentication:** Ensure user data security and privacy through robust authentication measures.

### Technical Details

- **Backend:** Developed using Flask (Python) and SQLite for efficient data management and API integration.
  
- **Frontend:** Built with HTML, CSS, and JavaScript for a responsive and intuitive user interface.
  
- **AI Integration:** Decision tree classifiers trained on user data to enhance habit recommendations and personalized insights.


### How to Use

1. **Clone the Repository:**
   
   ```
   git clone https://github.com/yourusername/quantumhabits.git
   ```

2. **Navigate to the Project Directory:**
   
   ```
   cd quantumhabits
   ```

3. **Backend Setup:**

   - Set up a virtual environment and activate it:
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows use `venv\Scripts\activate`
     ```
   - Install Python dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Initialize the SQLite database:
     ```bash
     flask db init
     flask db migrate -m "Initial migration"
     flask db upgrade
     ```
   - Start the Flask server:
     ```bash
     flask run
     ```

4. **Frontend Setup:**

   - Navigate to the frontend directory:
     ```bash
     cd quantumhabits-frontend
     ```
   - Open `index.html` in your preferred web browser to access the intuitive and interactive frontend interface.

5. **Training AI Models:**

   - Train decision tree classifiers on relevant datasets to enhance AI-driven habit recommendations.
   - Update the model integration in `app.py` to ensure personalized insights and suggestions for users.

### Contributing

QuantumHabits welcomes contributions to further enhance its functionality and user experience. To contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/new-feature`.
3. Implement changes and improvements.
4. Push to your branch: `git push origin feature/new-feature`.
5. Create a pull request.
