# 1_creating_bash_scripts.md

You can run a single command that can gather all these information in just one shot.

zsh: command not found: free
"The command you need is vm_stat"
[Apple Stack Exchange](https://apple.stackexchange.com/questions/4286/is-there-a-mac-os-x-terminal-version-of-the-free-command-in-linux-systems)

echo "Starting at: $(date)"
echo

echo "UPTIME"
uptime
echo

echo "VM_STAT"
vm_stat
echo

echo "WHO"
who
echo

echo "Finishing at: $(date)"



##### Which command will correctly run a bash script?
	Answer: user@ubuntu:~$./bash_sample.sh
	A bash script is run with the .sh file extension

