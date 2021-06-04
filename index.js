// Global variables are defined in data.js

init();

function init() // Initializes the site by loading everything neccessary
{
	loadProjects(projects);
}

function loadProjects(parent) // Loads projects from Projects and displays them according to the category
{
	parent.innerHTML = "";
	var sorted_articles = []
	for (var article in Articles)
		sorted_articles.push(Articles[article])
	sorted_articles.sort((a, b) => {
		let a_val = (new Date(a["Date"])).valueOf();
		let b_val = (new Date(b["Date"])).valueOf();
		return b_val - a_val;
	});
	console.log(sorted_articles);
	for (var article in sorted_articles)
		addProject(sorted_articles[article], parent);
}

function addProject(project, parent) // Adds a project and displays
{
	var html = generateHTML(project.Name, project.Description, project.Link, project.Date);
	parent.innerHTML += html;
}

function generateHTML(name, description, link, date) // Generates the HTML of a project
{
	var header = '<div><a href="' + link + '/index.html"><img src="' + link + '/cover.png' + '"></a>';
	var h1 = '<h1><a class="underline" href="' + link + '/index.html">' + name + '</a></h1>';
	var date = "<i>Last updated: " + date + "</i>"
	var p = "<p>" + description + "</p>";
	return header + h1 + date + p + "</div>";
}
