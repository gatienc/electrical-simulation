ce qu'on fait c'est qu'on va minimiser la dépense financière de la consommation électrique d'une maison avec une installation photovoltaïque et une batterie de grande capacité, la simulation est faite en fonction de la prévision météo pour prédire la production électrique des panneaux solaires le lendemain
pour trouver la valeure de charge de la batterie à atteindre pendant l'heure creuse, on minimise la fonction de coût de la dépense financière de la consommation électrique d'une maison. Cette fonction de coût est définie comme suit:
dépense d'achat d'éléctricité en heure creuse + depense d'achat d'éléctricité en heure pleine 

le inverter consomme : 0.003424 kWh par heure
ce qui correspond à 3.424 W/h
n'est-ce pas possible de l'éteindre la nuit ?


pour les prévisions de consommation éléctrique en france: https://www.rte-france.com/en/eco2mix/electricity-consumption-france

pour les méthodes de simulation de production éléctrique,étant donné qu'il est difficile de trouver l'efficacité d'un panneau solaire en fonction de la température,

on utilise le modèle de simulation SAM (System Advisor Model) qui est un modèle de simulation de production éléctrique de panneaux solaires, il est basé sur le modèle de perte de puissance de panneaux solaires de Sandia National Laboratories, il est utilisé pour simuler la production éléctrique d'un panneau solaire en fonction des paramètres météo, 


notre objectif est de minimiser les coûts financiers de la consommation électrique d'une maison avec une installation photovoltaïque et une batterie de grande capacité, la simulation est faite en fonction de la prévision météo pour prédire la production électrique des panneaux solaires le lendemain


sur un modèle où le calcul d'optimisation se fait toute les demies journées: 

il faut optimiser la charge de la batterie en fonction de la charche actuelle , de la production solaire prévue pour le lendemain et de la consommation prévue pour le lendemain


## bibliographie

[prix du kWh en france heure creuse/ pleine](https://electricite.net/edf/tarifs)



[données de production élétrique par heure en france](https://www.rte-france.com/en/eco2mix/electricity-consumption-france)

[Temperature Dependent Photovoltaic (PV) Efficiency and Its Effect on PV Production in the World](https://pdf.sciencedirectassets.com/277910/1-s2.0-S1876610213X00037/1-s2.0-S1876610213000829/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLWVhc3QtMSJGMEQCIDxwbCgPJIe3XepP7x%2B9BviopeA5bZwpAcfijwyOZhygAiAyfTq6NFQOFcIqa2Ggx3Ny%2BhvzWF6lSm4htz0oDTFCLyqyBQgVEAUaDDA1OTAwMzU0Njg2NSIMiufz7g%2B2fNuy6g9LKo8FCYAmdDXqllPvueQ%2FkZZun6%2BSlt253MHYQXnfA5%2FdgKE7jm6CbpEnf1GlkThnXRl0wircIz7TYjewV4aiUbYsmFYBeCC4OvzW6MsXzzQ6%2F0UobyWGYUEi%2FO1WGUiA2MljcUdFdeX4QX%2FYnHO00qiiPf78Y79TuUUgfuSxRo%2FzoP2M6vb7WLctXj27r1%2FYh4IC%2FBbtRhuk%2B3nSAl0v9JOGnR2UspXbIBe3pxEP%2BGPIdQVdUHbBVIhDA3%2FcDg3UIVTMmuKZPYjVjhTa0R2JY186W4p3GBPJZSPj3cAUuzrUlDpbSucDGQbm8aV4MV%2FQPMMMiTHKE0RArG%2BlXPEVBuy3RPYzpf3ecbEnfb1TOCN3V52d%2Bplzwydv%2BQ4sqINEyC6zL98n%2BaWQNxBYwCKaBQUdKNklEjolYsGWg3t%2FKlUXAVBDHdQ%2FlNv3zJKEc5cMpqhGRDZzgxoIcUzK6Ns2Rfo0H36YifiJ9UpFpRIEG3OlVBTRBekmQJxNPaD0xpwxvkxUhduDJFpgYXrjS%2B%2Bdo37aGaLpRzRZYVbzrMXEM%2FELN7j3CrlJPQEzU8JBzrCgEDMcvpuocEMLTR%2F7grgDCZLnX53H0eYgR4y%2BEpNewxs7hTPBqHPdanIyDHHn4TUwJJM%2F3Fe%2BpfHMXIfondr2XJ7NN8yzBraerZ1y4OPX7deGl32WuzjdDA%2F%2FbrGSuuO%2FcuVYnGouemZOekgV%2BlnzSFzuB8p4F%2B7%2Fnxtf4KuRYksGqw2GBsafJDxNP4CF%2Fwz9%2BkdrD31TQgLxobemkZcBTQKITQOEsSsDaDefad7JVJxNLaw8oGhckVdMVNDd%2FADqSNwaGBf5yfTxNuFTIjU3Y%2FgNuz9Vyvf9ac9Y2d8C4nC0ADDEtLWhBjqyAfhxml4zz1ucWhGCx6DmllRAHw0aG926xwlbkKay7NMZjyy1ZrwjpWBbGQvTe0%2BvIgEBhwp3dViKiGsgrGZMtLfDpYvr8xbyzccMMgKvD%2B1qa%2FSEISGm7Iq9yPnnB400Ipwix4ZGH6Lcm2E7CV0dTBBOfcZnIUDDeYAhAADAxPXZ4lnCV7K5GjtruQZ%2BXDcbxhpdaP0lpR2vjWqp1hQAziISNForrORTm7CgY%2Fr8vL0BZdY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20230405T124744Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTY3WG6V44O%2F20230405%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=1ee035e63c510d253c8cb1ef830c41db9a9735dbcd10651815d5cc867be8cad4&hash=dd5fcfd2e28d4ad1b4c378d828ee7a4c6d1fd1130e8276f820d8ba9d93427828&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S1876610213000829&tid=spdf-cdd80fd2-a92c-407c-b6ed-fb0bbcddc3c1&sid=4688a5f7248e884dd32a1b9-49feb8233f0dgxrqb&type=client&tsoh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&ua=0011590555570b5203&rr=7b31e6bcfe4037e9&cc=fr)