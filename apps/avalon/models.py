from django.db import models


class Room(models.Model):
    room_id = models.CharField(max_length=32, unique=True)

    def __str__(self): return self.room_id


class Player(models.Model):
    room = models.ForeignKey(Room, models.CASCADE, 'players')
    name = models.CharField(max_length=5, default='default_name')

    ROLE_CHOICES = (
        ('soldier', '兵士'), ('merlin', 'マーリン'),
        ('mordred', 'モードレッド'), ('assassin', '暗殺者'))
    role = models.CharField(max_length=12, choices=ROLE_CHOICES)

    class Meta:
        ordering = 'name',

    def __str__(self): return self.name


class Quest(models.Model):
    room = models.ForeignKey(Room, models.CASCADE, 'quests')
    num = models.IntegerField()
    leader = models.ForeignKey(Player, models.CASCADE)
    member1 = models.ForeignKey(Player, models.CASCADE, 'q1')
    member2 = models.ForeignKey(Player, models.CASCADE, 'q2')
    member3 = models.ForeignKey(Player, models.CASCADE, 'q3', null=True)
    result1 = models.BooleanField(null=True)
    result2 = models.BooleanField(null=True)
    result3 = models.BooleanField(null=True)

    def __str__(self): return f'{self.room}_{self.num}'


class Poll(models.Model):
    quest = models.ForeignKey(Quest, models.CASCADE, 'polls')
    num = models.IntegerField()
    leader = models.ForeignKey(Player, models.CASCADE)
    member1 = models.ForeignKey(Player, models.CASCADE, 'p1')
    member2 = models.ForeignKey(Player, models.CASCADE, 'p2')
    member3 = models.ForeignKey(Player, models.CASCADE, 'p3', null=True)
    poll1 = models.BooleanField(null=True)
    poll2 = models.BooleanField(null=True)
    poll3 = models.BooleanField(null=True)
    poll4 = models.BooleanField(null=True)
    poll5 = models.BooleanField(null=True)

    def __str__(self): return f'{self.room}_{self.quest.num}_{self.num}'


class State(models.Model):
    room = models.OneToOneField(Room, models.CASCADE)
    quest = models.IntegerField()
    poll = models.IntegerField()
    leader = models.ForeignKey(Player, models.CASCADE)

    def __str__(self): return f'{self.room}_state'
