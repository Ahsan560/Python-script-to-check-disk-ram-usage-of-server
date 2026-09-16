import psutil

print("====================================")
print("   SYSTEM HEALTH MONITOR ACTIVE     ")
print("====================================\n")

# 1. RAM Usage Check karna
ram = psutil.virtual_memory()
ram_used_percent = ram.percent

print(f"📊 Total RAM Usage: {ram_used_percent}%")
if ram_used_percent > 85:
    print("⚠️ ALERT: RAM usage is critically high!")
else:
    print("✅ RAM status: Normal.")

print("-" * 36)

# 2. Disk / Storage Space Check karna
# '/' ka matlab hai main storage drive
disk = psutil.disk_usage('/')
disk_used_percent = disk.percent

print(f"💾 Total Disk Space Used: {disk_used_percent}%")

# 3. Decision Logic (Senior Validation Rule)
# Agar storage 80% se zyada full hai toh alert generate karo
if disk_used_percent > 80:
    print("🚨 RED ALERT: Disk space is running out! Clean logs immediately.")
else:
    print("✅ Disk status: Healthy. Plenty of space available.")

print("====================================")

