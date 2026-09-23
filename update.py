import urllib.request

SOURCES = [
    "https://raw.githubusercontent.com/drmlive/sliv-live-events/refs/heads/main/sonyliv.m3u",
    "https://raw.githubusercontent.com/doctor-8trange/zyphx8/refs/heads/main/data/fancode.m3u"
]

output = ["#EXTM3U"]

for url in SOURCES:
    try:
        data = urllib.request.urlopen(url, timeout=30).read().decode("utf-8")
        lines = data.splitlines()

        for line in lines:
            line = line.strip()

            if line and line != "#EXTM3U":
                output.append(line)

        print("Updated:", url)

    except Exception as e:
        print("Error:", url, e)

with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write("\n".join(output) + "\n")

print("Merged playlist created successfully.")
