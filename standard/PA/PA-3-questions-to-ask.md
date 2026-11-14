---
id: PA-3
name: Questions to ask
module: PA
owner: The maintainer (protected area, MB-6)
status: decided
---

## PA-3 Questions to ask

| Area | Questions |
| --- | --- |
| Purpose and users | What must the user be able to do in the end? Who uses it? What will the first version *not* do? |
| Templates | What kind of software is it? Which architecture template is closest, and where does it differ? Which toolkit do the agents use? |
| Flows | What are the main scenarios? What starts them? When has a flow succeeded? |
| Data | What data comes in and goes out? Where does the source of truth live? Is there sensitive data? Must different customers' data be kept apart? |
| Quality | How many users, with which response time, which availability, how fast is a backup restored? |
| Security | Who can do what? Where is identity checked? Where could an attack come in? |
| Externals | Which systems outside your control do you depend on? What happens if they do not answer? |
| Constraints | Time, budget, imposed technologies, company rules? |
| Environments | Where does it run? Which machines and services are available? Where do configuration and secrets live? |
| Engine | Where does the controller run? Where does the method state live? Which compute resources do you have, local and online? How do you want to be able to stop it? |
| Person | Who decides what? What may an agent do on its own? When do you want to be interrupted, how many times a day, on which channel? How is the work verified? |
| Evolution | What will change most often? What must the user or the AI be able to change? |
