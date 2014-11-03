import lymph
import random


class Grumpy(lymph.Interface):

    @lymph.rpc()
    def can_i(self, channel):
        if random.random() < .75:
            channel.error(name='nargh!')
        else:
            channel.reply(True)
