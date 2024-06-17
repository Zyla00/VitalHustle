from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField


class Mood(models.Model):
    SCALE_CHOICES = [(i, str(i)) for i in range(0, 11)]

    EMOTION_CHOICES = (
        ('happy', 'Happy'),
        ('sad', 'Sad'),
        ('angry', 'Angry'),
        ('excited', 'Excited'),
        ('nervous', 'Nervous'),
        ('scared', 'Scared'),
        ('relaxed', 'Relaxed'),
        ('bored', 'Bored'),
        ('content', 'Content'),
        ('curious', 'Curious'),
        ('anxious', 'Anxious'),
        ('confused', 'Confused'),
        ('surprised', 'Surprised'),
        ('grateful', 'Grateful'),
        ('frustrated', 'Frustrated'),
        ('jealous', 'Jealous'),
        ('lonely', 'Lonely'),
        ('proud', 'Proud'),
        ('ashamed', 'Ashamed'),
        ('guilty', 'Guilty'),
        ('embarrassed', 'Embarrassed'),
        ('disappointed', 'Disappointed'),
        ('inspired', 'Inspired'),
        ('amused', 'Amused'),
        ('sympathetic', 'Sympathetic'),
        ('thoughtful', 'Thoughtful'),
        ('energetic', 'Energetic'),
        ('overwhelmed', 'Overwhelmed'),
        ('hopeful', 'Hopeful'),
    )

    scale = models.IntegerField(choices=SCALE_CHOICES, default=0,  help_text='How user felt today')
    slept_scale = models.IntegerField(choices=SCALE_CHOICES, default=0, help_text='How long user slept today')
    emotions = MultiSelectField(choices=EMOTION_CHOICES, max_length=100, help_text='Which emotions did user felt')
    note = models.TextField(help_text='Custom user note')
    updated_at = models.DateTimeField(auto_now=True, help_text='Time when the interface was last updated')


class Habit(models.Model):
    COFFEE_CHOICES = [(i, str(i)) for i in range(0, 1001, 1)]  # Example: [0, 50, 100, ..., 1000]
    UNIT_CHOICES = [
        ('ml', 'ml'),
        ('l', 'l')
    ]
    UNIT_SPORTS = [
        ('minutes', 'minutes'),
        ('hours', 'hours')
    ]
    CIGARETTE_CHOICES = [
        ('choose-type', 'Choose type'),
        ('full-flavor', 'Full Flavor'),
        ('light', 'Light'),
        ('ultra-light', 'Ultra Light'),
        ('menthol', 'Menthol'),
        ('flavored', 'Flavored'),
        ('heated-tobacco', 'Heated Tobacco Products (HTP)'),
        ('e-cigarette', 'E-Cigarette (Electronic Cigarette)'),
        ('roll-your-own', 'Roll-Your-Own'),
        ('nicotine-free', 'Nicotine-Free'),
        ('premium', 'Premium'),
        ('organic', 'Organic'),
        ('other', 'Other')
    ]
    ALCOHOL_CHOICES = [
        ('beer', 'Beer'),
        ('wine', 'Wine'),
        ('vodka', 'Vodka'),
        ('whiskey', 'Whiskey'),
        ('rum', 'Rum'),
        ('tequila', 'Tequila'),
        ('gin', 'Gin'),
        ('brandy', 'Brandy'),
        ('champagne', 'Champagne'),
        ('cider', 'Cider'),
        ('absinthe', 'Absinthe'),
        ('liqueur', 'Liqueur'),
        ('sake', 'Sake'),
        ('vermouth', 'Vermouth'),
        ('mead', 'Mead'),
        ('sherry', 'Sherry'),
        ('port', 'Port'),
        ('cocktail', 'Cocktail'),
        ('schnapps', 'Schnapps'),
        ('perry', 'Perry'),
        ('moonshine', 'Moonshine'),
        ('armagnac', 'Armagnac'),
        ('calvados', 'Calvados'),
        ('grappa', 'Grappa'),
        ('aquavit', 'Aquavit'),
        ('baijiu', 'Baijiu'),
        ('ouzo', 'Ouzo'),
        ('rakia', 'Rakia'),
        ('tequila-sunrise', 'Tequila Sunrise'),
        ('martini', 'Martini'),
        ('manhattan', 'Manhattan'),
        ('margarita', 'Margarita'),
        ('mojito', 'Mojito'),
        ('bloody-mary', 'Bloody Mary'),
        ('pina-colada', 'Piña Colada'),
        ('cosmopolitan', 'Cosmopolitan'),
        ('old-fashioned', 'Old Fashioned')
    ]

    SPORTS_CHOICES = [
        ('gym', 'Gym'),
        ('running', 'Running'),
        ('cycling', 'Cycling'),
        ('swimming', 'Swimming'),
        ('basketball', 'Basketball'),
        ('soccer', 'Soccer'),
        ('tennis', 'Tennis'),
        ('yoga', 'Yoga'),
        ('pilates', 'Pilates'),
        ('hiking', 'Hiking'),
        ('climbing', 'Climbing'),
        ('dancing', 'Dancing'),
        ('boxing', 'Boxing'),
        ('martial-arts', 'Martial Arts'),
        ('weightlifting', 'Weightlifting'),
        ('crossfit', 'CrossFit'),
        ('aerobics', 'Aerobics'),
        ('rowing', 'Rowing'),
        ('skiing', 'Skiing'),
        ('snowboarding', 'Snowboarding'),
        ('skating', 'Skating'),
        ('surfing', 'Surfing'),
        ('kayaking', 'Kayaking'),
        ('golf', 'Golf'),
        ('cricket', 'Cricket'),
        ('rugby', 'Rugby'),
        ('baseball', 'Baseball'),
        ('volleyball', 'Volleyball'),
        ('badminton', 'Badminton'),
        ('table-tennis', 'Table Tennis'),
        ('archery', 'Archery'),
        ('fencing', 'Fencing'),
        ('horse-riding', 'Horse Riding'),
        ('gymnastics', 'Gymnastics'),
        ('triathlon', 'Triathlon'),
        ('bouldering', 'Bouldering')
    ]

    # Field for number of coffees in milliliters
    coffee_amount = models.PositiveIntegerField("How much coffee did you drink?", default=0)
    coffee_unit = models.CharField("Unit of coffee", max_length=2, choices=UNIT_CHOICES, default='ml')

    # Field for number of cigarettes and type
    cigarettes = models.PositiveIntegerField("How many cigarettes did you smoke?", default=0)
    cigarette_type = models.CharField("Type of cigarette", max_length=20, choices=CIGARETTE_CHOICES, blank=True)

    # Field for amount of alcohol and type
    alcohol_amount = models.PositiveIntegerField("Did you drink any alcohol? (amount)", default=0)
    alcohol_unit = models.CharField("Unit of alcohol", max_length=2, choices=UNIT_CHOICES, default='ml')
    alcohol_type = MultiSelectField("Type of alcohol", max_length=20, choices=ALCOHOL_CHOICES, blank=True)

    # Field for duration of exercise in minutes and type of sport
    exercise_minutes = models.PositiveIntegerField("How long did you exercise?", default=0)
    exercise_unit = models.CharField("Unit of sports", max_length=8, choices=UNIT_SPORTS, default='minutes')
    exercise_type = MultiSelectField("Type of exercise", max_length=20, choices=SPORTS_CHOICES, blank=True)

    updated_at = models.DateTimeField(auto_now=True, help_text='Time when the interface was last updated')


class Day(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Replace 1 with the actual default User ID
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE, default=1)  # Replace 1 with the actual default Mood ID
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, default=1)  # Replace 1 with the actual default Habit ID
    date = models.DateField()
    updated_at = models.DateTimeField(auto_now=True, help_text='Time when the interface was last updated')


