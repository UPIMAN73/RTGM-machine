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
	Connections []Position // Position Connections to other Nodes
}

// Region Structure
type Region struct {
	Name        string
	Description string
	// Zones
}

// World Structure
type World struct {
	Name        string
	Description string
	// Regions
}
