from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


# --------------------------------------------------
# PAGE SETUP
# --------------------------------------------------
st.set_page_config(
    page_title="STREEDHAN | Money Made Simple",
    page_icon="💚",
    layout="wide",
    initial_sidebar_state="expanded",
)


# --------------------------------------------------
# TRANSLATIONS: ENGLISH, HINDI, MARATHI
# --------------------------------------------------
TEXT = {
    "English": {
        "language": "🌐 Language",
        "tagline": "Your money. Your goals. Your confidence.",
        "home": "Home",
        "budget": "Budget Planner",
        "savings": "Savings Goals",
        "learn": "Money School",
        "dashboard": "Dashboard",
        "welcome": "Make your money feel at home.",
        "intro": "A friendly space to plan your budget, celebrate savings, and learn money skills at your own pace.",
        "budget_card": "Budget your way",
        "budget_card_text": "See what comes in, what goes out, and what stays with you.",
        "savings_card": "Little steps. Big dreams.",
        "savings_card_text": "Turn your goals into a simple monthly savings plan.",
        "learn_card": "Money school",
        "learn_card_text": "Explore everyday money topics without the jargon.",
        "start_hint": "✨ Pick a page from the sidebar to begin.",
        "budget_title": "Your monthly money map",
        "budget_intro": "Add your income and monthly expenses. Your summary and charts update as you enter amounts.",
        "income": "Monthly income (₹)",
        "expenses": "Where does your money go?",
        "housing": "Home / Rent",
        "food": "Food & groceries",
        "transport": "Transport",
        "utilities": "Bills & utilities",
        "education": "Education",
        "health": "Health",
        "other": "Other expenses",
        "summary": "Your money snapshot",
        "total_income": "Income",
        "total_expenses": "Expenses",
        "balance": "Money left",
        "savings_rate": "Savings rate",
        "income_expense_chart": "Income vs. expenses",
        "expense_chart": "Your spending mix",
        "no_expenses": "Add some expenses to see your spending chart.",
        "positive": "Lovely! You have money left after these expenses.",
        "negative": "Your expenses are above your income. Review the amounts and adjust your plan.",
        "zero": "Your income and expenses are currently equal.",
        "savings_title": "Your savings adventure",
        "savings_intro": "Choose a goal, set a target, and watch your progress grow.",
        "goal_name": "What are you saving for?",
        "goal_target": "Your target amount (₹)",
        "saved_so_far": "Already saved (₹)",
        "months": "Your timeline (months)",
        "goal_progress": "Your progress",
        "saved": "Saved so far",
        "left_to_save": "Still to go",
        "monthly_saving": "Monthly savings target",
        "goal_done": "Goal reached! Look at you go! 🎉",
        "keep_going": "Every little bit counts. Keep going! 🌱",
        "jar_label": "Your savings jar",
        "goal_tip": "Tip: Try setting up a small, regular transfer on payday.",
        "learn_title": "Money School",
        "learn_intro": "Five bite-sized lessons to help you feel more confident with everyday money.",
        "lesson1": "🌿 1. Make a simple budget",
        "lesson1_text": "Write down your income, list your expenses, and check what remains. A budget is a plan—not a punishment. Adjust it when life changes.",
        "lesson2": "🐷 2. Build a saving habit",
        "lesson2_text": "Choose a realistic amount and save regularly. Small, repeatable steps can help you work toward a goal over time.",
        "lesson3": "🛟 3. Prepare for surprises",
        "lesson3_text": "An emergency fund is money set aside for unexpected needs. Build it gradually and keep it somewhere accessible and appropriate for your situation.",
        "lesson4": "🌼 4. Understand interest",
        "lesson4_text": "Interest may be paid when you borrow or earned on some savings. Check rates, fees, time periods, and compounding before choosing a product.",
        "lesson5": "🔐 5. Keep money information safe",
        "lesson5_text": "Never share your PIN, password, or OTP. Verify payment requests and contact your bank using official channels if something seems suspicious.",
        "dashboard_title": "Your financial dashboard",
        "dashboard_intro": "A colorful overview of the amounts you entered in your budget planner.",
        "dashboard_empty": "Start by entering your income or expenses in Budget Planner.",
        "dashboard_chart": "At a glance",
        "disclaimer": "STREEDHAN is an educational budgeting tool, not personalized financial, investment, tax, or legal advice.",
        "currency": "All amounts are in Indian rupees (₹).",
    },

    "हिंदी": {
        "language": "🌐 भाषा",
        "tagline": "आपका पैसा। आपके लक्ष्य। आपका आत्मविश्वास।",
        "home": "होम",
        "budget": "बजट योजनाकार",
        "savings": "बचत लक्ष्य",
        "learn": "मनी स्कूल",
        "dashboard": "डैशबोर्ड",
        "welcome": "अपने पैसों को सही दिशा दें।",
        "intro": "बजट बनाने, बचत की प्रगति देखने और अपनी गति से पैसों की जानकारी सीखने के लिए एक सरल जगह।",
        "budget_card": "अपना बजट बनाएं",
        "budget_card_text": "जानें कितनी आय आती है, कितना खर्च होता है और कितना बचता है।",
        "savings_card": "छोटे कदम, बड़े सपने।",
        "savings_card_text": "अपने लक्ष्य को आसान मासिक बचत योजना में बदलें।",
        "learn_card": "मनी स्कूल",
        "learn_card_text": "रोज़मर्रा के पैसों से जुड़े विषय सरल भाषा में सीखें।",
        "start_hint": "✨ शुरुआत करने के लिए साइडबार से पेज चुनें।",
        "budget_title": "आपका मासिक बजट नक्शा",
        "budget_intro": "अपनी आय और मासिक खर्च दर्ज करें। राशि बदलते ही सारांश और चार्ट अपडेट होंगे।",
        "income": "मासिक आय (₹)",
        "expenses": "आपका पैसा कहाँ खर्च होता है?",
        "housing": "घर / किराया",
        "food": "भोजन और किराना",
        "transport": "यातायात",
        "utilities": "बिल और उपयोगिताएँ",
        "education": "शिक्षा",
        "health": "स्वास्थ्य",
        "other": "अन्य खर्च",
        "summary": "आपके पैसों का सारांश",
        "total_income": "आय",
        "total_expenses": "खर्च",
        "balance": "बची हुई राशि",
        "savings_rate": "बचत दर",
        "income_expense_chart": "आय बनाम खर्च",
        "expense_chart": "आपके खर्च का विवरण",
        "no_expenses": "खर्च का चार्ट देखने के लिए कुछ खर्च दर्ज करें।",
        "positive": "बहुत अच्छा! इन खर्चों के बाद आपके पास कुछ राशि बच रही है।",
        "negative": "आपके खर्च आय से अधिक हैं। राशि की समीक्षा करें और योजना में बदलाव करें।",
        "zero": "आपकी आय और खर्च अभी बराबर हैं।",
        "savings_title": "आपकी बचत की यात्रा",
        "savings_intro": "लक्ष्य चुनें, राशि तय करें और अपनी प्रगति देखें।",
        "goal_name": "आप किस लिए बचत कर रहे हैं?",
        "goal_target": "लक्ष्य राशि (₹)",
        "saved_so_far": "अब तक बचाई गई राशि (₹)",
        "months": "कितने महीनों में लक्ष्य पूरा करना है?",
        "goal_progress": "आपकी प्रगति",
        "saved": "अब तक बचत",
        "left_to_save": "अभी और बचाना है",
        "monthly_saving": "मासिक बचत लक्ष्य",
        "goal_done": "लक्ष्य पूरा हुआ! बहुत खूब! 🎉",
        "keep_going": "हर छोटी बचत मायने रखती है। ऐसे ही आगे बढ़ें! 🌱",
        "jar_label": "आपका बचत जार",
        "goal_tip": "सुझाव: वेतन मिलने पर थोड़ी राशि नियमित रूप से बचाने की कोशिश करें।",
        "learn_title": "मनी स्कूल",
        "learn_intro": "रोज़मर्रा के पैसों को बेहतर समझने के लिए पाँच छोटी सीख।",
        "lesson1": "🌿 1. सरल बजट बनाएं",
        "lesson1_text": "अपनी आय लिखें, खर्चों की सूची बनाएं और बची हुई राशि देखें। बजट एक योजना है, सज़ा नहीं। जीवन की परिस्थितियों के अनुसार इसे बदलें।",
        "lesson2": "🐷 2. बचत की आदत बनाएं",
        "lesson2_text": "एक ऐसी राशि चुनें जिसे नियमित रूप से बचा सकें। छोटे और लगातार कदम समय के साथ लक्ष्य पाने में मदद कर सकते हैं।",
        "lesson3": "🛟 3. अचानक आने वाले खर्चों की तैयारी करें",
        "lesson3_text": "आपातकालीन निधि अप्रत्याशित ज़रूरतों के लिए अलग रखी गई राशि है। इसे धीरे-धीरे बनाएं और अपनी परिस्थिति के अनुसार सुलभ जगह रखें।",
        "lesson4": "🌼 4. ब्याज समझें",
        "lesson4_text": "उधार लेने पर ब्याज देना पड़ सकता है और कुछ बचत पर ब्याज मिल सकता है। कोई उत्पाद चुनने से पहले दर, शुल्क, अवधि और चक्रवृद्धि समझें।",
        "lesson5": "🔐 5. वित्तीय जानकारी सुरक्षित रखें",
        "lesson5_text": "अपना PIN, पासवर्ड या OTP किसी से साझा न करें। भुगतान अनुरोध जांचें और संदेह होने पर बैंक के आधिकारिक माध्यम से संपर्क करें।",
        "dashboard_title": "आपका वित्तीय डैशबोर्ड",
        "dashboard_intro": "बजट योजनाकार में दर्ज राशि का रंगीन सारांश।",
        "dashboard_empty": "शुरुआत करने के लिए बजट योजनाकार में आय या खर्च दर्ज करें।",
        "dashboard_chart": "एक नज़र में",
        "disclaimer": "STREEDHAN एक शैक्षिक बजट उपकरण है, व्यक्तिगत वित्तीय, निवेश, कर या कानूनी सलाह नहीं।",
        "currency": "सभी राशियां भारतीय रुपये (₹) में हैं।",
    },

    "मराठी": {
        "language": "🌐 भाषा",
        "tagline": "तुमचे पैसे. तुमची उद्दिष्टे. तुमचा आत्मविश्वास.",
        "home": "मुख्यपृष्ठ",
        "budget": "अर्थसंकल्प नियोजक",
        "savings": "बचतीची उद्दिष्टे",
        "learn": "मनी स्कूल",
        "dashboard": "डॅशबोर्ड",
        "welcome": "तुमच्या पैशांना योग्य दिशा द्या.",
        "intro": "अर्थसंकल्प तयार करा, बचतीची प्रगती पाहा आणि तुमच्या गतीने आर्थिक माहिती शिका.",
        "budget_card": "तुमचा अर्थसंकल्प तयार करा",
        "budget_card_text": "किती उत्पन्न येते, किती खर्च होते आणि किती शिल्लक राहते ते पाहा.",
        "savings_card": "लहान पावले, मोठी स्वप्ने.",
        "savings_card_text": "तुमच्या उद्दिष्टासाठी सोपी मासिक बचत योजना तयार करा.",
        "learn_card": "मनी स्कूल",
        "learn_card_text": "दैनंदिन पैशांशी संबंधित विषय सोप्या भाषेत शिका.",
        "start_hint": "✨ सुरुवात करण्यासाठी साइडबारमधून पान निवडा.",
        "budget_title": "तुमचा मासिक अर्थसंकल्प नकाशा",
        "budget_intro": "तुमचे उत्पन्न आणि मासिक खर्च नोंदवा. रक्कम बदलल्यावर सारांश आणि आलेख अपडेट होतील.",
        "income": "मासिक उत्पन्न (₹)",
        "expenses": "तुमचे पैसे कुठे खर्च होतात?",
        "housing": "घर / भाडे",
        "food": "अन्न आणि किराणा",
        "transport": "प्रवास",
        "utilities": "बिले आणि सुविधा",
        "education": "शिक्षण",
        "health": "आरोग्य",
        "other": "इतर खर्च",
        "summary": "तुमच्या पैशांचा आढावा",
        "total_income": "उत्पन्न",
        "total_expenses": "खर्च",
        "balance": "शिल्लक रक्कम",
        "savings_rate": "बचतीचे प्रमाण",
        "income_expense_chart": "उत्पन्न विरुद्ध खर्च",
        "expense_chart": "तुमच्या खर्चाचे प्रकार",
        "no_expenses": "खर्चाचा आलेख पाहण्यासाठी काही खर्च नोंदवा.",
        "positive": "छान! या खर्चांनंतर तुमच्याकडे काही रक्कम शिल्लक आहे.",
        "negative": "तुमचा खर्च उत्पन्नापेक्षा जास्त आहे. रकमेचा आढावा घेऊन योजना बदला.",
        "zero": "तुमचे उत्पन्न आणि खर्च सध्या समान आहेत.",
        "savings_title": "तुमचा बचतीचा प्रवास",
        "savings_intro": "उद्दिष्ट निवडा, लक्ष्य रक्कम ठरवा आणि प्रगती पाहा.",
        "goal_name": "तुम्ही कशासाठी बचत करत आहात?",
        "goal_target": "लक्ष्य रक्कम (₹)",
        "saved_so_far": "आतापर्यंत केलेली बचत (₹)",
        "months": "किती महिन्यांत उद्दिष्ट पूर्ण करायचे आहे?",
        "goal_progress": "तुमची प्रगती",
        "saved": "आतापर्यंत बचत",
        "left_to_save": "अजून बचत करायची",
        "monthly_saving": "मासिक बचतीचे लक्ष्य",
        "goal_done": "उद्दिष्ट पूर्ण झाले! अभिनंदन! 🎉",
        "keep_going": "प्रत्येक छोटी बचत महत्त्वाची आहे. असेच पुढे चला! 🌱",
        "jar_label": "तुमची बचतीची बरणी",
        "goal_tip": "टीप: पगार मिळाल्यावर थोडी रक्कम नियमितपणे बाजूला ठेवण्याचा प्रयत्न करा.",
        "learn_title": "मनी स्कूल",
        "learn_intro": "दैनंदिन पैशांचे व्यवस्थापन समजण्यासाठी पाच छोट्या गोष्टी.",
        "lesson1": "🌿 1. सोपा अर्थसंकल्प तयार करा",
        "lesson1_text": "उत्पन्न लिहा, खर्चांची यादी करा आणि उरलेली रक्कम तपासा. अर्थसंकल्प ही योजना आहे, शिक्षा नाही. परिस्थितीनुसार त्यात बदल करा.",
        "lesson2": "🐷 2. बचतीची सवय लावा",
        "lesson2_text": "नियमितपणे बाजूला ठेवता येईल अशी रक्कम निवडा. छोटे आणि सातत्यपूर्ण प्रयत्न उद्दिष्ट गाठण्यास मदत करू शकतात.",
        "lesson3": "🛟 3. अनपेक्षित खर्चांसाठी तयारी करा",
        "lesson3_text": "आपत्कालीन निधी म्हणजे अचानक उद्भवणाऱ्या गरजांसाठी बाजूला ठेवलेली रक्कम. तो हळूहळू तयार करा आणि गरज पडल्यास वापरता येईल अशा ठिकाणी ठेवा.",
        "lesson4": "🌼 4. व्याज समजून घ्या",
        "lesson4_text": "कर्ज घेतल्यावर व्याज द्यावे लागू शकते आणि काही बचतीवर व्याज मिळू शकते. उत्पादन निवडण्यापूर्वी दर, शुल्क, कालावधी आणि चक्रवाढ समजून घ्या.",
        "lesson5": "🔐 5. आर्थिक माहिती सुरक्षित ठेवा",
        "lesson5_text": "तुमचा PIN, पासवर्ड किंवा OTP कोणालाही सांगू नका. पेमेंट विनंत्या तपासा आणि संशय आल्यास बँकेशी अधिकृत माध्यमातून संपर्क साधा.",
        "dashboard_title": "तुमचा आर्थिक डॅशबोर्ड",
        "dashboard_intro": "अर्थसंकल्प नियोजकात नोंदवलेल्या रकमेचा रंगीत आढावा.",
        "dashboard_empty": "सुरुवात करण्यासाठी अर्थसंकल्प नियोजकात उत्पन्न किंवा खर्च नोंदवा.",
        "dashboard_chart": "एका नजरेत",
        "disclaimer": "STREEDHAN हे शैक्षणिक अर्थसंकल्प साधन आहे; वैयक्तिक आर्थिक, गुंतवणूक, कर किंवा कायदेशीर सल्ला नाही.",
        "currency": "सर्व रक्कम भारतीय रुपये (₹) मध्ये आहे.",
    },
}


def t(key):
    return TEXT[language].get(key, key)


# --------------------------------------------------
# SESSION STATE DEFAULTS
# --------------------------------------------------
if "monthly_income" not in st.session_state:
    st.session_state.monthly_income = 0.0

expense_keys = ["housing", "food", "transport", "utilities", "education", "health", "other"]

for key in expense_keys:
    state_key = f"expense_{key}"
    if state_key not in st.session_state:
        st.session_state[state_key] = 0.0


# --------------------------------------------------
# LANGUAGE AND NAVIGATION
# --------------------------------------------------
language = st.sidebar.selectbox(
    "🌐 Language / भाषा",
    ["English", "हिंदी", "मराठी"],
    index=0,
    key="language_choice",
)

# Rebuild page labels using the selected language
page_keys = ["home", "budget", "savings", "learn", "dashboard"]
page_labels = [t(key) for key in page_keys]

st.sidebar.markdown("---")
selected_label = st.sidebar.radio(
    "STREEDHAN",
    page_labels,
    label_visibility="collapsed",
)
current_page = page_keys[page_labels.index(selected_label)]


# --------------------------------------------------
# CUSTOM STYLES AND LOGO
# --------------------------------------------------
base_dir = Path(__file__).parent
css_file = base_dir / "style.css"
logo_file = base_dir / "assets" / "streedhan_logo.jpg"

if css_file.exists():
    st.markdown(
        f"<style>{css_file.read_text(encoding='utf-8')}</style>",
        unsafe_allow_html=True,
    )

if logo_file.exists():
    st.sidebar.image(str(logo_file), use_container_width=True)

st.sidebar.markdown(
    f"<div class='sidebar-tagline'>{t('tagline')}</div>",
    unsafe_allow_html=True,
)
st.sidebar.caption(t("currency"))


# --------------------------------------------------
# COMMON CALCULATIONS
# --------------------------------------------------
income = float(st.session_state.monthly_income)
expense_values = {
    key: float(st.session_state[f"expense_{key}"])
    for key in expense_keys
}
total_expenses = sum(expense_values.values())
balance = income - total_expenses
savings_rate = (balance / income * 100) if income > 0 else 0.0

expense_labels = {
    "housing": t("housing"),
    "food": t("food"),
    "transport": t("transport"),
    "utilities": t("utilities"),
    "education": t("education"),
    "health": t("health"),
    "other": t("other"),
}


# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------
if current_page == "home":
    st.markdown(
        f"""
        <div class="hero">
            <div class="hero-kicker">💚 STREEDHAN</div>
            <h1>{t("welcome")}</h1>
            <p>{t("intro")}</p>
            <div class="hero-decoration">🌸 &nbsp; 💰 &nbsp; 🌿 &nbsp; ✨</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            f"""
            <div class="feature-card feature-green">
                <div class="feature-art">🧾</div>
                <h3>{t("budget_card")}</h3>
                <p>{t("budget_card_text")}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            f"""
            <div class="feature-card feature-pink">
                <div class="feature-art">🐷</div>
                <h3>{t("savings_card")}</h3>
                <p>{t("savings_card_text")}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c3:
        st.markdown(
            f"""
            <div class="feature-card feature-yellow">
                <div class="feature-art">📚</div>
                <h3>{t("learn_card")}</h3>
                <p>{t("learn_card_text")}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.info(t("start_hint"))

    st.markdown(
        """
        <div class="quote-card">
            <span>🌷</span>
            <strong>Small steps today can make room for tomorrow’s dreams.</strong>
            <span>🌷</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


# --------------------------------------------------
# BUDGET PLANNER
# --------------------------------------------------
elif current_page == "budget":
    st.title("📊 " + t("budget_title"))
    st.write(t("budget_intro"))

    st.markdown("<div class='section-label'>💚 INCOME</div>", unsafe_allow_html=True)

    st.number_input(
        t("income"),
        min_value=0.0,
        step=500.0,
        key="monthly_income",
    )

    st.markdown("<div class='section-label'>🧺 EXPENSES</div>", unsafe_allow_html=True)
    st.subheader(t("expenses"))

    col_left, col_right = st.columns(2)

    for i, key in enumerate(expense_keys):
        target_col = col_left if i % 2 == 0 else col_right
        with target_col:
            st.number_input(
                expense_labels[key],
                min_value=0.0,
                step=100.0,
                key=f"expense_{key}",
            )

    income = float(st.session_state.monthly_income)
    expense_values = {
        key: float(st.session_state[f"expense_{key}"])
        for key in expense_keys
    }
    total_expenses = sum(expense_values.values())
    balance = income - total_expenses
    savings_rate = (balance / income * 100) if income > 0 else 0.0

    st.markdown("---")
    st.subheader("✨ " + t("summary"))

    m1, m2, m3 = st.columns(3)
    m1.metric(t("total_income"), f"₹{income:,.0f}")
    m2.metric(t("total_expenses"), f"₹{total_expenses:,.0f}")
    m3.metric(t("balance"), f"₹{balance:,.0f}")

    st.markdown(
        f"""
        <div class="savings-rate-card">
            <span>🌱 {t("savings_rate")}</span>
            <strong>{savings_rate:.1f}%</strong>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if balance > 0:
        st.success(t("positive"))
    elif balance < 0:
        st.warning(t("negative"))
    else:
        st.info(t("zero"))

    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        st.subheader(t("income_expense_chart"))
        overview = pd.DataFrame(
            {
                "Type": [t("total_income"), t("total_expenses"), t("balance")],
                "Amount": [income, total_expenses, balance],
            }
        )
        fig = px.bar(
            overview,
            x="Type",
            y="Amount",
            color="Type",
            text_auto=".2s",
            color_discrete_sequence=["#168064", "#E88BAE", "#E6B85C"],
        )
        fig.update_layout(
            showlegend=False,
            height=370,
            margin=dict(l=15, r=15, t=25, b=15),
            yaxis_title="₹",
            xaxis_title="",
            plot_bgcolor="white",
            paper_bgcolor="white",
        )
        fig.update_traces(textposition="outside", marker_line_width=0)
        st.plotly_chart(fig, use_container_width=True)

    with chart_col2:
        st.subheader(t("expense_chart"))
        chart_rows = [
            {"Category": expense_labels[key], "Amount": value}
            for key, value in expense_values.items()
            if value > 0
        ]

        if chart_rows:
            expense_df = pd.DataFrame(chart_rows)
            fig = px.pie(
                expense_df,
                names="Category",
                values="Amount",
                hole=0.58,
                color_discrete_sequence=[
                    "#168064",
                    "#E88BAE",
                    "#E6B85C",
                    "#7BA7D8",
                    "#A58BD4",
                    "#F29C72",
                    "#80B9A5",
                ],
            )
            fig.update_traces(
                textposition="inside",
                textinfo="percent+label",
                hole=0.58,
            )
            fig.update_layout(
                height=370,
                margin=dict(l=10, r=10, t=25, b=10),
                showlegend=False,
                paper_bgcolor="white",
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info(t("no_expenses"))


# --------------------------------------------------
# SAVINGS GOALS
# --------------------------------------------------
elif current_page == "savings":
    st.title("🐷 " + t("savings_title"))
    st.write(t("savings_intro"))

    goal_name = st.text_input(t("goal_name"), key="goal_name_input")

    goal_col1, goal_col2 = st.columns(2)

    with goal_col1:
        target = st.number_input(
            t("goal_target"),
            min_value=0.0,
            step=500.0,
            key="goal_target_input",
        )

    with goal_col2:
        saved = st.number_input(
            t("saved_so_far"),
            min_value=0.0,
            step=100.0,
            key="goal_saved_input",
        )

    months = st.number_input(
        t("months"),
        min_value=1,
        max_value=600,
        value=12,
        step=1,
        key="goal_months_input",
    )

    remaining = max(float(target) - float(saved), 0.0)
    progress = min(float(saved) / float(target), 1.0) if target > 0 else 0.0
    monthly_target = remaining / int(months)

    st.markdown("---")
    st.subheader("🌈 " + (goal_name.strip() if goal_name.strip() else t("jar_label")))

    progress_percent = int(progress * 100)

    jar_col1, jar_col2 = st.columns([1, 2])

    with jar_col1:
        st.markdown(
            f"""
            <div class="jar-card">
                <div class="jar-lid"></div>
                <div class="jar-body">
                    <div class="jar-emoji">🐷</div>
                    <div class="jar-percent">{progress_percent}%</div>
                </div>
                <div class="jar-caption">{t("jar_label")}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with jar_col2:
        st.markdown(f"### {t('goal_progress')}")
        st.progress(progress)
        st.markdown(
            f"""
            <div class="progress-labels">
                <span>💚 {t("saved")}: <b>₹{saved:,.0f}</b></span>
                <span>🎯 {t("goal_target")}: <b>₹{target:,.0f}</b></span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.metric(t("left_to_save"), f"₹{remaining:,.0f}")
        st.metric(t("monthly_saving"), f"₹{monthly_target:,.0f}")

        if target > 0 and saved >= target:
            st.success(t("goal_done"))
        else:
            st.info(t("keep_going"))

    st.caption(t("goal_tip"))


# --------------------------------------------------
# MONEY SCHOOL
# --------------------------------------------------
elif current_page == "learn":
    st.title("📚 " + t("learn_title"))
    st.write(t("learn_intro"))

    lessons = [
        ("lesson1", "lesson1_text"),
        ("lesson2", "lesson2_text"),
        ("lesson3", "lesson3_text"),
        ("lesson4", "lesson4_text"),
        ("lesson5", "lesson5_text"),
    ]

    for title_key, text_key in lessons:
        with st.expander(t(title_key)):
            st.write(t(text_key))


# --------------------------------------------------
# DASHBOARD
# --------------------------------------------------
elif current_page == "dashboard":
    st.title("📈 " + t("dashboard_title"))
    st.write(t("dashboard_intro"))

    income = float(st.session_state.monthly_income)
    expense_values = {
        key: float(st.session_state[f"expense_{key}"])
        for key in expense_keys
    }
    total_expenses = sum(expense_values.values())
    balance = income - total_expenses

    if income == 0 and total_expenses == 0:
        st.info(t("dashboard_empty"))
    else:
        d1, d2, d3 = st.columns(3)
        d1.metric(t("total_income"), f"₹{income:,.0f}")
        d2.metric(t("total_expenses"), f"₹{total_expenses:,.0f}")
        d3.metric(t("balance"), f"₹{balance:,.0f}")

        st.subheader(t("dashboard_chart"))

        dashboard_df = pd.DataFrame(
            {
                "Type": [t("total_income"), t("total_expenses")],
                "Amount": [income, total_expenses],
            }
        )

        fig = px.bar(
            dashboard_df,
            x="Type",
            y="Amount",
            color="Type",
            text_auto=".2s",
            color_discrete_sequence=["#168064", "#E88BAE"],
        )
        fig.update_layout(
            showlegend=False,
            height=400,
            margin=dict(l=15, r=15, t=25, b=15),
            yaxis_title="₹",
            xaxis_title="",
            plot_bgcolor="white",
            paper_bgcolor="white",
        )
        fig.update_traces(textposition="outside", marker_line_width=0)
        st.plotly_chart(fig, use_container_width=True)


# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("---")
st.caption(t("disclaimer"))