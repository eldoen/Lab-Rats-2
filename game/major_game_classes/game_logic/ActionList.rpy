# internal class to  handle list of actions
init -2 python:
    class ActionList(renpy.store.object):
        def __init__(self, actions = None):
            self._actions = []
            if isinstance(actions, list):
                for x in actions:
                    self.add_action(x)
            elif not actions is None:
                self.add_action(actions)

        def __repr__(self):
            return repr(self)

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
            self.add_action(action)

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

        def remove(self, item):
            self.remove_action(action)

        def clear(self):
            self._actions.clear()

        def extend(self, other):
            if isinstance(other, ActionList):
                self._actions.extend(other._actions)
            if isinstance(other, list):
                for x in other:
                    self.add_action(x)

        def pop(self, index = -1):
            return self._actions.pop(index)

        def index(self, action):
            found = self.find(action)
            if found:
                return self._actions.index(found)
            raise ValueError

        def find(self, action):
            if isinstance(action, Action):
                return next((x for x in self._actions if x.effect == action.effect), None)
            return None

        def add_action(self, action):
            found = self.find(action)
            if not found:
                self._actions.append(action)
            else:
                self.update_action(action)

        def remove_action(self, action):
            found = self.find(action)
            if not found and isinstance(action, basestring):
                found = next((x for x in self._actions if x.effect == action), None)

            if found:
                self._actions.remove(found)

        def update_action(self, action):
            self.name = action.name
            self.effect = action.effect
            self.requirement = action.requirement
            self.args = action.args
            self.menu_tooltip = action.menu_tooltip
            self.priority = action.priority
            self.event_duration = action.event_duration
            self.is_fast = action.is_fast
            return
