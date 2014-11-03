import lymph


class Echo(lymph.Interface):
    @lymph.rpc()
    def echo(self, channel, text=None):
        channel.reply(text)
