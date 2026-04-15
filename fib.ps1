Param(
    [int]$n = 10
)

if ($n -le 0) { exit }

$a = 0
$b = 1
for ($i = 0; $i -lt $n; $i++) {
    Write-Output $a
    $temp = $a + $b
    $a = $b
    $b = $temp
}
