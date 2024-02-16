Task-1

-   [Python Exercise (Intermediate-Level)](#python-exercise-intermediate-level)
    -   [Tasks](#tasks)
-   [Example Table](#example-table)
-   [Coding Guidelines](#coding-guidelines)

# Python Exercise (Intermediate-Level)

This exercise covers basic and intermediate level problem solving using python. The tasks below are segregated as per functionality, each when individually combined will add up to a whole solution.

## Tasks

-   **MySerial (Serial Module)**
    -   Create a module named **MySerial**. This module should hold **MySerial** class.
    -   **MySerial** class should hold below functionality:
        -   COM port connection
        -   Read
        -   Write
        -   Flush
        -   Writing Log File

> **Note**: Using Python’s **PySerial** module is allowed. Make sure above mentioned method’s functionality remains identical to those in **PySerial** without any loss in features.
> 
> **Time to Finish**: 1 Day

-   **Test Files**
    -   Create a test file named **COM_TEST** and write test code to test the **MySerial** module.
    -   Use Pytest to create testcase and execute them. Also use [Mocker](https://pytest-mock.readthedocs.io/en/latest/usage.html) to mock our **MySerial** module’s functionality
    -   Test file should be written in proper format with coverage of Positive Tests, Negative Tests, Functionality Tests and Repetitive Tests(Stress).
    -   Making more than one file is fine if needed.
    -   All files should collectively drop logs into single log file named `COM_test_Log.txt`

> **Note**: Use PyTest and Mocker to develop above test files
> 
> **Time to Finish**: 1.5 Days

-   **Continuous Integration**
    -   **Testing Job**
        -   Create Jenkins job which will checkout this code from GitHub.
        -   The job should be parameterized having features to run whole regression, partial regression(priority based) or selective module. Make changes to the test file execution by updating them accordingly.
        -   This job should have Artifacts saved in **Result** folder with job artifact being `COM_test_Log.txt`
        -   This job should trigger another Job after successful completion of this job.
    -   **Result Generation Job**
        -   This job should receive artifacts from **Testing Job**.
        -   Process the log file to generate `com_test_results.xlsx` and Test cases Pass/Fail Ratio Graph.
        -   Save the artifacts from this job.
        -   Run a post build python script after successful completion of this job.

> **Note**: Use your own Repository with different branch.  
> Jenkins should be set-up of your own system.
> 
> **Time to Finish**: 1.5 Days

-   **Post Build Python File**
    -   This python will take data from generated spreadsheet from **Result Generation Job** and paste it into markdown supported table format.
    -   This markdown table will be needed to be updated in your repository’s [ReadMe.md](http://ReadMe.md) file using this python script.

> **Note**: Any module that helps this functionality can be used. Use [GitPython](https://gitpython.readthedocs.io/en/stable/tutorial.html) module to help with GitHub operations.
> 
> **Time to Finish**: 1 Day
