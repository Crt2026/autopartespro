
import os

env_file = '.env'
new_keys = {
    'MERCADOPAGO_PUBLIC_KEY': 'APP_USR-7383f204-12f1-436a-8752-30bd447a968b',
    'MERCADOPAGO_ACCESS_TOKEN': 'APP_USR-1312973485211827-122522-ae36793a7772f07737f5454493e33585-343776998'
}

lines = []
if os.path.exists(env_file):
    with open(env_file, 'r') as f:
        lines = f.readlines()

updated_lines = []
seen_keys = set()

for line in lines:
    key = line.split('=')[0].strip()
    if key in new_keys:
        updated_lines.append(f"{key}={new_keys[key]}\n")
        seen_keys.add(key)
    else:
        updated_lines.append(line)

for key, value in new_keys.items():
    if key not in seen_keys:
        if updated_lines and not updated_lines[-1].endswith('\n'):
            updated_lines.append('\n')
        updated_lines.append(f"{key}={value}\n")

with open(env_file, 'w') as f:
    f.writelines(updated_lines)

print("Updated .env successfully")
