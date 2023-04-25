from enum import Enum

class Expressions(Enum):
    EMAIL_INPUT = "email"
    PASSWORD_INPUT = "password"
    LOGIN_BUTTON = "button[type='submit']"

    PRESS_VERIFY_BUTTON = "Press here to verify"
    CONFIRM_EXISTENCE_BUTTON = "Press here to confirm your existence"
    TAKE_STEP_BUTTON = "//button[contains(text(), 'Take a step')]"
    ATTACK_MOB_PAGE_LINK = "Attack"
    ATTACK_MOB_BUTTON = "//button[contains(text(), 'Attack')]"
    BATTLE_HAS_ENDED = "End Battle"
    LINK_TO_GATHERING_PAGE = "//button[contains(text(), '{}')]"
    GATHER_BUTTON = "crafting_button"
    GATHERING_LEVEL_TOO_LOW = "//small[contains(text(), \"Your skill level isn't high enough\")]"
    

