class SimpleSchoolProjectRepository:
    def __init__(self):
        self.project_data = []

    def add_project(self, project_name, description, tags, author):
        new_project = {"project_name": project_name, "description": description, "tags": tags, "author": author}
        self.project_data.append(new_project)

    def get_projects(self):
        return self.project_data

    def update_project(self, project_id, updated_info):
        for project in self.project_data:
            if project["id"] == project_id:
                project.update(updated_info)
                break
        else:
            print("Project not found")

    def delete_project(self, project_id):
        for index, project in enumerate(self.project_data):
            if project["id"] == project_id:
                del self.project_data[index]
                break

# Usage example:
repository = SimpleSchoolProjectRepository()
project1 = {"project_name": "Learning AI", "description": "Introduction to machine learning and deep learning", "tags": ["machine-learning"], "author": "John Doe"}
print("Before adding a project:", repository.get_projects())
repository.add_project("AI Project 2", "Exploring new technology", ["algorithmic trading"], "Jane Smith")
print("After adding a new project:", repository.get_projects())

# Updating the description of an existing project
repository.update_project(1, {"project_name": "AI Project 3", "description": "Advanced machine learning techniques", "tags": ["algorithms", "machine-learning"], "author": "John Doe"})
print("After updating the project's description:", repository.get_projects())

# Deleting a project by its ID
repository.delete_project(1)
print("Project with id 1 has been deleted.")
