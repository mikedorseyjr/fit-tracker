#!/usr/bin/env python
# coding: utf-8

from google.appengine.ext import db

# These are the base classes that make up the fitness tracker program.  These models will represent
# Sets, Exercises, and Workouts.  The will be used to store the contents of what a person is doing.

# The Set class represents a set of an exercise.  
class Set(db.Model):
    set_id = db.StringProperty(required=True) # set_id is a random identifier to recognize it
    set_owner = db.StringProperty(required=True) # set owner is the particular person, or identifier of the person performing the set
    workout_id = db.StringProperty()    # workout id represents an identifier for a particular workout.  It links the set to a workout.  However, if 
                                        # no workout identifier is provided, the system will fetch the most recent workout of the set owner and 
                                        # populate itself with that.
    actual = db.BooleanProperty(required=True)  # Determines whether this is an actual set where work was performed or if its a set prescribed by the 
                                                # workout creator
    work_set = db.BooleanProperty(required=True)    # Only valid if the set is an actual set.  If so, this determines whether this is a real work set OR
                                                    # a warm-up/feel set.
    exercise = db.StringProperty(required=True)     # This tells use the exercise the set is for.
    weight = db.IntegerProperty()                   # Records the resistance used for the exercise.  Only applies if set is an actual set
    reps = db.IntegerProperty(required=True)        # Records the number of reps used for the set
    date = db.DateTimeProperty()                    # This records the time the set was recorded.  If the sets of the workout are part of a created one to 
                                                    # be assigned, the dates will be 01-01-01 00:00:01 - 01-01-01 00:00:59 unless of course, your workouts have
                                                    # more than 59 sets.
    seconds_since_last_set = db.IntegerProperty()   # Internally calculated time between sets unless user overrides
 
# The activity class represents an activity.  This could be cardio, yoga, prowler pushing, or what have you.
class Activity(db.Model):
    activity_id = db.StringProperty(required=True)     # identifier of the activity
    name = db.StringProperty(required=True)            # Activity name
    workout_id = db.StringProperty(required=True)      # Links the activity to a workout
    activity_owner = db.StringProperty(required=True)  # Indicates the owner of the activity
    date = db.DateTimeProperty(required=True)          # Time the activity lasted
    duration = db.IntegerProperty(required=True)       # Length in minutes of the activity
    intensity = db.StringProperty()                    # represents how the activity felt
    description = db.StringProperty()                   # represent a description of the activity
     
        
# The workout represents a workout.  Workouts can either be created for someone to use and the blanks are filled in 
class Workout(db.Model):
    workout_id = db.StringProperty(required=True)       # An identifier for the workout
    name = db.StringProperty()                          # A name for the workout
    workout_owner = db.StringProperty(required=True)    # The creator of the workout or the person doing it.
    description = db.StringProperty()                   # A description of the workout
    date_created = db.DateTimeProperty()                # Date of the workout's creation
    date_updated = db.DateTimeProperty()                # Date the workout was last updated
    
# The user represents a person using the application to store his or her training in.
class User(db.Model):
    user_id = db.StringProperty(required=True)          # represents identifier from source used to authenticate user and authorize user to service
    name = db.StringProperty(required=True)             # Basic name of user
    assigned_workouts = db.StringListProperty()         # Represents a list of all of the workouts a user may be assigned
    current_assigned_workouts = db.StringProperty()     # Represents the currently assigned workout of the users
    current_workout = db.StringProperty()               # Represents the workout the user is currently doing.
    trainer = db.BooleanProperty()                      # Determines whether the user is allowed to assign workouts to other users other than self.
    trained = db.BooleanProperty()                      # Determines whether the user is trained or not
    trainer_id = db.StringProperty()                    # Determines the personal trainer of the logged in user.
    
# The exercise class represents an exercise.  These aren't linked to sets but can be, once populated by a user.
class Exercise(db.Model):
    exercise_id = db.StringProperty(required=True)
    name = db.StringProperty(required=True)
    classification = db.StringProperty()
    major_body_part = db.StringProperty()
    minor_body_parts = db.StringListProperty()
    instructions = db.StringProperty()
    video_instruction_url = db.StringProperty()
    