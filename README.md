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
7. Save `mlruns` to the repository
8. Upload to Google Drive

---

### Google Drive Link:
[Google Drive Folder](https://drive.google.com/drive/folders/1WVe4u-XA6lj2oodR4_XX25wE0COsDxs4?usp=sharing)

## Fixing Git Push Error (403 - Permission Denied)

If your workflow build fails due to a 403 error (permission denied), follow these steps to resolve the issue:

1. **Update your `main.yaml` workflow file** to use a token for pushing changes:

    ```yaml
    git push https://x-access-token:${{ secrets.GITHUB_TOKEN }}@github.com/${{ github.repository }}.git HEAD:main
    ```

2. **Add the following permissions** in your `main.yaml` file to grant the necessary access:

    ```yaml
    permissions:
      contents: write
      actions: read
    ```

This should resolve the permission denial during the Git push process.

## Fixing Failed Upload to Google Drive

If you encounter issues uploading files to Google Drive, ensure the following:

1. **Set proper permissions for the Google Drive folder**:
   - Make sure that the Google Drive folder is shared with the service account or your user as an **Editor**.
   - This will allow the script to upload files properly.

2. **Check the Google Drive API**:
   - Ensure that your Google Drive API is enabled for the project.
   - Ensure the credentials are correctly configured.

3. **Verify Folder ID**:
   - Double-check the `GDRIVE_FOLDER_ID` environment variable to ensure it's correct and refers to the proper folder.
   - Ensure that the folder ID is not malformed or missing.

Once these steps are applied, your CI workflow should be able to push to GitHub and upload files to Google Drive successfully.

---

### Important Notes:
- **Don't forget to change the permissions on the Google Drive folder** to allow the service account or user to have Editor access.
