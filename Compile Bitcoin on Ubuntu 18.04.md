# Compile Bitcoin on Ubuntu 18.04  

### 1. After installing (see [Ubuntu Notice.md](https://github.com/nourou4them/bitcoin/blob/main/Ubuntu%20Notice.md)), update and upgrade the system

        sudo apt-get update
        sudo apt-get upgrade


### 2. Install dependencies

        sudo apt-get install build-essential libtool autotools-dev autoconf pkg-config libssl-dev sqlite3
        sudo apt-get install libboost-all-dev
        sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools libprotobuf-dev protobuf-compiler
        sudo apt-get install libqrencode-dev autoconf openssl libssl-dev libevent-dev
        sudo apt-get install libminiupnpc-dev


### 3. Download Bitcoin source code

        cd ~
        git clone https://github.com/bitcoin/bitcoin.git


### 4. Download & install Berkeley DB
    
PS : Do not forget to replace the **"username"** below by yours.

        cd ~
        mkdir bitcoin/db4/
        wget 'http://download.oracle.com/berkeley-db/db-4.8.30.NC.tar.gz'
        tar -xzvf db-4.8.30.NC.tar.gz
        cd db-4.8.30.NC/build_unix/
        ../dist/configure --enable-cxx --disable-shared --with-pic --prefix=/home/theusername/bitcoin/db4/
        make install


### 5. Compile Bitcoin with Berkeley DB

PS : Do not forget to replace the **"username"** below by yours.  

        cd ~/bitcoin/
        ./autogen.sh
        ./configure LDFLAGS="-L/home/theusername/bitcoin/db4/lib/" CPPFLAGS="-I/home/theusername/bitcoin/db4/include/"

### 6. Build Bitcoin

This command below may take **5-10 minutes**  

        make -s -j5

### 7. Check everything is ok by trying to access below directory and the binaries

        cd ~/bitcoin/
        ./src/bitcoind
        ./src/bitcoin-qt
        ./src/bitcoin-cli
