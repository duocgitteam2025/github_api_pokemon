Write-Host "Hook post-commit activado: Realizando push automático..."

git push origin $(git branch --show-current)

if ($LASTEXITCODE -eq 0) {
    Write-Host "Push realizado correctamente!"
} else {
    Write-Host "Error al realizar el push, revisa la conexión o permisos."
}
