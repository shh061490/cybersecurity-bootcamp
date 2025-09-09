import winreg
def get_system_info():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion")
        os_name = winreg.QueryValueEx(key, "ProductName")[0]
        os_version = winreg.QueryValueEx(key, "CurrentVersion")[0]
        print(f"OS: {os_name}, Version: {os_version}")
    except PermissionError:
        print("Error: Permission denied")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_system_info()
