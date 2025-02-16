# BuysideWithReactExpo (English ver below)

基於 React Native 和 Expo 開發的行動應用程式，主要提供價格查詢與比較服務。

## 功能特點

- 使用者認證系統 (登入/註冊)
- 獲得當日菜價   (開發中)
- 菜價搜尋與收藏  (開發中)
- 個人檔案管理    (開發中)
- 食材建立與管理  (開發中)
- 分頁式導航      (開發中)

## 技術架構

- **前端框架**: React Native 與 Expo
- **導航系統**: Expo Router
- **樣式系統**: TailwindCSS + NativeWind
- **認證機制**: 基於 JWT 實作
- **後端整合**: 與 Golang RESTful API 串接

## 環境需求

- Node.js (v16 或更高版本)
- npm 或 yarn
- Expo CLI
- iOS 模擬器 (macOS) 或 Android 模擬器

## 安裝步驟

1. 複製專案：

```bash
git clone [repository-url]
cd buysideWithReactExpo
```

2. 安裝相依套件：

```bash
npm install
# 或
yarn install
```

3. 啟動開發伺服器：

```bash
npx expo start
```

## 專案結構

```
buysideWithReactExpo/
├── app/                   # 主要應用程式畫面和導航
│   ├── (auth)/           # 登入與註冊相關畫面
│   ├── (tabs)/           # 分頁導航畫面
│   └── search/           # 搜尋功能
├── assets/               # 靜態資源 (圖片、字體)
├── components/           # 可重複使用的 UI 元件
├── config/               # 設定檔
├── constants/            # 常數值和主題設定
├── hooks/                # 自訂 React Hooks
└── scripts/             # 建置和工具腳本
```

## 可用指令

- `npx expo start` - 啟動 Expo 開發伺服器
- `npm run ios` - 在 iOS 模擬器中啟動應用
- `npm run android` - 在 Android 模擬器中啟動應用
- `npm run web` - 在網頁瀏覽器中啟動應用

## 開發指南

### 導航系統

使用 Expo Router 處理導航，結構如下：

- Stack 導航用於認證流程
- Tab 導航用於主應用程式流程
- Modal 導航用於額外畫面

### 認證流程

應用程式實作完整的認證流程，包含：

- 登入
- 註冊
- 密碼重設 (計畫中)

### 自定義元件

主要的自定義元件包括：

- FormField: 表單輸入元件 (SignIn SignOut)
- - CustomButton: 客製化按鈕
- TabIconConfig: 分頁導航欄

## 聯絡方式

https://github.com/willie9011


---



# BuysideWithReactExpo

A mobile application built with React Native and Expo for price finding and comparison services, focused on daily food prices.

## Features

- User Authentication (Login/Register)
- Daily Ingredient Price Updates (In Development)
- Ingredient Price Search and Bookmarking (In Development)
- Profile Management (In Development)
- Food Ingredient Management (In Development)
- Tab-based Navigation (In Development)

## Tech Stack

- **Frontend Framework**: React Native with Expo
- **Navigation**: Expo Router
- **Styling**: TailwindCSS + NativeWind
- **Authentication**: JWT Implementation
- **Backend Integration**: RESTful API with Golang

## Prerequisites

- Node.js (v16 or higher)
- npm or yarn
- Expo CLI
- iOS Simulator (for Mac) or Android Emulator

## Installation

1. Clone the repository:

```bash
git clone [repository-url]
cd buysideWithReactExpo
```

2. Install dependencies:

```bash
npm install
# or
yarn install
```

3. Start the development server:

```bash
npx expo start
```

## Project Structure

```
buysideWithReactExpo/
├── app/                   # Main application screens and navigation
│   ├── (auth)/           # Authentication related screens
│   ├── (tabs)/           # Tab navigation screens
│   └── search/           # Search functionality
├── assets/               # Static assets (images, fonts)
├── components/           # Reusable UI components
├── config/               # Configuration files
├── constants/            # Constant values and theme
├── hooks/                # Custom React hooks
└── scripts/             # Build and utility scripts
```

## Available Scripts

- `npx expo start` - Start the Expo development server
- `npm run ios` - Start the app in iOS simulator
- `npm run android` - Start the app in Android emulator
- `npm run web` - Start the app in web browser

## Development Guide

### Navigation

Navigation is handled by Expo Router with the following structure:

- Stack navigation for auth flow
- Tab navigation for main app flow
- Modal navigation for additional screens

### Authentication Flow

The app implements a complete authentication flow with:

- Sign In
- Sign Up
- Password Reset (planned)

### Custom Components

Key custom components include:

- FormField: Reusable form input component
- CustomButton: Standardized button component
- TabIconConfig: Custom tab navigation icons

## Contact

https://github.com/willie9011
