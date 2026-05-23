#user Configuration Manager
# Manages user settings like theme, language, and notification preferences.

def add_setting( settings,new_setting):
    key, value = new_setting
    key = key.lower()
    value = value.lower()

    if key in settings:
        return f"Setting '{key}' already exists.Cannot add a new setting with this name."

    settings[key] = value
    return f"Setting '{key}' added successfully with value '{value}'."

def update_setting(settings, new_setting):
    key, value = new_setting
    key = key.lower()
    value = value.lower()

    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated successfully to value '{value}'."
    else:
        return f"Setting '{key}' does not exist. Cannot update a non-existing setting."
    

def delete_setting(settings, key):
    key = key.lower()

    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully."
    else:
        return "Setting not found!"
    

def view_settings(settings):
    if not settings:
        return "No settings found."
    result =["Current User Settings:"]
    for key, value in settings.items():
        result.append(f"{key.capitalize()}: {value}")  
    return "\n".join(result) + "\n"

# -------------------------
# Testing the functions
# -------------------------

if __name__ == "__main__":
    test_settings = {"theme": "light"}

    # Add tests
    print(add_setting(test_settings, ("volume", "high")))
    # Setting 'volume' added with value 'high' successfully!

    print(add_setting(test_settings, ("THEME", "dark")))
    # Setting 'theme' already exists! Cannot add a new setting with this name.

    # Update tests
    print(update_setting(test_settings, ("volume", "low")))
    # Setting 'volume' updated to 'low' successfully!

    print(update_setting(test_settings, ("notifications", "enabled")))
    # Setting 'notifications' does not exist! Cannot update a non-existing setting.

    # Delete tests
    print(delete_setting(test_settings, "theme"))
    # Setting 'theme' deleted successfully!

    print(delete_setting(test_settings, "language"))
    # Setting not found!

    # View tests
    print(view_settings(test_settings))
    # Current User Settings:
    # Volume: low

    print(view_settings({}))
    # No settings available.
