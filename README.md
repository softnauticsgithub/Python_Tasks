# What's Inside?
This repository holds Beginner to Advance level Python Tasks.
The aim of this repository is serve interest of Python Development in multiple ways.

> Feel free to **contribute**. 
# How to Contribute Ideas / Tasks?

 1. Start a [Discussion](https://github.com/softnauticsgithub/Sarth_Vadgama_Tasks/discussions).
 2. Discussion name should be proper and identifiable. 
 3. Submit your work by creating a PR.
 4. Mention the PR in discussion when ready to be added.
 5. PR will be merged once review is done.

# Coding Guidelines

-   Clean and minimalistic code
-   Useful and required comments
    
    ```
    for line in lines:  
    if line.strip("\n") != phrase: # Checks if line in file matches the phrase  
    fw.write(line)
    
    ```
    
-   Proper Docstrings and annotations (Required for each function, class, module, etc)
    
    ```
    def delete(self, phrase: str) -> bool:  
    """  
    This method will match given phrase from file and delete it if matches.  
    :param phrase: String to be deleted from file.:return: True on successful deletion.  
    """  
    try:  
    	with open(self.textfile, 'r') as fr:  
    	lines = fr.readlines()
    
    ```
    
-   Pylint Score(above 8.5/10)
-   Black Formatted (characters per line- 79)
-   No grammartical mistakes or typos in delivered code
-   dos2unix (LF) formatted  
    **Command**: `dos2unix [options] [file]`
-   `# TODO:` wherever necessary
-   Different directories for source file, modules, supoort files
-   Standard Naming Convection
-   Debug Prints should be removed before delivery or handled with flags.  
    Flag Implementation:
    
    ```
    debug = bool(True/False)
    if debug = True:
    	print(f"This is debug print for Variable A: {a}")
    
    ```
