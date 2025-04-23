### CI Workflow Details:

- **Name**: CI
- **Workflow File**: [main.yml](https://github.com/Maoelan/mlflow-credit-scoring/blob/main/.github/workflows/main.yml)
- **Trigger Events**:
  - `push`
  - `pull_request`
- **Job Environment**: Runs on Ubuntu

---

### Workflow Steps:

1. Set up Python 3.12.7
2. Check environment variables
3. Install dependencies
4. Clean `mlruns` directory
5. Run MLflow project
6. Set up Git LFS (Large File Storage)
7. Save `mlruns` to repository
8. Upload to Google Drive

---

### Google Drive Link:
You can access the uploaded files on Google Drive:  
[Google Drive Folder](https://drive.google.com/drive/folders/1WVe4u-XA6lj2oodR4_XX25wE0COsDxs4?usp=sharing)

---

## Fixing Git Push Error (403 - Permission Denied)

If your workflow build fails with a 403 error (permission denied), follow these steps to resolve the issue:

1. **Update your `main.yml` workflow file** to use a token for pushing changes:

    ```yaml
    git push https://x-access-token:${{ secrets.GITHUB_TOKEN }}@github.com/${{ github.repository }}.git HEAD:main
    ```

2. **Add the following permissions** in your `main.yml` file to grant the necessary access:

    ```yaml
    permissions:
      contents: write
      actions: read
    ```

This should resolve the permission denial during the Git push process.
