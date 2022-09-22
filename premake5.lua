workspace "glm"
	configuration {"Release"}


project "glm"
	location "."
	prebuildcommands("python ./scripts/prebuildcommandes.py")

	files {
		"glm/**.hpp",
		"glm/**.inl"
	}