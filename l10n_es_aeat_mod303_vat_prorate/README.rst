=====================
Prorrata de IVA [303]
=====================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:2708bb797c1ce17c7b070ebfac506b40f5ed10543ff7435a54510a54a005e0c8
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fl10n--spain-lightgray.png?logo=github
    :target: https://github.com/OCA/l10n-spain/tree/14.0/l10n_es_aeat_mod303_vat_prorate
    :alt: OCA/l10n-spain
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/l10n-spain-14-0/l10n-spain-14-0-l10n_es_aeat_mod303_vat_prorate
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/l10n-spain&target_branch=14.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

Este módulo contempla la casuística de prorrata en el modelo 303 cuando se han
creado ya los apuntes contables separados con el módulo `l10n_es_vat_prorate`.

Esto es necesario si se cuenta con el SII y se debe enviar la información ya
seccionada.

Para el caso de que se quiera hacer la repartición con el asiento de liquidación
del IVA, utilizar `l10n_es_aeat_vat_prorrate`.

**Table of contents**

.. contents::
   :local:

Configuration
=============

 Para entender el funcionamiento de la prorrata, remitirse a la configuración de
 `l10n_es_aeat_vat_prorate`.

Usage
=====

#. Realizar la declaración 303 de la forma habitual.
#. El IVA deducible ya vendrá minorado por el porcentaje de la prorrata.
#. En la casilla 44, se mostrará el importe de la prorrata que se minoró.

Known issues / Roadmap
======================

* La prorrata especial de IVA no está contemplada.
* No se incluye la posibilidad de las facturas de actividad diferenciada, de las
  que te puedes deducir el 100% del IVA de la factura.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/l10n-spain/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/l10n-spain/issues/new?body=module:%20l10n_es_aeat_mod303_vat_prorate%0Aversion:%2014.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Tecnativa

Contributors
~~~~~~~~~~~~

* `Tecnativa <https://www.tecnativa.com>`_

  * Pedro M. Baeza
  * Víctor Martínez

Maintainers
~~~~~~~~~~~

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

.. |maintainer-victoralmau| image:: https://github.com/victoralmau.png?size=40px
    :target: https://github.com/victoralmau
    :alt: victoralmau
.. |maintainer-pedrobaeza| image:: https://github.com/pedrobaeza.png?size=40px
    :target: https://github.com/pedrobaeza
    :alt: pedrobaeza

Current `maintainers <https://odoo-community.org/page/maintainer-role>`__:

|maintainer-victoralmau| |maintainer-pedrobaeza| 

This module is part of the `OCA/l10n-spain <https://github.com/OCA/l10n-spain/tree/14.0/l10n_es_aeat_mod303_vat_prorate>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
