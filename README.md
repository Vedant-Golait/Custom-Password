# Custom Strong Password Generator

This Python script generates strong, customized passwords that incorporate the user's name and a specified number, along with random characters from various character sets, including uppercase letters, lowercase letters, digits, and symbols.

## Features

- **Custom User Input**: The script prompts the user to enter their name and a custom number, which are then incorporated into the generated passwords.
- **Character Set Selection**: Users can choose which character sets (uppercase letters, lowercase letters, digits, and symbols) to include in the generated passwords.
- **Password Length Control**: Users can control the length of the random character segments in the generated passwords.
- **Multiple Password Generation**: The script can generate multiple passwords (default is 10) in a single run.
- **Password Storage**: The generated passwords are stored in a file named `passlist.txt` for future reference.

## Mind Map

+-----------------------------------+
|    Custom Strong Password Generator    |
+-----------------------------------+
             |
+------------+------------+
|                         |
+--------+--------+       |
|        |        |       |
| User Input      | Character Sets
|        |        |       |
+--------+--------+       |
|        |        |       |
| Name   | Number |       +-----------+------------+
|        |        |                  |            |
+--------+--------+        +---------+-+  +-------+-------+
                           | Uppercase |  | Lowercase    |
                           +-----------+  +-------+-------+
                                               |
                           +-----------+  +-------+-------+
                           | Digits    |  | Symbols      |
                           +-----------+  +-------+-------+
                                               |
                           +-----------+  +-------+-------+
                           | Password  |  | Password     |
                           | Length    |  | Amount       |
                           +-----------+  +-------+-------+
                                               |
                                       +-------+-------+
                                       | Password      |
                                       | Storage       |
                                       +---------------+


## Getting Started

1. Clone the repository or download the `main.py` file.
2. Open a terminal or command prompt and navigate to the directory containing the `main.py` file.
3. Run the script using the following command:
4. Follow the prompts to enter your name and a custom number.
5. The script will generate and display the customized strong passwords, which will also be saved in the `passlist.txt` file.

## Usage

- **Name and Number Input**: When prompted, enter your name and a custom number. These values will be incorporated into the generated passwords.
- **Character Set Selection**: The script will automatically include all character sets by default. However, you can modify the script to exclude specific character sets by setting the corresponding flags (`upper`, `lower`, `nums`, `syms`) to `False`.
- **Password Length**: The length of the random character segments in the generated passwords is set to 4 by default. You can modify the `Length` variable in the script to change this value.
- **Number of Passwords**: The script generates 10 passwords by default. You can modify the `Amount` variable to generate a different number of passwords.

## Contributing

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).

# Buy Me a Book # Support

If you found this project helpful and would like to support its development, consider buying me a book. Your contribution, no matter how small, will go a long way in helping me continue to learn and improve.

[![Buy Me a Book][https://www.buymeacoffee.com/Vedant.Golait]

Your support means a lot and will be greatly appreciated!
