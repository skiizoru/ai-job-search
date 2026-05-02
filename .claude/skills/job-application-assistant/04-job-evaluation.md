# Job Evaluation Framework

## Scoring Dimensions

Evaluate each job posting against these five dimensions:

### 1. Technical Skills Match (0-100)
How well do the required/preferred skills align with the candidate's capabilities?

| Score | Meaning |
|-------|---------|
| 80-100 | Core requirements are primary skills |
| 60-79 | Most requirements match, 1-2 gaps that are learnable |
| 40-59 | Partial match, significant upskilling needed |
| 0-39 | Fundamental mismatch |

**Strong match areas:** Policy development, plan change management, section 32 evaluation, RMA/statutory planning compliance, hearing preparation and expert witness, GIS and spatial analysis (ArcGIS, QGIS), stakeholder and iwi consultation, technical report writing, project management, generative AI integration (Claude Code, NotebookLM, ChatGPT), cross-functional coordination, mentoring

**Moderate match areas:** Central government policy analysis, planning consultancy (private sector), environmental remote sensing (in progress), research analyst roles (adjacent), GovTech/spatial technology policy

**Weak match areas:** Software engineering or data science (beyond applied planning use), commercial property advisory, pure quantitative research, roles requiring a postgraduate degree beyond B.Planning(Hons), finance or economics-primary roles

### 2. Experience Match (0-100)
Does work history align with what they're looking for?

| Score | Meaning |
|-------|---------|
| 80-100 | Direct experience in the same domain and role type |
| 60-79 | Related experience, transferable skills clear |
| 40-59 | Adjacent experience, would need to make the case |
| 0-39 | Unrelated experience |

**Strong:** Urban policy planning (city centre, built form, densification, heritage), statutory plan change management (NZ/RMA), resource consent processing, local government policy and advisory, GIS-based spatial analysis, statutory hearings and expert witness, stakeholder and iwi engagement, public sector briefing and reporting

**Moderate:** Central government policy (transferable analytical and statutory skills), international planning practice (common law jurisdictions), planning consultancy, research and policy analysis roles, GovTech product/policy advisory

**Entry-level / thin:** Private sector commercial roles, academic research, engineering or infrastructure delivery, software/product development

### 3. Behavioral/Culture Fit (0-100)
Does the role and company culture match the behavioral profile?

| Score | Meaning |
|-------|---------|
| 80-100 | Culture strongly matches behavioral preferences |
| 60-79 | Mixed signals but mostly compatible |
| 40-59 | Some friction areas |
| 0-39 | Significant culture mismatch |

**Good fit signals:** Evidence-based decision making, long-horizon projects, specialist expertise valued, collaborative but autonomous, quality over volume, policy or regulatory rigour expected, cross-disciplinary teamwork, room to mentor or develop others

**Red flags to research:** High-volume transactional environment, sales or business development primary, startup with no structure or framework, culture of rapid judgment over careful analysis, micromanagement, no path to strategic or policy work

### 4. Location & Logistics (Pass/Fail + Notes)
- Auckland (local): PASS
- UK, Australia, Canada, Singapore, Nordics: PASS (actively seeking international relocation)
- Remote roles (anywhere): PASS
- Requires on-site in other locations: DISCUSS (relocation support, timeline)
- Frequent international travel with no relocation: FLAG (discuss with user)

### 5. Career Alignment & Motivation (0-100)
Does this role advance career goals and contain tasks that energize?

| Score | Meaning |
|-------|---------|
| 80-100 | Strongly aligned with career direction, clear growth path |
| 60-79 | Good role but only partially aligned with long-term goals |
| 40-59 | Decent job but doesn't build toward career goals |
| 0-39 | Dead end or backwards step |

**Career goals:**
- Secure an international planning policy or strategic advisory role (UK, Australia, Canada, Singapore, or Nordics)
- Progress to Planning Policy Manager or Strategic Policy Advisor level
- Develop expertise at the intersection of urban policy, spatial technology, and generative AI
- Build experience with comparative international planning frameworks

**Motivation filter:** Evaluate not just whether the tasks *can* be done, but whether they will *energise*.
- Tasks that energise: Complex policy synthesis and analysis, expert witness and public advocacy, GIS and spatial analysis, AI tool development and integration, mentoring and knowledge transfer, shaping built environment outcomes
- Tasks that drain: Routine administrative processing, high-volume transactional work, maintenance-only roles with no policy development component, sales or commercial development

**Life situation alignment:**
- **Security:** Currently employed; can be selective — no urgency to accept a poor fit
- **Flexibility:** Open to international relocation; remote roles also strongly preferred for international opportunities
- **Professional development:** Actively building spatial/remote sensing and AI skills alongside planning practice

### 6. Salary Benchmark (Optional)

If the salary lookup tool is configured (`salary_data.json` exists), look up the company:
```
python salary_lookup.py "<Company Name>" --json
```

If a city is known from the posting, add `--city "<City>"` to narrow results.

Present findings as:
```
### Salary Benchmark
| Metric | Value |
|--------|-------|
| [Category] index | XX.X (+/-X.X% vs baseline) |
| Overall index | XX.X (+/-X.X% vs baseline) |
```

If the salary tool is not configured, skip this section.

## Output Format

Present the evaluation as:

```
## Job Fit Evaluation: [Role] at [Company]

| Dimension | Score | Notes |
|-----------|-------|-------|
| Technical Skills | XX/100 | [brief note] |
| Experience Match | XX/100 | [brief note] |
| Behavioral Fit | XX/100 | [brief note] |
| Location | PASS/FAIL | [brief note] |
| Career Alignment | XX/100 | [brief note] |

**Overall Score: XX/100** (weighted average of scored dimensions)

### Verdict: [Strong Fit / Good Fit / Moderate Fit / Weak Fit / Poor Fit]

### Key Strengths for This Role
- [bullet points]

### Gaps to Address
- [bullet points]

### Recommendation
[1-2 sentences: apply/skip/apply with caveats]

### Company Research Checklist
- [ ] Checked company website (mission, values, recent news)
- [ ] Checked review sites (Glassdoor, etc.)
- [ ] Checked LinkedIn for team size, recent hires, connections
- [ ] Checked media for restructuring, growth, or workplace issues
- [ ] Identified network contacts who may know the team/manager
```

## Weighting
- Technical Skills: 30%
- Experience Match: 25%
- Behavioral Fit: 15%
- Career Alignment: 30%

(Location is pass/fail, not weighted)

## Thresholds
- **Strong Fit** (75+): Definitely apply, tailor everything
- **Good Fit** (60-74): Apply, address gaps in cover letter
- **Moderate Fit** (45-59): Consider carefully, discuss with user
- **Weak Fit** (30-44): Probably skip unless strategic reasons
- **Poor Fit** (<30): Skip

## Pre-Application: Call the Employer (Best Practice)

Before writing the application, consider whether the candidate should call the contact person listed in the posting. **Only call if there are substantive questions** — never call just to "be remembered."

### When to Suggest Calling
- The posting has unclear or ambiguous requirements
- It's unclear which competencies are essential vs. nice-to-have
- The role description is vague about day-to-day tasks
- There's a named contact person who invites questions

### Good Questions to Ask
- "What are the primary challenges in this role?"
- "How is time typically divided across the listed responsibilities?"
- "Which competencies are most critical for success in this position?"
- "What does success look like in the first 6-12 months?"

### Rules for the Call
- Prepare a 30-second "elevator pitch" about your background in case they ask
- The call's purpose is **gathering information**, not delivering a pitch
- Take notes — use what you learn to tailor the application
- Reference the conversation naturally in the cover letter ("After speaking with [name], I was especially drawn to...")
