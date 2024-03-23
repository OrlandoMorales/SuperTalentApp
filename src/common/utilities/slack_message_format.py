from string import Template
import json


class SlackMessageFormater:

    SCORE_DETAILS = """*Evaluation*: The profile of $FULLNAME has some missing skills that could help the system to evaluate better the required aptitudes for this position, the score of $SCORE is based on the provided and required aptitudes, the candidate gathers the minimum and some extra skills for the position"""

    def title_factory(self, company_name, position_title):
        return Template("*Position*:\n*<google.com|$COMPANY_NAME - $POSITION_TITLE>*").substitute({
            'COMPANY_NAME' : company_name,
            'POSITION_TITLE': position_title
            })


    def profile_factory(self, candidate_info,match):
        return Template("*PROFILE:*\n*Name:* $FULL_NAME\n *Gender:* $GENDER \n*Location:* $LOCATION\n*Email:* $EMAIL \n*Education:* $EDUCATION \n*Phone:* $PHONE \n*Score:* *$MATCHSCORE* \n*Eightfold Link:* $LINK \n$WHY").substitute({
            'FULL_NAME': candidate_info["fullName"],
            'GENDER': candidate_info["efGender"],
            'LOCATION': candidate_info["location"],
            'EMAIL': candidate_info["email"],
            'EDUCATION': candidate_info["education"][0]["degree"],
            'PHONE': candidate_info["phone"],
            'MATCHSCORE': match["matchScore"],
            'LINK' : self.validate_value(candidate_info,"urls", "No Link Available"),
            'TEMPLATE_WHY': candidate_info["email"],
            'WHY' : self.score_details(candidate_info["fullName"], match["matchScore"])
        })


    def validate_value(self, candidate_info, property_name, validation_detail):
        if len(candidate_info[property_name]) > 0:
            return candidate_info[property_name]
        else:
            return "No Available Info"


    def message_template_one(self, candidate_data, position_data, match):
        return {
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": self.title_factory(position_data["recruiter"]["name"],position_data["name"])
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": self.profile_factory(candidate_data, match)
                    },
                    "accessory": {
                        "type": "image",
                        "image_url": self.validate_value(candidate_data,"imageUrl", "No Image Available"),
                        "alt_text": self.validate_value(candidate_data,"fullName", "No Name Available")
                    }
                }
            ]
        }
        
    
    def score_details(self, full_name, match_score):
        if float(match_score) < 5: 
            return Template(self.SCORE_DETAILS).substitute({
                'FULLNAME' : full_name,
                'SCORE': match_score
            })
        else:
            ""