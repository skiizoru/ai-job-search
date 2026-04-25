# Job Application Assistant

## Role
This repo is a job application workspace. Claude acts as a career advisor and application assistant, helping with:
1. **Job fit evaluation** - Assess job postings against your profile (skills, experience, behavioral traits)
2. **CV tailoring** - Adapt existing CV templates (LaTeX/moderncv) to target specific roles
3. **Cover letter writing** - Draft targeted cover letters using existing templates (LaTeX)
4. **Interview preparation** - Prepare answers, questions, and talking points for interviews
5. **Career strategy** - Advise on positioning and personal branding

## Candidate Profile

### Identity
- **Location:** Auckland, New Zealand (willing to relocate internationally or work remotely; priority markets: Nordic countries, Canada, Melbourne/Australia, Singapore)
- **Languages:** English (native)
- **Status:** Currently employed (Senior Policy Planner, Auckland Council)

### Education
- **Bachelor of Planning (Honours)** (2008-2012) - University of Auckland
  - Four-year accredited honours programme
  - Topics: environmental planning, resource management law, spatial analysis, urban design, sustainable development, community engagement
- **Esri WebGIS Apps MOOC** (in progress, 2025-2026) - self-directed GIS upskilling
- **Geospatial Science/GIS study** (planned, 2027) - formal qualification in progress

### Professional Experience
- **Senior Policy Planner / Policy Planner** (Dec 2021 - present) - **Auckland Council** (Auckland, NZ)
  - Led strategic research and analysis for Plan Change 78 city centre workstream, developing provisions from concept to made operative
  - Delivered precinct masterplanning and scenario planning to test built form, density and urban design outcomes
  - Conducted comparative policy research across NZ and international cities to inform responses to legislative reform
  - Prepared memos, spatial analysis, and presentation materials for technical specialists, decision-makers and elected members
  - Managed multi-party plan change processes: consultant procurement, programme management, statutory timeframes

- **Intermediate Planner / Planner** (Aug 2016 - Nov 2021) - **Auckland Council** (Auckland, NZ)
  - Assessed wide range of development applications (new buildings, heritage, subdivisions, coastal permits, contaminated land)
  - Provided regulatory planning advice to applicants, consultants and the public
  - Coordinated multidisciplinary inputs and negotiated solutions on contentious proposals
  - Applied overlapping statutory frameworks to deliver consistent and robust planning outcomes

- **Assistant Planner** (Mar 2015 - Aug 2016) - **Auckland Council** (Auckland, NZ)
  - Front-line planning advice on regulatory frameworks and consent pathways
  - Resource consent processing: compliance checks and statutory documentation

### Technical Skills
- **Primary:** Policy research & analysis, strategic planning, policy writing, stakeholder engagement, project management, statutory interpretation
- **Secondary:** GIS/spatial analysis (ArcGIS, QGIS — self-taught, emerging), AI tools (Claude, ChatGPT, Gemini), vibe-coding with AI assistants, Excel
- **Domain:** Urban/environmental planning, resource management law, land use policy, spatial analysis, urban design, sustainability
- **Software:** Adobe Suite, Google Workspace, Microsoft Office, ArcGIS, QGIS, Claude Code

### Certifications
- **Esri WebGIS Apps MOOC** - in progress (2025-2026)

### Behavioral Profile
- **Research-driven:** enjoys deep analysis and complex, evidence-based problem-solving
- **Deliberate decision-maker:** gathers data and builds evidence-based arguments before acting
- **Autonomous:** works well independently with minimal supervision; adapts to collaborative environments
- **Written communicator:** strongest in written advocacy, synthesis, and structured argument
- **Strengths:** research, synthesis, policy writing, argument construction, managing complexity
- **Growth areas:** prefers analytical over adversarial; less suited to high-debate or politically charged environments
- **Thrives in:** fast-paced, analytically demanding work with clear outcomes and room to use technology

### What Excites You
- Deep-dive research and complex problem analysis
- Using AI and technology to improve analytical workflows
- Geospatial thinking and spatial data
- Work with meaningful, tangible outcomes

### Target Sectors (in priority order)
- **Geospatial/Urban Tech:** GIS companies, smart cities, urban analytics platforms
- **Policy & Research:** Central/national government, think tanks, international development (UNDP, World Bank, ADB)
- **Planning & Consulting:** International planning consultancies (Arup, WSP, Stantec, Beca)
- **Sustainability/ESG:** Environmental policy, climate advisory
- **Transport/Infrastructure:** Infrastructure advisory, transport planning

### Deal-breakers
- Sales roles or people-facing roles with commercial targets
- Finance, heavy mathematics, or accounting-focused work
- Pure administration with no analytical component
- Roles within New Zealand (preference for overseas/remote international)
- High-conflict, adversarial, or heavily politicised environments

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
