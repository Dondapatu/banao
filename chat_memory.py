class ChatMemory:
    def __init__(self, max_turns=5):
        self.max_turns = max_turns
        self.memory = []

    def add_turn(self, user, bot):
        self.memory.append({"user": user, "bot": bot})
        if len(self.memory) > self.max_turns:
            self.memory.pop(0)

    def build_prompt(self, user_input):
        prompt = ""
        for turn in self.memory:
            prompt += f"<|user|>\n{turn['user']}\n<|assistant|>\n{turn['bot']}\n"
        prompt += f"<|user|>\n{user_input}\n<|assistant|>\n"
        return prompt