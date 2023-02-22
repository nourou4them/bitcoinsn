# Bitcoin

### The aim of this repository is to give step by step guide for people that want make their first step in Bitcoin programming.  
The example have been made on a fresh Ubuntu install.  
This has been done as a test to be in the bitcoin labs seminary, to learn more and deeply about Bitcoin. 

### **STEPS**

1. There is a guide to install WSL on a windows machine and on a non-system drive

    [Ubuntu Notice.md](https://github.com/nourou4them/bitcoin/blob/main/Ubuntu%20Notice.md)  

2. The next step is to compile bitcoin on the Ubuntu or Fedora server  
    [Compile Bitcoin on Ubuntu 18.04](https://github.com/nourou4them/bitcoin/blob/main/Compile%20Bitcoin%20on%20Ubuntu%2018.04.md#compile-bitcoin-on-ubuntu-1804)  
    [Compile Bitcoin on Fedora](https://github.com/nourou4them/bitcoinsn/blob/main/Compile-Bitcoin-Core-on-Fedora-37.md)

3. The next step, after a successful installation, is to run unit/reression tests  
I have provide the logs when I have run them.  
    [Unit tests - Logs](https://github.com/nourou4them/bitcoin/blob/main/Unit%20tests%20-%20Logs.md)  
    [Regression tests - Full Logs](https://github.com/nourou4them/bitcoin/blob/main/Regression%20tests%20-%20All%20Logs.md#regression-tests---logs)  
    [Regression tests - Light Logs](https://github.com/nourou4them/bitcoin/blob/main/Regression%20tests%20-%20Light%20Logs.md)  

4. Finally, I had to provide a modified code from the test_example.py testing script in order to do 3 actions :  
        - Mine a block  
        - Send it to a dedicated node  
        - Check that node has received it.  
    [example_test_mk.py](https://github.com/nourou4them/bitcoin/blob/main/example_test_mk.py) 
    
I have also added some words about bitcoin-related subjects.
- [Full Node](https://github.com/nourou4them/bitcoinsn/blob/main/full_node.md)

## Do not hesitate to contribute as this would be useful for anyone that is interested in Bitcoin Programming.
