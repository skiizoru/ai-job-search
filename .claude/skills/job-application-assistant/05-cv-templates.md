# CV Templates and Tailoring Guide

## Template: LaTeX moderncv (Banking Style)

All CVs use the moderncv LaTeX package with the "banking" style and "blue" color scheme.

**Output file:** `cv/main_<company>.tex`
**Compile with:** pdflatex (not xelatex)
**Master reference:** `cv/main_example.tex` (comprehensive CV with all competencies, experience, and achievements — use as source when building targeted CVs)

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

% 1. Profile statement (tailored per role)
% 2. Core Competencies
% 3. Professional Experience
% 4. Volunteer Experience (include for roles valuing leadership/coaching)
% 5. Education
% 6. Professional Memberships
% 7. Languages
% 8. References

\end{document}
```

## Profile Statement Templates

This is the most important section to customize. It appears right after `\makecvtitle`. Write 5–7 lines as a concise, compelling elevator pitch explaining why you're qualified for *this specific role*.

---

**For senior policy planning roles (local/central government):**
> Senior urban policy planner with 10 years of experience at Auckland Council, specialising in plan change development, statutory hearings, and city centre policy frameworks. Proven track record leading complex, multi-disciplinary plan changes from concept through to operative — including acting as expert witness before Independent Commissioners — with a consistent record of quality and no appeals. Skilled at translating spatial analysis, technical modelling, and international planning precedent into clear, defensible policy positions. Brings complementary skills in GIS-based spatial analysis and generative AI tooling, and strong experience in stakeholder and iwi engagement across diverse and politically sensitive environments.

---

**For spatial / GIS policy analyst roles:**
> Urban policy planner with 10 years of applied GIS and spatial analysis experience, specialising in city-wide and precinct-level spatial analysis to inform planning policy and land use decisions. Combines hands-on ESRI ArcGIS and QGIS capability with deep policy expertise in urban planning frameworks and statutory processes. Experienced reviewing technical modelling and translating findings into policy-ready positions. Brings emerging expertise in environmental remote sensing and a track record building AI-powered tools — including workflows using Claude Code and NotebookLM — to accelerate spatial and policy workflows.

---

**For GovTech / spatial technology / research policy roles:**
> Senior urban planner and applied technologist with 10 years of policy and regulatory experience, and a self-directed track record integrating generative AI into complex policy work. Built AI-powered planning tools using Claude Code, NotebookLM, and ChatGPT to accelerate document synthesis, policy drafting, and project management in a statutory environment. Combines deep domain knowledge of urban planning and resource management with practical GIS skills and an ability to translate technical findings for non-specialist audiences. Seeking roles at the intersection of policy, spatial analysis, and technology — particularly where AI or GovTech is being applied to built environment or regulatory challenges.

---

**For planning consultancy roles:**
> Senior urban policy planner with 10 years of public sector experience, including end-to-end leadership of complex plan changes, expert witness work before Independent Commissioners, and specialist policy advice to elected members and resource consent planners. Brings deep working knowledge of the Auckland Unitary Plan and New Zealand's RMA framework, with skills that transfer directly to development plan policy, statutory plan-making, and planning appeals in comparable common law jurisdictions. Strong record in stakeholder engagement, technical report writing, GIS-based spatial analysis, and multi-disciplinary project coordination.

---

**For research / policy analyst roles (think tanks, research institutes):**
> Urban policy analyst with 10 years of applied research, policy synthesis, and statutory planning experience, specialising in city centre planning, densification policy, and built environment outcomes. Strong track record translating complex spatial data, technical modelling, and legislative frameworks into clear, evidence-based policy positions. Experienced preparing section 32 evaluations, legal memos, and hearing evidence — work that demands the same analytical rigour as policy research. Brings an applied interest in generative AI tools and spatial technology, and a commitment to producing policy that is both rigorous and practically implementable.

---

## Section-by-Section Tailoring

### Core Competencies / Skills Section
Reorder and emphasise based on the role. Use bold category labels. List **5 key competencies**, each 1–2 lines, tailored to the specific job.

Competency pool to draw from:
- **Policy Development & Plan Change Management** — end-to-end statutory process leadership
- **Statutory Planning & Hearings** — section 32, hearing reports, expert witness, expert conferencing
- **Spatial Analysis & GIS** — ArcGIS, QGIS, city-wide and precinct-level spatial analysis
- **Stakeholder & Iwi Engagement** — statutory consultation, elected member briefings, public engagement
- **AI-Augmented Planning Practice** — Claude Code, NotebookLM, ChatGPT; document synthesis, provision drafting, project management automation
- **Research & Policy Analysis** — policy synthesis, international precedent review, technical modelling translation
- **Project Management** — multi-disciplinary coordination, consultant procurement, statutory timeframe delivery
- **Technical Report Writing** — s32 reports, hearing evidence, legal memos, briefings for non-specialist audiences

### Professional Experience Tailoring
- **For policy/government roles:** Lead with plan change leadership and expert witness experience; highlight coordination of specialist disciplines and stakeholder engagement
- **For GIS/spatial roles:** Lead with spatial analysis work on PC78; highlight technical modelling review; mention remote sensing enrolment
- **For tech/GovTech roles:** Lead with AI tooling; position the planning background as domain expertise applied through technology
- **For consultancy:** Emphasise breadth of statutory process experience; highlight ability to advise both council and applicant contexts (PC115 collaboration is useful here)

### Education
For all roles: list B.Planning(Hons) and the Massey Certificate (note as enrolling July 2026). For GIS/spatial roles, give the remote sensing certificate more prominence.

### Volunteer Experience (BJJ Coaching)
Include for roles that explicitly value leadership, coaching, programme design, or adaptive instruction. Frame as: designed and delivered a structured curriculum with measurable student progression; led mixed-ability groups; progressed to black belt during the coaching period.

## Page Budget — Hard 2-Page Limit

| Section | Max budget |
|---------|-----------|
| Profile statement | 4–5 lines |
| Core competencies | 5 items, each 1–2 lines |
| Most recent role (Senior Policy Planner) | 5–6 bullets |
| Previous role (Planner/Intermediate) | 3–4 bullets |
| Earlier role (Assistant Planner) | 2 bullets |
| Volunteer (BJJ) | 2–3 lines (omit if tight) |
| Education | 2 entries |
| Memberships | 1 line |
| Languages | 1 line |
| References | "Available upon request." |

**If in doubt, cut rather than squeeze.**

## Recommended Section Order

**For policy / government / research roles:**
1. Profile statement
2. Core Competencies
3. Professional Experience
4. Volunteer Experience (if relevant)
5. Education
6. Professional Memberships
7. Languages
8. References

**For GIS / spatial / tech roles:**
1. Profile statement
2. Core Competencies
3. Professional Experience
4. Education (give remote sensing certificate visibility)
5. Professional Memberships
6. Languages
7. References

## International Terminology Mapping

When adapting for international roles, translate NZ-specific terms:

| NZ Term | International Equivalent |
|---------|--------------------------|
| Plan change | Local plan amendment / development plan review |
| Resource consent | Planning application / development management |
| Section 32 evaluation | Sustainability appraisal / evidence base report |
| Auckland Unitary Plan | District plan / local plan / development plan |
| Independent Commissioner | Planning inspector / hearing officer |
| RMA | Planning Acts (TCPA in UK, EPA in various jurisdictions) |
| NZPI | RTPI (UK), PIA (Australia), CIP (Canada) |
| Iwi engagement | Indigenous consultation / First Nations engagement |
| Environment Court | Planning Court / Land and Environment Court |
