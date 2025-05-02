import csv

with open("template.html", encoding="utf-8") as f:
    template = f.read()

with open("data.csv", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        html = template.replace("{{title}}", row["title"]) \
                       .replace("{{image}}", row["image"]) \
                       .replace("{{description}}", row["description"])
        filename = f'detail-{row["filename"]}.html'
        with open(filename, 'w', encoding='utf-8') as out:
            out.write(html)
