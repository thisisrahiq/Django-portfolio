import os
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage

# ── Admin credentials (set 'ADMIN_PASSWORD' in Railway variables) ──
ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'portfolio2025')


def home(request):
    context = {
        'name': 'Rahiq Al Makhtum',
        'title': 'Full Stack Developer',
        'email': 'rahiq_1@outlook.com',
        'phone': '(+880) 01790584856',
        'linkedin': 'https://linkedin.com/in/thisisrahiq',
        'github': 'https://github.com/thisisrahiq',
        'location': 'Chattogram, Bangladesh',
        'about': "I'm a full stack developer with 3+ years of experience building web applications using React, Node.js, and Python. I've worked across Bangladesh, Germany, and China — which has given me a solid appreciation for clear communication and adaptable engineering. Currently open to freelance and contract work.",
        'skills': [
            {'category': 'Frontend', 'items': ['React.js', 'JavaScript', 'Tailwind CSS', 'DaisyUI', 'HTML/CSS']},
            {'category': 'Backend', 'items': ['Node.js', 'Express.js', 'Django', 'Python', 'REST APIs']},
            {'category': 'Database', 'items': ['MongoDB', 'PostgreSQL', 'MySQL']},
            {'category': 'Tools', 'items': ['Git', 'GitHub', 'Docker', 'Railway']},
        ],
        'experience': [
            {
                'title': 'Full Stack Developer',
                'company': 'Diganta Homes Limited',
                'location': 'Chattogram, Bangladesh',
                'period': 'Jan 2025 – Present',
                'points': [
                    'Built form-driven workflows using React and RESTful backend APIs.',
                    'Reduced form submission errors by ~35% through structured input validation.',
                    'Optimized data storage schemas for high-frequency submissions.',
                ]
            },
            {
                'title': 'Software Engineer Intern',
                'company': 'Chengdu Suncaper Data Co. Ltd.',
                'location': 'Chengdu, China',
                'period': 'Jan – Jun 2021',
                'points': [
                    'Led development of a Java-based e-commerce platform for large-scale inventory.',
                    'Optimized backend queries for faster search and navigation.',
                    'Authored technical documentation and analytics reports.',
                ]
            },
            {
                'title': 'IT Engineering Intern',
                'company': 'Kabir Steel Re-Rolling Mills Ltd.',
                'location': 'Chattogram, Bangladesh',
                'period': 'Feb – May 2022',
                'points': [
                    'Resolved network issues to improve system uptime.',
                    'Assisted in hardware configuration and authored IT documentation.',
                ]
            },
        ],
        'projects': [
            {
                'title': 'IBN Sina Health Card Generator',
                'description': 'A full-stack Django web app that generates and manages health cards for families and members. Features photo upload, Google Drive image embedding, print-ready card layout, and fixture-based data management.',
                'tags': ['Python', 'Django', 'PostgreSQL', 'Railway', 'Bootstrap'],
                'type': 'Full-Stack App',
                'live': 'https://health-card.up.railway.app',
                'github': 'https://github.com/thisisrahiq/Health_card',
                'tech_icons': [
                    {'src': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg', 'label': 'Python'},
                    {'src': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg', 'label': 'Django', 'filter': 'brightness(0) invert(1)'},
                    {'src': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg', 'label': 'PostgreSQL'},
                    {'src': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bootstrap/bootstrap-original.svg', 'label': 'Bootstrap'},
                    {'src': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg', 'label': 'Docker'},
                ],
            },
            {
                'title': 'CPSC Alumni Association Website',
                'description': 'A clean, responsive static website built for the CPSC Alumni Association. Features sections for news, events, member directory, and contact — designed to keep the community connected.',
                'tags': ['HTML5', 'CSS3', 'JavaScript', 'Responsive Design'],
                'type': 'Frontend Website',
                'live': 'https://cpsc-alumni.org/#home',
                'github': 'https://github.com/thisisrahiq/CPSC-Alumni-Website',
                'tech_icons': [
                    {'src': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg', 'label': 'HTML5'},
                    {'src': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg', 'label': 'CSS3'},
                    {'src': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg', 'label': 'JavaScript'},
                    {'src': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/figma/figma-original.svg', 'label': 'Figma'},
                ],
            },
            {
                'title': "Coach's Weekly Planner",
                'description': 'A productivity tool built for gym and fitness coaches to plan, schedule, and track client workout sessions week by week. Features a drag-and-drop interface, session notes, and weekly summaries.',
                'tags': ['React', 'JavaScript', 'CSS3', 'Local Storage'],
                'type': 'Web App',
                'live': 'https://thisisrahiq.github.io/gymTrainersList/',
                'github': 'https://github.com/thisisrahiq/gymTrainersList',
                'tech_icons': [
                    {'src': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg', 'label': 'React'},
                    {'src': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg', 'label': 'JavaScript'},
                    {'src': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg', 'label': 'CSS3'},
                    {'src': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nodejs/nodejs-original.svg', 'label': 'Node.js'},
                ],
            },
        ],
        'education': [
            {
                'degree': 'M.Sc. Computer Science (Coursework Completed)',
                'school': 'University of Passau',
                'location': 'Passau, Germany',
                'period': '2023 – 2024',
                'note': '',
            },
            {
                'degree': 'B.Eng. Software Engineering',
                'school': 'Sichuan University',
                'location': 'Chengdu, China',
                'period': '2018 – 2021',
                'note': 'GPA: 3.27 / 4.0',
            },
        ],
    }
    return render(request, 'home.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message_text = request.POST.get('message', '').strip()

        if name and email and message_text:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message_text,
            )
            messages.success(request, f"Thanks {name}! Your message has been received. I'll get back to you within 24 hours.")
        else:
            messages.error(request, "Please fill in all required fields (Name, Email, Message).")

    return redirect('home')


def admin_login(request):
    error = None
    if request.method == 'POST':
        password = request.POST.get('password', '')
        if password == ADMIN_PASSWORD:
            request.session['admin_auth'] = True
            return redirect('admin_panel')
        else:
            error = 'Incorrect password. Please try again.'
    return render(request, 'admin_login.html', {'error': error})


def admin_logout(request):
    request.session.flush()
    return redirect('admin_login')


def admin_panel(request):
    if not request.session.get('admin_auth'):
        return redirect('admin_login')

    # Mark message as read when expanded
    mark_read_id = request.GET.get('mark_read')
    if mark_read_id:
        ContactMessage.objects.filter(pk=mark_read_id).update(is_read=True)
        return redirect('admin_panel')

    # Delete message
    delete_id = request.GET.get('delete')
    if delete_id:
        ContactMessage.objects.filter(pk=delete_id).delete()
        return redirect('admin_panel')

    all_messages = ContactMessage.objects.all()
    unread_count = all_messages.filter(is_read=False).count()
    total_count = all_messages.count()

    return render(request, 'admin_panel.html', {
        'messages_list': all_messages,
        'unread_count': unread_count,
        'total_count': total_count,
    })
