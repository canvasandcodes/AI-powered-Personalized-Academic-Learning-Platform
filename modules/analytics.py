import streamlit as st
import pandas as pd
import plotly.express as px

from utils.analytics_tracker import (
    load_analytics
)


def analytics_ui():

    st.header(
        "Lumora Analytics Dashboard"
    )

    data = load_analytics()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "📄 Documents",
            data["documents_uploaded"]
        )

    with col2:
        st.metric(
            "❓ Questions",
            data["questions_asked"]
        )

    with col3:
        st.metric(
            "📚 Notes",
            data["notes_generated"]
        )

    col4, col5 = st.columns(2)

    with col4:
        st.metric(
            "📝 Exams",
            data["exam_generations"]
        )

    with col5:
        st.metric(
            "🎓 Viva Sessions",
            data["viva_sessions"]
        )

    st.divider()

    st.subheader(
        "📈 Platform Usage"
    )

    metrics_df = pd.DataFrame(
        {
            "Feature": [
                "Documents",
                "Questions",
                "Notes",
                "Exams",
                "Viva"
            ],
            "Count": [
                data["documents_uploaded"],
                data["questions_asked"],
                data["notes_generated"],
                data["exam_generations"],
                data["viva_sessions"]
            ]
        }
    )

    fig = px.bar(
        metrics_df,
        x="Feature",
        y="Count",
        title="Platform Usage Statistics"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    st.subheader(
        "🔥 Most Searched Topics"
    )

    if data["topics"]:

        topic_df = pd.DataFrame(
            {
                "Topic": list(
                    data["topics"].keys()
                ),
                "Count": list(
                    data["topics"].values()
                )
            }
        )

        pie = px.pie(
            topic_df,
            names="Topic",
            values="Count",
            title="Topic Distribution"
        )

        st.plotly_chart(
            pie,
            use_container_width=True
        )

        st.dataframe(
            topic_df,
            use_container_width=True
        )

    else:

        st.info(
            "No topics searched yet."
        )

    st.divider()

    st.subheader(
        "🕒 Recent Activity"
    )

    if data["recent_activity"]:

        for item in data["recent_activity"]:

            st.markdown(
                f"**{item['time']}** — {item['activity']}"
            )

    else:

        st.info(
            "No activity recorded."
        )