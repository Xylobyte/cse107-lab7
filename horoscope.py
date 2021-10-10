"""
A program that prompts the user for a date then gives them their horoscope

file: horoscope.py

author: Donovan Griego

Date: 10-10-2021

assignment: Lab 7
"""

import date

# Dates and their horoscopes
dates = {"aries": (80, 110), "taurus": (110, 142),
         "gemini": (142, 172), "cancer": (172, 205),
         "leo": (205, 236), "virgo": (236, 267),
         "libra": (267, 296), "scorpio": (296, 326),
         "sagittarius": (326, 356), "capricorn": (356, 20),
         "aquarius": (20, 50), "pisces": (50, 80)}
horoscopes = {"aries": "Concentrate on spending quality time with children and friends. Heed the advice given by family or old reliable friends. Problems with appliances or electrical gadgets will drive you crazy.",
              "taurus": "You may be in an extremely passionate mood today. However, you should be concerned about what they want in return. This is a turning point.",
              "gemini": "Direct your energy wisely. Calm down and take a step back. You cant lose today unless you get involved in gossip or overwork to the point of exhaustion.",
              "cancer": "You will have additional discipline that will aid you in your objectives. Family outings will make you feel secure and happy. You cant always have your own way.",
              "leo": "Changes in your home environment may cause friction. Dont get involved in other people private doings. New emotional connections can be made through business contacts.",
              "virgo": "Deal with the needs of children and get into groups that deal with self awareness. You will have the discipline to make changes you feel are necessary. Secret affairs may be tempting.",
              "libra": "Education may be the answer. Delve into your work if you cant make amends at home. Do not let others saddle you with guilt that isnt warranted.",
              "scorpio": "Try to join groups of interest such as ballroom dance classes or perhaps an internet organization. Help elders with their concerns. Trips will be more than adventurous.",
              "sagittarius": "Opportunities for romance will flourish through travel. Your mate may be distressed if you refuse to make a commitment. You can ask for favors and get sound advice from close friends or relatives.",
              "capricorn": "Be sure to get involved in self improvement programs that will bring you in contact with interesting people. Obstacles may stand in your way where career and success are concerned. Make sure that all your legal papers are in proper order.",
              "aquarius": "You will have no trouble getting things to fall into place. You may have difficulties with someone close to you. This is a great day to beautify your living quarters or to entertain at home.",
              "pisces": "Youll meet new friends if you try new activities. Be careful not to confuse issues when discussing the matters at hand. Join humanitarian groups and let your leadership ability take over."}


def main():
    while True:
        print("Type stop or enter a month, day, and year.")
        string = input("> ")
        if string.strip() == "stop":
            break
        tp = date.get_doy(string)
        for k in dates.keys():
            if tp[0] >= dates[k][0] and tp[0] < dates[k][1]:  # Checking for matching horoscope
                print("{}: {}".format(k, horoscopes[k]))


if __name__ == "__main__":
    main()
