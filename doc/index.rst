.. ConWhAt documentation master file, created by
   sphinx-quickstart on Mon Apr 23 21:31:41 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to ConWhAt's documentation!
===================================

.. include:: ../README.md

.. toctree::
   :maxdepth: 1
   :caption: About ConWhAt
   :glob:
      
   about_conwhat/overview
   about_conwhat/ontology_and_representation
   about_conwhat/conwhat_atlases

.. toctree::
   :maxdepth: 1
   :caption: Getting Started
   :glob:
 
   getting_started/installation
   auto_examples/eg01r__downloading_conwhat_atlases
   auto_examples/eg02r__exploring_conwhat_atlases

.. toctree::
   :maxdepth: 1
   :caption: Analyses of Brain Lesions
   :glob:

   auto_examples/eg03r__defining_a_synthetic_lesion
   auto_examples/eg04r__assessing_the_network_impact_of_lesions


.. toctree::
   :maxdepth: 1
   :caption: Other Applications
   :glob:

   auto_examples/eg05r__connectivity_based_decomposition_of_white_matter_tracts
   auto_examples/eg06r__setting_up_tvb_simulations_from_conwhat_outputs
