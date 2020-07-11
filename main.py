import base64
import config
import requests
import telebot

bot = telebot.TeleBot(config.token)


# Узнать название растение по фото, а также просто фактики

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'My name is PlantBot. I can help to identify plants.' + '\n'
                     + '/send - to start a identification' + '\n\n' +
                     'I hope it is of interest to you:' + '\n' +
                     '/repot - how to repot your plants' + '\n' +
                     '/overwatering - signs of overwatering your plants' + '\n' +
                     '/smallPlants - small plants, big love' + '\n' +
                     '/resource - establishment and resources' + '\n\n' +
                     'It’s true when we say plants make people happy.')


@bot.message_handler(commands=['send'])
def start_message(message):
    bot.send_message(message.chat.id, 'Send me pic of your plant whose name you want to know')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAICG18JrTgoESf2YLFl2_Fo9kr0fQnmAAICAAOXjm0U9hEDwg-E_-QaBA')
    bot.send_message(message.chat.id, 'Hello, flower. Send me /help to know more information')


@bot.message_handler(content_types=['sticker'])
def start_message(message):
    bot.send_message(message.chat.id, message)


@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    try:
        file_info = bot.get_file(message.photo[0].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = 'C:/Users/helen/PycharmProjects/PlantBot/' + file_info.file_path
        with open('file_info.file_path', 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.send_message(message.chat.id, 'Checking in flower database, please wait..')

        with open('file_info.file_path', "rb") as file:
            images = [base64.b64encode(file.read()).decode("ascii")]

        your_api_key = "Ek2byOWEWo1cwLZMCaq0P0ywmYxKdv7DsW6nTka6lYkIWvo9F6"
        json_data = {
            "images": images,
            "modifiers": ["similar_images"],
            "plant_details": ["url"]
        }
        response = requests.post(
            "https://api.plant.id/v2/identify",
            json=json_data,
            headers={
                "Content-Type": "application/json",
                "Api-Key": your_api_key
            }).json()
        suggestion = response["suggestions"][0]
        bot.send_message(message.chat.id, 'Maybe your plant is ' + suggestion["plant_name"] + "\n"
                         + suggestion["plant_details"]["url"])
        bot.send_message(message.chat.id, 'If it does not look like your flower, change a position and try again')
    except Exception as e:
        bot.reply_to(message, e)


@bot.message_handler(commands=['resource'])
def start_message(message):
    bot.send_photo(message.chat.id, 'https://i.pinimg.com/564x/b8/f4/09/b8f4092d781cf01ed832eefee3aa4b71.jpg',
                   'ESTABLISHMENT & RESOURCES' + '\n\n' +
                   'Larger plants are more established in that they have bigger roots and bigger shoots, and are more '
                   'anchored into their place. These plants have many leaves, and in the event of stress, can afford '
                   'to lose a few whereas smaller plants cannot. Larger plants also have the a large store of '
                   'resources to draw from to grow and withstand periods of stress. This reserve of energy and '
                   'nutrients gives you a buffer zone of time to act before the stress does damage to the plant.  '
                   'Smaller plants react immediately because they do not have energy or nutrient reserves to fight '
                   'the stress.')


@bot.message_handler(commands=['smallPlants'])
def start_message(message):
    bot.send_photo(message.chat.id, 'https://i.pinimg.com/564x/91/fe/8e/91fe8eff90ffa1a7345a5de780179b20.jpg',
                   'SMALL PLANTS, BIG LOVE' + '\n\n' +
                   'Think of your plants like children. Babies need a lot more attention than teenagers. It’s a '
                   'common misconception that smaller plants are easier to take care of. Smaller plants, like babies, '
                   'need more attention than larger plants do. Perhaps it’s the intimidation factor of a large plant '
                   'that makes it seem more labor intensive, but in fact, larger plants are easier to care for. It’s '
                   'about establishment, resources, and soil size.')


@bot.message_handler(commands=['overwatering'])
def start_message(message):
    bot.send_photo(message.chat.id,
                   'https://cdn.shopify.com/s/files/1/0150/6262/articles/blog-signs-overwatering_1080x.jpg?v=1575048469',
                   'HOW DO I KNOW IF I AM OVERWATERING MY HOUSEPLANTS?' + '\n\n' +
                   'It’s easy to want to give your plant babies too much love and attention — but did you know '
                   'overwatering is the most common way to kill a houseplant?' + '\n' +
                   'Overwatering is a relatively easy mistake to diagnose, and many symptoms of overwatering are '
                   'unique to it. '
                   'When diagnosing a sad plant sign, it’s important to look at the plant as a whole, and not just '
                   'the plant part that is negatively affected. '
                   'Although we think of overwatering as just adding too much water to a plant is potting mix — '
                   'what’s really going on is that the surrounding soil is not drying out fast enough. It may very '
                   'well be from too much water (and most commonly is), but it may also be from not enough natural '
                   'sunlight. If you water a plant with the appropriate amount of water, but it doesn’t get enough '
                   'sunlight, then the potting mix will stay moist, and the plant will be effectively overwatered. A '
                   'good strategy for combating that is watering in the morning hours.')
    bot.send_message(message.chat.id,
                     'The first thing you should do, when diagnosing an overwatered plant, is to feel the plant is '
                     'potting mix! Feel the mix a few inches deep. If it feels moist or wet, it is most likely '
                     'overwatered. Another sign of overwatering can be fungus gnats. Fungus gnats feed on the fungi '
                     'that show up in moist environments. They proliferate when the soil stays too wet for too long. '
                     'But don’t fret — you can get rid of them.' + '\n' +
                     'The best way to keep a plant from being overwatered is to give the plant water only when the '
                     'potting mix is dry — and to give it enough light and warmth to help dry out efficiently. It is '
                     'definitely easier to overwater a plant in a non-draining container, so consider repotting to a '
                     'planter with drainage holes (or add a layer of lava rocks to the bottom of a container within '
                     'holes).')


@bot.message_handler(commands=['repot'])
def start_message(message):
    bot.send_photo(message.chat.id,
                   'https://xslib-img.picturethisai.com/prod/uploads/cms/12/26/f9560e974e5cfbf19b417c2829f8c5b1.jpg',
                   '1. Remove plant from current pot' + '\n' +
                   'Turn your new plant sideways, hold it gently by the stems or leaves, and tap the bottom of its '
                   'grow pot until the plant slides out. '
                   'You might need to give it a bit of help with a couple gentle tugs on the base of the stems.')
    bot.send_photo(message.chat.id,
                   'https://xslib-img.picturethisai.com/prod/uploads/cms/18/94/cdd7f7ffa4b52f20b9816b1991dabff1.jpg',
                   '2. Loosen the roots' + '\n' +
                   'Loosen the plant’s roots gently with your hands.'
                   'You can prune off any threadlike roots that are extra long, just make sure to leave the thicker '
                   'roots at the base of the foliage. If your plant is root bound – the roots are growing in very '
                   'tight circles around the base of the plant – unbind the roots as best you can and give them a '
                   'trim. ')
    bot.send_photo(message.chat.id,
                   'https://xslib-img.picturethisai.com/prod/uploads/cms/0/70/e6d88be40b24bb97635c098ba82068ff.jpg',
                   '3. Remove old potting mix' + '\n' +
                   'Remove about one third or more of the potting mix surrounding the plant. As it grew, your plant '
                   'removed some of the nutrients in the current mix, '
                   ' so you will want to give it fresh mix if you are potting it anyway!')
    bot.send_photo(message.chat.id,
                   'https://xslib-img.picturethisai.com/prod/uploads/cms/94/71/7c2d2aa50eeb45d0c7c1515e2ddbc6ea.jpg',
                   '4. Add new potting mix' + '\n' +
                   'Pour a layer of fresh potting soil into the new planter and pack it down, removing any air '
                   'pockets. If your new planter does not have a drainage hole, layer the bottom with lava rocks or '
                   'similar (rocks, gravel, etc.) before adding the potting mix. The goal is to create crevices for '
                   'the extra water to pool into, away from your plant’s roots.')
    bot.send_photo(message.chat.id,
                   'https://xslib-img.picturethisai.com/prod/uploads/cms/58/61/2577be0d07ccc00833c71468fd243dcf.jpg',
                   '5. Add plant' + '\n' +
                   'Set your plant that you removed from the grow pot on top of the fresh layer of mix in the new '
                   'planter, making sure it is centered, then add potting mix around the plant until it is secure. Be '
                   'sure not to pack too much soil into the planter, as you want the roots to breathe. ')
    bot.send_photo(message.chat.id,
                   'https://xslib-img.picturethisai.com/prod/uploads/cms/12/34/09627a4e3f64cf57eddd7abfa3a85cc2.jpg',
                   '6. Water and enjoy ' + '\n' +
                   'Even out the potting soil on top, water well, and enjoy!')


@bot.message_handler()
def unknown(message):
    bot.send_message(message.chat.id, 'Sorry, unknown command' + '\n' + 'Read /help')


bot.polling()
