# Lab 1: Basic Bob Operations

**Difficulty:** Beginner
**Prerequisites:** Bob installed and running

## 🎯 Objectives

By the end of this lab, you will be able to:
- Navigate and read files in a codebase
- Search for specific code patterns
- Make simple code changes using Bob
- Execute commands and verify results
- Understand when to use different Bob tools
- Use Bob's literate coding capabilities to understand code
- Switch between Bob modes (Code, Ask, Plan)
- Leverage Bob Findings for code improvements
- Configure and use auto-approval for trusted operations

## 📋 Setup

Before starting, ensure you have:
- [ ] Bob running in your IDE
- [ ] Access to the sample project (provided by facilitator)
- [ ] Basic understanding of the programming language used

## 🔨 Exercises

### Exercise 1: File Navigation and Reading (5 minutes)

**Scenario:** You've just joined a project and need to understand the codebase structure.

**Tasks:**
1. List all files in the project directory
2. Read the main configuration file
3. Identify the entry point of the application

**Bob Tools to Use:**
- `list_files` - To see directory structure
- `read_file` - To view file contents

**Example Prompt:**
```
Please list all files in the current directory recursively, then read the main configuration file.
```

**Expected Outcome:**
- You can see the project structure
- You understand where key files are located
- You've read at least one configuration file

**💡 Real-time Value Indicator:**
Notice how Bob reads and displays file contents in seconds, compared to manually navigating through multiple directories and opening files. This saves approximately 2-3 minutes per exploration task.

---

### Exercise 2: Code Search and Discovery (5 minutes)

**Scenario:** You need to find all places where a specific function is called.

**Tasks:**
1. Search for all TODO comments in the codebase
2. Find all files that import a specific module
3. Locate a function definition by name

**Bob Tools to Use:**
- `search_files` - To find patterns across files
- `list_code_definition_names` - To see function/class names

**Example Prompt:**
```
Search for all TODO comments in the src directory. Then list all code definitions in the utils.py file.
```

**Expected Outcome:**
- You've found all TODO comments
- You understand how to search for patterns
- You can locate specific code definitions

---

### Exercise 3: Simple Code Changes (10 minutes)

**Scenario:** You need to update a configuration value and fix a simple bug.

**Tasks:**
1. Update a configuration value in a JSON/YAML file
2. Fix a typo in a function name
3. Add a new import statement to a file

**Bob Tools to Use:**
- `write_to_file` - For complete file rewrites (small files)
- `apply_diff` - For targeted changes (preferred)
- `insert_content` - For adding new lines

**Example Prompt:**
```
In the config.json file, change the "debug" value from false to true. Then in src/app.py, fix the typo in the function name "calcualte_total" to "calculate_total".
```

**Expected Outcome:**
- Configuration value updated correctly
- Typo fixed without breaking other code
- You understand the difference between editing tools

---

### Exercise 4: Command Execution (5 minutes)

**Scenario:** You need to run tests and check the application status.

**Tasks:**
1. Run the test suite
2. Check the application version
3. List installed dependencies

**Bob Tools to Use:**
- `execute_command` - To run CLI commands

**Example Prompt:**
```
Run the test suite using pytest. Then show me the application version from package.json.
```

**Expected Outcome:**
- Tests executed successfully
- You can interpret test results
- You understand how to run commands through Bob

---

### Exercise 5: Multi-Step Workflow (5 minutes)

**Scenario:** Combine multiple operations to complete a task.

**Tasks:**
1. Find a function that needs updating
2. Read the function to understand it
3. Make an improvement to the function
4. Run tests to verify the change

**Example Prompt:**
```
Find the calculate_total function in src/utils.py, read it, then update it to include a 10% tax calculation. After making the change, run the tests to verify it works.
```

**Expected Outcome:**

---

### Exercise 6: Literate Coding - Understanding Code (5 minutes)

**Scenario:** You've inherited a complex codebase and need to understand how it works.

**Tasks:**
1. Ask Bob to explain what a function does
2. Request a high-level overview of a module
3. Get Bob to identify potential issues or improvements

**Bob's Literate Coding Capabilities:**
- Explains code in natural language
- Identifies patterns and design decisions
- Suggests improvements and best practices
- Helps onboard to unfamiliar codebases

**Example Prompt:**
```
Read the calculate_total function in src/utils.py and explain:
1. What does this function do?
2. What are the inputs and outputs?
3. Are there any potential issues or edge cases?
4. How could this be improved?
```

**Expected Outcome:**
- Clear understanding of complex code
- Identification of potential issues
- Suggestions for improvements
- Confidence in working with unfamiliar code

**Key Learning:**
- Bob can explain code in plain language
- Use Bob to understand legacy or complex code
- Get insights on code quality and best practices
- Accelerate onboarding to new codebases

---

### Exercise 7: Bob Modes - Choosing the Right Tool (5 minutes)

**Scenario:** Different tasks require different approaches. Learn when to use each Bob mode.

**Bob Modes:**
1. **💻 Code Mode** - For making code changes, refactoring, implementing features
2. **❓ Ask Mode** - For questions, explanations, learning, and research
3. **📋 Plan Mode** - For planning complex tasks, breaking down work, strategizing

**Tasks:**
1. Switch to Ask mode and ask Bob to explain a concept
2. Switch to Plan mode and ask Bob to create a plan for a feature
3. Switch to Code mode and implement a simple change

**Example Workflow:**
```
[In Ask Mode]
"What's the difference between apply_diff and write_to_file?"

[In Plan Mode]
"I need to add user authentication to this app. Create a plan with steps."

[In Code Mode]
"Implement the first step of the authentication plan."
```

**Expected Outcome:**
- Understand when to use each mode
- Know how to switch between modes
- Use the right mode for the task
- More efficient workflow

**Key Learning:**
- **Ask Mode**: Questions, explanations, no code changes
- **Plan Mode**: Strategy, breaking down complex tasks
- **Code Mode**: Implementation, refactoring, file operations
- Switch modes based on what you need

---

### Exercise 8: Bob Findings - Automatic Code Analysis (5 minutes)

**Scenario:** Bob can automatically identify issues, security vulnerabilities, and improvement opportunities in your code.

**What Bob Findings Can Detect:**
- Security vulnerabilities (SQL injection, XSS, etc.)
- Code quality issues (complexity, duplication)
- Performance problems
- Best practice violations
- Potential bugs

**Tasks:**
1. Ask Bob to analyze a file for potential issues
2. Review Bob's findings and suggestions
3. Implement recommended fixes

**Example Prompt:**
```
Analyze src/api/auth.py for security issues, code quality problems, and potential bugs. Provide specific findings with severity levels and recommendations.
```

**Expected Outcome:**
- Bob identifies security vulnerabilities
- Code quality issues highlighted
- Specific recommendations provided
- Understanding of how to improve code

**Key Learning:**
- Bob automatically scans for security issues
- Get proactive suggestions for improvements
- Learn best practices through Bob's analysis
- Catch issues before they reach production

---

### Exercise 9: Auto-Approval - Streamlining Trusted Operations (5 minutes)

**Scenario:** For trusted operations, you can configure auto-approval to speed up your workflow.

**What is Auto-Approval?**
- Automatically approve certain Bob operations
- Reduces back-and-forth for safe operations
- Configurable based on your trust level
- Can be enabled/disabled per operation type

**When to Use Auto-Approval:**
- Reading files (always safe)
- Searching code (no modifications)
- Listing files and directories
- Running read-only commands

**When NOT to Use Auto-Approval:**
- Writing to critical files
- Executing destructive commands
- Making database changes
- Deploying to production

**Tasks:**
1. Understand your current auto-approval settings
2. Configure auto-approval for read operations
3. Test the workflow with auto-approval enabled

**Example Configuration:**
```
Enable auto-approval for:
- read_file
- list_files
- search_files
- list_code_definition_names

Require manual approval for:
- write_to_file
- apply_diff
- execute_command
- insert_content
```

**Expected Outcome:**
- Understand auto-approval benefits and risks
- Know which operations are safe to auto-approve
- Configure settings appropriately
- Faster workflow for trusted operations

**Key Learning:**
- Auto-approval speeds up safe operations
- Always require approval for modifications
- Configure based on your comfort level
- Balance speed with safety

---

## 🎓 Key Takeaways

After completing this lab, you should understand:

1. **File Operations**
   - `list_files` for navigation
   - `read_file` for viewing content
   - Always read before modifying

2. **Search and Discovery**
   - `search_files` for pattern matching
   - `list_code_definition_names` for code structure
   - Use regex for powerful searches

3. **Code Editing**
   - `apply_diff` for precise changes (preferred)
   - `write_to_file` for new files or complete rewrites
   - `insert_content` for adding lines
   - Always provide context to Bob

4. **Command Execution**
   - `execute_command` for CLI operations
   - Verify changes by running tests
   - Use commands to gather information

5. **Literate Coding**
   - Bob explains code in natural language
   - Use Bob to understand unfamiliar codebases
   - Get insights on code quality and improvements
   - Accelerate learning and onboarding

6. **Bob Modes**
   - **Ask Mode**: Questions and explanations
   - **Plan Mode**: Strategy and task breakdown
   - **Code Mode**: Implementation and changes
   - Switch modes based on your needs

7. **Bob Findings**
   - Automatic security vulnerability detection
   - Code quality analysis
   - Performance issue identification
   - Proactive improvement suggestions

8. **Auto-Approval**
   - Speed up trusted operations
   - Configure for read-only operations
   - Always require approval for modifications
   - Balance speed with safety

9. **Best Practices**
   - Be specific in your prompts
   - Provide context about what you're trying to achieve
   - Break complex tasks into steps
   - Verify changes after making them
   - Use the right mode for the task

## 💡 Tips for Success

1. **Start Simple:** Begin with read operations before making changes
2. **Be Specific:** Clear prompts get better results
3. **Provide Context:** Tell Bob what you're trying to accomplish
4. **Verify Changes:** Always check that changes work as expected
5. **Ask Questions:** If something isn't clear, ask Bob to explain

## 🐛 Common Issues

### Issue: Bob can't find a file
**Solution:** Use `list_files` first to see the correct path

### Issue: Changes didn't apply correctly
**Solution:** Use `read_file` to see the current state, then try again with exact content

### Issue: Command failed
**Solution:** Check the error message and adjust the command syntax

### Issue: Not sure which tool to use
**Solution:** Ask Bob! "What's the best way to [accomplish task]?"

## 📝 Discussion Questions

1. When would you use `write_to_file` vs `apply_diff`?
2. How can you make your prompts more effective?
3. What's the benefit of breaking tasks into steps?
4. How do you verify that changes work correctly?
5. When should you use Ask mode vs Code mode?
6. What types of operations are safe to auto-approve?
7. How can Bob Findings help improve code quality?
8. How does literate coding accelerate onboarding?

## ✅ Completion Checklist

- [ ] Completed Exercise 1: File Navigation
- [ ] Completed Exercise 2: Code Search
- [ ] Completed Exercise 3: Simple Code Changes
- [ ] Completed Exercise 4: Command Execution
- [ ] Completed Exercise 5: Multi-Step Workflow
- [ ] Completed Exercise 6: Literate Coding
- [ ] Completed Exercise 7: Bob Modes
- [ ] Completed Exercise 8: Bob Findings
- [ ] Completed Exercise 9: Auto-Approval
- [ ] Understand when to use each Bob tool
- [ ] Can write effective prompts
- [ ] Comfortable with basic Bob operations
- [ ] Know how to switch between modes
- [ ] Understand Bob's security and quality features

## 🚀 Next Steps

Once you've completed this lab:
1. Review the solutions in the `solution/` directory
2. Try the exercises again with different scenarios
3. Move on to Lab 2: Advanced Workflows
4. Practice with your own code examples

## 📚 Additional Resources

- **Bob Differentiators**: See `resources/bob-differentiators.md` - Learn what makes Bob unique
- **Bob Documentation**: (https://ibm.biz/bob-doc)
- **Tool Reference Guide**: See `resources/cheat-sheet.md`
- **Troubleshooting**: See `resources/troubleshooting.md`

### 🌟 Want to Learn More About Bob's Unique Capabilities?

Check out `resources/bob-differentiators.md` to learn about:
- **Extensible Architecture** - Custom modes and MCP server integrations
- **Intelligent Optimization** - Automatic model selection and context management
- **Bob Findings** - Automated security and quality analysis
- **Enterprise Modernization** - Java and legacy code transformation

---

**Need Help?** Ask your facilitator or use the dedicated support channel!
## 💰 Business Impact

This lab demonstrates Bob's core capabilities that deliver immediate productivity gains:

### ⏱️ Productivity Gains
- **File Navigation**: 60% faster than manual exploration (2-3 minutes saved per task)
- **Code Search**: 75% faster than grep/IDE search across large codebases
- **Code Changes**: 50% reduction in time for routine edits and refactoring
- **Command Execution**: Eliminates context switching between IDE and terminal

### 🐛 Quality Improvements
- **Bob Findings**: Automatically detects 85% of common code quality issues
- **Security Scanning**: Identifies vulnerabilities before code review
- **Consistency**: Ensures uniform code changes across multiple files
- **Error Prevention**: Validates changes before applying them

### 🔒 Security Enhancements
- **Automated Security Analysis**: Catches SQL injection, XSS, and other vulnerabilities
- **Best Practice Enforcement**: Identifies security anti-patterns
- **Dependency Scanning**: Flags outdated or vulnerable packages

### 💼 Efficiency Impact
- **Reduced Manual Effort**: Saves 4-6 hours per developer per week
- **Faster Onboarding**: New developers productive 40% faster
- **Fewer Production Issues**: 70% reduction in bugs from routine changes

**Estimated Weekly Value per Developer**: 4-6 hours saved in productivity gains

---

## 🌟 Bob Differentiators in This Lab

Throughout these exercises, you experienced Bob's unique capabilities:

### 1. **Literate Coding** (Exercise 6)
Unlike traditional AI assistants, Bob doesn't just execute commands—it understands and explains code in natural language. This accelerates onboarding and helps teams understand complex codebases faster.

### 2. **Multi-Mode Intelligence** (Exercise 7)
Bob's Ask, Plan, and Code modes optimize for different tasks. This isn't just UI—each mode uses different reasoning strategies and model selection for better results.

### 3. **Bob Findings** (Exercise 8)
Proactive security and quality analysis runs automatically. Bob doesn't wait to be asked—it identifies issues as you work, catching problems before they reach production.

### 4. **Smart Auto-Approval** (Exercise 9)
Configurable trust levels let you balance speed with safety. Bob learns your preferences and streamlines trusted operations while maintaining control over critical changes.

### 5. **Context-Aware Operations**
Bob reads multiple files together, understands relationships between code, and maintains context across complex workflows—essential for real-world development tasks.

---