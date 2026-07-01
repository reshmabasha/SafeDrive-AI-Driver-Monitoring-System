class RiskEngine:

    def __init__(self):

        self.risk_score = 0
        self.driver_status = "SAFE"

    def calculate(
        self,
        blink_data,
        yawn_data,
        head_data,
        phone_data
    ):

        score = 0
        reasons = []

        # ---------------------------------------
        # Eye Closure Risk
        # ---------------------------------------

        closed = blink_data["closed_frames"]

        if closed >= 15:
            score += 20
            reasons.append("Eyes Closed")

        if closed >= 25:
            score += 20
            reasons.append("Possible Drowsiness")

        if closed >= 40:
            score += 30
            reasons.append("Driver Sleeping")

        # ---------------------------------------
        # Frequent Yawning
        # ---------------------------------------

        if yawn_data["is_yawning"]:
            score += 10
            reasons.append("Yawning")

        if yawn_data["yawn_count"] >= 5:
            score += 10

        # ---------------------------------------
        # Head Pose
        # ---------------------------------------

        pose = head_data["head_pose"]

        if pose in ["LEFT", "RIGHT"]:
            score += 10
            reasons.append("Looking Away")

        elif pose == "DOWN":
            score += 20
            reasons.append("Looking Down")

        elif pose == "UP":
            score += 10
            reasons.append("Looking Up")

        # ---------------------------------------
        # Phone Detection
        # ---------------------------------------

        if phone_data["phone_detected"]:

            confidence = phone_data["phone_confidence"]

            if confidence >= 80:

                score += 35

            elif confidence >= 60:

                score += 25

            else:

                score += 15

            reasons.append("Phone Usage")

        # ---------------------------------------
        # Limit Score
        # ---------------------------------------

        score = min(score, 100)

        # ---------------------------------------
        # Driver Status
        # ---------------------------------------

        if score < 25:

            status = "SAFE"

        elif score < 60:

            status = "WARNING"

        else:

            status = "DROWSY"

        # ---------------------------------------
        # Alarm Decision
        # ---------------------------------------

        alarm = False

        reason = ""

        if score >= 60:

            alarm = True

            if reasons:

                reason = reasons[0]

            else:

                reason = "Driver Risk"

        # ---------------------------------------
        # Save State
        # ---------------------------------------

        self.risk_score = score
        self.driver_status = status

        return {

            "risk_score": score,

            "driver_status": status,

            "alarm": alarm,

            "alarm_reason": reason,

            "risk_reasons": reasons

        }
