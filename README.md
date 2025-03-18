# Proxima AI

<div align="center">
An advanced AI-powered interview preparation platform with real-time feedback and interactive features.
</div>

## Overview
Proxima AI is a cutting-edge interview preparation platform that combines modern UI/UX with powerful AI capabilities. Built with Next.js 14, Tailwind CSS, and the Gemini API, it offers a seamless and interactive experience for job seekers to practice and enhance their interview skills. The platform leverages advanced AI algorithms to simulate realistic interview scenarios, provide instant feedback, and help users improve their interview performance systematically.

## Key Features

### AI-Powered Interviews
- **Dynamic Question Generation**: Utilizes Gemini API to generate contextually relevant questions based on the selected job role and experience level
- **Real-time Feedback**: Instant analysis of responses for clarity, relevance, and completeness
- **Adaptive Difficulty**: Questions adapt based on user performance and confidence levels
- **Multi-format Support**: Handles technical, behavioral, and situational interview questions
- **Natural Language Processing**: Advanced NLP for understanding context and nuances in responses
- **Sentiment Analysis**: Real-time analysis of response tone and emotional content

### Interactive UI/UX
- **Responsive Design**: Seamless experience across desktop, tablet, and mobile devices
- **Intuitive Navigation**: User-friendly interface with clear progression paths
- **Real-time Animations**: Smooth transitions and feedback indicators
- **Accessibility Features**: WCAG 2.1 compliant with screen reader support
- **Dark/Light Mode**: Customizable theme settings for optimal viewing
- **Interactive Code Editor**: Built-in Monaco editor for technical interviews

### Advanced Interview Features
- **Webcam Integration**: 
  - HD video recording capability
  - Body language and facial expression analysis
  - Gesture recognition for engagement metrics
  - Downloadable session recordings
  - Real-time posture feedback
  - Eye contact tracking

- **Voice Analysis**:
  - Speech clarity assessment
  - Pace and tone evaluation
  - Filler word detection
  - Confidence level analysis
  - Accent neutrality feedback
  - Voice modulation suggestions

### Personalization & Learning
- **Custom Learning Paths**:
  - Industry-specific question sets
  - Role-based competency assessment
  - Skill gap analysis
  - Personalized improvement recommendations
  - Adaptive learning algorithms
  - Custom practice schedules

- **Progress Tracking**:
  - Detailed performance metrics
  - Improvement trends
  - Skill proficiency scores
  - Interview readiness index
  - Comparative benchmarking
  - Historical performance data

### Analytics & Insights
- **Performance Dashboard**:
  - Session-wise analysis
  - Response quality metrics
  - Communication effectiveness scores
  - Comparative performance analysis
  - Real-time progress indicators
  - Custom performance reports

- **Improvement Metrics**:
  - Skill development tracking
  - Weak area identification
  - Success rate analytics
  - Personalized improvement suggestions
  - Learning velocity metrics
  - Competency heat maps

### Collaborative Features
- **Peer Review System**:
  - Interview recording sharing
  - Feedback exchange
  - Community ratings
  - Expert mentorship connections

- **Group Practice**:
  - Mock interview sessions
  - Real-time collaboration
  - Shared learning resources
  - Team feedback mechanisms

### Interview Question Bank
- **Comprehensive Collection**:
  - 10,000+ curated questions
  - Industry-specific sets
  - Difficulty-based categorization
  - Regular updates

- **Question Categories**:
  - Technical interviews
  - Behavioral questions
  - System design problems
  - Company-specific questions
  - Coding challenges
  - Brain teasers

### Aptitude Assessment
- **Test Categories**:
  - Quantitative Aptitude
  - Logical Reasoning
  - Verbal Ability
  - Data Interpretation
  - General Knowledge
  - Technical Aptitude

- **Assessment Features**:
  - Adaptive difficulty levels
  - Timed sections
  - Detailed solutions
  - Performance analytics
  - Practice mode
  - Mock tests

- **Scoring System**:
  - Section-wise scoring
  - Percentile ranking
  - Comparative analysis
  - Time management metrics
  - Accuracy tracking
  - Improvement suggestions

### Project Portfolio
- **Project Categories**:
  - Web Development
  - Mobile Applications
  - Machine Learning
  - Data Science
  - System Design
  - Cloud Architecture

- **Project Features**:
  - Real-world scenarios
  - Industry-aligned challenges
  - Guided implementations
  - Code review system
  - Version control integration
  - Collaboration tools

- **Learning Integration**:
  - Project-based assessments
  - Skill validation
  - Portfolio builder
  - Progress tracking
  - Mentor feedback
  - Industry benchmarking

## Project Architecture
### Frontend Architecture
- **Pages & Routing**: Next.js 14 App Router for efficient page navigation
- **Components**: Reusable UI components built with React and Shadcn UI
- **State Management**: React hooks and context for local state management
- **Styling**: Tailwind CSS for responsive and maintainable styling
- **Animations**: Framer Motion for smooth transitions and interactions
- **Code Editor**: Monaco Editor integration for technical interviews

### Backend Architecture
- **API Routes**: Next.js API routes for serverless backend functionality
- **Database**: PostgreSQL with Neon for serverless database operations
- **ORM**: Drizzle for type-safe database queries and migrations
- **Authentication**: Clerk for secure user authentication and management
- **AI Integration**: Google Gemini API for intelligent interview interactions
- **WebRTC**: Real-time video and audio streaming
- **WebSocket**: Real-time collaboration and messaging

## Tech Stack
- **Frontend**: Next.js 14, React, Tailwind CSS, Framer Motion
- **UI Components**: Shadcn UI
- **Authentication**: Clerk
- **Database**: PostgreSQL with Neon (Serverless)
- **ORM**: Drizzle
- **AI Integration**: Google Gemini API
- **Video Processing**: WebRTC, MediaRecorder API
- **Code Editor**: Monaco Editor

## User Flow
### 1. Onboarding
- User registration and profile creation
- Skill assessment and goal setting
- Industry and role selection
- Experience level configuration
- Learning path customization
- Initial readiness assessment

### 2. Interview Preparation
- **Pre-interview Setup**:
  - Select interview type (Technical/Behavioral)
  - Choose specific focus areas
  - Configure session duration
  - Test audio/video settings
  - Review preparation materials
  - Set practice goals

- **During Interview**:
  - Real-time question presentation
  - Response recording and analysis
  - Immediate feedback on key metrics
  - Progress indicators
  - AI-powered suggestions
  - Performance monitoring

- **Post-interview**:
  - Comprehensive performance report
  - Detailed feedback on each response
  - Improvement suggestions
  - Practice recommendations
  - Personalized study plan
  - Success metrics

### 3. Progress Tracking
- View historical performance
- Track improvement metrics
- Access saved sessions
- Review feedback history
- Compare with benchmarks
- Generate progress reports

## Getting Started
### Prerequisites
- Node.js 18+ installed
- PostgreSQL database (or Neon account)
- Clerk account for authentication
- Gemini API key
- WebRTC-compatible browser
- Webcam and microphone access

### Environment Setup
1. Clone the repository
2. Copy `.env.local.example` to `.env.local`
3. Configure the following environment variables:
   ```
   NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=
   CLERK_SECRET_KEY=
   NEXT_PUBLIC_CLERK_SIGN_IN_URL=
   NEXT_PUBLIC_CLERK_SIGN_UP_URL=
   NEXT_PUBLIC_CLERK_AFTER_SIGN_IN_URL=
   NEXT_PUBLIC_CLERK_AFTER_SIGN_UP_URL=
   DATABASE_URL=
   GEMINI_API_KEY=
   WEBSOCKET_URL=
   MEDIA_STORAGE_KEY=
   ```

### Installation
1. Install dependencies:
   ```bash
   npm install
   ```
2. Run database migrations:
   ```bash
   npm run db:migrate
   ```
3. Start the development server:
   ```bash
   npm run dev
   ```

## Docker Support
The project includes Docker support for containerized deployment:

1. Build the image:
   ```bash
   docker build -t proxima-ai .
   ```
2. Run the container:
   ```bash
   docker run -p 3000:3000 proxima-ai
   ```

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Support
Show your support by giving the project a ⭐️!

## Contact
For questions or feedback, reach out to:
- Email: [hbhanushali2017@gmail.com](mailto:hbhanushali2017@gmail.com)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

==============================
# Proxima AI

<div align="center">
An advanced AI-powered interview preparation platform with real-time feedback and interactive features.
</div>

## Overview
Proxima AI is a cutting-edge interview preparation platform that combines modern UI/UX with powerful AI capabilities. Built with Next.js 14, Tailwind CSS, and the Gemini API, it offers a seamless and interactive experience for job seekers to practice and enhance their interview skills.

## Key Features
- **AI-Powered Interviews**: Dynamic interview sessions with intelligent question generation and real-time feedback
- **Interactive UI**: Modern, responsive interface with smooth animations and transitions
- **Webcam Integration**: Optional video recording feature for a more realistic interview experience
- **Personalized Experience**: Tailored questions based on job roles, industries, and experience levels
- **Comprehensive Question Bank**: Extensive collection of interview questions across various domains
- **Performance Analytics**: Detailed feedback, insights, and overall grading for each session
- **Progress Tracking**: Easy access to recent interviews and improvement metrics
- **Dark/Light Mode**: Support for both dark and light themes

## Project Architecture
### Frontend Architecture
- **Pages & Routing**: Next.js 14 App Router for efficient page navigation
- **Components**: Reusable UI components built with React and Shadcn UI
- **State Management**: React hooks and context for local state management
- **Styling**: Tailwind CSS for responsive and maintainable styling
- **Animations**: Framer Motion for smooth transitions and interactions

### Backend Architecture
- **API Routes**: Next.js API routes for serverless backend functionality
- **Database**: PostgreSQL with Neon for serverless database operations
- **ORM**: Drizzle for type-safe database queries and migrations
- **Authentication**: Clerk for secure user authentication and management
- **AI Integration**: Google Gemini API for intelligent interview interactions

## Tech Stack
- **Frontend**: Next.js 14, React, Tailwind CSS, Framer Motion
- **UI Components**: Shadcn UI
- **Authentication**: Clerk
- **Database**: PostgreSQL with Neon (Serverless)
- **ORM**: Drizzle
- **AI Integration**: Google Gemini API

## Getting Started
### Prerequisites
- Node.js 18+ installed
- PostgreSQL database (or Neon account)
- Clerk account for authentication
- Gemini API key

### Environment Setup
1. Clone the repository
2. Copy `.env.local.example` to `.env.local`
3. Configure the following environment variables:
   ```
   NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=
   CLERK_SECRET_KEY=
   NEXT_PUBLIC_CLERK_SIGN_IN_URL=
   NEXT_PUBLIC_CLERK_SIGN_UP_URL=
   NEXT_PUBLIC_CLERK_AFTER_SIGN_IN_URL=
   NEXT_PUBLIC_CLERK_AFTER_SIGN_UP_URL=
   DATABASE_URL=
   GEMINI_API_KEY=
   ```

### Installation
1. Install dependencies:
   ```bash
   npm install
   ```
2. Run database migrations:
   ```bash
   npm run db:migrate
   ```
3. Start the development server:
   ```bash
   npm run dev
   ```

## Usage Guide
1. **Sign Up/Login**: Create an account or log in using Clerk authentication
2. **Dashboard**: Access your interview dashboard with recent sessions and analytics
3. **Start Interview**: 
   - Choose interview type (technical/behavioral)
   - Select job role and experience level
   - Optional: Enable webcam for video recording
   - Begin the interview session
4. **During Interview**:
   - Respond to AI-generated questions
   - Receive real-time feedback and suggestions
5. **Post Interview**:
   - Review detailed performance analysis
   - Access improvement recommendations
   - Save and track progress

## Docker Support
The project includes Docker support for containerized deployment:

1. Build the image:
   ```bash
   docker build -t proxima-ai .
   ```
2. Run the container:
   ```bash
   docker run -p 3000:3000 proxima-ai
   ```

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Support
Show your support by giving the project a ⭐️!

## Contact
For questions or feedback, reach out to:
- Email: [hbhanushali2017@gmail.com](mailto:hbhanushali2017@gmail.com)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
