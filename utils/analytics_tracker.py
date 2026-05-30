import json
import os
from datetime import datetime

ANALYTICS_FILE = "data/analytics.json"


def default_data():

    return {
        "documents_uploaded": 0,
        "questions_asked": 0,
        "notes_generated": 0,
        "exam_generations": 0,
        "viva_sessions": 0,
        "topics": {},
        "recent_activity": []
    }


def load_analytics():

    if not os.path.exists(ANALYTICS_FILE):

        os.makedirs("data", exist_ok=True)

        data = default_data()

        with open(ANALYTICS_FILE, "w") as f:
            json.dump(data, f, indent=4)

        return data

    with open(ANALYTICS_FILE, "r") as f:
        return json.load(f)


def save_analytics(data):

    os.makedirs("data", exist_ok=True)

    with open(ANALYTICS_FILE, "w") as f:
        json.dump(data, f, indent=4)


def increment_metric(metric):

    data = load_analytics()

    if metric not in data:
        data[metric] = 0

    data[metric] += 1

    save_analytics(data)


def track_topic(topic):

    if not topic:
        return

    data = load_analytics()

    topic = topic.lower().strip()

    if topic not in data["topics"]:
        data["topics"][topic] = 0

    data["topics"][topic] += 1

    save_analytics(data)


def add_activity(activity):

    data = load_analytics()

    data["recent_activity"].insert(
        0,
        {
            "activity": activity,
            "time": datetime.now().strftime(
                "%Y-%m-%d %H:%M"
            )
        }
    )

    data["recent_activity"] = (
        data["recent_activity"][:20]
    )

    save_analytics(data)


def get_top_topics(limit=10):

    data = load_analytics()

    topics = sorted(
        data["topics"].items(),
        key=lambda x: x[1],
        reverse=True
    )

    return topics[:limit]