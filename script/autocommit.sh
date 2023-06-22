x=1
i=0
while [ $x -le 10 ]
do
	python getter.py
	line=$(head -n 1 instructions.txt)
	line=$(echo $line|tr -d '\n')
	filename="$line.json"
	mv -f "$line.json" ../divegrass/"$line.json"
	cd ..
	git add .
	if git diff-index --quiet HEAD
	then
		echo "No changes detected"
	else
		echo "Changes detected, committing"
		i=$(( $i + 1 ))
		git commit -m "Autocommit: matches from $line"
		git push
	fi
	cd script
	x=$(( $x + 1 ))
	sleep 2400
done
echo "Committed $i times"
