---
title: IDE Setup
slug: brax/ide-setup
url: https://sbox.game/learn/brax/ide-setup
author: Braxnet
author_slug: brax
difficulty: Beginner
topic: Coding
content_type: Text
rating: 4
views: 1358
upvotes: 14
downvotes: 0
updated: 'Updated

  13 Days Ago'
summary: How to set up your IDE so Intellisense/lookups work
scraped_at: '2026-06-04T10:02:31Z'
---

# IDE Setup

> How to set up your IDE so Intellisense/lookups work

If you don’t set up your IDE (like Visual Studio or JetBrains Rider) correctly, you might run into issues like missing IntelliSense and missing references. Here’s how to set it up properly.

# **Visual Studio**

1. Make sure you have the latest version of [Visual Studio](https://visualstudio.microsoft.com/downloads/) installed, at the time of writing, Visual Studio 2026 is required.
2. Install the `.NET desktop development` and `ASP.Net and web development` workload during installation, via the Visual Studio Installer, or go to `Tools -> Get Tools and Features` in Visual Studio.
3. Just to be sure, install the latest [.NET SDK](https://dotnet.microsoft.com/en-us/download/dotnet/10.0) as well. At the time of writing, s&box uses .NET 10. You may need to download both the SDK and the Runtime.

**Common Issues**

- **Missing IntelliSense/References**: Open the solution file (`.slnx`) located in your project folder. You can do this from the `Project -> Open Solution` menu in the s&box editor.
- **slnx file opens as text**: Your Visual Studio installation is too old. Update to 2026 or later.

# **JetBrains Rider**

1. Make sure you have the latest version of [JetBrains Rider](https://www.jetbrains.com/rider/download/) installed.
2. Install the latest [.NET SDK](https://dotnet.microsoft.com/en-us/download/dotnet/10.0) as well. At the time of writing, s&box uses .NET 10. You may need to download both the SDK and the Runtime.
3. Open the solution file (`.slnx`) located in your project folder. You can do this from the `Project -> Open Solution` menu in the s&box editor.

# **Visual Studio Code**

Even if you follow the steps below, Visual Studio Code might still not work perfectly with s&box development. For the best experience, consider using Visual Studio or JetBrains Rider.

1. Make sure you have the latest version of [Visual Studio Code](https://code.visualstudio.com/download) installed.
2. Install the latest [.NET SDK](https://dotnet.microsoft.com/en-us/download/dotnet/10.0) as well. At the time of writing, s&box uses .NET 10. You may need to download both the SDK and the Runtime.
3. Install the `C#` and `C# Dev Kit` extensions from the extensions tab.
4. Open your s&box project folder in Visual Studio Code using `File -> Open Folder...`. Do not open the `code` folder, you want to open the root project folder.
5. If the solution file (`.slnx`) does not open automatically, open it manually from the dropdown in the bottom left corner of the window.

**Common Issues**

- **Missing IntelliSense/References**: Make sure you have the `C#` and `C# Dev Kit` extensions installed. Make sure you have the latest .NET SDK installed. Open the solution properly as described above.
