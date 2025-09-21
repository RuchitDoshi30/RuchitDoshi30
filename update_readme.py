import datetime

# Load your template README
with open("README_TEMPLATE.md", "r", encoding="utf-8") as f:
    template = f.read()

# Replace placeholders with dynamic data
new_readme = template.replace("{{last_updated}}", datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"))

# Save as README.md
with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_readme)
