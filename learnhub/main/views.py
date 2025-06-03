from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages


def home(request):
    return render(request, 'main/home.html')

def cover(request):
    articles = generate_articles()
    return render(request, 'main/cover.html', {'articles': articles})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('cover')  # Redirect to cover page on successful login
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'main/login.html')

def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use")
        else:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, "Account created successfully. Please login.")
            return redirect('login')

    return render(request, 'main/register.html')
from django.shortcuts import render

def cover(request):
    articles = [
        {
            'type': 'AI Tutors Revolutionizing Personalized Learning',
            'title': 'AI Tutors Revolutionizing Personalized Learning',
            'desc': 'AI-driven tutors are transforming education by adapting lessons to individual student needs. These systems analyze performance data to provide tailored explanations and practice exercises, helping learners master concepts faster. This personalized approach enhances engagement and retention, bridging gaps caused by large class sizes or limited access to expert teachers.'
        },
        {
            'type': 'Blockchain Securing Academic Credentials',
            'title': 'Blockchain Securing Academic Credentials',
            'desc': 'Blockchain technology is emerging as a reliable solution for issuing and verifying academic certificates. By storing credentials on an immutable ledger, it prevents fraud and simplifies verification for employers and institutions. This innovation fosters trust and enables global portability of qualifications.'
        },
        {
            'type': 'Virtual Reality Enhancing Immersive Learning',
            'title': 'Virtual Reality Enhancing Immersive Learning',
            'desc': 'Virtual Reality (VR) creates immersive educational environments where students can explore complex subjects firsthand. From virtual labs to historical recreations, VR engages multiple senses and supports experiential learning, making abstract concepts tangible and improving knowledge retention.'
        },
        {
            'type': 'AI-Powered Grading Systems Improving Efficiency',
            'title': 'AI-Powered Grading Systems Improving Efficiency',
            'desc': 'AI systems are automating grading of essays, exams, and assignments, allowing educators to focus more on teaching. These tools analyze content for accuracy and coherence, providing consistent, unbiased feedback while speeding up assessment processes.'
        },
        {
            'type': '5G Networks Enabling Real-Time Remote Learning',
            'title': '5G Networks Enabling Real-Time Remote Learning',
            'desc': 'The rollout of 5G technology supports high-speed, low-latency connections crucial for seamless remote education. It enables live streaming of high-quality lectures and interactive sessions, ensuring students in remote areas receive the same learning experience as their urban counterparts.'
        },
        {
            'type': 'Data Analytics Driving Student Success Prediction',
            'title': 'Data Analytics Driving Student Success Prediction',
            'desc': 'Educational institutions increasingly use data analytics to identify at-risk students early. By tracking attendance, engagement, and performance trends, educators can intervene with personalized support, reducing dropout rates and improving overall success.'
        },
        {
            'type': 'Microlearning Platforms for Busy Professionals',
            'title': 'Microlearning Platforms for Busy Professionals',
            'desc': 'Microlearning offers bite-sized educational content accessible anytime, perfect for working professionals. These platforms deliver targeted lessons focused on specific skills, enabling efficient learning without overwhelming schedules.'
        },
        {
            'type': 'Gamification Increasing Student Motivation',
            'title': 'Gamification Increasing Student Motivation',
            'desc': 'Gamification incorporates game mechanics into learning to boost engagement and motivation. Points, badges, and leaderboards make education fun and competitive, encouraging students to persist and achieve goals.'
        },
        {
            'type': 'AI Ethics Education Preparing Future Innovators',
            'title': 'AI Ethics Education Preparing Future Innovators',
            'desc': 'As AI technologies advance, educating students about ethical considerations is critical. Curriculums are integrating AI ethics to teach responsible development and use, ensuring future innovators prioritize societal well-being.'
        },
        {
            'type': 'Cloud Computing Supporting Scalable E-Learning',
            'title': 'Cloud Computing Supporting Scalable E-Learning',
            'desc': 'Cloud-based platforms provide scalable infrastructure for online courses, allowing institutions to serve large numbers of students globally. Cloud computing also supports storage, collaboration tools, and AI integrations.'
        },
        {
            'type': 'Augmented Reality for Interactive Science Classes',
            'title': 'Augmented Reality for Interactive Science Classes',
            'desc': 'Augmented Reality (AR) overlays digital information onto the real world, enhancing science education. Students can interact with 3D models of molecules or ecosystems, fostering deeper understanding through visualization.'
        },
        {
            'type': 'AI Chatbots Enhancing Student Support Services',
            'title': 'AI Chatbots Enhancing Student Support Services',
            'desc': 'AI chatbots provide instant answers to student queries, from course information to technical support. Available 24/7, they improve accessibility and reduce workload for administrative staff.'
        },
        {
            'type': 'Wearable Tech Monitoring Student Health and Focus',
            'title': 'Wearable Tech Monitoring Student Health and Focus',
            'desc': 'Wearable devices track physiological data like heart rate and attention levels during lessons. This real-time monitoring helps educators tailor activities to maintain student well-being and optimize learning conditions.'
        },
        {
            'type': 'Open Educational Resources Expanding Access to Knowledge',
            'title': 'Open Educational Resources Expanding Access to Knowledge',
            'desc': 'Open Educational Resources (OER) provide free, high-quality learning materials online, democratizing education worldwide. These resources support self-paced learning and supplement traditional teaching.'
        },
        {
            'type': 'AI-Driven Language Learning Apps',
            'title': 'AI-Driven Language Learning Apps',
            'desc': 'Language apps use AI to personalize vocabulary and grammar exercises based on learner progress. Speech recognition and feedback improve pronunciation and conversational skills effectively.'
        },
        {
            'type': 'Cybersecurity Training for Students in the Digital Age',
            'title': 'Cybersecurity Training for Students in the Digital Age',
            'desc': 'With increasing online activity, cybersecurity education is vital. Programs teach students safe internet practices, data protection, and threat awareness, preparing them for a digital future.'
        },
        {
            'type': 'EdTech Startups Innovating Hybrid Learning Models',
            'title': 'EdTech Startups Innovating Hybrid Learning Models',
            'desc': 'Startups are developing platforms that blend online and in-person education, offering flexible learning tailored to different needs. These hybrid models maximize accessibility without sacrificing interaction quality.'
        },
        {
            'type': 'AI-Assisted Content Creation for Educators',
            'title': 'AI-Assisted Content Creation for Educators',
            'desc': 'Educators use AI tools to generate quizzes, lesson plans, and multimedia content rapidly. This support streamlines preparation and allows more time for direct student engagement.'
        },
        {
            'type': 'Digital Credentialing Platforms for Lifelong Learning',
            'title': 'Digital Credentialing Platforms for Lifelong Learning',
            'desc': 'Digital badges and certificates verify skills acquired through informal education, like online courses or workshops. These credentials help learners showcase continuous growth to employers.'
        },
        {
            'type': 'Personalized Learning Analytics for Educators',
            'title': 'Personalized Learning Analytics for Educators',
            'desc': 'Advanced analytics platforms help educators understand student progress at an individual level, tailoring instruction methods and identifying gaps early to improve outcomes.'
        },
        {
            'type': 'Mobile Learning Transforming On-the-Go Education',
            'title': 'Mobile Learning Transforming On-the-Go Education',
            'desc': 'Mobile apps and responsive platforms allow students to learn anytime, anywhere, accommodating busy lifestyles and diverse learning environments.'
        },
        {
            'type': 'AI-Powered Adaptive Testing Methods',
            'title': 'AI-Powered Adaptive Testing Methods',
            'desc': 'Adaptive testing adjusts question difficulty in real-time based on student responses, providing accurate assessment of knowledge and learning needs.'
        },
        {
            'type': 'Interactive Video Lessons Increasing Engagement',
            'title': 'Interactive Video Lessons Increasing Engagement',
            'desc': 'Interactive videos with embedded quizzes and clickable content foster active learning and improve retention by keeping students engaged throughout lessons.'
        },
        {
            'type': 'Cloud-Based Collaboration Tools for Students',
            'title': 'Cloud-Based Collaboration Tools for Students',
            'desc': 'Cloud platforms enable students to work together on projects in real-time, share resources, and communicate seamlessly, supporting teamwork and peer learning.'
        },
        {
            'type': 'AI in Special Education Enhancing Accessibility',
            'title': 'AI in Special Education Enhancing Accessibility',
            'desc': 'AI tools assist students with disabilities by providing customized learning aids, speech recognition, and alternative communication methods, promoting inclusivity.'
        },
        {
            'type': 'Learning Management Systems Integrating AI',
            'title': 'Learning Management Systems Integrating AI',
            'desc': 'Modern LMS platforms use AI to personalize course recommendations, automate administrative tasks, and provide data-driven insights for educators.'
        },
        {
            'type': 'Virtual Labs Offering Hands-On Experience Remotely',
            'title': 'Virtual Labs Offering Hands-On Experience Remotely',
            'desc': 'Virtual labs allow students to conduct experiments and practice skills online, overcoming physical constraints and expanding access to practical learning.'
        },
        {
            'type': 'AI-Enhanced Language Translation in Education',
            'title': 'AI-Enhanced Language Translation in Education',
            'desc': 'AI-powered translation tools break down language barriers, enabling diverse student populations to access learning materials in their preferred languages.'
        },
        {
            'type': 'Blockchain-Based Student Records Management',
            'title': 'Blockchain-Based Student Records Management',
            'desc': 'Blockchain secures and streamlines student data management, making records immutable, verifiable, and easily accessible across institutions.'
        },
        {
            'type': 'Wearable AR Devices for Experiential Learning',
            'title': 'Wearable AR Devices for Experiential Learning',
            'desc': 'Wearable AR devices immerse students in interactive educational experiences, from virtual field trips to complex visualizations.'
        },
        {
            'type': 'AI-Driven Career Counseling Platforms',
            'title': 'AI-Driven Career Counseling Platforms',
            'desc': 'Platforms use AI to analyze student skills and preferences, offering personalized career advice and job matching.'
        },
        {
            'type': 'Digital Twins in Education for Simulations',
            'title': 'Digital Twins in Education for Simulations',
            'desc': 'Digital twins create virtual replicas of real-world systems, enabling students to experiment and learn in risk-free environments.'
        },
        {
            'type': 'AI-Based Plagiarism Detection Improving Academic Integrity',
            'title': 'AI-Based Plagiarism Detection Improving Academic Integrity',
            'desc': 'AI tools detect plagiarism more accurately and efficiently, helping uphold standards and educate students on originality.'
        },
        {
            'type': 'Cloud Gaming for Educational Purposes',
            'title': 'Cloud Gaming for Educational Purposes',
            'desc': 'Cloud gaming platforms deliver interactive educational games accessible from any device, promoting learning through play.'
        },
        {
            'type': 'AI-Supported Peer Review and Feedback Systems',
            'title': 'AI-Supported Peer Review and Feedback Systems',
            'desc': 'AI facilitates peer assessment by providing structured feedback and highlighting key areas for improvement.'
        },
        {
            'type': 'Real-Time Language Learning with AI Assistants',
            'title': 'Real-Time Language Learning with AI Assistants',
            'desc': 'AI assistants offer conversational practice and instant feedback, accelerating language acquisition.'
        },
        {
            'type': 'Data Privacy in EdTech Ensuring Student Protection',
            'title': 'Data Privacy in EdTech Ensuring Student Protection',
            'desc': 'With increased digital learning, data privacy measures safeguard student information and build trust in EdTech solutions.'
        },
    ]

    return render(request, 'main/cover.html', {'articles': articles})
