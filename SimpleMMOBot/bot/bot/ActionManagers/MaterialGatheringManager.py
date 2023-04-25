from Constants.Expressions import Expressions
from selenium.webdriver.common.by import By
from ActionManagers.FileManager import FileManager
from ActionManagers.VerificationManager import VerificationManager

class MaterialGatheringManager:
    def get_gathering_actions():
        gathering_actions = ["Grab", "Salvage", "Catch", "Chop", "Mine"]
        return gathering_actions

    def click_gather_button_until_close(element_handler, discord_model):
        materials_can_be_gathered = True
        while materials_can_be_gathered:
            VerificationManager.check_for_afk_verification(element_handler, discord_model)
            gather_button = element_handler.find_element(By.ID, Expressions.GATHER_BUTTON.value)
            gather_button.click()

            if "close" in gather_button.text.lower():
                materials_can_be_gathered = False

    def gather_materials(element_handler, action, link_to_material_gathering_page, discord_model):
        gathering_level_too_low = element_handler.find_element(By.XPATH, Expressions.GATHERING_LEVEL_TOO_LOW.value)
        if gathering_level_too_low:
            return "Step"

        FileManager.update_status(status_text=f"Gathering materials, Action: {action}")
        element_handler.go_to_page_by_clicking_element(link_to_material_gathering_page)
        MaterialGatheringManager.click_gather_button_until_close(element_handler, discord_model)