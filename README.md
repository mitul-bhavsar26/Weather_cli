# weather_cli

This small script fetches current weather from OpenWeather. Important: do NOT commit your API key.

Usage

1. Obtain an OpenWeather API key.
2. Set it in your environment:

```bash
export OPENWEATHER_API_KEY="YOUR_KEY_HERE"
# optionally set a default city
export OPENWEATHER_DEFAULT_CITY="Cleveland"
```

Run:

```bash
python3 weather.py [City Name]
```

If no city is provided, it will use the `OPENWEATHER_DEFAULT_CITY` environment variable or default to `Cleveland`.

Remediation if you accidentally committed a key

- Rotate the key in the OpenWeather dashboard immediately (revoke and recreate).
- Remove the key from your repo history. Recommended tools:
  - BFG Repo-Cleaner: https://rtyley.github.io/bfg-repo-cleaner/
  - git filter-repo: https://github.com/newren/git-filter-repo

Example with BFG (after installing):

```bash
# remove the literal string
bfg --replace-text <(printf "cdd236dc19ab07035a60334675d12174==>***REMOVED***\n")
git reflog expire --expire=now --all && git gc --prune=now --aggressive
```

Or use `git filter-repo` to remove file paths or secrets; follow the tool docs.

If you want, I can help run the history-cleanup commands (I will not run destructive commands without your confirmation).
