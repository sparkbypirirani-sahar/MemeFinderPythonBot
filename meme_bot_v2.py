#!/usr/bin/env python
# coding: utf-8

# In[29]:


from rich.console import Console
from rich.table import Table
from rich.text import Text
import requests

console = Console()

url = "https://api.geckoterminal.com/api/v2/networks/bsc/pools"
params = {
    "include": "base_token,quote_token",
    "page": "1"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    pools = data.get("data", [])

    table = Table(title="🚀 استخرهای داغ با USDT - بررسی تغییر قیمت", show_lines=True,
                  #expand=True,
    pad_edge=True)

  
    table.add_column("📈 ۵m", style="bold" , min_width=17, max_width=17)
    table.add_column("📊 حجم ۲۴س", style="green" , min_width=17, max_width=17)
    table.add_column("💧 نقدینگی", style="magenta" , min_width=17, max_width=17)
    table.add_column("🪙 توکن", style="cyan", justify="right" , min_width=17, max_width=17)
    

    for pool in pools:
        attrs = pool["attributes"]
        name = attrs.get("name", "Unknown")
        liquidity = float(attrs.get("reserve_in_usd", 0) or 0)
        volume_24h = float(attrs.get("volume_usd", {}).get("h24", 0) or 0)
        change_data = attrs.get("price_change_percentage", {})
        change_m5 = change_data.get("m5", None)

        if not change_m5:
            continue

        try:
            change_val = float(change_m5)
            change_text = Text(f"{change_val:.2f}%")
            change_text.stylize("green" if change_val > 0 else "red")
        except:
            change_text = Text("ندارد", style="grey50")

        if liquidity > 110000 and volume_24h > 1000000:
            table.add_row(
                name,
                f"${liquidity:,.0f}",
                f"${volume_24h:,.0f}",
                change_text
            )

    console.print(table)
else:
    console.print(f"[red]❌ خطا در دریافت اطلاعات: {response.status_code}[/red]")


# In[30]:


from rich.console import Console
from rich.table import Table
from rich.text import Text
import requests

console = Console()

url = "https://api.geckoterminal.com/api/v2/networks/bsc/pools"
params = {
    "include": "base_token,quote_token",
    "page": "1"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    pools = data.get("data", [])

    table = Table(
        title="🚀 استخرهای داغ با USDT - بررسی تغییر قیمت",
        show_lines=True,
        pad_edge=True
    )

    # تنظیم دقیق و هماهنگ ستون‌ها
    table.add_column("📈 ۵m", style="bold", min_width=17, max_width=17, justify="center")
    table.add_column("📊 حجم ۲۴س", style="green", min_width=17, max_width=17, justify="center")
    table.add_column("💧 نقدینگی", style="magenta", min_width=17, max_width=17, justify="center")
    table.add_column("🪙 توکن", style="cyan", justify="right", min_width=17, max_width=17)

    for pool in pools:
        attrs = pool["attributes"]
        name = attrs.get("name", "Unknown")
        liquidity = float(attrs.get("reserve_in_usd", 0) or 0)
        volume_24h = float(attrs.get("volume_usd", {}).get("h24", 0) or 0)
        change_data = attrs.get("price_change_percentage", {})
        change_m5 = change_data.get("m5", None)

        if not change_m5:
            continue

        try:
            change_val = float(change_m5)
            change_text = Text(f"{change_val:.2f}%")
            change_text.stylize("green" if change_val > 0 else "red")
        except:
            change_text = Text("ندارد", style="grey50")

        if liquidity > 110000 and volume_24h > 1000000:
            table.add_row(
                change_text,                        # 📈 ۵m
                f"${volume_24h:,.0f}",              # 📊 حجم ۲۴س
                f"${liquidity:,.0f}",               # 💧 نقدینگی
                name                                # 🪙 توکن
            )

    console.print(table)
else:
    console.print(f"[red]❌ خطا در دریافت اطلاعات: {response.status_code}[/red]")


# In[167]:


from rich.console import Console
from rich.table import Table
from rich.text import Text
import requests
import time
from datetime import datetime

console = Console()

def style_change(value):
    try:
        val = float(value)
        text = Text(f"{val:.2f}%")
        text.stylize("green" if val > 0 else "red")
        return text
    except:
        return Text("ندارد", style="grey50")

def fetch_and_display():
    url = "https://api.geckoterminal.com/api/v2/networks/bsc/pools"
    params = {
        "include": "base_token,quote_token",
        "page": "1"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        pools = data.get("data", [])

        #table = Table(
            #title="🚀 تغییرات قیمتی استخرهای داغ USDT",
            #show_lines=True,
            #pad_edge=True
        #)
        table = Table(
            title=f"🚀 تغییرات قیمتی استخرهای داغ USDT | {datetime.now().strftime('%H:%M:%S')}",
            show_lines=True,
            pad_edge=True
        )
        # تعریف ستون‌ها
        table.add_column("📈 ۵m"     ,style="green"    , justify="center", min_width=8, max_width=20)
        table.add_column("📈 ۱۵m"    ,style="magenta"  , justify="center", min_width=8, max_width=9)
        table.add_column("📈 ۱h"     ,style="cyan"     , justify="center", min_width=8, max_width=9)
        table.add_column("📈 ۶h"     ,style="green"    , justify="center", min_width=8, max_width=9)
        table.add_column("📈 ۲۴h"    ,style="magenta"  , justify="center", min_width=8, max_width=9)
        table.add_column("📊 حجم ۲۴س",style="green"    , justify="center", min_width=14, max_width=17)
        table.add_column("💧 نقدینگی"   ,style="magenta" , justify="center", min_width=14, max_width=17)
        table.add_column("🪙 توکن "    ,style="cyan"    , justify="left", min_width=1, max_width=17, no_wrap=True)      
        
        
        for pool in pools:
            attrs = pool["attributes"]
            name = attrs.get("name", "Unknown")
            liquidity = float(attrs.get("reserve_in_usd", 0) or 0)
            volume_24h = float(attrs.get("volume_usd", {}).get("h24", 0) or 0)
            change_data = attrs.get("price_change_percentage", {})

            if liquidity > 110000 and volume_24h > 1000000:
                table.add_row(
                    name
                    ,f"${liquidity:,.0f}"
                    ,f"${volume_24h:,.0f}"
                    ,style_change(change_data.get("m5"))
                    ,style_change(change_data.get("m15"))
                    ,style_change(change_data.get("h1"))
                    ,style_change(change_data.get("h6"))
                    ,style_change(change_data.get("h24")),
                )

        console.print(table)
    else:
        console.print(f"[red]❌ خطا در دریافت اطلاعات: {response.status_code}[/red]")
# اجرا فقط یک‌بار:        
fetch_and_display()
  # حلقه رفرش خودکار هر ۳ دقیقه
#while True:
    #console.clear()
    #console.print(f"⏰ آخرین بروزرسانی: {datetime.now().strftime('%H:%M:%S')}\n", style="bold blue")
    #fetch_and_display()
    #time.sleep(180)  # 180 ثانیه = 3 دقیقه


# In[169]:


import csv
from rich.console import Console
from rich.table import Table
from rich.text import Text
import requests
from datetime import datetime

console = Console()
output_file = "hot_pools.csv"  # ← فایل خروجی

def style_change(value):
    try:
        val = float(value)
        text = Text(f"{val:.2f}%")
        text.stylize("green" if val > 0 else "red")
        return text, f"{val:.2f}%"
    except:
        return Text("ندارد", style="grey50"), "ندارد"

def fetch_and_save():
    url = "https://api.geckoterminal.com/api/v2/networks/bsc/pools"
    params = {
        "include": "base_token,quote_token",
        "page": "1"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        pools = data.get("data", [])

        table = Table(
            title=f"🚀 تغییرات قیمتی استخرهای داغ USDT | {datetime.now().strftime('%H:%M:%S')}",
            show_lines=True,
            pad_edge=True
        )

        table.add_column("📈 ۵m", justify="center")
        table.add_column("📈 ۱۵m", justify="center")
        table.add_column("📈 ۱h", justify="center")
        table.add_column("📈 ۶h", justify="center")
        table.add_column("📈 ۲۴h", justify="center")
        table.add_column("📊 حجم ۲۴س", style="green", justify="center")
        table.add_column("💧 نقدینگی", style="magenta", justify="center")
        table.add_column("🪙 توکن", style="cyan", justify="left", min_width=20)

        rows_for_csv = []

        for pool in pools:
            attrs = pool["attributes"]
            name = attrs.get("name", "Unknown")
            liquidity = float(attrs.get("reserve_in_usd", 0) or 0)
            volume_24h = float(attrs.get("volume_usd", {}).get("h24", 0) or 0)
            change_data = attrs.get("price_change_percentage", {})

            if liquidity > 110000 and volume_24h > 1000000:
                # دریافت متن رنگی و ساده برای CSV
                m5_text, m5_val = style_change(change_data.get("m5"))
                m15_text, m15_val = style_change(change_data.get("m15"))
                h1_text, h1_val = style_change(change_data.get("h1"))
                h6_text, h6_val = style_change(change_data.get("h6"))
                h24_text, h24_val = style_change(change_data.get("h24"))

                # نمایش در جدول
                table.add_row(
                    name,
                    f"${liquidity:,.0f}",
                    f"${volume_24h:,.0f}",
                    m5_text,
                    m15_text,
                    h1_text,
                    h6_text,
                    h24_text,
                )

                # ذخیره برای فایل CSV
                rows_for_csv.append({
                    "token": name,
                    "liquidity": liquidity,
                    "volume_24h": volume_24h,
                    "change_5m": m5_val,
                    "change_15m": m15_val,
                    "change_1h": h1_val,
                    "change_6h": h6_val,
                    "change_24h": h24_val,
                })

        console.print(table)

        # ذخیره در فایل CSV
        with open(output_file, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=rows_for_csv[0].keys())
            writer.writeheader()
            writer.writerows(rows_for_csv)

        console.print(f"\n✅ داده‌ها با موفقیت در فایل [bold green]{output_file}[/bold green] ذخیره شدند.")
    else:
        console.print(f"[red]❌ خطا در دریافت اطلاعات: {response.status_code}[/red]")

# اجرای تابع
fetch_and_save()


# In[ ]:




