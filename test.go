package main

import (
	"encoding/json"
	"fmt"
	"os"
	// "Map"
)

type Position struct {
	World  uint16 // For World HashMap
	Region uint16 // For Region HashMap
	Zone   uint16 // For Zone HashMap
}

type Zone struct {
	Name        string
	Description string
	Connections []Position
}

type Region struct {
	Name        string
	Description string
	Zones       map[uint16]Zone
}

type World struct {
	Name        string
	Description string
	Regions     map[uint16]Region
}

func main() {
	// Sample data
	// Serialize to JSON
	data, err := os.ReadFile("./test_map.json")
	var cur_world World
	fmt.Println(data)
	json.Unmarshal(data, &cur_world)
	if err != nil {
		fmt.Println("Error serializing to JSON:", err)
		return
	}

	// Print serialized JSON
	fmt.Println(cur_world)
}
