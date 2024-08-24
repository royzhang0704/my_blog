# 我的BLOG專案

這是一個基於 Django 的博客專案，用戶可以創建和管理博客文章、對文章留言，並追蹤自己的現金和股票投資組合。

## 功能

- **博客文章**：用戶可以創建、查看和管理博客文章。
- **留言功能**：用戶可以在博客文章下方留言。
- **財務投資組合**：用戶可以追蹤現金和股票投資。
- **稍後閱讀**：用戶可以將文章保存至稍後閱讀清單。

## 安裝

### 先決條件

- Python 3.9 或更高版本
- pip
- Virtualenv（可選但推薦使用）

### 設置

1. **Clone 此倉庫**：
    ```bash
    git clone https://github.com/royzhang0704/My_blog.git
    cd My_blog
    ```

2. **創建並啟用虛擬環境**（可選但推薦）：
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # Windows 系統使用 `.venv\Scripts\activate`
    ```

3. **安裝所需依賴**：
    ```bash
    pip install -r requirements.txt
    ```

4. **創建本地 MySQL 資料庫**：
    ```bash
    CREATE DATABASE my_blog_db;
    ```

5. **複製 .env.example 文件並重命名為 .env**：
    ```bash
    cp .env.example .env
    ```
    在 `.env` 文件中填寫：
    - SECRET_KEY: 你的密鑰。
    - DATABASE_NAME: 你的資料庫名稱（例如 `my_blog_db`）
    - DATABASE_USER: 你的資料庫用戶名
    - DATABASE_PASSWORD: 你的資料庫密碼

6. **應用數據遷移**：
    ```bash
    python3 manage.py migrate
    ```

7. **加載初始 JSON 數據到資料庫**：
    ```bash
    python manage.py loaddata initial_data.json
    ```

8. **運行開發伺服器**：
    ```bash
    python3 manage.py runserver
    ```

## 技術說明

- 利用 Django 框架使用 FBV 與 CBV 處理不同的操作邏輯讓代碼有更多的擴充性與良好架構性。
- 選擇 MySQL 當作我的資料庫，在理財管理系統利用到了 CRUD 功能，展示了我對資料庫的基本操作，並且使用了 ORM 進行資料庫的操作，且有（one to one）、（one to many）與（many to many）的設計架構。
- 利用 Django 的 Session 機制去實現稍後觀看清單的功能，因為它簡單且與 Django 框架深度整合。
- 使用 DTL (Django Template Language) 去呈現動態網頁，讓使用者體驗更加良好。
- 使用 Django 內建 Form 表單功能去實現部落格留言與現金股票庫存表單，在設計上有更好的結構性。
- 在美金匯率與股票價格使用了第三方 API 做串接，以達成即時更新的功能。

##

