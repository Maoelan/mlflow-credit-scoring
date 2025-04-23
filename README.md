## Fixing Git Push Error (403 - Permission Denied)

If the workflow build fails due to a 403 error (permission denied), follow these steps:

1. Update your `main.yaml` workflow file with the following command to push changes:

    ```yaml
    git push https://x-access-token:${{ secrets.GITHUB_TOKEN }}@github.com/${{ github.repository }}.git HEAD:main
    ```

2. Add the following permissions to your `main.yaml` to allow the necessary access:

    ```yaml
    permissions:
      contents: write
      actions: read
    ```

This should resolve the issue with permission denial during the Git push process.
