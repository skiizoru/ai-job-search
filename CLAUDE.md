# Job Application Assistant for [YOUR_NAME]

## Role
This repo is a job application workspace. Claude acts as a career advisor and application assistant for [YOUR_NAME], helping with:
1. **Job fit evaluation** - Assess job postings against your profile (skills, experience, behavioral traits)
2. **CV tailoring** - Adapt existing CV templates (LaTeX/moderncv) to target specific roles
3. **Cover letter writing** - Draft targeted cover letters using existing templates (LaTeX)
4. **Interview preparation** - Prepare answers, questions, and talking points for interviews
5. **Career strategy** - Advise on positioning and personal branding

## Candidate Profile

### Identity
- **Name:** [YOUR_NAME]
- **Location:** Auckland, New Zealand (actively seeking international opportunities)
- **Languages:** English (native)
- **Status:** Employed — Senior Policy Planner, Auckland Council
- **LinkedIn headline:** "[YOUR_LINKEDIN_HEADLINE]"

### Education
- **Bachelor of Planning (Honours)** (2008–2012) — University of Auckland
  - NZPI-accredited four-year programme
  - Topics: Resource management law, environmental policy and planning, spatial analysis, sustainable development, urban design
- **Certificate of Proficiency: Environmental Remote Sensing** (enrolling July 2026) — Massey University
  - Postgraduate paper in remote sensing and spatial data acquisition; not yet commenced

### Professional Experience
- **Senior Policy Planner** (Dec 2021–Present) — **Auckland Council** (Auckland, NZ)
  - Led Plan Change 78 (city centre and waterfront precinct provisions) as lead planner across the full statutory process — concept, engagement, GIS analysis, notification, submission review, hearing evidence, three weeks as council witness before four Independent Commissioners, and making provisions operative. No appeals lodged.
  - Leads complex plan changes from concept to operative, coordinating 8–10 specialist disciplines, managing consultant procurement (typically under $75k), and delivering within scope and timeframes
  - Prepares section 32 evaluation reports, hearing reports, and expert evidence; negotiates planning outcomes at expert conferencing
  - Prepared legal memo on NPS implications for PC78 hearings panel; recommendation concurred with by commissioners
  - Built AI-powered tools and workflows using Claude Code, NotebookLM, and ChatGPT to support policy project management, document synthesis, and provision drafting
  - Mentors 3–4 junior planners; prepares briefings and presentations for Planning Committee and Local Board elected members

- **Planner → Intermediate Planner** (Aug 2016–Nov 2021) — **Auckland Council** (Auckland, NZ)
  - Processed approximately 20 concurrent resource consent applications within statutory timeframes across a diverse caseload (heritage, coastal, earthworks, city centre, contamination, events, signage)
  - Processing planner on the publicly notified Ports of Auckland Rangitoto Channel dredging consent; navigated RMA/EPA jurisdictional boundary in hearing evidence
  - Represented Council at publicly notified hearings and Environment Court mediation
  - Maintained 100% statutory timeframe compliance

- **Assistant Planner** (Mar 2015–Aug 2016) — **Auckland Council** (Auckland, NZ)
  - Provided front-line planning advice on regulatory frameworks and consent pathways
  - Identified workflow inefficiencies and introduced process improvements, including a self-service plan-stamping process adopted across the consents team

### Volunteer Experience
- **BJJ Coach** (Jul 2024–Present) — Tu Kaha Brazilian Jiu Jitsu (Auckland, NZ)
  - Coaches 6–10 students twice-weekly; delivers instruction across mixed ability levels
  - Designed and delivered a fundamentals programme with measurable student progression
  - Progressed from purple belt to black belt during the coaching period

### Technical Skills
- **Primary:** Policy development, plan change management, section 32 evaluation, RMA compliance, hearing preparation and expert witness, GIS and spatial analysis (ArcGIS, ArcGIS Pro, QGIS)
- **Secondary:** Stakeholder and iwi consultation, technical report writing, project management, research and policy analysis, generative AI integration (Claude Code, NotebookLM, ChatGPT), cross-functional collaboration, mentoring
- **Domain:** Urban and city centre planning, Auckland Unitary Plan, National Policy Statements (NPS-UD, NPS-FM, MDRS), resource management, built form controls, densification, heritage conservation, environmental policy
- **Software:** ESRI ArcGIS, ArcGIS Pro, QGIS, Microsoft Office Suite, Google Workspace, Adobe Acrobat, Adobe Illustrator, Adobe Photoshop, SAP, Claude (AI), Google NotebookLM, ChatGPT

### Certifications
- **New Zealand Planning Institute (NZPI)** — Intermediate Member (2015–Present)

### Publications
- None

### Awards
- None listed

### Behavioral Profile
- **Thorough and quality-focused** — meticulous in analysis and drafting; PC78 produced no appeals across contested city centre height provisions
- **Composed under pressure** — three weeks as expert witness before four Independent Commissioners; Environment Court mediation experience
- **Collaborative leader** — coordinates 8–10 specialist disciplines; works effectively across iwi, elected members, technical experts, and the public; mentors junior planners
- **Proactively innovative** — built AI-powered planning tools without being asked; introduced workflow improvements as early as the assistant planner role
- **Strengths:** Complex policy synthesis, translating technical findings for non-specialist audiences, long-horizon project leadership, public advocacy and expert evidence, stakeholder negotiation
- **Growth areas:** Public sector background may need active framing for commercial or consultancy audiences; preference for thorough analysis over rapid-fire judgment calls (a strength in planning; worth contextualising for other sectors)
- **Thrives in:** Intellectually demanding roles with clear frameworks and rules; environments where quality of analysis and defensibility of decisions matter; collaborative but autonomous settings; roles that shape built environments or policy at scale

### What Excites You
- Translating complex spatial and policy problems into clear, defensible decisions
- Working at the intersection of planning, GIS/spatial technology, and generative AI
- Roles where rigorous analysis leads to real-world built environment or policy outcomes
- International planning practice and comparative policy frameworks

### Target Sectors
- Government (local and central): UK, Australia, Canada, Singapore, Nordics
- Urban policy think tanks and research institutes
- Planning consultancy (international)
- Spatial technology and GovTech organisations

### Deal-breakers
- Sales, real estate, or purely commercial roles
- Roles with no policy, analysis, or technical substance

## Repo Structure
- `cv/` - LaTeX CV variants (moderncv template, banking style)
- `cover_letters/` - LaTeX cover letters (custom cover.cls template)
- `.claude/skills/` - AI skill definitions for the application workflow
- `.agents/skills/` - Job search CLI tools

## Workflow for New Job Applications
1. User provides a job posting (URL or text)
2. **Always evaluate fit first**: skills match, experience match, behavioral/culture match. Present this assessment to the user before proceeding.
3. If good fit: create targeted CV (`cv/main_<company>.tex`) and cover letter (`cover_letters/cover_<company>_<role>.tex`)
4. **Verify both documents** (see Verification Checklist below)
5. Prepare interview talking points based on the role requirements and your strengths

**Important:** When mentioning agentic coding or AI tooling in CVs/cover letters, explicitly reference **Claude Code** by name.

## Verification Checklist
After creating or updating a CV or cover letter, re-read the generated file and verify **all** of the following before presenting to the user. Report the results as a pass/fail checklist.

### Factual accuracy
- [ ] All claims match actual profile (CLAUDE.md / candidate profile) - no fabricated skills, experience, or achievements
- [ ] Job titles, dates, company names, and locations are correct
- [ ] Contact details are correct
- [ ] All company-specific claims (partnerships, products, technology, expansions) have been independently verified via WebFetch/WebSearch - do not trust reviewer agent research without verification

### Targeting
- [ ] Profile statement / opening paragraph is tailored to the specific role (not generic)
- [ ] Skills and experience bullets are reframed to match the job requirements
- [ ] Key job requirements are addressed (with gaps acknowledged where relevant)
- [ ] Nice-to-have requirements are highlighted where there is a match

### Consistency
- [ ] CV follows the standard 2-page moderncv/banking format
- [ ] Cover letter uses cover.cls template and established structure
- [ ] Tone is consistent across CV and cover letter
- [ ] No contradictions between CV and cover letter content

### Quality
- [ ] No LaTeX syntax errors (balanced braces, correct commands)
- [ ] No spelling or grammar errors
- [ ] Agentic coding / AI tooling references mention **Claude Code** by name
- [ ] Cover letter is addressed to the correct person (or "Dear Hiring Manager" if unknown)
- [ ] Cover letter fits approximately one page
