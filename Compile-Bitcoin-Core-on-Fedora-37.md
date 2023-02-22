# Compile Bitcoin Core on Fedora Linux

### 1. Update and upgrade the system 

       sudo dnf update
       sudo dnf upgrade

### 2. Install dependencies

       sudo dnf install gcc-c++ libtool make autoconf automake python3 
       sudo dnf install libevent-devel boost-devel
       sudo dnf install sqlite-devel
       sudo dnf install libdb-devel
       sudo dnf install libdb-cxx-devel
       sudo dnf install miniupnpc-devel libnatpmp-devel 
       sudo dnf install zeromq-devel
       sudo dnf install systemtap
       sudo dnf install qt5-qttools-devel qt5-qtbase-devel
       sudo dnf install qt5-qtwayland
       sudo dnf install qrencode-devel

### 3. Download Bitcoin Core source code

       cd ~
       git clone https://github.com/bitcoin/bitcoin.git

### 4. (Optional) Show all version tags 
       
       git tag

## 5. Checkout to the last release version. At this time the last release version is v24.0.1
PS: Do not forget to replace the **"v24.0.1"** by the last release version
  
       git checkout "v24.0.1"

### 6. Download & install Berkeley DB 4.8. The legacy wallet uses Berkeley DB. To ensure backwards compatibility it is recommended to use Berkeley DB 4.8

       cd ~/bitcoin
       ./contrib/install_db4.sh `pwd`    

### 7. Compile Bitcoin Core 

       cd ~/bitcoin/
       ./autogen.sh
       ./configure 

### 8. Build Bitcoin Core

       make
       sudo make install

### 9. Check everything is ok by trying to access below directory and the binaries

       cd ~/bitcoin/
       ./src/bitcoind
       ./src/bitcoin-qt
       ./src/bitcoin-cli
