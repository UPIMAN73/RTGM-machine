package main

import (
	"fmt"

	"Map"
)

type Skill struct {
	Name        string
	Description string
	Power       int // Effect magnitude. Can be damage, healing, or any other metric.
	Cooldown    int // Time or turns to wait before using again.
}

type Item struct {
	Name        string
	Description string
	Effect      int // This can represent healing power, buff strength, etc.
}

type Weapon struct {
	Name        string
	Description string
	AttackPower int
	XP          int // Weapons Experience

	// TODO projectile based weapons
	// TODO Weapons Skills and added stats
	// TODO List of Magic Abilities
}

type Armor struct {
	Name         string
	Description  string
	DefensePower int
	MagicResist  int // Resistance to magic attacks.
}

type Magic struct {
	Name        string
	Description string
	Power       int // Magical damage or healing power.
	ManaCost    int // Cost to use this magic.
}

type Character struct {
	Name   string
	HP     int
	Mana   int // Magic resource, reduced when casting spells.
	Level  int
	XP     int // Experience points. Can be used for leveling up.
	Skills []Skill
	Items  []Item
	Weapon Weapon
	Armors []Armor // Characters might have multiple pieces: helmet, chestplate, etc.
	Magics []Magic
	// ... and potentially many other attributes like agility, strength, dexterity, etc.
}

func main() {
	// Example usage:
	cur_world := Map.World{Key: 1, Name: "test", Description: "Test World!"}

	// Create a skill
	fireball := Skill{Name: "Fireball", Description: "Throw a fiery ball.", Power: 50, Cooldown: 2}

	// Create a weapon
	sword := Weapon{Name: "Greatsword", Description: "A large, double-edged sword.", AttackPower: 75}

	// Create a character
	character := Character{
		Name:   "Aragon",
		HP:     100,
		Mana:   50,
		Level:  1,
		XP:     0,
		Skills: []Skill{fireball},
		Weapon: sword,
		// ... and so on
	}

	// Print character's name and weapon
	fmt.Println(character.Name + " wields the " + character.Weapon.Name)
	fmt.Println(cur_world.Key)
}
