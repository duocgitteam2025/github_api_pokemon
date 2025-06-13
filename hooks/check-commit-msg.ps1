param (
    [string]$CommitMsgFile
)

# Leer el mensaje del commit
$CommitMsg = Get-Content $CommitMsgFile -Raw

# Definir el patrón que debe cumplir
$Pattern = '^(feat|fix): .+'

# Validar que el primer renglón del mensaje cumpla
if ($CommitMsg -notmatch $Pattern) {
    Write-Host "ERROR: El mensaje de commit debe comenzar con feat: o fix: seguido de un espacio y texto."
    exit 1
}