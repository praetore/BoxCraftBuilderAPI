import datetime
from app import db

__author__ = 'darryl'


class Product(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now)
    name = db.StringField(max_length=255)
    price = db.DecimalField()
    manufacturer = db.StringField(max_length=255)
    seller = db.StringField(max_length=255)
    link = db.StringField(max_length=255)
    img_link = db.StringField(max_length=255)


class Motherboard(Product):
    formfactor = db.StringField(max_length=25)
    memory_slots = db.IntField()
    socket = db.StringField(max_length=25)
    max_ram_supported = db.StringField(max_length=25)
    usb_slots = db.IntField()
    sata_slots = db.IntField()


class Gpu(Product):
    chipset = db.StringField(max_length=255)
    memory_type = db.StringField(max_length=25)
    memory_amount = db.IntField()
    slot_space = db.IntField()


class Cpu(Product):
    socket = db.StringField(max_length=25)
    speed = db.DecimalField()
    cores = db.IntField()


class Memory(Product):
    memory_type = db.StringField(max_length=25)
    memory_amount = db.IntField()
    memory_slots = db.IntField()


class Psu(Product):
    power = db.IntField()
    formfactor = db.StringField(max_length=25)


class Hdd(Product):
    physical_size = db.StringField(max_length=25)
    capacity = db.StringField(max_length=25)
    interface = db.StringField(max_length=25)
    type = db.StringField(max_length=25)


class Case(Product):
    external_35 = db.IntField()
    color = db.StringField(max_length=25)
    internal_35 = db.IntField()
    internal_25 = db.IntField()
    formfactor_mobo = db.StringField(max_length=25)
    formfactor_psu = db.StringField(max_length=25)


class Configuration(db.Document):
    cpu = db.StringField(max_length=50)
    gpu = db.StringField(max_length=50)
    case = db.StringField(max_length=50)
    hdd = db.StringField(max_length=50)
    psu = db.StringField(max_length=50)
    mem = db.StringField(max_length=50)
    mobo = db.StringField(max_length=50)