from app import db

__author__ = 'darryl'


class Product(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    price = db.Column(db.Float)
    manufacturer = db.Column(db.String(255))
    supplier = db.Column(db.String(255))
    link = db.Column(db.String(255))
    img_link = db.Column(db.String(255))
    product_type = db.Column(db.String(255))
    hash = db.Column(db.String(50))


class Motherboard(Product):
    __tablename__ = 'moederborden'
    socket = db.Column(db.String(25))
    formfactor = db.Column(db.String(25))
    mem_slots = db.Column(db.Integer)
    mem_max = db.Column(db.String(25))
    sata_slots = db.Column(db.Integer)
    usb_slots = db.Column(db.Integer)


class Gpu(Product):
    __tablename__ = 'videokaarten'
    chipset = db.Column(db.String(255))
    mem_type = db.Column(db.String(25))
    mem_amount = db.Column(db.Integer)
    slots = db.Column(db.Integer)


class Cpu(Product):
    __tablename__ = 'processoren'
    socket = db.Column(db.String(25))
    speed = db.Column(db.Float)
    cores = db.Column(db.Integer)


class Memory(Product):
    __tablename__ = 'geheugen'
    type = db.Column(db.String(25))
    amount = db.Column(db.String(25))
    slots = db.Column(db.Integer)


class Psu(Product):
    __tablename__ = 'voedingen'
    formfactor = db.Column(db.String(25))
    power = db.Column(db.Integer)


class Hdd(Product):
    __tablename__ = 'harddisks'
    physical_size = db.Column(db.String(25))
    capacity = db.Column(db.String(25))
    interface = db.Column(db.String(25))
    type = db.Column(db.String(25))


class Case(Product):
    __tablename__ = 'behuizingen'
    external_35 = db.Column(db.Integer)
    color = db.Column(db.String(25))
    internal_35 = db.Column(db.Integer)
    internal_25 = db.Column(db.Integer)
    external_525 = db.Column(db.Integer)
    formfactor_mobo = db.Column(db.String(25))
    formfactor_psu = db.Column(db.String(25))


class Configs(db.Model):
    __tablename__ = 'configuraties'
    id = db.Column(db.Integer, primary_key=True)
    cpu = db.Column(db.String(50))
    gpu = db.Column(db.String(50))
    case = db.Column(db.String(50))
    hdd = db.Column(db.String(50))
    psu = db.Column(db.String(50))
    mem = db.Column(db.String(50))
    mobo = db.Column(db.String(50))
