# Install WSL on D:\ drive
## 1. Enable windows subsystem for Linux system feature  
Open **Powershell** as admin  
*Run this command :*  
        
        Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux 
## 2. Download and install a Linux distribution (example : Ubuntu 18.04)
*Run this command :*  
        
        Invoke-WebRequest -Uri https://aka.ms/wsl-ubuntu-1804 -OutFile Ubuntu.appx -UseBasicParsing 

*Unpack the zip file*  
        
        move .\Ubuntu.appx .\Ubuntu.zip 
        Expand-Archive .\Ubuntu.zip```*

*Initialize Linux distro*  
        
        cd .\Ubuntu\  
        .\ubuntu1804.exe 

Once the instllation is done, you would have something like :  
        
        PS D:\WSL\Ubuntu> ls   

            Répertoire : D:\WSL\Ubuntu


    Mode                 LastWriteTime         Length Name
    ----                 -------------         ------ ----
    d-----        20/06/2021     11:40                AppxMetadata
    d-----        20/06/2021     11:40                Assets
    da----        20/06/2021     11:41                rootfs
    d-----        20/06/2021     11:41                temp
    -a----        22/05/2019     08:15         219038 AppxBlockMap.xml
    -a----        22/05/2019     08:15           3851 AppxManifest.xml
    -a----        22/05/2019     08:15          11209 AppxSignature.p7x
    -a---l        20/06/2021     11:42              0 fsserver
    -a----        22/05/2019     08:15      231179584 install.tar.gz
    -a----        22/05/2019     08:15           5400 resources.pri
    -a----        22/05/2019     08:15         211968 ubuntu1804.exe
    -a----        22/05/2019     08:15            744 [Content_Types].xml  
    ```




