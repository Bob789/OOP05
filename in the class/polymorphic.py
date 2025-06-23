from abc import ABC, abstractmethod
from typing import override

# We use in this sample with polymorphic by using extra external methode
# def talk(m: IMobilePhone, minutes):
#     m.talk(minutes)
# and we call to this external methode and send the Object as parameter
# talk(m1, 5)
#     talk(m2, 10)
#     talk(mega_phone, 3)



# Abstract base class defining the contract for all mobile phone implementations
class IMobilePhone(ABC):
    @abstractmethod
    def turn_on(self):
        """Power on the mobile phone"""
        pass

    @abstractmethod
    def turn_off(self):
        """Power off the mobile phone"""
        pass

    @abstractmethod
    def talk(self, minutes):
        """Make a phone call for specified duration in minutes"""
        pass

    @abstractmethod
    def get_battery_perc(self):
        """Return current battery percentage as integer"""
        pass


# Concrete implementation of a basic mobile phone
class MobilePhone(IMobilePhone):

    def __init__(self, model):
        """Initialize phone with model name, full battery, and powered off state"""
        self.model = model
        self.__battery = 100  # Private attribute: battery percentage
        self.__is_on = False  # Private attribute: power state

    @override
    def turn_on(self):
        """Turn on phone if currently off, otherwise show already on message"""
        if not self.__is_on:
            self.__is_on = True
            print(f"{self.model} is now ON.")
        else:
            print(f"{self.model} is already ON.")

    @override
    def turn_off(self):
        """Turn off phone if currently on, otherwise show already off message"""
        if self.__is_on:
            self.__is_on = False
            print(f"{self.model} is now OFF.")
        else:
            print(f"{self.model} is already OFF.")

    @override
    def talk(self, minutes):
        """Make call if phone is on and has sufficient battery"""
        if not self.__is_on:
            print("Phone is OFF. Please turn it on first.")
            return
        battery_usage = minutes * 2  # Battery consumption: 2% per minute
        if self.__battery >= battery_usage:
            self.__battery -= battery_usage
            print(f"Talking for {minutes} minutes...")
        else:
            print("Battery too low to talk for that long.")
        print(f"Battery now at {self.__battery}%")

    @override
    def get_battery_perc(self):
        """Return current battery level"""
        return self.__battery

# External methode
# Polymorphic function that works with any IMobilePhone implementation
def talk(m: IMobilePhone, minutes):
    """Delegate call functionality to the phone's talk method"""
    m.talk(minutes)


# Extended implementation with enhanced features
class MegaPhone(IMobilePhone):
    def __init__(self, model):
        """Initialize MegaPhone with enhanced audio capabilities"""
        self.model = model
        self.__battery = 100
        self.__is_on = False
        self.__volume_boost = True  # Special feature: enhanced volume

    @override
    def turn_on(self):
        """Power on with volume boost notification"""
        if not self.__is_on:
            self.__is_on = True
            print(f"{self.model} MEGA PHONE is now ON with VOLUME BOOST!")
        else:
            print(f"{self.model} is already ON.")

    @override
    def turn_off(self):
        """Power off MegaPhone"""
        if self.__is_on:
            self.__is_on = False
            print(f"{self.model} MEGA PHONE is now OFF.")
        else:
            print(f"{self.model} is already OFF.")

    @override
    def talk(self, minutes):
        """Make enhanced call with higher battery consumption due to volume boost"""
        if not self.__is_on:
            print("MEGA PHONE is OFF. Please turn it on first.")
            return
        # Higher battery consumption due to volume boost feature
        battery_usage = minutes * 3  # Battery consumption: 3% per minute
        if self.__battery >= battery_usage:
            self.__battery -= battery_usage
            print(f"MEGA TALKING for {minutes} minutes with LOUD VOLUME!")
        else:
            print("Battery too low for MEGA TALK.")
        print(f"MEGA Battery now at {self.__battery}%")

    @override
    def get_battery_perc(self):
        """Return current battery level"""
        return self.__battery


# Demo usage showing polymorphism and inheritance
if __name__ == "__main__":
    print("=== Creating Phone Instances ===")
    # Interface reference allows polymorphic behavior
    m1: IMobilePhone = MobilePhone("iPhone 15")
    # Concrete reference allows access to all features
    m2: MobilePhone = MobilePhone("Samsung Galaxy")
    # Specialized phone with enhanced features
    mega_phone: MegaPhone = MegaPhone("MegaPhone Pro")

    print("\n=== Powering On Devices ===")
    m1.turn_on()
    m2.turn_on()
    mega_phone.turn_on()

    print("\n=== Making Calls ===")
    # Polymorphic calls - same interface, different implementations
    talk(m1, 5)
    talk(m2, 10)
    talk(mega_phone, 3)

    print("\n=== Checking Battery Levels ===")
    print(f"iPhone battery: {m1.get_battery_perc()}%")
    print(f"Samsung battery: {m2.get_battery_perc()}%")
    print(f"MegaPhone battery: {mega_phone.get_battery_perc()}%")

    print("\n=== Powering Off Devices ===")
    m1.turn_off()
    m2.turn_off()
    mega_phone.turn_off()

    # Output
    # === Creating Phone Instances ===
    #
    # === Powering On Devices ===
    # iPhone 15 is now ON.
    # Samsung Galaxy is now ON.
    # MegaPhone Pro MEGA PHONE is now ON with VOLUME BOOST!
    #
    # === Making Calls ===
    # Talking for 5 minutes...
    # Battery now at 90%
    # Talking for 10 minutes...
    # Battery now at 80%
    # MEGA TALKING for 3 minutes with LOUD VOLUME!
    # MEGA Battery now at 91%
    #
    # === Checking Battery Levels ===
    # iPhone battery: 90%
    # Samsung battery: 80%
    # MegaPhone battery: 91%
    #
    # === Powering Off Devices ===
    # iPhone 15 is now OFF.
    # Samsung Galaxy is now OFF.
    # MegaPhone Pro MEGA PHONE is now OFF.