# Publish this ready-to-upload project on GitHub

**Recommended repository name:** `bike-purchase-behaviour-excel-analysis`  
**Visibility:** Public (if you want recruiters to view it).  
**Description:** Excel customer segmentation and interactive bike purchase dashboard with validated insights.

## Option A: GitHub website (no Git required)

1. Sign in at https://github.com and select **New repository**.
2. Enter the recommended name and a short description. Choose **Public**. Do not ask GitHub to add a README because this package already includes one.
3. Create the empty repository.
4. Extract the ZIP package. Open the extracted `bike-purchase-behaviour-excel-analysis` folder.
5. On GitHub, choose **uploading an existing file** / **Add file → Upload files**. Drag the **files and folders inside** the extracted project folder into the upload area, not the ZIP itself. Preserve folder paths. If the website does not preserve folders with your browser, upload by folder path or use Option B.
6. Add commit message: `Add Excel bike purchase portfolio case study`. Commit to `main`.
7. Verify that your README renders the dashboard image and that the workbook download works.
8. Pin the new repository to your GitHub profile and share its URL on your CV or LinkedIn.

## Option B: Git command line (preserves all folders)

Create the empty GitHub repository first, without initializing README or other files. In a terminal, navigate into the extracted project folder and run:

```bash
git init
git add .
git commit -m "Add bike purchase Excel portfolio analysis"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/bike-purchase-behaviour-excel-analysis.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username. GitHub may prompt you to authenticate. If your Git identity is not set up, configure `git config --global user.name` and `git config --global user.email` first.

## What to check once published

- GitHub's front page shows your real `README.md`, not a ZIP file.
- The main dashboard screenshot displays under the title.
- The XLSX has seven working worksheets and can be downloaded.
- The cleaned CSV has **1,000** rows plus a header.
- From a terminal, `python scripts/validate_metrics.py` completes successfully.
- Data source and educational limitations are visible in the README.

## Recruiter-friendly presentation

Use the repo URL on your LinkedIn Featured section or CV. Add one bullet showing data cleaning, a second showing your dashboard, and a third communicating the strongest measured insight. The `docs/PORTFOLIO_PRESENTATION.md` file has ready-to-edit copy.

**Connection note:** An automated creation of a repository in your GitHub account requires a connected account with permission to create repositories. This ZIP is complete and can be published immediately using either option above.