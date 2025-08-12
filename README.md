# Week 0

This week is meant to give you a very basic introduction to ... In particular, we will focus on the following:

- XXX
- XXX

## setup

*(As of April 2025)*

1. [Fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#forking-a-repository) this repository.
2. [Create a Codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace/creating-a-codespace-for-a-repository#creating-a-codespace-for-a-repository) for your repository. Use this to view the lab notebook and work on your weekly coding exercise.
3. Once you're ready, [commit and push](https://docs.github.com/en/codespaces/developing-in-a-codespace/using-source-control-in-your-codespace#committing-your-changes) your final changes to your repository. *Note: You can also make quick edits using the [GitHub Dev Editor](https://docs.github.com/en/codespaces/the-githubdev-web-based-editor#opening-the-githubdev-editor).*

## Packages Available:

The environment for this week is built with the following environment.yml:

```yml
name: coding-exercise
dependencies:
  - python=3.11
  - pip
  - pip:
    - streamlit
    - pandas
    - numpy
```

*Note: you are welcome to install more pacakges in your codespace, but they will not be used by the autograder.*

---

**<font color='darkred'>DELETE THIS SECTION BEFORE SHARING WITH STUDENTS</font>**

## for instructors

- **Before sharing the template with students, <font color='darkred'>DELETE THE *autograder* DIRECTORY</font> and save it in a *private* repository.** Refer to the [autograder settings](https://gradescope-autograders.readthedocs.io/en/latest/autograder_settings.png) for more, but this is just an example.
- If you're running on a recent MacBook, you'll need to use [multi-platform building](https://docs.docker.com/build/building/multi-platform/#simple-multi-platform-build-using-emulation). For this, reference the command commented at the top of the *Dockerfile*.
- This repository (aside from the *autograder* directory) represents an example of a students's submission.
- The contents of the *autograder/tests* folder and the *results.json* file are only examples, and should be tailored to the exercise at hand.
  - Everything else in the *autograder* directory is meant to be generic for all exercises.
- See the [gradescope Python example](https://github.com/gradescope/autograder_samples/tree/master/python) for more on how this repo is organized.
- See [here](https://www.docker.com/blog/docker-best-practices-understanding-the-differences-between-add-and-copy-instructions-in-dockerfiles/) for the difference between `ADD` and `COPY` in Docker, explaining why the latter was used here.
- Note that you cannot `COPY` from a parent directory, so we need to add the environment update to the *run_autograder* file.
