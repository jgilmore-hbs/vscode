#!/usr/bin/env sh

n=10
if [ "$#" -gt 0 ]; then
  n="$1"
fi

case "$n" in
""|*[!0-9]*)
  echo "Usage: $0 [count]" >&2
  exit 1
  ;;
*)
  ;;
esac

a=0
b=1
i=0
while [ "$i" -lt "$n" ]; do
  printf "%s\n" "$a"
  tmp=$((a + b))
  a=$b
  b=$tmp
  i=$((i + 1))
done
