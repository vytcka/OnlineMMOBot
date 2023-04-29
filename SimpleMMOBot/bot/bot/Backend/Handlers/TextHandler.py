from Handlers.TimeHandler import TimeHandler

class TextHandler:
    @staticmethod
    def split_lines_to_array(lines, delimiter):
        array = []
        for line in lines:
            line = line.strip()
            if line:
                split_line = line.split(delimiter)
                array.extend(split_line)
        return array

    @staticmethod
    def split_credentials(credentials):
        email_or_discord_webhook_url = credentials[0].strip() if credentials[0] else ''
        password_or_discord_token = credentials[1].strip() if credentials[1] else ''
        return email_or_discord_webhook_url, password_or_discord_token
    
    @staticmethod
    def get_bot_status(lines):
        if len(lines) > 0 and lines[0].lower() == "continue":
            return "Continue"
        
        return "Pause"
    
    @staticmethod
    def get_current_action_in_text(next_action):
        max_width = len("Gather Materials")
        current_datetime = TimeHandler.get_current_datetime()
        return f"Action: {next_action.ljust(max_width)} | Time: {current_datetime}"