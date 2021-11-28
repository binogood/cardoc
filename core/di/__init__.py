from pythondi import Provider, configure
from app.user.repository.user import UserRepo, UserMySQLRepo
from app.user.repository.user_car import UserCarRepo, UserCarMySQLRepo
from app.tire.repository.tire import TireRepo, TireMySQLRepo
from app.tire.repository.tire_type import TireTypeRepo, TireTypeMySQLRepo
from app.car.repository.car import CarRepo, CarMySQLRepo
from app.car.repository.car_tire import CarTireRepo, CarTireMySQLRepo


def init_di():
    provider = Provider()
    provider.bind(UserRepo, UserMySQLRepo)
    provider.bind(UserCarRepo, UserCarMySQLRepo)
    provider.bind(TireRepo, TireMySQLRepo)
    provider.bind(TireTypeRepo, TireTypeMySQLRepo)
    provider.bind(CarRepo, CarMySQLRepo)
    provider.bind(CarTireRepo, CarTireMySQLRepo)
    configure(provider=provider)