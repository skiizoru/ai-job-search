# Search Queries for Job Scraper

## Target Markets
Focus is **international** — no New Zealand-based roles unless exceptional circumstances.

Priority markets (in order):
1. Nordic countries (Denmark, Sweden, Norway, Finland)
2. Canada (major cities: Toronto, Vancouver, Ottawa, Calgary)
3. Melbourne, Australia
4. Singapore

## Search Sites by Market

### Global (works across all markets)
- **linkedin.com/jobs** — best single source for international roles; use location filter per market
- **indeed.com** — global; filter by country/city

### Nordic Countries
- **jobindex.dk** — largest Danish job board (built-in CLI scraper available)
- **thelocal.se / thelocal.dk / thelocal.no** — English-language job listings in Nordic countries
- **finn.no** — Norway's main job board
- **arbetsformedlingen.se** — Sweden's national job board

### Canada
- **jobs.gc.ca** — Government of Canada jobs
- **indeed.ca** — Canadian Indeed
- **eluta.ca** — Canadian job aggregator

### Melbourne / Australia
- **seek.com.au** — Australia's largest job board
- **indeed.com.au** — Australian Indeed
- **vic.gov.au/careers** — Victorian public service roles
- **apsjobs.gov.au** — Australian federal public service

### Singapore
- **mycareersfuture.gov.sg** — official Singapore government jobs portal
- **jobstreet.com.sg** — major Singapore job board
- **indeed.com.sg** — Singapore Indeed

---

## Query Categories

### Priority 1: GIS / Geospatial Roles
These align with the planned career direction (GIS study, spatial analysis).

```
site:linkedin.com/jobs "GIS Analyst" Denmark OR Sweden OR Norway OR Canada OR Melbourne OR Singapore
site:linkedin.com/jobs "Spatial Analyst" Denmark OR Sweden OR Norway OR Canada OR Melbourne OR Singapore
site:linkedin.com/jobs "Geospatial Analyst" Denmark OR Sweden OR Norway OR Canada OR Melbourne OR Singapore
site:linkedin.com/jobs "GIS Technician" planning OR urban OR environment
site:seek.com.au "GIS Analyst" Melbourne
site:mycareersfuture.gov.sg "GIS" OR "Geospatial" planning
site:jobindex.dk GIS byplanlægning OR spatial
site:thelocal.se "GIS" OR "spatial analyst"
site:jobs.gc.ca "GIS" OR "geospatial" planner
```

### Priority 2: Urban Planning / Town Planning (International)
Direct planning experience — strongest technical match, good bridge role.

```
site:linkedin.com/jobs "Urban Planner" Denmark OR Sweden OR Norway OR Canada OR Melbourne OR Singapore
site:linkedin.com/jobs "Town Planner" Melbourne OR Singapore OR Canada
site:linkedin.com/jobs "City Planner" Canada OR Australia
site:linkedin.com/jobs "Planning Consultant" Arup OR WSP OR Stantec OR Jacobs
site:linkedin.com/jobs "Policy Planner" OR "Planning Researcher" international
site:seek.com.au "Urban Planner" OR "Town Planner" Melbourne
site:mycareersfuture.gov.sg "Urban Planner" OR "Planning"
site:jobindex.dk byplanlægger OR planlægger
site:jobs.gc.ca "Urban Planner" OR "City Planner"
```

### Priority 3: Policy Analyst / Research Analyst
Strong transferable match — research, analysis, written communication.

```
site:linkedin.com/jobs "Policy Analyst" environment OR planning OR urban Denmark OR Sweden OR Norway OR Canada OR Melbourne OR Singapore
site:linkedin.com/jobs "Policy Advisor" OR "Policy Adviser" urban OR environment OR sustainability
site:linkedin.com/jobs "Research Analyst" planning OR urban OR policy
site:linkedin.com/jobs "Planning Analyst" OR "Urban Analyst"
site:seek.com.au "Policy Analyst" Melbourne
site:jobs.gc.ca "Policy Analyst" environment OR urban OR housing
site:mycareersfuture.gov.sg "Policy Analyst" OR "Research Analyst"
site:jobindex.dk "policy" OR "analyse" OR "forsker" byplanlægning
```

### Priority 4: Adjacent / Transferable Roles
Broader net — transferable skills from planning into adjacent sectors.

```
site:linkedin.com/jobs "Sustainability Analyst" OR "ESG Analyst" policy OR planning
site:linkedin.com/jobs "Transport Planner" Denmark OR Sweden OR Norway OR Canada OR Melbourne OR Singapore
site:linkedin.com/jobs "Urban Data Analyst" OR "City Data"
site:linkedin.com/jobs "Smart Cities" analyst OR planner OR researcher
site:linkedin.com/jobs "International Development" urban OR housing OR planning
site:linkedin.com/jobs "Planning Technician" GIS OR spatial
site:seek.com.au "Environmental Planner" OR "Transport Planner" Melbourne
site:linkedin.com/jobs "Arup" OR "WSP" OR "Stantec" planner analyst
```

---

## Location Filter

When evaluating results, filter as follows:

| Tier | Areas | Status |
|------|-------|--------|
| **Preferred** | Copenhagen, Stockholm, Oslo, Helsinki, Toronto, Vancouver, Melbourne, Singapore | Apply |
| **Acceptable** | Other major Nordic cities, Ottawa, Calgary, Sydney, Brisbane | Apply |
| **Consider** | Other Canadian cities, other Australian cities, remote roles with international teams | Flag to user |
| **Exclude** | New Zealand (any city) | Skip unless exceptional |
| **Remote** | Roles explicitly listed as remote-friendly with international teams | Apply |

---

## Date Filter

Only include jobs posted within the last 14 days, or with an application deadline that has not yet passed. If a posting date cannot be determined, include it but flag as "date unknown".

---

## Adapting Queries

If the user specifies a focus area or market, select queries from the matching category and generate 2-3 custom queries for that focus. For example:
- "/scrape nordic" → Priority 1 + 2 Nordic queries + custom Nordic-specific searches
- "/scrape gis" → All Priority 1 queries across all markets
- "/scrape canada" → All priorities filtered to Canadian sites and locations

---

## Notes on Built-in Scraper Tools

The built-in CLI scrapers (jobindex, jobbank, jobdanmark, jobnet) target the **Danish job market** — which is relevant given Denmark is a priority market. Use these for Danish searches; use manual LinkedIn/Indeed searches or Google `site:` queries for other markets.
