# Verify Hash

 Verify Hash can be use to generate hash of a file or to verify the integrity of the file.

### Supports Platform: Cross Platform

### Programming Language: Python 3 and above

### How to use:
 1. If you have *Python3* installed. You can use the `.py` file.
  - If you are using *Python with Windows*, use [verify_hash_no_color.py][1] file.
  - If you are using *Linux/macOS*, you can use any `.py` file. But if you are using colored version i.e., [verify_hash.py][2] make sure you install, *termcolor* package in Python.

2. You can use **binaries/executable** version as well.
 - Binaries are in [executables][6] folder.
    - For ***Windows*** -> [Download][3]
    - For ***Linux*** -> [Download][4]
    - For ***macOS*** -> [Download][5]
  - After downloading, paste the file in `Documents` folder and open **Terminal/Command Prompt**.
  - Enter the command, `cd Documents`.
  - Run the file by typing `./` followed by file name. For eg., `./verify_hash.exe` (for Windows) and `./verify_hash` (for Linux/macOS).   

**Note:** On *Linux/macOS*, before running the file, you might need to run `chmod 755 verify_hash` to make it *executable*.

### Available Arguments:
 - **-h or --help:** *Displays all the available options.*
 - **-f or --file:** *This option needs to be used as to define for which file you need the program to calculate hash value.*
 - **-t or --type:** *This options needs to be used as to define which type of hashing algorithm to support.*
 - **-v or --verify-hash:** *Optional. Can be used to specify a MAC Address.*

**Note:** Program supports most of the common hashing algorithm, but if you uses an algorithm that is not supported by the program, it will gives back an **error**.

### Color Significance:
 - **Green:** Successful.
 - **Blue:** In process.
 - **Red:** Unsuccessful or Errors.

### Licensed: GNU General Public License, version 3

### Developer Information:
- **Website:** https://www.hackhunt.in/
- **Contact:** hh.hackunt@gmail.com
- **LinkedIn:** https://www.linkedin.com/company/hackhunt
- **Youtube:** [@hackhunt](https://youtube.com/hackhunt)
- **Instagram:** [@hh.hackhunt](https://www.instagram.com/hh.hackhunt/)
- **Facebook:** [@hh.hackhunt](https://www.facebook.com/hh.hackhunt/)
- **Twitter:** [hh_hackhunt](https://twitter.com/hh_hackhunt/)
- **Patreon:** [@hackhunt](https://www.patreon.com/hackhunt)

[1]: ./verify_hash_no_color.py
[2]: ./verify_hash.py
[3]: ./executables/windows/
[4]: ./executables/linux/
[5]: ./executables/mac/
[6]: ./executables/
