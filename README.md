# design tools 
[zerosec.tools](http://zerosec.tools) is a webapp for designers where they can find ML-tools that might be useful in real applications. For now, there is only 1 tool - hieroglyph generator, but in near future arsenal is going to be extended.

Webapp is built with flask-Jinja-js stack and uses tensorflow apis to access models.
Final docker container is deployed to the google cloud.

#### [hieoglyph generator](http://zerosec.tools/tools/hieroglyph)

Cherry-picked examples:
![](https://i.imgur.com/4By0Am5.jpg)

There are many types of generative models, but for this problem I've tried two of them: variational autoencoders and GANs. I've experienced with many approaches and different models' architectures and found WGAN with general penalty the most effective in my sample.

For dataset I simply used hangul hieroglyphs: I've gerenated them as text first by unicode range, and then created images for each of them with [this](https://github.com/IBM/tensorflow-hangul-recognition/blob/master/tools/hangul-image-generator.py) script. After generation, hieroglyph is traced to svg to remove noise, make it rounded and create scalable vector that could be used in design.

I've trained the network for about 3 days using google cloud AI-platform. As for now, model performs very poorly.
