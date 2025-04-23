import streamlit as st

# =================== CONFIG ===================
QUESTIONS = [
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

SCORE_LABELS = {
    "Hoàn toàn không đồng ý": -2,
    "Không đồng ý": -1,
    "Trung lập": 0,
    "Đồng ý": 1,
    "Hoàn toàn đồng ý": 2
}

DESCRIPTIONS = {
    "Grey": "**Grey**: Mysterious, powerful, independent. Bạn sống kín đáo, bí ẩn và không dễ bị thấu hiểu.",
    "Orange": "**Orange**: Friendly, optimistic, emotional. Bạn hòa đồng, vị tha và luôn tìm kiếm sự kết nối.",
    "Green": "**Green**: Peaceful, relaxed, chill. Bạn ưa thích sự yên bình, nhẹ nhàng và tránh xung đột.",
    "Crimson": "**Crimson**: Bold, adventurous, extroverted. Bạn mạnh mẽ, thích thử thách và nổi bật giữa đám đông.",
    "Purple": "**Purple**: Creative, expressive, unique. Bạn sáng tạo, lập dị và yêu nghệ thuật.",
    "Blue": "**Blue**: Dependable, structured, honest. Bạn đáng tin cậy, kỷ luật và trung thành."
}

# =================== STREAMLIT UI ===================
st.set_page_config(page_title="Personality Color Quiz", page_icon="🎨")
st.title("🎨 Personality Color Quiz")
st.markdown("Hãy chọn mức độ phù hợp với bạn nhất cho mỗi câu hỏi bên dưới. Sau đó, nhấn **'Xem kết quả'** để khám phá màu sắc cá nhân của bạn!")

responses = []

with st.form("quiz_form"):
    for idx, (question, _) in enumerate(QUESTIONS):
        answer = st.radio(
            f"{idx + 1}. {question}",
            list(SCORE_LABELS.keys()),
            key=f"q{idx}"
        )
        responses.append(answer)
    submitted = st.form_submit_button("🔍 Xem kết quả")

# =================== SCORING ===================
if submitted:
    scores = {color: 0 for color in DESCRIPTIONS.keys()}
    for idx, answer in enumerate(responses):
        _, color = QUESTIONS[idx]
        scores[color] += SCORE_LABELS[answer]

    top_color = max(scores, key=scores.get)

    st.subheader(f"🎯 Màu sắc cá nhân của bạn là: {top_color}")
    st.markdown(DESCRIPTIONS[top_color])

    st.markdown("### 📊 Điểm số các màu khác:")
    for color, score in sorted(scores.items(), key=lambda x: -x[1]):
        st.write(f"- {color}: {score}")
