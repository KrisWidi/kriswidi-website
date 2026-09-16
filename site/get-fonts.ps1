# KWiDi – lädt Fraunces und Jost von Google Fonts und legt sie lokal ab (DSGVO: keine Google-Verbindung auf der Website).
# Doppelklick auf get-fonts.bat oder: powershell -ExecutionPolicy Bypass -File get-fonts.ps1
$ErrorActionPreference = "Stop"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$targets = @("$here\docs\assets", "$here\..\docs\assets", "$here\dist\assets", "$here\..\dist\assets", "$here\site\assets", "$here\assets") | Where-Object { Test-Path $_ } | ForEach-Object { Join-Path $_ "fonts" }
if (-not $targets) { throw "Kein assets-Ordner gefunden – Skript neben docs/ oder in site/ ablegen." }
$ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
$css = Invoke-WebRequest -UseBasicParsing -Headers @{ "User-Agent" = $ua } "https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..700;1,9..144,300..700&family=Jost:wght@100..900&display=swap"
$blocks = ($css.Content -split "@font-face") | Where-Object { $_ -match "unicode-range: U\+0000-00FF" }
function Pick($family, $style) {
  $b = $blocks | Where-Object { $_ -match "font-family: '$family'" -and $_ -match "font-style: $style" } | Select-Object -First 1
  if (-not $b) { throw "Kein Font-Block für $family $style gefunden" }
  return [regex]::Match($b, "url\((https://[^)]+)\)").Groups[1].Value
}
$map = @{
  "Fraunces-Variable.woff2"        = Pick "Fraunces" "normal"
  "Fraunces-Italic-Variable.woff2" = Pick "Fraunces" "italic"
  "Jost-Variable.woff2"            = Pick "Jost" "normal"
}
foreach ($t in $targets) {
  New-Item -ItemType Directory -Force -Path $t | Out-Null
  foreach ($k in $map.Keys) {
    Invoke-WebRequest -UseBasicParsing -Headers @{ "User-Agent" = $ua } $map[$k] -OutFile (Join-Path $t $k)
    Write-Host "OK  $k -> $t"
  }
}
Write-Host "`nFertig. Die drei Schriftdateien liegen in assets/fonts (site und docs). Jetzt auf GitHub hochladen."
