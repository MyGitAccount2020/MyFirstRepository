from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.profileDB

profile = {
    "name": "Atul Gunjal",
    "contact_details": "Warudi Pathar, Tal-Sangamner, Dist-Ahmednagar, Maharashtra, India - 422620, Phone: 8806874459, Email: atul.v.gunjal@gmail.com, Portfolio: www.atulgunjal.com, LinkedIn: https://www.linkedin.com/in/atul-gunjal, GitHub: https://github.com/MyGitAccount 2020/, Twitter: @AtulVGunjal",
    "objective": "Eager to leverage my expertise in software development, with a strong foundation in Angular and a keen interest in Microsoft Dynamics 365 technologies, to contribute to the success and growth of an innovative organization as a D365 Technical Developer.",
    "skills": [
        "JavaScript", "Java", "HTML5", "CSS3", "Angular 8 & 14", "React", "Bootstrap", "Node.js", "Express", "MongoDB", "MySQL", "VS Code", "Eclipse", "Angular-CLI", "JIRA", "CI/CD pipelines", "Microsoft Dynamics 365 for Finance and Operations (F&O)", "Business Central", "Agile SCRUM"
    ],
    "experience": "Software Development Engineer at Brillio Technologies Pvt. Ltd. | March 2022 – June 2023. Developed and maintained projects using Angular 8 and 14, focusing on creating reusable UI components and enhancing application performance. Integrated responsive design principles to improve user experience across multiple devices. Implemented effective testing frameworks and tools to increase test coverage, ensuring robust application performance. Collaborated with cross-functional teams, contributing to the successful implementation of Agile methodologies to streamline project development.",
    "education": [
        {"degree": "Bachelor of Engineering", "stream": "Information Technology", "college": "SVPM's College Of Engineering, Malegaon (BK)", "year": 2021, "percentage": "6.8 CGPA", "project": "COVID-19 Detection System using Image Processing and Machine Learning (Achieved 80% accuracy)"},
        {"degree": "Diploma", "stream": "Computer Engineering", "college": "ATES's Faculty Of Polytechnic, Akole", "year": 2018, "percentage": "66.75%", "project": "College Fee Management System (Improved administrative efficiency by automating fee calculations)"},
        {"degree": "HSC", "stream": "Science", "college": "Sahyadri Jr College, Sangamner", "year": 2015, "percentage": "40.20%", "project": "-"},
        {"degree": "SSC", "stream": "-", "college": "Pragati Vidyalaya Pokhari Baleshwar", "year": 2013, "percentage": "75.20%", "project": "-"}
    ],
    "projects": [
        "COVID-19 Detection System (Utilized image processing and machine learning to develop a system for early detection of COVID-19 from medical images using Python. Achieved 80% accuracy, demonstrating the system’s potential in assisting early diagnosis.)",
        "College Fee Management System (Developed a system for managing college fees, significantly reducing manual calculation errors and administrative workload using Java.)"
    ],
    "certifications": [
        "AWS Cloud Practitioners Foundational",
        "Google Cloud Certified Associate"
    ],
    "languages": [
        "Marathi (Native)", "Hindi (Fluent)", "English (Fluent)"
    ]
}

db.profile.insert_one(profile)
