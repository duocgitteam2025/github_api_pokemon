# Obtener la ruta absoluta del proyecto
$projectRoot = Resolve-Path "$PSScriptRoot\.."
$excludeDirs = @("$projectRoot\myvenv", "$projectRoot\.git", "$projectRoot\__pycache__")

Write-Host "Running pytest..."
pytest
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Tests failed. Push cancelled."
    exit 1
}

Write-Host "Running bandit security scan (excluding virtual env)..."

# Construir cadena --exclude para Bandit
$excludeString = ($excludeDirs -join ",").Replace("\", "/")  # Convertir a formato Unix
bandit -r "$projectRoot" -ll --exclude "$excludeString" --skip B101,B102

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Bandit found security issues. Push cancelled."
    exit 1
}

Write-Host "✅ Pre-push checks passed. Proceeding with push."
exit 0
