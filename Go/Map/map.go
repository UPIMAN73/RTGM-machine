package Map

type Position struct {
	World  uint16 // For World HashMap
	Region uint16 // For Region HashMap
	Zone   uint16 // For Zone HashMap
}

// Zone Structure
type Zone struct {
	Name        string
	Description string
	// Position Connections to other Zones (this includes other Regions & Worlds as well)
	Connections []Position 
}

// Region Structure
type Region struct {
	Name        string
	Description string
	zones = map[uint16]Zone	// Zones
}

// World Structure
type World struct {
	Name        string
	Description string
	Regions = map[uint16]Region	// Regions
}
