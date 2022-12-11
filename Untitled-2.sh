a=$(echo $(curl https://api.openai.com/v1/completions -H "Content-Type: application/json" -H "Authorization: Bearer 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" -d '{"model": "text-davinci-003", "prompt": "I am trying to write a web application. What backend frameworks could I use, and what are their pros and cons?", "temperature": 1, "max_tokens": 100}'))
b=$(echo $a | jq -r '.choices[0] | {text} | join(" ")')
echo -e "$a\n\n\n"
echo -e $b