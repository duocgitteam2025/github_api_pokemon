Write-Host "Verificando conflictos antes del merge..."

# Verificar conflictos
if (git diff --name-only --diff-filter=U) {
    Write-Host "❌ Existen conflictos sin resolver. No se puede realizar el merge."
    exit 1
}

# Verificar errores de sintaxis
Write-Host "Revisando errores de sintaxis..."
python -m py_compile $(git diff --name-only --diff-filter=ACM)

if ($LASTEXITCODE -eq 0) {
    Write-Host "✔ Sin conflictos ni errores de sintaxis. Listo para merge."
    exit 0
} else {
    Write-Host "❌ Errores de sintaxis encontrados. Corrige antes de hacer merge."
    exit 1
}
