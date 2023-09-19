# Super Path Creator


Super Path Creator is a must-have tool for data scientists and data analysts, designed to simplify your workflow by automating the creation of project directories. No more manual setup – just call the function, and it will generate all the necessary folders and files to kickstart your data project.

## Features

When you use Super Path Creator, it will create the following folder structure and files for you:

```
- data
  - cleaned
  - processed
  - raw

- docs
- LICENCE
- Makefile
- Models
- notebooks
  - main.py
- README.md
- reports
- requirements.txt
- src
  - utils.py
  - process.py
  - train.py
```

## Getting Started

### Installation

To get started, follow these simple steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/BIGMOUSSA/super_arbo.git
   ```

2. Create a virtual environment:

   ```bash
   py -m venv venv
   ```

3. Activate the virtual environment:

   ```bash
   source venv/Scripts/activate
   ```

4. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

Once you've set up your environment, using Super Path Creator is a breeze. In your console, simply run:

```bash
py main.py folder_name
```

Replace `folder_name` with the path to your project directory. Even if the directory doesn't exist, Super Path Creator will create it for you with the complete folder structure and files.

## Enjoy Super Path Creator!

With Super Path Creator, you can jump-start your data projects without the hassle of manual directory setup. If you have any questions or need assistance, feel free to reach out to us at diallomous@gmail.com. Happy data coding! 🚀
