#! /usr/bin/env fish

if test -n "$PYENV_ROOT"
    source $PYENV_ROOT/versions/Maze-solver/bin/activate.fish
else
    echo "Error, virtualenv not found" >&2
    exit 1
end

python src/main.py
