from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from decimal import Decimal


class MoodScale(models.Model):
    SCALE_CHOICES = [(i, str(i)) for i in range(0, 11)]
    scale = models.IntegerField(choices=SCALE_CHOICES, default=0, blank=True, null=True,
                                help_text='How user felt today on a scale from 0 to 10')
    updated_at = models.DateTimeField(auto_now=True, help_text='Time when the scale was last updated')


class MoodEmotion(models.Model):
    EMOTION_CHOICES = (
        ('happy', 'Happy'), ('sad', 'Sad'), ('angry', 'Angry'), ('excited', 'Excited'),
        ('nervous', 'Nervous'), ('scared', 'Scared'), ('relaxed', 'Relaxed'),
        ('bored', 'Bored'), ('content', 'Content'), ('curious', 'Curious'),
        ('anxious', 'Anxious'), ('confused', 'Confused'), ('surprised', 'Surprised'),
        ('grateful', 'Grateful'), ('frustrated', 'Frustrated'), ('jealous', 'Jealous'),
        ('lonely', 'Lonely'), ('proud', 'Proud'), ('ashamed', 'Ashamed'),
        ('guilty', 'Guilty'), ('embarrassed', 'Embarrassed'), ('disappointed', 'Disappointed'),
        ('inspired', 'Inspired'), ('amused', 'Amused'), ('sympathetic', 'Sympathetic'),
        ('thoughtful', 'Thoughtful'), ('energetic', 'Energetic'), ('overwhelmed', 'Overwhelmed'),
        ('hopeful', 'Hopeful')
    )
    emotions = MultiSelectField(choices=EMOTION_CHOICES, max_length=99999, blank=True,
                                help_text='Which emotions did user feel')
    updated_at = models.DateTimeField(auto_now=True, help_text='Time when emotions were last updated')

class MoodNote(models.Model):
    note = models.TextField(blank=True, help_text='Custom user note related to their mood')
    updated_at = models.DateTimeField(auto_now=True, help_text='Time when the note was last updated')

class Sleep(models.Model):
    SCALE_CHOICES_HALF = [(Decimal(i) / 2, f'{Decimal(i) / 2:.1f}') for i in range(0, 49)]

    slept_scale = models.FloatField(choices=SCALE_CHOICES_HALF, default=0, blank=True, null=True,
                                    help_text='How long user slept today')
    updated_at = models.DateTimeField(auto_now=True, help_text='Time when the interface was last updated')

class CoffeHabit(models.Model):
    CHOICES = [(i, str(i)) for i in range(0, 1001, 1)]
    UNIT_CHOICES = [
        ('ml', 'ml'),
        ('l', 'l')
    ]

    coffee_amount = models.PositiveIntegerField("How much coffee did you drink?", blank=True, null=True)
    coffee_unit = models.CharField("Unit of coffee", max_length=2, choices=UNIT_CHOICES, default='ml', blank=True,
                                   null=True)
    updated_at = models.DateTimeField(auto_now=True, help_text='Time when the interface was last updated')

class CigaretteHabit(models.Model):
    CHOICES = [
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

    cigarettes = models.PositiveIntegerField("How many cigarettes did you smoke?", blank=True, null=True)
    cigarette_type = models.CharField("Type of cigarette", max_length=20, choices=CHOICES, blank=True)
    updated_at = models.DateTimeField(auto_now=True, help_text='Time when the interface was last updated')

class Sports(models.Model):
    UNIT = [
        ('minutes', 'minutes'),
        ('hours', 'hours')
    ]

    CHOICES = [
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

    exercise_times = models.PositiveIntegerField("How long did you exercise?", blank=True, null=True)
    exercise_unit = models.CharField("Unit of sports", max_length=8, choices=UNIT, default='minutes', blank=True,
                                     null=True)
    exercise_type = MultiSelectField("Type of exercise", max_length=99999, choices=CHOICES, blank=True)
    updated_at = models.DateTimeField(auto_now=True, help_text='Time when the interface was last updated')

class AlcoholHabit(models.Model):
    UNIT = [
        ('ml', 'ml'),
        ('l', 'l')
    ]

    CHOICES = [
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

    alcohol_amount = models.PositiveIntegerField("Did you drink any alcohol? (amount)", blank=True,
                                                 null=True)
    alcohol_unit = models.CharField("Unit of alcohol", max_length=2, choices=UNIT, default='ml', blank=True,
                                    null=True)
    alcohol_type = MultiSelectField("Type of alcohol", max_length=99999, choices=CHOICES, blank=True)
    updated_at = models.DateTimeField(auto_now=True, help_text='Time when the interface was last updated')

class Day(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood_scale = models.OneToOneField(MoodScale, on_delete=models.CASCADE, null=True, blank=True)
    mood_emotion = models.OneToOneField(MoodEmotion, on_delete=models.CASCADE, null=True, blank=True)
    mood_note = models.OneToOneField(MoodNote, on_delete=models.CASCADE, null=True, blank=True)
    sleep = models.ForeignKey('Sleep', on_delete=models.CASCADE, null=True, blank=True)
    coffee_habit = models.ForeignKey('CoffeHabit', on_delete=models.CASCADE, null=True, blank=True)
    cigarette_habit = models.ForeignKey('CigaretteHabit', on_delete=models.CASCADE, null=True, blank=True)
    alcohol_habit = models.ForeignKey(AlcoholHabit, on_delete=models.CASCADE, null=True, blank=True)
    sports = models.ForeignKey('Sports', on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)

    def delete(self, *args, **kwargs):
        if self.mood_scale:
            self.mood_scale.delete()
        if self.mood_emotion:
            self.mood_emotion.delete()
        if self.mood_note:
            self.mood_note.delete()
        if self.sleep:
            self.sleep.delete()
        if self.coffee_habit:
            self.coffee_habit.delete()
        if self.cigarette_habit:
            self.cigarette_habit.delete()
        if self.alcohol_habit:
            self.alcohol_habit.delete()
        if self.sports:
            self.sports.delete()
        super().delete(*args, **kwargs)
