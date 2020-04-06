### Windows
在執行redis並指派工作給worker時，需要使用os.fork()這個函式來執行一個新的程序。
遺憾的是，在Windows中並無相對應的方法給Python去呼叫，勉強能借助subprocess模組或multiprocessing模組來模擬，但使用起來相當麻煩。
有鑑於日後大部分用於部屬網路應用的伺服器都是使用Linux，不如就直接在Windows上安裝一個Linux子系統來操作吧！
若是使用Linux或macOS可直接安裝redis伺服器，請跳過此步驟。
1. 安裝ubuntu 18.0.4，使用Windows Subsystem for Linux
    - Windows需要以系統管理員身分執行下列指令，來啟用「適用於 Linux 的 Windows 子系統」選用功能：
        ```bash
        Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
        ```
    - 或是開啟 [控制台] -> [程式和功能] -> [開啟或關閉 Windows 功能] -> 檢查適用於 Linux 的 Windows 子系統
1. 打開Microsoft Store，搜尋Ubuntu，選擇Ububtu 18.04 LTS下載並安裝。

詳細安裝方法請參考[官方網站](https://docs.microsoft.com/zh-tw/windows/wsl/install-win10)。

### 在Linux上安裝所需軟體
1. 透過以下指令來更新已配置來源((configured sources)中所有的套件資訊(packages info)。
    在更新軟體前建議都要執行此一指令。
    ```bash
    sudo apt-get update
    ```
1. 安裝Python3
    ```bash
    sudo apt install python3
    ```
1. 安裝使用redis的必要套件
    rq和redis
    ```bash
    pip3 install rq, redis
    ```

### redis伺服器
1. 安裝redis-server
    ```bash
    sudo apt install redis-server
    ```
    
    > 如果出現：unable to locate package redis-server
    > 很可能是universe package沒有被啟用。
    > 請使用指令
    ```bash
    sudo add-apt-repository universe
    ```
1. 透過以下指令在ubuntu啟動redis-server

    ```bash
    redis-server
    ```

### 使用Hyper來操作多介面與多系統的Terminal
#### 安裝與修改
1. 到[官方網站](https://hyper.is/)安裝Hyper
1. 開啟後，到Edit -> prefrence，修改shell和shellArgs
    ```bash
    shell: 'C:\\Windows\\System32\\wsl.exe',
    shellArgs: ['~'],
    ```
    日後開啟進入Hyper即可進入WLS環境中

#### 簡易操作
1. 快捷鍵：Ctrl+Shift+T，可開啟新的分頁

#### 到主系統的硬碟資料夾中
1. 使用cd來切換到mnt資料夾，再選擇所在的硬碟即可。
    ```bash
    cd /mnt/所在硬碟/Users/使用者名稱/目標資料夾...
    ```

### Windows Terminal
安裝完WLS之後，就可以在Terminal的標籤頁下拉選單中看到Ubuntu-18.04。
開啟後路徑會直接指向「使用者資料夾」，即可開始操作Linux。

