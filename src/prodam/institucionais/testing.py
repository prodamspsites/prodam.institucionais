# -*- coding: utf-8 -*-

# from plone.app.testing import FunctionalTesting
# from plone.app.testing import IntegrationTesting
# from plone.app.testing import PLONE_FIXTURE
# from plone.app.testing import PloneSandboxLayer


# class Fixture(PloneSandboxLayer):

#     defaultBases = (PLONE_FIXTURE,)

#     def setUpZope(self, app, configurationContext):
#         # Load ZCML
#         import prodam.institucionais
#         self.loadZCML(package=prodam.institucionais)

#     def setUpPloneSite(self, portal):
#         self.applyProfile(
#             portal, 'prodam.institucionais:default')


# FIXTURE = Fixture()

# INTEGRATION_TESTING = IntegrationTesting(
#     bases=(FIXTURE,),
#     name='prodam.institucionais:Integration')

# FUNCTIONAL_TESTING = FunctionalTesting(
#     bases=(FIXTURE,),
#     name='prodam.institucionais:Functional')
