# Z3_FEISTU Tester Guide ♿→👨‍🔬

---

## Table of Contents

- [Installation & Setup](#installation--setup)
- [Docker 🐋](#docker-)

---

## Installation & Setup

Hey there! Ready to get started? Follow these steps to install and run the project on your local machine:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/zxcamon4ik/Z3_FEISTU.git
   cd Z3_FEISTU
   ```

2. **Install Dependencies:**
   Make sure you have [Python 3.12+](https://www.python.org/), [Make](https://www.gnu.org/software/make/manual/make.html) and [GCC](https://gcc.gnu.org/) installed.

3. **Prepare Your C File:**
   - Place your `.c` file named **z3.c** into project root

4. **Run the Project:**
   ```bash
   make run
   ```
   
---

## Docker 🐋

A few Docker commands for fun and convenience!

### Run in Docker 🏃
To execute the tester inside a Docker container:

```bash
make d-run
```

### Purge Docker Content ♻️
To clean up Docker-related artifacts:
```bash
make d-purge
```

---
