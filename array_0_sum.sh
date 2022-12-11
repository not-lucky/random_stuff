
echo "Enter size of the array: "
read n

echo "Enter the elements of the array (only numeric characters): "
for ((i = 0; i < n; i++)); do
    read arr[$i]
done

sum=0
bad=0

for ((i = 0; i < n; i++)); do
    sum=$((sum + ${arr[$i]}))
done

if [[ $sum -eq 0 ]]; then
    echo "Error: All elements in the array are 0."
    bad=1
fi

if [[ $bad -eq 0 ]]; then
    sum=0
    for ((i = 0; i < n; i++)); do
        index=$i

        while [[ ${arr[$index]} -eq 0 ]]; do
            index=$(($index - 1))
            if [[ $index -lt 0 ]]; then
                index=$(($n - 1))
            fi
        done

        sum=$(($sum + ${arr[$index]}))
    done
    echo $sum
fi
