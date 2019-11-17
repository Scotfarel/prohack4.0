from django.db import models


class Sensor(models.Model):
    sensor_id = models.IntegerField()
    working_state = models.BooleanField()


class WorkerCoordinate(models.Model):
    worker_id = models.IntegerField()
    x_coordinate = models.FloatField()
    y_coordinate = models.FloatField()
