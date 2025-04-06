class SimpleSchoolProject:
    def __init__(self):
        self.project_name = "Simple School Project"
        self.description = "A simple school project repository."

    def add_project(self, name, description):
        new_project = {"name": name, "description": description}
        return new_project

    def delete_project(self, name):
        projects = self.get_projects()
        for project in projects:
            if project["name"] == name:
                self.remove_project(project)
                break
        else:
            print("Project not found.")

    def update_project(self, name, updated_description):
        projects = self.get_projects()
        for project in projects:
            if project["name"] == name:
                project.update(updated_description)
                break
        else:
            print(f"Project {name} not found.")
