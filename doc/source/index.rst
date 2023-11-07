PDFO documentation
==================

.. toctree::
    :maxdepth: 1
    :hidden:

    User guide <user/index>
    Python API reference <python/index>

:Version: |version|
:Downloads: |total_downloads|
:Author of solvers: `M. J. D. Powell <https://www.zhangzk.net/powell.html>`_
:Authors of PDFO: `Tom M. Ragonneau <https://www.tomragonneau.com>`_ | `Zaikun Zhang <https://www.zhangzk.net>`_

PDFO is a cross-platform package providing the late `Professor M. J. D. Powell <https://www.zhangzk.net/powell.html>`_'s derivative-free (i.e., zeroth-order) optimization solvers.
Using only function values, but not derivatives, it solves problems of the form

.. math::

    \min_{x \in \R^n} \quad \obj ( x ) \quad \text{s.t.} \quad
    \begin{cases}
        \xl \le x \le \xu,\\
        \aub x \le \bub, ~ \aeq x = \beq,\\
        \cub ( x ) \le 0, ~ \ceq ( x ) = 0.
    \end{cases}

To install PDFO for Python, run in your terminal

.. code-block:: bash

    pip install pdfo

You can also check the :ref:`installation guide for MATLAB<matlab-installation>`.
For more details, see the :ref:`user guide<user-guide>`.

Citing PDFO
-----------

If you would like to acknowledge the significance of PDFO in your research, we suggest citing the project as follows:

- T.\  M.\  Ragonneau and Z.\  Zhang. PDFO: a cross-platform package for Powell's derivative-free optimization solvers. arXiv:`2302.13246 [math.OC] <https://arxiv.org/abs/2302.13246>`_, 2023.

The corresponding BibTeX entry is given hereunder.

.. code-block:: bib

    @misc{pdfo,
        author       = {Ragonneau, T. M. and Zhang, Z.},
        title        = {{PDFO}: a cross-platform package for {P}owell's derivative-free optimization solvers},
        howpublished = {arXiv:2302.13246 [math.OC]},
        year         = 2023,
    }

Statistics
----------

As of |today|, PDFO has been downloaded |total_downloads| times, including

- |github_downloads| times on `GitHub <https://hanadigital.github.io/grev/?user=pdfo&repo=pdfo>`_,
- |pypi_downloads| times on `PyPI <https://pypistats.org/packages/pdfo>`_ (`mirror downloads <https://pypistats.org/faqs>`_ excluded), and
- |conda_downloads| times on `Anaconda <https://anaconda.org/conda-forge/pdfo>`_.

The following figure shows the cumulative downloads of PDFO.

.. plot::

    import json
    from datetime import datetime
    from urllib.request import urlopen

    from matplotlib import dates as mdates
    from matplotlib import pyplot as plt
    from matplotlib.ticker import FuncFormatter

    # Download the raw statistics from GitHub.
    base_url = 'https://raw.githubusercontent.com/pdfo/stats/main/archives/'
    conda = json.loads(urlopen(base_url + 'conda.json').read())
    github = json.loads(urlopen(base_url + 'github.json').read())
    pypi = json.loads(urlopen(base_url + 'pypi.json').read())

    # Keep only the mirror-excluded statistics for PyPI.
    pypi = [{'date': d['date'], 'downloads': d['downloads']} for d in pypi if d['category'] == 'without_mirrors']

    # Combine the daily statistics into a single list.
    download_dates = []
    daily_downloads = []
    for src in [conda, github, pypi]:
        for d in src:
            date = datetime.strptime(d['date'], '%Y-%m-%d').date()
            try:
                # If the date is already in the list, add the downloads.
                i = download_dates.index(date)
                daily_downloads[i] += d['downloads']
            except ValueError:
                # Otherwise, add the date and downloads.
                download_dates.append(date)
                daily_downloads.append(d['downloads'])
    daily_downloads = [d for _, d in sorted(zip(download_dates, daily_downloads))]
    download_dates = sorted(download_dates)
    cumulative_downloads = [sum(daily_downloads[:i]) for i in range(1, len(daily_downloads) + 1)]

    # Plot the cumulative downloads.
    fig, ax = plt.subplots()
    ax.xaxis.set_minor_locator(mdates.MonthLocator())
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda y, p: format(int(y), ',')))
    ax.margins(x=0, y=0)
    ax.plot(download_dates, cumulative_downloads, color='#4f8d97')
    ax.set_title('Cumulative downloads of PDFO')

We started tracking the downloads of PDFO on `Anaconda <https://anaconda.org/conda-forge/pdfo>`_ on October 2022.
The API we employ to track the downloads of PDFO on `Anaconda <https://anaconda.org/conda-forge/pdfo>`_ only provides the cumulative downloads.
Therefore, we do not know when the downloads of PDFO on `Anaconda <https://anaconda.org/conda-forge/pdfo>`_ have been made.
In this plot, all of them are assumed to have been made on October 2022.

Acknowledgments
---------------

PDFO is dedicated to the memory of the late `Professor M. J. D. Powell <https://www.zhangzk.net/powell.html>`_ with gratitude for his inspiration and for the treasures he left to us.
We are grateful to `Professor Ya-xiang Yuan <http://lsec.cc.ac.cn/~yyx/>`_ for his everlasting encouragement and support.

The development of PDFO is a long-term project, which would not be sustainable without the continued funds from the `Hong Kong Research Grants Council <https://www.ugc.edu.hk/eng/rgc/>`_ (ref. PolyU 253012/17P, PolyU 153054/20P, and PolyU 153066/21P), the `Hong Kong PhD Fellowship Scheme <https://cerg1.ugc.edu.hk/hkpfs/index.html>`_ (ref. PF18-24698), and `The Hong Kong Polytechnic University <https://www.polyu.edu.hk/>`_ (PolyU), in particular the `Department of Applied Mathematics <https://www.polyu.edu.hk/ama>`_ (AMA).
