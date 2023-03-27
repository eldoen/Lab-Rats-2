# internal class to  handle list of actions
init -2 python:
    class ActionList():
        def __init__(self, actions = None):
            self._actions = []
            if not actions is None:
                if isinstance(actions, ActionList):
                    self._actions[:] = actions[:]
                if isinstance(actions, list):
                    for x in actions:
                        self.add_action(x)
                else:
                    self.add_action(actions)

        def __getitem__(self, key):
            if isinstance( key, slice ) :
                #Get the start, stop, and step from the slice
                return [self[ii] for ii in xrange(*key.indices(len(self)))]
            elif isinstance(key, int):
                if key < 0 : #Handle negative indices
                    key += len( self )
                if key < 0 or key >= len( self ) :
                    raise IndexError
                return self._actions[key]
            raise TypeError

        def __repr__(self):
            return repr(self._actions)

        def __call__(self):
            return self._actions

        def __iter__(self):
            return iter(self._actions)

        def __len__(self):
            return len(self._actions)

        def __contains__(self, action):
            found = self.find(action)
            return not found is None

        def __add__(self, action):
            if isinstance(action, ActionList):
                return self.__class__(self._actions + action._actions)
            elif isinstance(action, list):
                return self.__class__(self._actions + action)
            elif isinstance(action, Action):
                return self.__class__(self._actions + [action])

        def __radd__(self, action):
            if isinstance(action, ActionList):
                return self.__class__(action._actions + self._actions)
            elif isinstance(action, list):
                return self.__class__(action + self._actions)
            elif isinstance(action, Action):
                return self.__class__([action] + self._actions)

        def __iadd__(self, action):
            if isinstance(action, ActionList):
                self._actions += other._actions
            elif isinstance(action, list):
                for x in action:
                    self.add_action(x)
            else:
                self.add_action(action)
            return self

        def __sub__(self, action):
            self.remove_action(action)

        def __iadd__(self, action):
            self.append_action(action)
            return self

        def __isub__(self, action):
            self.remove_action(action)
            return self

        def append(self, action):
            self.add_action(action)

        def remove(self, action):
            self.remove_action(action)

        def clear(self):
            self._actions.clear()

        def copy(self):
            return self.__class__(self)

        def extend(self, other):
            if isinstance(other, ActionList):
                self._actions.extend(other._actions)
            elif isinstance(other, list):
                for x in other:
                    self.add_action(x)
            elif isinstance(other, Action):
                self.add_action(other)

        def pop(self, index = -1):
            return self._actions.pop(index)

        def index(self, action):
            found = self.find(action)
            if found:
                return self._actions.index(found)
            raise ValueError

        def find(self, action):
            if isinstance(action, Action):
                return next((x for x in self._actions if x == action), None)
            return None

        def add_action(self, action):
            if isinstance(action, Action):
                found = self.find(action)
                if not found:
                    self._actions.append(action)
                else:
                    found.update(action)

        def remove_action(self, action):
            found = self.find(action)
            if not found and isinstance(action, basestring):
                found = next((x for x in self._actions if x.effect == action), None)
            if found:
                self._actions.remove(found)

        def enabled_actions(self, extra_args = None):
            return [x for x in self._actions if x.is_action_enabled(extra_args)]

        def has_action(self, action):
            found = self.find(action)
            if not found and isinstance(action, basestring):
                found = next((x for x in self._actions if x.effect == action), None)
            return not found is None
