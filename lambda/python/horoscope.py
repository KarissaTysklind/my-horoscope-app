import json

def lambda_handler(event, context):
    response = event

    match event["sign"]:     
        case "aries":
            response = "You might feel a burst of energy this week, Aries, but don't let it lead you to impulsive decisions. Channel your enthusiasm into a new project and watch it flourish. Embrace challenges with determination, and remember, patience is your key to success."

        case "taurus":
            response = "This is a great time for Taurus to focus on self-care and relaxation. Treat yourself to a spa day or a quiet evening at home. Financially, your steady approach will lead to unexpected windfalls. Remember to express your feelings to your loved ones."
        
        case "gemeni":
            response = "Communication is your forte, Gemini, but make sure to listen as much as you talk this week. Your social circle might expand, leading to exciting new connections. Embrace change and adaptability as opportunities arise, and you'll find success in unexpected places."
        
        case "cancer":
            response = "Your intuition is heightened, Cancer, so trust your gut feelings. Focus on nurturing relationships and spending time with loved ones. You might find yourself reminiscing about the past, leading to a burst of creativity and inspiration."
        
        case "leo":
            response = "This is your time to shine, Leo. Your natural charisma is on full display, and you'll be the center of attention wherever you go. Use this energy to start a new project or pursue a personal goal. Just remember to stay humble and open to others' perspectives."
        
        case "virgo":
            response = "Attention to detail is your strength, Virgo, but don't get lost in the minutiae. Focus on the bigger picture and delegate tasks when necessary. Your dedication to your work will lead to recognition and rewards, but make sure to find time for relaxation too."
        
        case "libra":
            response = "Balance is key for Libra this week. Strive for harmony in your relationships and take time to reflect on your personal needs. New opportunities may arise, so be open to trying something different. Remember, decisions made with a clear mind will lead to the best outcomes."
        
        case "scorpio":
            response = "Your intensity is captivating, Scorpio. Use your passion to tackle challenges head-on and make progress on long-standing goals. Don't be afraid to express your emotions to others, as it will lead to deeper connections and understanding."
        
        case "sagittarius":
            response = "Adventure calls, Sagittarius. Embrace your love for exploration and consider planning a spontaneous trip or trying a new hobby. Your optimism is contagious, so share your positivity with those around you. Financial opportunities might also be on the horizon."
        
        case "capricorn":
            response = "Your strong work ethic is highlighted, Capricorn. Focus on your professional goals and don't shy away from taking on extra responsibilities. Remember to also make time for self-care and relaxation to maintain your well-being."
        
        case "aquarius":
            response = "Your innovative ideas are flowing, Aquarius. Collaborate with others to turn your visions into reality. Embrace your uniqueness and don't be afraid to stand out from the crowd. Social interactions will be rewarding, so prioritize spending time with friends and loved ones."

        case "pisces":
            response = "Your intuition is heightened, Pisces, so pay attention to your dreams and gut feelings. This is a great time for creative pursuits, so indulge in your artistic interests. Your compassion and empathy will lead to deeper connections with those around you."

        case _:
            response = "Input a valid star sign.."    
    
    return response