param(
    [string]$SourcePath = (Join-Path (Split-Path $PSScriptRoot -Parent) 'figures\Figures-revised.vsdx'),
    [string]$PdfPath = (Join-Path (Split-Path $PSScriptRoot -Parent) 'figures\figure-03-oal-framework.pdf'),
    [string]$PythonExecutable = 'python'
)
# Run build_figures.py --data-only first. Only Figure 3 is changed/exported.
$ErrorActionPreference = 'Stop'
& $PythonExecutable (Join-Path $PSScriptRoot 'update_oal_visio.py') $SourcePath
if ($LASTEXITCODE -ne 0) { throw 'Native OAL data update failed.' }
$source = (Resolve-Path -LiteralPath $SourcePath).Path
$destination = [IO.Path]::GetFullPath($PdfPath)
$application = $null
$document = $null
try {
    $application = New-Object -ComObject Visio.InvisibleApp
    $application.AlertResponse = 7
    $document = $application.Documents.OpenEx($source, 2 + 64 + 128)
    $page = $document.Pages.Item('Figure-03')
    $document.ExportAsFixedFormat(1, $destination, 1, 1, $page.Index, $page.Index, $false, $true, $false, $false, $false)
    Write-Output 'Exported Figure 3. Other figure PDFs were not exported.'
} finally {
    if ($null -ne $document) { $document.Saved = $true; $document.Close() }
    if ($null -ne $application) {
        $application.Quit()
        [void][Runtime.InteropServices.Marshal]::ReleaseComObject($application)
    }
}
