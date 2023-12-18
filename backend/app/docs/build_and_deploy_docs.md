---
title: Project Documentation
---

# Documentation Guide

In this project, we use MkDocs, a fast, simple and handsome static site generator that's geared towards building project documentation. It's written in Python and uses the Markdown language for input files.

## How is the documentation built?

The documentation for this project is built using MkDocs. When you write your documentation in markdown files (.md), MkDocs will use these files to generate a complete, navigable website for your project documentation.

To build your documentation, use the `mkdocs build` command. This will generate a new directory, named `site`, filled with your HTML files.

## Deployment on GitHub Pages

The documentation website is hosted on GitHub Pages. The `gh-pages` branch of the GitHub repository contains all the necessary files for the website.

To deploy the documentation to GitHub Pages, MkDocs will commit the `site` directory to the `gh-pages` branch and then push to GitHub.

Once this is pushed, GitHub will automatically serve the new documentation website under the `vanbuiten.github.io/sandbox` URL.

Therefore, anytime there is an update or change to the documentation, pushing the changes to the `gh-pages` branch will automatically deploy the new changes to the live site.

## Continuous Integration (CI)

This project uses a GitHub Actions workflow to automate the build and deployment process for the documentation.
