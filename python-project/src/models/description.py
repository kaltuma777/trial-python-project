from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from faker import Faker
import random


f = Faker ()

# An instance for Faker
fake = Faker (locale='en_US')
