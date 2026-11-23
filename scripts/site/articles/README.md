# Brief: how-to articles for coutume.app

Coutume is a free habit tracker for iPhone (not out yet, "coming soon to the App Store"), by Wibeset, a small studio in Canada. Its site has a page of 40 habit ideas; each idea becomes a short how-to article, in English, French and Spanish. You write the content of some of them as Python data; a generator (not yours) turns the data into HTML pages.

## Output

Write ONE Python file at the path given in your task, defining `ARTICLES = [dict(...), ...]`, with exactly the schema of the model article in `example.py` (same folder — read it first, and match its tone, length and structure closely). The file must import nothing and run with `python3 -I file.py` without error.

Fields:
- `key`, `theme`, `kind` ("build" or "quit"), `health` (None, or "steps", "exercise", "mindful", "water" — only if Apple Health can fill that habit in), as given in your task.
- `en`, `fr` and `es`, each with:
  - `slug`: as given in your task for `en` and `fr`; don't change those. For `es`, write your own: lowercase ASCII words joined by hyphens, no accents (beber-mas-agua).
  - `crumb`: the idea's short name (3–6 words), used in breadcrumbs and lists.
  - `title`: `How to … — Coutume` / `Comment … — Coutume` / `Cómo … — Coutume`, under ~70 characters before the dash if you can.
  - `desc`: meta description, 140–165 characters, concrete.
  - `h1`: `How to …` / `Comment …` / `Cómo …`, no final period.
  - `lede`: 1–2 sentences, a fresh angle on why people struggle with it.
  - `why`: 2–3 sentences: why it’s worth it. Practical, not preachy.
  - `steps`: 4–6 strings, each `<strong>Short imperative.</strong> One or two sentences.` Concrete, specific, useful even to someone who will never install the app.
  - `hard`: exactly 3 strings, `<strong>The obstacle.</strong> What to do.`
  - `track`: 1–2 sentences on how to set it up in Coutume, using ONLY the facts below.
  - `note`: "" or one sentence of caution when health, medication or money advice calls for it (e.g. "Follow your doctor’s or pharmacist’s instructions for any medication."). Keep it short.
- Allowed HTML inside strings: `<strong>`, `<em>`, and nothing else (no links).

## What Coutume does (the only facts you may use in `track`)

- A **habit to build** is either a simple check, or a count toward a daily target (8 glasses). Tap its ring to log; touch and hold the ring to enter a number or undo.
- A **habit to quit** is kept by default: you only log the day you slip. Coutume counts the days without, the money saved and the urges resisted. A slip restarts the count of days without, never the level or the month.
- **Apple Health** (read only) can fill in four habits on its own: steps, exercise minutes, mindful minutes, water.
- Habits are **daily**. Streaks forgive one missed day per week. Eleven levels (Good intention → Legend; FR: Bonne intention → Légende), eighteen milestones, perfect days, a calendar of the month, Home Screen and Lock Screen widgets, iCloud sync, no account, free.
- Each habit has a name and an icon.
- Apple Health is called “Santé” in French and “Salud” in Spanish. The app is in French, English and Spanish.
- Do NOT mention reminders, notifications, timers, notes, weekly or custom schedules, social features, or anything not listed. For something weekly or one-off (checking accounts, cancelling subscriptions), suggest a small daily version or a habit to quit instead.

## Voice and rules

- English: Canadian/US spelling is fine ("practise" verb is OK but be consistent within an article), plain, warm, second person, short sentences. No hype, no emoji, no exclamation marks, no clichés ("game-changer", "unlock", "journey").
- French: Québec French, **tutoiement**, the same content (adapt, don't translate word for word). Use Québec words: souper (dinner), dîner (lunch), déjeuner (breakfast), courriel, magasiner, cellulaire or téléphone. Coutume is feminine ("Coutume est gratuite"). Write ordinary spaces before `? ! : ;` and inside « » — the generator adds no-break spaces. Use typographic apostrophes `’` in both languages.
- Spanish: neutral international Spanish, **tú**, the same content (adapt, don't translate word for word). A habit to build is “un hábito por crear”, a habit to quit is “un hábito por dejar”; days without = “días sin”; the levels go from “Buena intención” to “Leyenda” (the app has no Spanish yet, so translate them plainly). Use ¿ ? and ¡ ! correctly, quotes “…”.
- Curly apostrophes and quotes in English too (’ “ ”).
- No statistics, studies or numbers you aren’t sure of. No medical claims; prefer practical advice. Never shame the reader.
- Habit names inside `track` in quotes: “…” in English and Spanish, « … » in French.
- Each article stands alone; don’t refer to the other articles.
- Length: about 350–450 words per language (three languages per article), like the model.

When done, run `python3 -I <your file>` to check it loads, and `python3 -I -c "exec(open('<your file>').read()); print(len(ARTICLES))"` to check the count. Report only the file path and the count.
