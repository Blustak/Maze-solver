#! /usr/bin/env fish

if test -n "$PYENV_ROOT"
    source $PYENV_ROOT/versions/3.12.9/envs/Maze-solver/bin/activate.fish
else
    echo "Error, Maze-solver venv not found." >&2
    exit 1
end

python src/tests.py
