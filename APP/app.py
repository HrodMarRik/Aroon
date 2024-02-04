"""
au lancement du code : ouverture du GUI, qui lance le BACK 

GUI different pour PC/tel/tablet mais BACK identique 


"""


class APP_GUI(object):
	"""docstring for APP_GUI"""
	def __init__(self, arg):
		super(APP_GUI, self).__init__()
		self.arg = arg
		
class APP_BACK(object):
	"""docstring for APP_BACK"""
	def __init__(self, arg):
		super(APP_BACK, self).__init__()
		self.arg = arg
	
	def ouverture_BDD(self.ID_client):
		pass	


ouverture_BDD(ID_client)

if etat_avancement == None:
	pass
elif etat_avancement == "recherche":
	pass
elif etat_avancement == "organisation":
	pass
elif etat_avancement == "pret":
	pass
else :
	gestion_erreur(etat_avancement)


if __name__ == '__main__':
	APP_GUI()
	
