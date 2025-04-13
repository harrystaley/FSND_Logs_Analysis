# FSND_Logs_Analysis

## Project Overview

The FSND_Logs_Analysis repository is part of the Udacity Full Stack Web Developer Nanodegree program. This project is designed to provide a real-world scenario in which students can practice and hone their database and SQL querying skills. By using Python and SQL, students will analyze web server logs to discover insights about the website's traffic.

### Project Structure

- `logs_analysis.py`: Main Python script to run the logs analysis.
- `results.txt`: Example output of the analysis.
- `/vagrant`: Directory containing Vagrantfile for setting up the virtual environment.
- `README.md`: Documentation about this project.

## Setup and Installation

### Prerequisites

- [Python 3](https://www.python.org/downloads/)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- [Vagrant](https://www.vagrantup.com/downloads.html)
- Access to a command-line interface.

### Installation Steps

1. **Install VirtualBox**: Download and install VirtualBox, which will run the virtual machine.

2. **Install Vagrant**: Download and install Vagrant, which will configure the VM environment.

3. **Clone the Repository**: Clone this repository to your local machine.
   ```bash
   git clone https://github.com/your-username/FSND_Logs_Analysis.git
   ```

4. **Navigate to the Vagrant Directory**:
   ```bash
   cd FSND_Logs_Analysis/vagrant
   ```

5. **Start Vagrant**:
   ```bash
   vagrant up
   ```
   This command will set up the virtual machine as per the configuration specified in the `Vagrantfile`.

6. **Log into Vagrant VM**:
   ```bash
   vagrant ssh
   ```

7. **Navigate to the Shared Directory**:
   ```bash
   cd /vagrant
   ```

8. **Run the Logs Analysis Script**:
   ```bash
   python3 logs_analysis.py
   ```

## Usage

After setting up the environment as described above, you can run the script using the following command:

```bash
python3 logs_analysis.py
```

This will execute the SQL queries defined in the script and output the analysis results. The results will be printed to the console and can also be found in the `results.txt` file.

## How to Contribute

Contributions to the FSND_Logs_Analysis project are welcome! Here are ways you can contribute:

- Submit bugs and feature requests.
- Review code and improve documentation.
- Submit pull requests to enhance the project.

Before contributing, please read the contribution guidelines carefully.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details. This ensures that all users have the freedom to use, modify, and distribute the software.

## Final Notes

Thank you for your interest in the FSND_Logs_Analysis project. We hope it helps you learn more about handling and analyzing server logs using Python and SQL in a virtualized environment. Happy coding!