# Stem Sims

A collaborative, open source collection of mathematical simulations, implemented across different programming languages.

## What is this?

Stem Sims is a growing library of maths focused simulations. Each simulation explores a mathematical idea by modelling it in code, often in more than one language.

The goal is not just to show results, but to make abstract maths tangible through experimentation and comparison.

## Why does this exist?

Most mathematical examples and simulations are locked into a single language or framework. That makes them harder to compare, harder to port, and harder to learn from if you do not already know that ecosystem.

This repo is language agnostic and maths first. The same idea can live side by side in Python, Swift, JavaScript, C, Rust, or anything else.

Seeing the same simulation expressed in different languages helps you understand both the maths and the code more deeply.

## What belongs here?

Anything that is fundamentally mathematical and benefits from being simulated, for example:

- probability experiments
- stochastic processes and random walks
- graph theory and network algorithms
- statistical simulations
- numerical methods
- physics inspired models

If it helps someone explore or understand a mathematical idea, it probably fits.

## Structure (loose, not strict)

Simulations generally live in their own directory and may include multiple implementations in different languages.

A common pattern looks like:

```
coin_toss/
    coin_toss.py
    coin_toss.swift
    coin_toss.js
```

Some simulations may also include a short README explaining the maths behind them.

This structure is not enforced, but clarity and consistency are encouraged.

## Contributing

There is no heavy process here.

You can contribute by:
- adding a new simulation
- porting an existing simulation to a new language
- improving explanations or documentation
- cleaning up or simplifying code

Good contributions usually have:
- clear, readable code
- minimal dependencies
- comments or notes explaining the maths
- code that can be run without complex setup

Clarity matters more than cleverness.

## Philosophy

- maths first, code second
- simple over clever
- readable over optimised
- comparison over perfection

This is a place to explore ideas, not to show off.

## Closing note

If you enjoy maths, simulations, or translating ideas between programming languages, you will probably feel at home here.

Feel free to explore, experiment, and contribute.
