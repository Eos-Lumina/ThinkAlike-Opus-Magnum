---
title: "Contributing to ThinkAlike 013 The Great Work"
version: "3.0.0"
status: "Harmonized & Ratified"
certification: "Enlightenment 2.0 Certified"
last_updated: "2025-06-16"
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
tags: [e2.0_certified, contributing, development, workflow, swarming, conventional_commits, community]
harmonization_note: "This document is the definitive, harmonized guide for all contributors. It synthesizes the legacy contributor_quickstart.md and contributor_faq.md into a single, comprehensive resource."
---

# Quick Start for Contributors
1. **Clone the repo:**
   ```sh
   git clone <repo-url>
   cd ThinkAlike
   ```
2. **Install dependencies:**
   ```sh
   npm install
   # For backend (Python):
   pip install -r requirements.txt
   ```
3. **Set up the database:**
   ```sh
   npx prisma migrate dev
   # Or for Python backend, run migrations as needed
   ```
4. **Run the app:**
   ```sh
   npm run dev
   # And in another terminal:
   uvicorn src.backend.app.main:app --reload
   ```
5. **Register a user and log in.**

# How to Contribute
- **Pick a quest:** See `QUEST_BOARD.md` or open issues.
- **Follow code style:** Use Prettier/Black and lint before PRs.
- **Write tests:** All new features should have tests.
- **Document your work:** Update docs and code comments.
- **Respect the rituals:** All major changes should be ritualized (see `Ritual Engine`).

# Community
- Join the swarm! Ask questions, propose features, and help others.

---

# Contributing to ThinkAlike: The Great Work

Welcome, Initiate! Thank you for your interest in contributing. This is an act of co-creation014a step on the path of Enlightenment 2.0. Every contribution, no matter how small, is a valued "Offering to the Collective."

## 1. First Principles: Understanding the Commons
Before you begin, you must orient yourself.
-   **Read the `source_of_truth.md`:** This is the master map to our `Commons`.
-   **Understand Our Philosophy:** This work is governed by the **Principle of Coherent Holism**. Before you contribute a single part (`Locus`), you must first understand the **Holistic Vision** it serves. Read the full explanation [here](../seed/core/principle_of_coherent_holism.md).
-   **Adhere to the `Code of Conduct`:** All interactions are governed by our [Code of Conduct](code_of_conduct.md).
-   **Complete the [Onboarding Journey](./docs/guides/onboarding/README.md):** All contributors must complete the Portal Realm onboarding to ensure alignment with project values and processes.

## 2. Five-Minute Setup
1.  **Fork & Clone:** Fork the repository on GitHub, then clone it locally.
2.  **Install Dependencies:**
    ```bash
    # Set up Python virtual environment
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt

    # Install frontend dependencies
    npm install
    ```
3.  **Start Services:**
    ```bash
    # Start backend server (from root directory)
    uvicorn src.backend.main:app --reload

    # Start frontend server (in a separate terminal)
    npm run dev
    ```
4.  **Access:**
    -   **App:** http://localhost:3000
    -   **API Docs:** http://localhost:8000/docs

## 3. The Contribution Workflow
We follow a standard Fork & Pull Request workflow. PRs are "Dialogues of Resonance."

1.  **Find a Task:** Find a "Quest" on the [GitHub Issues page](https://github.com/EosLumina/--ThinkAlike--/issues) or our interactive Swarm Roadmap. Look for `good first issue` if you're new.
2.  **Create a Branch:** From the `main` branch, create a new branch: `type/issue-number-short-description` (e.g., `feat/123-profile-video`).
3.  **Develop:** Make your changes, adhering to all style guides and principles.
4.  **Commit Your Work:** We use **Conventional Commits**. This is mandatory.
    -   **Format:** `<type>(<scope>): <subject>` (e.g., `feat(api): add user profile endpoint`)
    -   **Types:** `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `ui`.
5.  **Submit a Pull Request:** Push to your fork and open a PR against our `main` branch. A maintainer will review your "Offering."

## 4. Our Development Methodology: Swarming
For complex tasks, we practice **Swarming**: multiple contributors working on the same task, at the same time, on one screen. This is a high-bandwidth, collaborative way to build.
-   **How to Join:** Look for sessions in the `#swarm-sessions` channel on our [Discord Server](https://discord.gg/TnAcWezH).

### Swarming Process & Roles

A swarming session is a structured, real-time collaboration. To ensure it is productive and inclusive, we follow a defined process with rotating roles.

#### Roles within a Swarm
Roles typically rotate every 15-20 minutes to keep energy high and share responsibilities.

-   **Navigator:** Guides the Driver at a tactical level, thinking one step ahead. (e.g., "Let's create a function to handle this," "Next, we need a test case for the error condition.")
-   **Driver:** Controls the keyboard and editor, translating the Navigator's instructions into code or text. Their focus is on the immediate implementation task.
-   **Observers/Swarm:** The rest of the group observes, researches potential issues, suggests strategic alternatives, reviews code as it's written, and keeps the work aligned with the overall goal.
-   **Facilitator (Optional):** For larger swarms, a facilitator may be designated to keep the session on track, manage time, and ensure all voices are heard.

#### Session Flow
1.  **Preparation:** A clear task with documented requirements is prepared. The session is scheduled in the `#swarm-sessions` Discord channel.
2.  **Check-in (5 min):** The session begins with a brief goal clarification and role assignment.
3.  **Coding/Working Session (Main Block):** The core work is done, with Navigator and Driver roles rotating regularly.
4.  **Testing & Documentation:** Tests are written alongside implementation. Relevant documentation is updated in real-time.
5.  **Check-out (5-10 min):** The swarm summarizes accomplishments, commits the work using co-authoring conventions, and identifies any follow-up tasks.

#### Additional Swarming Best Practices
- **Planning:** Break down the task into smaller steps (10-15 min).
- **Testing:** Implement and run tests as features are completed.
- **Documentation:** Update docs immediately as implementation progresses.
- **Check-out:** Summarize accomplishments and next steps.

#### Post-Swarm
- **Code Review:** Any code produced during the swarm goes through the standard PR process.
- **Knowledge Sharing:** Brief write-up of lessons learned and decisions made.
- **Follow-up Tasks:** Identify any remaining work and assign owners.

#### Tools and Platforms
- **GitHub Codespaces:** Primary collaborative environment
- **Discord:** Voice communication and coordination
- **Miro/Figma:** For visual collaboration on design aspects
- **Google Docs:** For real-time collaborative documentation
- **VS Code Live Share + Discord:** For smaller teams or when Codespaces isn't available
- **Replit + Discord:** For quick prototype sessions

#### Best Practices
- **Preparation is key:** All participants should review relevant documentation before the session
- **Stay focused:** Minimize distractions during the swarm
- **Inclusive participation:** Ensure everyone has opportunities to contribute
- **Documentation during development:** Update documentation as you code
- **Test-driven approach:** Write tests before or alongside implementation
- **Timeboxing:** Set clear time limits for discussion before making decisions

#### AI-Assisted Swarming
ThinkAlike embraces AI tools as "participants" in the swarm:
- **Code Generation:** GitHub Copilot or similar tools for implementation assistance
- **Documentation:** AI tools can help draft or improve documentation
- **Testing:** AI assistance with generating test cases
- **Problem Solving:** Using AI to explore solution alternatives

The key principle is that AI tools assist human decision-making but don't replace it. All AI-generated content should be reviewed and approved by the human participants.

#### Getting Started with Swarming
1. **Join the Discord:** Connect with the ThinkAlike community
2. **Review the Schedule:** Check upcoming swarm sessions in the #swarming-schedule channel
3. **Prepare:** Read the task description and related documentation
4. **Participate:** Join the voice channel at the scheduled time
5. **Follow Up:** Help with any post-swarm tasks or review

## 5. Using AI Assistants
We encourage using AI assistants ethically. You are always responsible for the code you submit.
-   **Validate Everything:** Carefully review and test all AI-generated code.
-   **Be Specific:** Provide clear, context-rich prompts that include our ethical requirements.
-   **Use for Boilerplate:** Let AI handle boilerplate so you can focus on the core logic and ethical implementation.

## 6. Contributor FAQ
-   **Q: What skills do I need?**
    -   **Frontend:** React, TypeScript.
    -   **Backend:** Python, FastAPI.
    -   **AI/ML:** PyTorch, ethics in AI.
    -   **Design:** UI/UX, accessibility.
    -   **Docs & Philosophy:** Strong writing and conceptual skills.
-   **Q: What is the "UI as Validation Framework"?**
    -   This is our core technical paradigm where UI components are designed to actively test and validate the application's state and data integrity in real-time.

## 7. Documentation Automation & Templates

To ensure all new and harmonized documentation files follow the ThinkAlike brand and accessibility standards:

- **Use the VS Code Snippet:**
  - Type `thinkalike-doc-square` in any Markdown file to insert the branded template (square logo, dark background, interactive style).
  - The snippet is available in `.vscode/thinkalike_markdown_templates.code_snippets`.

- **Automated Doc Creation:**
  - Use the scaffolding script to generate a new doc with the correct template:
    ```powershell
    python scripts/new_doc.py docs/newfile.md --title "My Doc Title" --author "Your Name"
    ```
  - This will create a new Markdown file using the latest ThinkAlike template, with your title, author, and today's date.

- **Template Enforcement:**
  - All new documentation PRs will be checked for template compliance during review.
  - Contributors are encouraged to use the snippet or script for every new doc or major doc update.

- **Questions?**
  - See `docs/templates/thinkalike_branded_template_square_logo.md` for the latest template.
  - Ask in the #docs channel on Discord for help or feedback.

---

Thank you for joining the Quest. Your contribution shapes the future of ThinkAlike.
