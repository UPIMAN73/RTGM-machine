package Map

type Position struct {
	World  uint16 // For World HashMap
	Region uint16 // For Region HashMap
	Zone   uint16 // For Zone HashMap
}

// Zone Structure
type Zone struct {
	Name        string `json:"name"`
	Description string `json:"description"`
	// Position Connections to other Zones (this includes other Regions & Worlds as well)
	Connections []Position
}

// Region Structure
type Region struct {
	Name        string          `json:"name"`
	Description string          `json:"description"`
	zones       map[uint16]Zone // Zones
}

// World Structure
type World struct {
	Name        string            `json:"name"`
	Description string            `json:"description"`
	Regions     map[uint16]Region // Regions
}
