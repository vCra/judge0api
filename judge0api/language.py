class Language:
    verbose_name = None
    language_id = None


def load(client):
    headers = {"Content-Type": "application/json"}
    r = client.endpoint.get(f"{client.endpoint}/submissions/", headers=headers)
    r.raise_for_status()

    languages = []

    for l in r.json():
        language = Language()
        language.verbose_name = l["name"]
        language.language_id = l["id"]
        languages.append(language)

    return languages

