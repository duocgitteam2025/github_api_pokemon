Write-Host "======== Hook post-commit activado: Realizando push automático ========"

# Verifica en qué rama estás y haz el push
$currentBranch = git branch --show-current

if ($currentBranch) {
    git push origin $currentBranch

    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Push realizado correctamente en la rama: $currentBranch"
    } else {
        Write-Host "❌ Error al realizar el push. Revisa la conexión o permisos."
    }
} else {
    Write-Host "⚠️ No se detectó ninguna rama activa."
}
