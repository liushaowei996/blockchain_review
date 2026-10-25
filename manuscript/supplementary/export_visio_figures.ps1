param(
    [string]$SourcePath = (Join-Path (Split-Path $PSScriptRoot -Parent) 'figures\Figures-revised.vsdx'),
    [string]$OutputDirectory = (Join-Path (Split-Path $PSScriptRoot -Parent) 'figures')
)
# Export the retained, editable Visio pages without changing the source drawing.
# Requires Microsoft Visio for Windows. The supplied PDFs compile on any OS.
$ErrorActionPreference = 'Stop'
$source = (Resolve-Path -LiteralPath $SourcePath).Path
[void](New-Item -ItemType Directory -Path $OutputDirectory -Force)
$destination = (Resolve-Path -LiteralPath $OutputDirectory).Path
$names = @(
    'figure-01-reference-architecture', 'figure-02-assurance-chain',
    'figure-03-oal-framework', 'figure-04-dependency-threat',
    'figure-05-ctg-reasoning-loop', 'figure-06-blockchain-boundary',
    'figure-07-evidence-maturity'
)
$application = $null
$document = $null
try {
    $application = New-Object -ComObject Visio.InvisibleApp
    $application.AlertResponse = 7
    $document = $application.Documents.OpenEx($source, 2 + 64 + 128)
    for ($i = 0; $i -lt $names.Count; $i++) {
        $page = $document.Pages.Item(('Figure-{0:D2}' -f ($i + 1)))
        $pdf = Join-Path $destination ($names[$i] + '.pdf')
        # PDF, print intent, explicit page range; omit document properties.
        $document.ExportAsFixedFormat(1, $pdf, 1, 1, $page.Index, $page.Index,
            $false, $true, $false, $false, $false)
        Write-Output $pdf
    }
} finally {
    if ($null -ne $document) { $document.Saved = $true; $document.Close() }
    if ($null -ne $application) {
        $application.Quit()
        [void][Runtime.InteropServices.Marshal]::ReleaseComObject($application)
    }
}
