import lymph


class Albert(lymph.Interface):

    @lymph.event('add')
    def add(self, event):
        grumpy = self.proxy('grumpy')
        try:
            grumpy.can_i()
        except lymph.exceptions.ErrorReply:
            print 'leave me alone.'
        else:
            print sum(event.body.values())
