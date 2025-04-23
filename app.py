import streamlit as st

# =================== CONFIG ===================
LANGUAGE_OPTIONS = ["Tiếng Việt", "English"]

QUESTIONS_VI = [
    ("Tôi thường giữ khoảng cách với người khác và không thích chia sẻ nhiều.", "Grey"),
    ("Tôi thường nhận được lời mời từ người khác mà không cần chủ động trước.", "Grey"),
    ("Tôi cảm thấy thoải mái khi ở một mình và thích khám phá theo cách riêng.", "Grey"),
    ("Tôi tin rằng ai cũng có điều tốt đẹp bên trong họ.", "Orange"),
    ("Tôi cảm thấy vui vẻ khi được giúp đỡ hoặc động viên người khác.", "Orange"),
    ("Tôi dễ rung động trong tình yêu và thường nghĩ đến người cũ.", "Orange"),
    ("Tôi tránh cãi vã hoặc mâu thuẫn nếu có thể.", "Green"),
    ("Tôi thích làm mọi việc một cách nhẹ nhàng, không căng thẳng.", "Green"),
    ("Tôi không để tâm nhiều đến việc cạnh tranh hay nổi bật.", "Green"),
    ("Tôi luôn sẵn sàng thử điều mới và thích cảm giác mạo hiểm.", "Crimson"),
    ("Tôi thường là người đầu tiên đưa ra ý tưởng hoặc quyết định.", "Crimson"),
    ("Tôi thích được chú ý và không ngại thể hiện bản thân.", "Crimson"),
    ("Tôi có xu hướng suy nghĩ theo lối sáng tạo và khác biệt.", "Purple"),
    ("Tôi yêu nghệ thuật và thường tìm kiếm cảm hứng từ những điều nhỏ bé.", "Purple"),
    ("Tôi thấy mình thuộc về thế giới đa dạng, khác thường và độc đáo.", "Purple"),
    ("Tôi làm việc có tổ chức và luôn đảm bảo mọi thứ được hoàn thành đúng lúc.", "Blue"),
    ("Tôi luôn trung thành và đáng tin cậy trong các mối quan hệ.", "Blue"),
    ("Tôi thấy hài lòng khi được làm việc theo quy trình rõ ràng.", "Blue"),
]

QUESTIONS_EN = [
    ("I usually keep distance from others and don’t like to share much.", "Grey"),
    ("People often invite me to events, even when I don’t ask.", "Grey"),
    ("I enjoy being alone and doing things in my own way.", "Grey"),
    ("I believe that everyone has something good inside.", "Orange"),
    ("I feel happy when I help or support other people.", "Orange"),
    ("I easily fall in love and often think about my past love.", "Orange"),
    ("I don’t like fighting or arguing with others.", "Green"),
    ("I like to do things in a calm and easy way.", "Green"),
    ("I don’t care much about competition or standing out.", "Green"),
    ("I enjoy trying new things and exciting experiences.", "Crimson"),
    ("I’m often the first person to speak or decide in a group.", "Crimson"),
    ("I like to be noticed and don’t mind showing myself.", "Crimson"),
    ("I often think in creative or different ways.", "Purple"),
    ("I love art and often find inspiration in small things.", "Purple"),
    ("I feel I belong to a unique and colorful world.", "Purple"),
    ("I like to keep things organized and always finish my work on time.", "Blue"),
    ("I am loyal and reliable in relationships.", "Blue"),
    ("I feel good when I work with clear steps and plans.", "Blue"),
]

SCORE_LABELS = {
    "Strongly disagree": -2,
    "Disagree": -1,
    "Neutral / Not sure": 0,
    "Agree": 1,
    "Strongly agree": 2
}

SCORE_LABELS_VI = {
    "Hoàn toàn không đồng ý": -2,
    "Không đồng ý": -1,
    "Trung lập": 0,
    "Đồng ý": 1,
    "Hoàn toàn đồng ý": 2
}

DESCRIPTIONS = {
    "Grey": "**Grey** (**Powerful**, **Mysterious**, **Provocative**): People with Grey personality value **solitude**, **privacy**, and **mystery**. You keep people guessing and never let anyone too close. You enjoy doing things your own way and don’t care about others’ judgment. This color suits those who are **bold**, yet **calm**, and prefer to live on the edge without fear.",
    "Orange": "**Orange** (**Optimistic**, **Friendly**, **Perceptive**): As an Orange, you're **warm** and **joyful**. You love small, close gatherings and deeply value human connection. You see the best in people and **forgive** easily. **Romantic** at heart, you love deeply and hurt deeply, always **hopeful** for future connections.",
    "Green": "**Green** (**Peaceful**, **Serene**, **Accommodating**): Green personalities are **calm** and **peaceful**. You prefer a **stress-free** life, enjoy **comfort**, and avoid confrontation. You allow others to find peace without disturbing your own. You’re **easygoing**, attractive in your **calmness**, but may sometimes overlook things that need serious attention.",
    "Crimson": "**Crimson** (**Adventurous**, **Bold**, **Direct**): People with Crimson energy are **daring** and **passionate**. You love **excitement** and being in the **spotlight**. You're **assertive**, **outspoken**, and **energetic**. **Popularity** and **achievement** are important to you. You **thrive** in fast-moving environments and enjoy being **admired**.",
    "Purple": "**Purple** (**Creative**, **Expressive**, **Emotive**): Purple personalities are **artistic** and **thoughtful**. You live life with **imagination** and **depth**, often thinking **differently** from others. You love **culture**, **philosophy**, and **art**. You’re **expressive**, open to possibilities, and proud of your **unique** lifestyle.",
    "Blue": "**Blue** (**Dependable**, **Practical**, **Directive**): Blue types are **trustworthy** and **organized**. You follow rules, keep promises, and value **honesty**. You stick to **routines**, make **sacrifices** to reach goals, and always support your loved ones. **Discipline** and **responsibility** define you, even if it means missing out on fun sometimes."
}

# =================== STREAMLIT UI ===================
st.set_page_config(page_title="Personality Color Quiz", page_icon="🎨", layout="centered")

# Add custom font
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito&display=swap');
    html, body, [class*="css"]  {
        font-family: 'Nunito', sans-serif;
    }
    </style>
""", unsafe_allow_html=True)
st.title("🎨 Personality Color Quiz")

language = st.radio("Chọn ngôn ngữ / Choose your language:", LANGUAGE_OPTIONS)

if language == "English":
    QUESTIONS = QUESTIONS_EN
    LABELS = list(SCORE_LABELS.keys())
    SCORE_MAP = SCORE_LABELS
else:
    QUESTIONS = QUESTIONS_VI
    LABELS = list(SCORE_LABELS_VI.keys())
    SCORE_MAP = SCORE_LABELS_VI

responses = []

with st.form("quiz_form"):
    for idx, (question, _) in enumerate(QUESTIONS):
        answer = st.radio(
            f"{idx + 1}. {question}",
            LABELS,
            key=f"q{idx}"
        )
        responses.append(answer)
    submitted = st.form_submit_button("🔍 Xem kết quả / See Result")

# =================== SCORING ===================
if submitted:
    scores = {color: 0 for color in DESCRIPTIONS.keys()}
    for idx, answer in enumerate(responses):
        _, color = QUESTIONS[idx]
        scores[color] += SCORE_MAP[answer]

    top_color = max(scores, key=scores.get)

    st.subheader(f"🎯 Màu sắc cá nhân của bạn là: {top_color}")
    st.markdown(DESCRIPTIONS[top_color])

    st.markdown("### 📊 Điểm số các màu khác:")
    for color, score in sorted(scores.items(), key=lambda x: -x[1]):
        st.write(f"- {color}: {score}")
