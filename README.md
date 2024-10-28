# Vital Hustle

Vital Hustle is a health and wellness tracking application designed to monitor well-being and healthy habits. By tracking daily patterns, users can make informed health decisions and identify trends over time.

## Project Goals

The primary objective of Vital Hustle is to enable users to monitor their mood, daily activities, sleep patterns, and other habits through a user-friendly interface. This allows for a personalized approach to health tracking, where users can log and review their habits to identify patterns that may impact their wellness.

## Key Features

### Models for Tracking
Vital Hustle includes several customizable tracking modules:
- **Mood** - Rate mood on a 1-10 scale.
- **Day** - Aggregate data from various models for a daily overview.
- **Emotions** - Multiple selectable emotions.
- **Sleep** - Track hours slept.
- **Notes** - Add text notes for additional context.
- **Alcohol, Coffee, Cigarettes, Activity** - Log daily amounts with predefined units.

### Core Modules
1. **authCustom** - Handles user registration, login, and password management.
2. **cald (Calendar)** - Displays entries from the "Day" model, with pagination, day editing, deletion, and data retrieval for specific date ranges.
3. **wellnessTracker** - Main page for entering data in the mood and habit models.
4. **Statistics** - Shows visual statistics on mood trends.

### Sidebar Navigation
A sliding sidebar provides easy access to:
- **Home** - Main form for entering data for the current day.
- **Calendar** - Access all saved calendar entries.
- **Statistics** - Graphical representation of mood frequencies.
- **User Panel** - Change password or log out.

### User Interface Elements
- **Home View** - Includes:
  - **Slider Bars** - Color-coded based on value.
  - **Multi-select Options** - Choose multiple emotions.
  - **Text Field** - Record notes not covered by the form fields.

- **Calendar View** - Displays data entries as cards with options to edit or delete. Each card lifts when hovered over for a polished visual effect.

### Additional Functionalities
1. **Form Controls** - Includes four additional forms accessible from the sidebar for:
   - **Data Retrieval** - Download entries within a date range in `.xlsx` format.
   - **Password Change** - Modify the logged-in user’s password.
   - **Day Editing** - Edit saved data directly.
   - **Day Addition** - Log missed entries by selecting a past date.

2. **Pagination** - In the Calendar view, only 12 entries display per page, with intuitive navigation to move forward, backward, or to the start/end.

3. **Icons and Button Styling** - Button functions are visually guided with icons, enlarging slightly on hover for enhanced usability.

4. **Mood Frequency Chart** - Dynamically updated to reflect mood tracking data, including new entries, edits, and deletions. This chart gives a clear view of emotional trends over time.

5. **Pop-Up Notifications** - Form submissions and actions (e.g., deletion) trigger notifications, which auto-dismiss after a few seconds or require confirmation for deletions.

