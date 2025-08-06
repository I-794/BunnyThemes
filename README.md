# Pisscord Themes

This repository is a collection of themes for what is presumably a custom Discord client or mod, referred to as "Pisscord". It also includes a Python script to generate new, randomized color themes from the existing ones.

## Included Themes

This repository comes with a few pre-made themes:

*   `Pisscord.json`
*   `Pisscord Final.json`
*   `pisscord v2.json`
*   `pisscord3.json`
*   `ChatGPT.json`
*   `test_theme.json`

## Create Your Own Randomized Theme

You can use the included Python script to generate your own themes with randomized colors.

### Prerequisites

*   Python 3.x

### Usage

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/i-794/pisscord-themes.git
    cd pisscord-themes
    ```

2.  **Choose a base theme:**
    Select one of the existing `.json` theme files to use as a template.

3.  **Run the script:**
    Execute the `replace_colors.py` script and provide the path to the theme file you want to modify. The script will overwrite the specified file with randomized colors.

    For example, to randomize the colors in `Pisscord.json`:
    ```bash
    python replace_colors.py Pisscord.json
    ```

    A new set of random colors will be applied to the theme file. You can then use this modified file in your client.
