# Credit Scoring MLflow Project

## CI Workflow Details

- **Workflow Name**: CI  
- **Workflow File**: [main.yml](https://github.com/Maoelan/mlflow-credit-scoring/blob/main/.github/workflows/main.yml)  
- **Trigger Events**:  
  - `push`  
  - `pull_request`  
- **Job Environment**: Ubuntu

---

## Workflow Steps

1. **Set up Python 3.12.7**  
   Configure Python version for the project.

2. **Check Environment Variables**  
   Ensure all necessary environment variables are available.

3. **Install Dependencies**  
   Install all the required dependencies for the project.

4. **Clean `mlruns` Directory**  
   Remove any previous logs from the `mlruns` directory.

5. **Run MLflow Project**  
   Execute the MLflow project with the necessary configurations.

6. **Set up Git LFS (Large File Storage)**  
   Initialize Git LFS for handling large files.

7. **Save `mlruns` to Repository**  
   Save the MLflow logs and artifacts back into the repository.

8. **Upload `mlruns` to Google Drive**  
   Upload the resulting `mlruns` folder to Google Drive for storage.

---

## Google Drive Output

📁 [Google Drive Folder](https://drive.google.com/drive/folders/1WVe4u-XA6lj2oodR4_XX25wE0COsDxs4?usp=sharing)

---

## Fixing Git Push Error (403 - Permission Denied)

If your workflow fails due to a 403 permission error when pushing to GitHub, follow these steps:

1. **Update your `main.yml` Workflow to Use the GitHub Token**:

    Add the following to use the GitHub token for pushing changes:

    ```yaml
    git push https://x-access-token:${{ secrets.GITHUB_TOKEN }}@github.com/${{ github.repository }}.git HEAD:main
    ```

2. **Set Permissions in `main.yml`**:

    Ensure the following permissions are included for the necessary access:

    ```yaml
    permissions:
      contents: write
      actions: read
    ```

---

## Fixing Google Drive Upload Failures

If you encounter issues uploading to Google Drive, follow these steps:

1. **Check Google Drive Folder Permissions**:  
   Ensure that the Google Drive folder is shared with the service account or user as an **Editor**.

2. **Verify Google Drive API Settings**:  
   Make sure the Google Drive API is enabled for your Google Cloud project and that the credentials are correctly configured.

3. **Verify Folder ID**:  
   Double-check the `GDRIVE_FOLDER_ID` environment variable to ensure it's correct and points to the right folder.

---

## Serve the Model via REST API

To serve the model as a REST API, use the following command:

```bash
mlflow models serve -m "models:/serve-model/3" --port 5002 --no-conda
```

This will expose the model on port `5002` for HTTP requests.

---

## Prediction via cURL

### 1. Check if the Server is Running:

To check if the server is running, use the following `curl` command to perform a health check:

```bash
curl.exe -I http://127.0.0.1:5002/health
```

### 2. Send Prediction Request with JSON Input:

To send a prediction request, use the following `curl` command with your input data:

```bash
curl.exe -X POST http://127.0.0.1:5002/invocations -H "Content-Type: application/json" --data-binary "@input.json"
```

Make sure `input.json` contains the necessary data for the prediction.

---

## Important Notes

- ✅ Make sure the Google Drive folder is shared with your service account or user as an Editor  
- 🔑 Use the correct Google Drive API credentials and enable the API in your Google Cloud Console  
- 📁 Double-check your GDRIVE_FOLDER_ID and ensure it’s valid  
- 🚀 Ensure the MLflow model server is running locally before sending prediction requests
