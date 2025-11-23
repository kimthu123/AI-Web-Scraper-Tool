<?php
@set_time_limit(60);
header('Expires: 0');
header('Cache-Control: no-store');

$q = isset($_GET['q']) ? trim($_GET['q']) : '';
$limit = isset($_GET['limit']) ? intval($_GET['limit']) : 10;

if ($q === '') {
  http_response_code(400);
  header('Content-Type: application/json; charset=utf-8');
  echo json_encode(['error' => "Missing 'q'"]);
  exit;
}

// 1) Set your Python path (use:  py -c "import sys; print(sys.executable)")
$PY = 'py'; // or 'python' or full path like 'C:\\Users\\YOU\\AppData\\Local\\Programs\\Python\\Python311\\python.exe'
$SCRIPT = __DIR__ . DIRECTORY_SEPARATOR . 'run_scraper.py';

// 2) Build command
$cmd = [$PY, $SCRIPT, $q, (string)$limit];

// 3) Run & capture
$spec = [1 => ['pipe','w'], 2 => ['pipe','w']];
$proc = proc_open($cmd, $spec, $pipes, __DIR__, $_ENV);
if (!is_resource($proc)) {
  http_response_code(500);
  header('Content-Type: application/json; charset=utf-8');
  echo json_encode(['error' => 'Failed to start Python process.']);
  exit;
}
$stdout = stream_get_contents($pipes[1]); fclose($pipes[1]);
$stderr = stream_get_contents($pipes[2]); fclose($pipes[2]);
$status = proc_close($proc);

// 4) If Python errored, show details
if ($status !== 0) {
  http_response_code(500);
  header('Content-Type: text/plain; charset=utf-8');
  echo "Python exit code: $status\n\nSTDERR:\n$stderr\n\nSTDOUT:\n$stdout";
  exit;
}

// 5) Parse JSON
$json = json_decode($stdout, true);
if ($json === null && json_last_error() !== JSON_ERROR_NONE) {
  http_response_code(500);
  header('Content-Type: text/plain; charset=utf-8');
  echo "Non-JSON output from Python:\n\n$stdout\n\nSTDERR:\n$stderr";
  exit;
}

header('Content-Type: application/json; charset=utf-8');
echo $stdout;
