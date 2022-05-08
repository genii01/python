import torch 
def forward(self, features):
        output_states = self.backbone(**features, return_dict=False)
        attention_mask = features['attention_mask']
        
        if self.config.pooling_type == 'mean':
            output_vector = self.mean_pooling(output_states, attention_mask)
        elif self.config.pooling_type == 'max':
            output_vector = self.max_pooling(output_states, attention_mask)
        else:
            raise NotImplementedError('wrong pooling type inserted')
        
        features.update({'sentence_embedding': output_vector})
        return features


def mean_pooling(self, output_states, attention_mask):
    token_embeddings = output_states[0] #First element of output_states contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)

def max_pooling(self, output_states, attention_mask):
    token_embeddings = output_states[0] #First element of output_states contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    token_embeddings[input_mask_expanded == 0] = -1e9  # Set padding tokens to large negative value
    return torch.max(token_embeddings, 1)[0]
