# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

from abc import abstractmethod


@abstractmethod
class BaseStrategy:
    def __init__(self, mode, config, model_path=None):
        '''Federated learning strategy

        Args:
            mode (str): which part the instantiated object should play,
                typically either :code:`client` or :code:`server`.
            config (dict): initial config dict.
            model_path (str): where to find model, needed for debugging only.
        '''
        pass

    def generate_client_payload(self, trainer):
        '''Generate client payload

        Args:
            trainer (core.Trainer object): trainer on client.

        Returns:
            dict containing payloads in some specified format.
        '''
        pass

    def process_individual_payload(self, worker_trainer, payload):
        '''Process client payload
        
        Args:
            worker_trainer (core.Trainer object): trainer on server
                (aka model updater).
            payload (dict): whatever is generated by
                :code:`generate_client_payload`.

        Returns:
            True if processed succesfully, False otherwise.
        '''
        pass

    def combine_payloads(self, worker_trainer, curr_iter, num_clients_curr_iter, total_clients, client_stats, logger=None):
        '''Combine payloads to update model
        
        Args:
            worker_trainer (core.Trainer object): trainer on server
                (aka model updater).
            curr_iter (int): current iteration.
            num_clients_curr_iter (int): number of clients on current iteration.
            total_clients (int): size of total pool of clients (for privacy accounting)
            client_stats (dict): stats being collected.
            logger (callback): function called to log quantities.
        '''
        pass