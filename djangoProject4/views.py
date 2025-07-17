from django.shortcuts import render
from projects.models import Project



def main(request):
    # 2. Get all project objects from the database
    all_projects = Project.objects.all()

    # 3. Create the context dictionary to pass the data
    context = {
        'projects': all_projects
    }

    # 4. Pass the context to your template
    return render(request, 'main.html', context)

# Your about page view remains unchanged
def about(request):
    return render(request, 'about.html')
