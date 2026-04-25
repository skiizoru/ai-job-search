# CV Templates and Tailoring Guide

## Template: LaTeX moderncv (Banking Style)

All CVs use the moderncv LaTeX package with the "banking" style and "blue" color scheme.

**Output file:** `cv/main_<company>.tex`
**Compile with:** pdflatex (not xelatex)
**Master reference:** `cv/main_example.tex` (comprehensive CV with all competencies, experience, and achievements - use as source when building targeted CVs)

## Document Structure

```latex
\documentclass[11pt,a4paper,sans]{moderncv}
\moderncvstyle{banking}
\moderncvcolor{blue}

\usepackage[utf8]{inputenc}
\usepackage{hyperref}
\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    filecolor=magenta,
    urlcolor=blue,
    pdftitle={[YOUR_NAME] - CV},
    pdfpagemode=FullScreen,
}
\usepackage[scale=0.77]{geometry}
\usepackage{import}

% Personal data
\name{[FIRST_NAME]}{[LAST_NAME]}
\address{Auckland, New Zealand}{}{}
\phone[mobile]{[YOUR_PHONE]}
\email{[YOUR_EMAIL]}
\extrainfo{\href{[YOUR_LINKEDIN_URL]}{LinkedIn}}

\begin{document}
\makecvtitle

% 1. Profile statement (1-3 sentences, tailored per role)
% 2. Core Competencies section
% 3. Professional Experience section
% 4. Education section
% 5. References

\end{document}
```

## Profile Statement Templates

This is the most important section to customize. Write 4-6 lines as an elevator pitch explaining why you're qualified for *this specific role*.

### For GIS / Spatial Analyst roles:
> Planning and policy professional with 10+ years of experience in strategic research, spatial analysis and evidence-based policy development. Brings practical GIS skills (ArcGIS, QGIS) developed through urban planning practice, complemented by active development of geospatial capabilities through Esri training. Experienced in translating spatial data into clear analytical outputs for decision-makers. Applies AI tools including Claude Code daily to enhance research workflows and output quality.

### For Policy Analyst / Research Analyst roles:
> Strategic policy professional with 10+ years of progressive experience in urban planning, policy research and analysis. Proven ability to synthesise complex research into clear, evidence-based recommendations for senior decision-makers and elected members. Led the city centre workstream of Plan Change 78 from concept to operative — one of Auckland Council's most significant statutory planning processes. Seeking to apply rigorous research, analysis and policy skills in a new sector context.

### For Urban / Town Planner roles (international):
> Senior policy planner with 10+ years of experience in strategic urban planning and policy development at Auckland Council, New Zealand's largest local authority. Led city centre provisions for Plan Change 78 from concept through to made operative, coordinating multi-party statutory processes and delivering complex policy outcomes. Skilled in comparative international planning research, spatial analysis and stakeholder engagement at decision-maker level. Available for international relocation.

### For Planning Consultant / Advisory roles:
> Experienced urban planning and policy professional with a strong record of leading complex, multi-party statutory planning processes for one of the Southern Hemisphere's largest cities. Combines deep policy analysis and statutory planning expertise with practical GIS skills and a proactive approach to AI-assisted research and workflow automation. Brings a consultancy mindset to public sector experience — focused on outcomes, evidence and clear deliverables.

### For Sustainability / ESG roles:
> Policy and research professional with 10+ years of experience in environmental planning, land use policy and sustainability analysis. Background in resource management law, sustainable development frameworks and comparative policy research. Experienced in synthesising complex regulatory and environmental information into evidence-based recommendations. Actively developing geospatial capabilities to complement policy skills.

## Section-by-Section Tailoring

### Core Competencies / Skills Section (Best Practice)
Reorder and emphasize based on the role. Use bold category labels.

List **5-6 key competencies** in bullet format, tailored to the specific job. Standard competency pool to draw from:

- **Policy Research & Analysis:** Comparative research across NZ and international contexts; synthesising complex legislative and policy frameworks into evidence-based recommendations
- **Strategic Planning:** Led Plan Change 78 city centre workstream from concept to operative; precinct masterplanning and scenario planning
- **Spatial & GIS Analysis:** ArcGIS and QGIS for spatial analysis and map-based analysis; Esri WebGIS training in progress
- **Project Management:** Managed multi-party plan change processes including consultant procurement, programme management and statutory timeframes
- **Stakeholder Engagement:** Prepared briefings and presentations for elected members, technical specialists and senior decision-makers
- **Written Communication:** Policy memos, planning assessments, technical reports; consistently translates complex regulatory content for non-specialist audiences
- **AI & Digital Workflow:** Daily use of Claude Code, ChatGPT, Gemini for research, drafting and content creation; built productivity tools using AI-assisted coding
- **Regulatory Interpretation:** Deep expertise in Auckland Unitary Plan, RMA and NPS-UD; experience applying overlapping statutory frameworks

### Education
- List BPlan(Hons) with institution and dates
- Note Esri WebGIS MOOC as in progress
- For GIS/geospatial roles, note planned formal GIS study (2027)
- Keep brief for senior planning roles — credentials are assumed

### Professional Experience
- Use 4-5 bullets for Senior Policy Planner role, 3 for Intermediate Planner, 2 for Assistant Planner
- Lead with Plan Change 78 and the concept-to-operative achievement as the anchor bullet
- Reframe bullets to match the target role's language and priorities
- **Emphasize measurable scope** where possible: "Auckland's largest city", "multi-party statutory process", "from concept to operative"

### Handling the Career Transition
When applying outside of planning:
- Frame the move as deliberate and forward-looking: "Seeking to apply transferable research and analytical skills in [sector]"
- Lead with the skills that transfer (research, analysis, written communication, project management, AI tools, spatial thinking)
- Acknowledge the pivot directly in the cover letter — don't obscure it

### References
- End with: "References available upon request."
- Do not attach reference letters

## Page Budget - Hard 2-Page Limit

| Section | Max budget |
|---------|-----------|
| Profile statement | 4-5 lines |
| Core competencies | 5-6 items, each 1-2 lines |
| Senior Policy Planner role | 4-5 bullets |
| Intermediate Planner role | 3 bullets |
| Assistant Planner role | 2 bullets |
| Education | 2 entries |
| References | "Available upon request." (single line) |

**If in doubt, cut rather than squeeze.**

## Recommended Section Order

**For planning / policy / research roles:**
1. Profile statement / elevator pitch
2. Core Competencies
3. Professional Experience (reverse chronological)
4. Education
5. References

**For GIS / spatial / technical roles:**
1. Profile statement / elevator pitch
2. Core Competencies (lead with GIS, spatial analysis, AI tools)
3. Education (note GIS training prominently)
4. Professional Experience
5. References
