// Global variables are defined in data.js

init();

// Initializes the site by loading everything neccessary
function init() {
	loadProjects(projects);
}

// Loads projects from Projects and displays them according to the category
function loadProjects(parent) {
	parent.innerHTML = "";
	for (var article in Articles)
		addProject(Articles[article], parent);
}

// Adds a project and displays
function addProject(project, parent) {
	var html = generateHTML(project.Name, project.Description, project.Link, project.Date);
	parent.innerHTML += html;
}

// Generates the HTML of a project
function generateHTML(name, description, link, date) {
	var header = '<div><a href="articles/' + link + '/index.html"><img src="articles/' + link + '/cover.png' + '"></a>';
	var h1 = '<h1><a class="underline" href="articles/' + link + '/index.html">' + name + '</a></h1>';
	var date = "<i>Last updated: " + date + "</i>"
	var p = "<p>" + description + "</p>";
	return header + h1 + date + p + "</div>";
}
