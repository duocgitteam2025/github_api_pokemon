Write-Host "Running pytest..."
pytest
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Tests failed. Push cancelled."
    exit 1
}

Write-Host "Running bandit security scan..."
bandit -r . -ll --skip B101,B102
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Bandit found security issues. Push cancelled."
    exit 1
}

Write-Host "✅ Pre-push checks passed."
exit 0
