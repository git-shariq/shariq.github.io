import os

# Template for the Game Pages (Dark Theme)
template = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Shariq | Unity Developer</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{
                        sans: ['Outfit', 'sans-serif'],
                    }},
                    colors: {{
                        brand: {{
                            50: '#f0f9ff',
                            100: '#e0f2fe',
                            400: '#38bdf8',
                            500: '#0ea5e9', // Sky blue-ish
                            600: '#0284c7',
                            900: '#0c4a6e',
                        }}
                    }}
                }}
            }}
        }}
    </script>
    <style>
        /* Custom scrollbar styling */
        ::-webkit-scrollbar {{
            width: 10px;
        }}
        ::-webkit-scrollbar-track {{
            background: #0f172a;
        }}
        ::-webkit-scrollbar-thumb {{
            background: #334155;
            border-radius: 5px;
        }}
        ::-webkit-scrollbar-thumb:hover {{
            background: #475569;
        }}
        .glass-nav {{
            background: rgba(15, 23, 42, 0.85);
            backdrop-filter: blur(12px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        }}
    </style>
</head>
<body class="bg-slate-950 text-slate-200 antialiased overflow-x-hidden">

    <!-- Navbar -->
    <header class="fixed top-0 left-0 w-full z-50 transition-all duration-300 glass-nav" id="navbar">
        <nav class="container mx-auto px-6 py-4 flex items-center justify-between">
            <a href="index.html" class="text-2xl font-bold text-white flex items-center gap-2 group">
                <span class="w-8 h-8 bg-brand-600 rounded-lg flex items-center justify-center text-white text-lg group-hover:-rotate-12 transition-transform">S</span>
                <span>Portfolio</span>
            </a>
            
            <!-- Desktop Menu -->
            <div class="hidden md:flex items-center space-x-8">
                <a href="index.html#about" class="text-sm font-medium text-slate-300 hover:text-brand-500 transition-colors">About</a>
                <a href="index.html#skills" class="text-sm font-medium text-slate-300 hover:text-brand-500 transition-colors">Skills</a>
                <a href="index.html#projects" class="text-sm font-medium text-slate-300 hover:text-brand-500 transition-colors">Projects</a>
                <a href="index.html#contact" class="px-5 py-2.5 rounded-full bg-white text-slate-900 text-sm font-medium hover:bg-brand-500 hover:text-white transition-colors shadow-lg shadow-brand-500/10">Contact Me</a>
            </div>

            <!-- Mobile Menu Button -->
            <button class="md:hidden text-white focus:outline-none">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
            </button>
        </nav>
    </header>

    <main>
        <!-- Project Detail Section -->
        <section class="relative pt-32 pb-20 lg:pt-48 lg:pb-32 overflow-hidden min-h-screen flex items-center">
            <!-- Background Elements -->
            <div class="absolute top-0 left-0 w-full h-full bg-slate-950 z-[-1]">
                <div class="absolute top-[-10%] left-[20%] w-[500px] h-[500px] bg-brand-900/20 rounded-full blur-3xl opacity-40 animate-pulse"></div>
                <div class="absolute bottom-[-10%] right-[10%] w-[400px] h-[400px] bg-indigo-900/20 rounded-full blur-3xl opacity-40"></div>
            </div>

            <div class="container mx-auto px-6 text-center">
                
                <!-- Back Button -->
                <div class="mb-8 flex justify-center md:justify-start max-w-4xl mx-auto" data-aos="fade-down">
                    <a href="index.html#projects" class="inline-flex items-center text-brand-400 hover:text-brand-300 transition-colors group">
                        <svg class="w-4 h-4 mr-2 transform group-hover:-translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
                        Back to Projects
                    </a>
                </div>

                <h1 class="text-4xl md:text-6xl font-extrabold text-white mb-8 tracking-tight" data-aos="fade-up">
                    {title}
                </h1>

                <!-- Media Container (Landscape with Contain) -->
                <div class="max-w-4xl mx-auto mb-12 rounded-2xl overflow-hidden shadow-2xl shadow-brand-900/20 border border-slate-800 bg-slate-900 aspect-video relative group" data-aos="zoom-in" data-aos-delay="100">
                    {media_content}
                </div>

                <!-- Content -->
                <div class="max-w-3xl mx-auto" data-aos="fade-up" data-aos-delay="200">
                    <h2 class="text-2xl font-bold text-white mb-4 flex items-center justify-center gap-2">
                        <span class="w-8 h-1 bg-brand-500 rounded-full"></span>
                        About the Game
                        <span class="w-8 h-1 bg-brand-500 rounded-full"></span>
                    </h2>
                    <p class="text-lg text-slate-400 leading-relaxed mb-8">
                        {description}
                    </p>
                    
                    <div class="flex flex-col sm:flex-row justify-center gap-4">
                        <a href="#" class="px-8 py-4 rounded-full bg-brand-600 text-white font-semibold hover:bg-brand-500 transition-all shadow-lg hover:shadow-brand-500/25 flex items-center justify-center gap-2">
                            <svg class="w-5 h-5" viewBox="0 0 24 24" fill="currentColor"><path d="M3 20.5v-9l6-2.25V3h5.25v2.25L21 9v11.5H3zm1.5-1.5h15V10l-4.5-1.5V5.25h-2.25V8.5L5.25 10.75v8.25zM6 12h2v2H6v-2zm0 3h2v2H6v-2zm3.5-3h2v2h-2v-2zm0 3h2v2h-2v-2zm3.5-3h2v2h-2v-2zm0 3h2v2h-2v-2z"/></svg>
                            Download on Play Store
                        </a>
                        <a href="index.html#contact" class="px-8 py-4 rounded-full bg-slate-800 text-slate-200 font-semibold hover:bg-slate-700 hover:text-white transition-all shadow-lg border border-slate-700 flex items-center justify-center gap-2">
                           <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
                           Contact Developer
                        </a>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <footer class="bg-slate-950 text-slate-500 py-8 border-t border-slate-900">
        <div class="container mx-auto px-6 text-center">
            <p>© 2025 Shariq. Built with <span class="text-red-500">❤</span> and Unity.</p>
        </div>
    </footer>

    <!-- Scripts -->
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>
        AOS.init({{
            duration: 800,
            once: true,
            offset: 50,
        }});

        // Navbar Scroll Effect
        const navbar = document.getElementById('navbar');
        window.addEventListener('scroll', () => {{
            if (window.scrollY > 20) {{
                navbar.classList.add('shadow-md');
                navbar.classList.replace('bg-opacity-0', 'glass-nav');
            }} else {{
                navbar.classList.remove('shadow-md');
            }}
        }});
    </script>
</body>
</html>
"""

# Game Data
games = {
    "screw-puzzle.html": {
        "title": "Screw Puzzle",
        "desc": "A challenging puzzle game where players strategically remove screws to disassemble intricate wooden blocks. Test your logic and patience in this mechanical brain-teaser.",
        "type": "video",
        "src": "../Media/Screw_Puzzle.mp4"
    },
    "sliding-puzzle.html": {
        "title": "Sliding Puzzle",
        "desc": "A classic sliding tile puzzle game. Challenge your spatial reasoning by arranging numbered blocks into a complete sequence with the fewest moves possible.",
        "type": "image",
        "src": "https://play-lh.googleusercontent.com/ZOuUYolyaQ9UW4a86cZ8UZylWUKH-NBVy3-EIZrRxbqvYhzlYtZxzi4vQddFpf_aNg=w526-h296-rw"
    },
    "ball-sort.html": {
        "title": "Ball Sort",
        "desc": "A relaxing yet addictive color-sorting puzzle. Sort the colored balls into their matching tubes to solve increasingly complex logic puzzles and clear the levels.",
        "type": "image",
        "src": "https://play-lh.googleusercontent.com/QUnXRcXNDig8yCv5PpuYYc7HX_Zj_UnL1Ly3vda9D4jjEXlKyxJmwy6whLCfXRXJ8yF_wMXaHqG9vbmDd8vAbsc=w832-h470-rw"
    },
    "pocket-games.html": {
        "title": "Pocket Games",
        "desc": "The ultimate offline arcade collection! Enjoy a variety of mini-games including block puzzles, sliding puzzles, screw puzzles, and more—anytime, anywhere.",
        "type": "image",
        "src": "https://play-lh.googleusercontent.com/DqWl57MyTXRMfSl97oj_jE01pI46-8tdnpohAWOAx4P4LiaWFMxxnPQaNlrduAMqCpGn=w416-h235-rw"
    },
    "wooden-block-puzzle.html": {
        "title": "Wooden Block Puzzle",
        "desc": "A Zen-like puzzle experience. Drag and drop wooden blocks onto a grid to create and clear complete lines or 3x3 squares. Perfect for relaxation and brain training.",
        "type": "image",
        "src": "https://play-lh.googleusercontent.com/1JnyWM4iOWw0rWBS863S0Vk13rxxp_iphp5udec7T8otMEFN2s_Eau_ofZFOynPVew=w416-h235-rw"
    },
    "fruit-block-puzzle.html": {
        "title": "Fruit Block Puzzle",
        "desc": "A juicy twist on the block puzzle genre. Strategically match and remove vibrant fruit blocks to score high and unlock refreshing new levels.",
        "type": "image",
        "src": "https://play-lh.googleusercontent.com/rMnonVaxZTdWUBhL92ugI3C9ktrwVA9HuRqd_AJWgvvjvJNzg84hIvn61tw00QjVwoNw=w416-h235-rw"
    },
    "turbo-burst.html": {
        "title": "Turbo Burst",
        "desc": "A relaxing 2D car game where you navigate through traffic to collect and deliver packages. Master the controls to become the ultimate delivery driver.",
        "type": "video",
        "src": "../Media/Turbo_Burst.mp4"
    },
    "slope-glide.html": {
        "title": "Slope Glide",
        "desc": "Hit the slopes in this smooth snowboarding game. Glide down the mountain, avoid obstacles, and reach the finish line without crashing in this physics-based adventure.",
        "type": "video",
        "src": "../Media/Slope Glide.mp4"
    },
    "jump-quest.html": {
        "title": "Jump Quest",
        "desc": "An exciting 2D platformer. Run, jump, and dodge treacherous traps as you navigate through challenging levels to reach the goal.",
        "type": "video",
        "src": "../Media/Jump_Quest.mp4"
    },
    "brain-rush.html": {
        "title": "Brain Rush",
        "desc": "Draw your way to victory! In this puzzle game, you must draw paths to guide cars to their designated parking spots without them crashing into each other.",
        "type": "video",
        "src": "../Media/Brain Rush.mp4"
    },
    "star-fire.html": {
        "title": "Star Fire",
        "desc": "Blast off into a retro-style 2D space shooter. Dodge enemy fire, upgrade your ship, and survive endless waves of alien adversaries.",
        "type": "video",
        "src": "../Media/Star_Fire.mp4"
    },
    "hyper-lift.html": {
        "title": "Hyper Lift",
        "desc": "Take control of a futuristic 3D spaceship. Navigate through tight corridors, avoid deadly hazards, and reach the goal to complete the level.",
        "type": "video",
        "src": "../Media/Hyper_Lift.mp4"
    },
    "space-warrior.html": {
        "title": "Space Warrior",
        "desc": "A fast-paced 3D tactical rail shooter. Pilot your ship through intense enemy waves using realistic physics, particle effects, and advanced C# combat mechanics.",
        "type": "image",
        "src": "../Media/SpaceWarrior.jpg"
    },
    "agyaat.html": {
        "title": "Agyaat",
        "desc": "A spine-chilling Indian classic horror PC game. Immerse yourself in a narrative driven by psychological fear, Indian folklore, and a dark, atmospheric world.",
        "type": "image",
        "src": "../Media/Agyaat Logo.jpg"
    },
    "car-parking-3d.html": {
        "title": "Car Parking 3D",
        "desc": "Master the art of parking! Draw paths to guide cars to their parking spots without crashing in this addictive 3D puzzle game.",
        "type": "image",
        "src": "https://placehold.co/600x400/3d5885/ffffff?text=Car+Parking+3D"
    }
}

def generate_pages():
    for filename, data in games.items():
        media_html = ""
        if data["type"] == "video":
            # UPDATED: Use object-contain and bg-black to fit portrait videos in landscape player
            media_html = f"""<video class="w-full h-full object-contain bg-black" autoplay muted loop playsinline controls>
                        <source src="{data['src']}" type="video/mp4">
                        Your browser does not support the video tag.
                    </video>"""
        else:
            # Images typically fill the space, object-cover is usually best here
            media_html = f"""<img src="{data['src']}" alt="{data['title']}" class="w-full h-full object-cover">"""

        content = template.format(
            title=data["title"],
            description=data["desc"],
            media_content=media_html
        )
        
        file_path = os.path.join("Pages", filename)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {filename}")

if __name__ == "__main__":
    generate_pages()