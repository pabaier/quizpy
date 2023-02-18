class Hook:
    def __init__(self, name, creator_id=None, code=None):
        self.name = name
        self.creator_id = creator_id
        self.code = code


class Hooks:
    def __init__(self):
        self.hooks = {}
        self.length = 0

    def add(self, hook):
        if hook.creator_id in self.hooks:
            if hook.name not in self.hooks[hook.creator_id]:
                self.hooks[hook.creator_id][hook.name] = hook
                self.length += 1
        else:
            self.hooks[hook.creator_id] = {hook.name: hook}
            self.length += 1

    def get(self, creator_id, name) -> Hook:
        return self.hooks[creator_id][name]

    def __iter__(self):
        ''' returns the Iterator object '''
        return HooksIterator(self)

    def __len__(self):
        return self.length


class HooksIterator:
    ''' Iterator class '''

    def __init__(self, hooks):
        self._creators = list(hooks.keys())
        try:
            self._hook_names = self._creators[0]
        except:
            raise StopIteration
        self._hooks = hooks
        self._creator_index = 0
        self._name_index = 0

    def __next__(self):
        ''''Returns the next value from team object's lists '''
        if self._creator_index < len(self._creators):
            if self._name_index < len(self._hook_names):
                result = self._hooks.get(self._creators[self._creator_index], self._hook_names[self._name_index])
                self._name_index += 1
                if self._name_index is len(self._hook_names):
                    self._creator_index += 1
                    self._name_index = 0
                    if self._creator_index < len(self._creators):
                        self._hook_names = self._creators[self._creator_index]
                return result
        # End of Iteration
        raise StopIteration
