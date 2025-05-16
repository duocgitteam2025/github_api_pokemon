# post-commit.ps1
Write-Host "Hook post-commit activado: Realizando push automático..."

# Realizamos el push automático a la rama actual
git push origin $(git branch --show-current)

if ($LASTEXITCODE -eq 0) {
    Write-Host "Push realizado correctamente!"
} else {
    Write-Host "Error al realizar el push, revisa la conexión o permisos."
}
