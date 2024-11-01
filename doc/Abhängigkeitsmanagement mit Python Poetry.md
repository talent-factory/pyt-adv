---
ref:
- "https://realpython.com/dependency-management-python-poetry"
tags:
- python
- requirements
- poetry
- pip
- pypi
---

# Abhängigkeitsmanagement mit Python Poetry

---

## Inhaltsverzeichnis

- [Voraussetzungen](#Voraussetzungen "wikilink")
  - [Terminologien](#Terminologien "wikilink")
  - [Installation von Poetry](#Installation von Poetry "wikilink")
- [Erste Schritte mit Python Poetry](#Erste Schritte mit Python Poetry "wikilink")
  - [Erstellen eines neues Poetry-Projekt](#Erstellen eines neues Poetry-Projekt "wikilink")
  - [Verstehen der Projektstruktur](#Verstehen der Projektstruktur "wikilink")
  - [Inhalt der pyproject.toml Datei](#Inhalt der pyproject.toml Datei "wikilink")
- [Arbeiten Sie mit Python Poetry](#Arbeiten Sie mit Python Poetry "wikilink")
  - [Aktivieren einer benutzerdefinierte virtuelle Umgebung](#Aktivieren einer benutzerdefinierte virtuelle Umgebung "wikilink")
  - [Verwenden der virtuelle Umgebung von Poetry](#Verwenden der virtuelle Umgebung von Poetry "wikilink")
  - [Laufzeitabhängigkeiten deklarieren](#Laufzeitabhängigkeiten deklarieren "wikilink")
  - [Gruppenabhängigkeiten und zusätzliche Funktionen hinzufügen](#Gruppenabhängigkeiten und zusätzliche Funktionen hinzufügen "wikilink")
  - [Installieren unseres Pakets mit Poetry](#Installieren unseres Pakets mit Poetry "wikilink")
- [Abhängigkeiten mit Poetry verwalten](#Abhängigkeiten mit Poetry verwalten "wikilink")
  - [Manuelles Sperren von Abhängigkeiten](#Manuelles Sperren von Abhängigkeiten "wikilink")
  - [Synchronisieren der Umgebung](#Synchronisieren der Umgebung "wikilink")
  - [Aktualisieren von Abhängigkeiten](#Aktualisieren von Abhängigkeiten "wikilink")
  - [Vergleich von pyproject.toml und poetry.lock](#Vergleich von pyproject.toml und poetry.lock "wikilink")
- [Poetry in einem bestehenden Projekt verwenden](#Poetry in einem bestehenden Projekt verwenden "wikilink")
  - [Einen Ordner in ein Poetry-Projekt umwandeln](#Einen Ordner in ein Poetry-Projekt umwandeln "wikilink")
  - [Abhängigkeiten in Poetry importieren](#Abhängigkeiten in Poetry importieren "wikilink")
  - [Abhängigkeiten von Poetry exportieren](#Abhängigkeiten von Poetry exportieren "wikilink")
- [Befehlsreferenz](#Befehlsreferenz "wikilink")


<hr>

Wenn Ihr Python-Projekt auf externe Pakete angewiesen ist, müssen Sie sicherstellen, dass Sie die richtige Version jedes Pakets verwenden. Nach einem Update funktioniert ein Paket möglicherweise nicht mehr wie zuvor. Ein **Abhängigkeitsmanager** wie Python Poetry hilft Ihnen dabei, externe Pakete in Ihren Projekten zu spezifizieren, zu installieren und zu lösen. Auf diese Weise können Sie sicher sein, dass Sie immer mit der richtigen Abhängigkeitsversion auf jeder Maschine arbeiten.

**In diesem Tutorial lernen Sie, wie man:**

- Erstellen Sie ein **neues Projekt** mit Poetry
- Fügen Sie Poetry zu einem **bestehenden Projekt** hinzu
- Konfigurieren Sie Ihr Projekt über **`pyproject.toml`**
- Fixieren Sie die **Versionsabhängigkeiten** Ihres Projekts
- Installieren Sie Abhängigkeiten aus einer **`poetry.lock`** Datei
- Führen Sie grundlegende Poetry-Befehle mit der **Poetry CLI** aus

[Poetry](https://python-poetry.org/) hilft Ihnen, neue Projekte zu erstellen oder bestehende Projekte zu pflegen, während es sich um die **Abhängigkeitsverwaltung** für Sie kümmert. Es verwendet die `pyproject.toml` Datei, die zum Standard für die Definition von Build-Anforderungen in modernen Python-Projekten geworden ist.

Um dieses Tutorial abzuschliessen und das Beste daraus zu holen, sollten Sie ein grundlegendes Verständnis von [virtuellen Umgebungen], [Modulen und Paketen] und [`pip`] haben.

Während Sie sich in diesem Tutorial auf die Abhängigkeitsverwaltung konzentrieren, kann Poetry Ihnen auch dabei helfen, ein [Vertriebspaket zu erstellen](https://python-poetry.org/docs/cli/#build) für Ihr Projekt. Wenn Sie Ihre Arbeit teilen möchten, dann können Sie Poetry verwenden, um Ihr Projekt auf dem [Python Packaging Index (PyPI)](https://pypi.org/) zu [veröffentlichen](https://python-poetry.org/docs/cli/#publish).

## Voraussetzungen

Bevor Sie sich in die Feinheiten von Python Poetry vertiefen, kümmern Sie sich um einige Voraussetzungen. Zuerst lesen Sie einen kurzen Überblick über die Terminologie, die Sie in diesem Tutorial antreffen werden. Als nächstes installieren Sie Poetry selbst.

### Terminologien

Wenn Sie jemals eine [`import` Anweisung] in einem Ihrer Python-Skripte verwendet haben, dann haben Sie mit **Modulen** und **Paketen** gearbeitet. Einige davon könnten Python-Dateien sein, die Sie selbst geschrieben haben. Andere könnten **Standardbibliotheks-Module** sein, die mit Python geliefert werden, wie [`datetime`]. Manchmal reicht jedoch das, was Python bietet, nicht aus. Das ist der Moment, in dem Sie sich möglicherweise an externe Module und Pakete wenden, die von Dritten gepflegt werden.

Wenn Ihr Python-Code auf solche externen Module und Pakete angewiesen ist, werden diese zu den **Anforderungen** oder **Abhängigkeiten** Ihres Projekts.

Um Pakete zu finden, die von der Python-Community beigetragen wurden und nicht Teil der [Python-Standardbibliothek](https://docs.python.org/3/py-modindex.html) sind, können Sie [PyPI](https://pypi.org/) durchsuchen. Sobald Sie ein Paket gefunden haben, das Sie interessiert, können Sie Poetry verwenden, um dieses Paket in Ihrem Projekt zu verwalten und zu installieren. Bevor Sie sehen, wie das funktioniert, müssen Sie Poetry auf Ihrem System installieren.

### Installation von Poetry

Poetry wird als ein [Python-Paket selbst](https://pypi.org/project/poetry/) verteilt, was bedeutet, dass Sie es in eine virtuelle Umgebung mit `pip` installieren können, genau wie jedes andere externe Paket:

``` bash
python3 -m pip install poetry
```

Das ist in Ordnung, wenn Sie es nur schnell ausprobieren möchten. Die [offizielle Dokumentation](https://python-poetry.org/docs/) rät jedoch *dringend davon ab*, Poetry in die virtuelle Umgebung Ihres Projekts zu installieren, die das Tool verwalten muss. Da Poetry selbst auf mehrere externe Pakete angewiesen ist, besteht die Gefahr eines **Abhängigkeitskonflikts** zwischen einer Ihrer Projektabhängigkeiten und denen, die von Poetry benötigt werden. Dies könnte dazu führen, dass Poetry oder Ihr Code nicht richtig funktioniert.

In der Praxis möchten Sie Poetry immer von jeder virtuellen Umgebung trennen, die Sie für Ihre Python-Projekte erstellen. Sie möchten Poetry auch **systemweit** installieren, um darauf als eigenständige Anwendung zuzugreifen, unabhängig von der spezifischen virtuellen Umgebung oder Python-Version, in der Sie gerade arbeiten.

Es gibt mehrere Möglichkeiten, Poetry auf Ihrem Computer zum Laufen zu bringen, einschließlich:

1.  Ein Werkzeug namens `pipx`
2.  Der offizielle Installer
3.  Manuelle Installation
4.  Vorgefertigte Systempakete

In den meisten Fällen ist der *empfohlene Weg zur Installation von Poetry* mit Hilfe von `pipx`, das sich um die Erstellung und Pflege isolierter virtueller Umgebungen für Python-Anwendungen in der Befehlszeile kümmert. Nachdem Sie [`pipx` installiert](https://pipx.pypa.io/stable/installation/) haben, können Sie Poetry installieren, indem Sie den folgenden Befehl in Ihrem Terminalfenster ausführen:

``` bash
pipx install poetry
```

Obwohl dieser Befehl sehr ähnlich zu dem aussieht, den du zuvor gesehen hast, wird er Poetry in einer dedizierten virtuellen Umgebung installieren, die nicht mit anderen Python-Paketen geteilt wird.

Entscheidend ist, dass `pipx` auch einen Alias für das `poetry`-Ausführbare in Ihrer [Shell](https://de.wikipedia.org/wiki/Shell_(Informatik)) setzt, sodass Sie Poetry aus jedem Verzeichnis aufrufen können, ohne die zugehörige virtuelle Umgebung manuell zu aktivieren:

``` bash
poetry --version
Poetry (version 1.8.4)
```

Wenn Sie `poetry` in Ihrem Terminal oder PowerShell-Konsole eingeben, beziehen Sie sich immer auf das ausführbare Skript, das in seiner isolierten virtuellen Umgebung installiert ist. Tatsächlich führen Sie den `poetry` Befehl oft innerhalb einer aktiven virtuellen Umgebung Ihres Projekts aus, und Poetry wird es korrekt aufnehmen!

Falls Sie aus irgendeinem Grund `pipx` nicht verwenden können oder möchten, dann ist das Nächstbeste, was Sie tun können, die Nutzung des [**offiziellen Installers**](https://github.com/python-poetry/install.python-poetry.org), den Sie herunterladen und mit einem Befehl wie diesem ausführen können:

``` bash
curl -sSL https://install.python-poetry.org | python3 -
```

Auf Windows können Sie den `Invoke-WebRequest` PowerShell-Befehl zusammen mit der Option `-UseBasicParsing` verwenden, um den Inhalt einer angeforderten URL herunterzuladen und ihn auf den **Standardausgabestrom (stdout)** zu drucken. Mit dem Pipe-Operator (`|`) können Sie das heruntergeladene `install-poetry.py` Skript abfangen und es in Ihren Python-Interpreter aus dem **Standardeingabestrom (stdin)** umzuleiten.

Der `curl`-Befehl lädt den Inhalt einer angeforderten URL herunter und druckt ihn auf den **Standardausgabestrom (stdout)**. Wenn Sie den Pipe-Operator (`|`) verwenden, definieren Sie eine [Unix-Pipeline](https://en.wikipedia.org/wiki/Pipeline_(Unix)), die das heruntergeladene `install-poetry.py`-Skript abfängt und es in Ihren Python-Interpreter aus dem **Standardeingabestrom (stdin)** *leitet*.

Unter der URL [`install.python-poetry.org`](https://install.python-poetry.org/) befindet sich ein plattformübergreifendes Python-Skript, das mehr oder weniger das repliziert, was `pipx` tut, aber auf eine etwas andere Weise.

Wenn Sie an den technischen Details interessiert sind, werfen Sie einen Blick auf den zugrunde liegenden [Quellcode](https://github.com/python-poetry/install.python-poetry.org/blob/main/install-poetry.py) des Installationsskripts. Indem Sie seine Schritte **manuell** befolgen, haben Sie die Möglichkeit, den Installationsprozess anzupassen, wenn Sie etwas Spezifisches für Ihre Einrichtung benötigen. Dies kann besonders nützlich sein, wenn Sie eine [kontinuierliche Integration](https://python-poetry.org/docs/#ci-recommendations) Umgebung vorbereiten.

Schliesslich können einige Betriebssysteme Poetry als **natives Paket** bündeln. Zum Beispiel, wenn Sie ein [Debian-basiertes](https://en.wikipedia.org/wiki/List_of_Linux_distributions#Debian-based) System wie Ubuntu verwenden, könnten Sie in der Lage sein, Poetry mit `apt` zu installieren, so

``` bash
sudo apt install python3-poetry
```

Beachten Sie, dass die auf diese Weise verpackte Poetry-Version möglicherweise nicht die neueste ist. Darüber hinaus kann das native Paket Hunderte von Megabyte zusätzlicher Abhängigkeiten mitbringen, wie zum Beispiel einen weiteren Python-Interpreter, der völlig unnötig wäre, wenn Sie Poetry mit einer der früheren Methoden installiert hätten.

Sobald die Poetry-Installation abgeschlossen ist, können Sie bestätigen, dass sie korrekt funktioniert, indem Sie `poetry --version` in Ihre Befehlszeile eingeben. Dies sollte Ihre aktuelle Version von Poetry ausgeben.

> **Hinweis**
>
> Je nachdem, wie Sie Poetry installiert haben, können Sie einen dieser Befehle versuchen, um es zu aktualisieren:
>
> - `python3 -m pip install --upgrade poetry`
> - `pipx upgrade poetry`
> - `poetry self update`
> - `sudo apt install --only-upgrade python3-poetry`
>
> Alle bis auf den letzten sollten im Allgemeinen sicherstellen, dass Sie die neueste Version von Poetry auf Ihrem Computer installiert haben.

Nun, da Sie überprüft haben, dass Poetry korrekt installiert wurde, ist es an der Zeit zu sehen, wie es funktioniert.

## Erste Schritte mit Python Poetry

In diesem Abschnitt lernen Sie, wie Sie ein neues Poetry-Projekt mit der Befehlszeilenschnittstelle (CLI) des Tools erstellen. Sie werden auch die Projektstruktur erkunden und die `pyproject.toml` Datei inspizieren, welche die Metadaten und Konfiguration des Projekts beinhaltet.

### Erstellen eines neues Poetry-Projekt

Um ein neues Poetry-Projekt von Grund auf neu zu erstellen, verwenden Sie den Befehl [`poetry new`](https://python-poetry.org/docs/cli/#new) gefolgt vom gewünschten Projektnamen. In diesem Tutorial arbeiten Sie an einem Projekt namens `my-poetry`. Machen Sie weiter, erstellen Sie dieses Projekt jetzt und navigieren Sie dann in das neu erstellte Verzeichnis, indem Sie die folgenden Befehle in Ihrem Terminal eingeben:

``` bash
poetry new my-poetry
cd my-poetry
```

Das Ausführen von `poetry new my-poetry` erstellt einen neuen Ordner namens `my-poetry`. Wenn Sie in diesen Ordner schauen, sehen Sie die folgende Struktur:

``` text
my-poetry
├── README.md
├── my_poetry
│   └── __init__.py
├── pyproject.toml
└── tests
    └── __init__.py
```

Haben Sie bemerkt, wie Poetry den Bindestrich (`-`) im bereitgestellten Namen in einen Unterstrich (`_`) im entsprechenden `my_poetry` Unterordner übersetzt hat? Das Tool normalisiert automatisch Python-Paketnamen für Sie. Dies stellt sicher, dass Sie sie als Python-Pakete importieren können. Andernfalls wäre `my-poetry` kein gültiger Bezeichner, da ein Bindestrich den Minusoperator in der Python-Syntax darstellt.

Um mehr Kontrolle über den resultierenden **Paketnamen** zu haben, können Sie optional das Argument `--name` übergeben, das es Ihnen ermöglicht, einen anderen Namen für das Python-Paket als Ihren Projektordner anzugeben:

``` bash
poetry new my-poetry --name project
```

Beachten Sie, dass Poetry den über dieses Argument bereitgestellten Paketnamen auch normalisiert, sollte er einen Bindestrich enthalten.

Bei der Erstellung der Ordnerstruktur für ein neues Projekt folgt Poetry standardmäßig dem **flachen Layout**. In diesem Layout befindet sich Ihr Python-Paket auf der obersten Ebene des Projektordners. Eine weitere beliebte Wahl in Python ist das **src Layout**, das den Code in einem zusätzlichen `src/` Elternordner hält. Wenn Sie dieses Layout bevorzugen, dann geben Sie die `--src` Flagge an Poetry weiter, wenn Sie ein neues Projekt erstellen:

``` bash
poetry new my-poetry --name project --src
```

Wenn Sie diese Flagge hinzufügen, ergibt sich eine leicht andere Ordnerstruktur:

``` text
my-poetry
├── README.md
├── pyproject.toml
├── src
│   └── project
│       └── __init__.py
└── tests
    └── __init__.py
```

Nun ist Ihr `project` Paket im `src` Ordner verschachtelt. Sowohl das flache als auch das src Layout haben ihre Vor- und Nachteile, die Sie vergleichen können, indem Sie den [Python Packaging Guide](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/) lesen, falls Sie interessiert sind. Sie werden jedoch für den Rest dieses Tutorials beim Standard-Flachlayout bleiben.

> **Hinweis**
>
> Es ist möglich, eine benutzerdefinierte Ordnerstruktur anzugeben und sogar mehrere Python-Pakete in einem Poetry-Projekt zu haben. Dies kann in grösseren Projekten nützlich sein, die in mehrere, separate Komponenten organisiert werden müssen. 
>
> Um dies mit Poetry zu erreichen, müssen Sie jedoch die Konfigurationsdatei Ihres Projekts von Hand bearbeiten. Weitere Details finden Sie in der [offiziellen Dokumentation](https://python-poetry.org/docs/pyproject#packages).

Wie Sie sehen können, ist das Erstellen eines neuen Projekts mit Poetry ziemlich einfach und bequem. Sie erhalten kostenlos eine grundlegende Ordnerstruktur, ohne zu viel darüber nachdenken zu müssen, wie Sie Ihre Python-Dateien organisieren.

### Verstehen der Projektstruktur

Der `my_poetry` Unterordner selbst ist noch nicht sehr spektakulär. Darin finden Sie nur eine leere `__init__.py` Datei, die es in ein importierbares Python-Paket verwandelt.

Ähnlich ist der `tests` Unterordner ein weiteres Python-Paket, das dazu gedacht ist, die [Unit Tests] und möglicherweise andere Arten von Tests für Ihr Projekt zu enthalten und so die besten Programmierpraktiken zu fördern.

> **Hinweis**
>
> Ältere Poetry-Versionen haben diese beiden `__init__.py` Dateien an dieser Stelle mit Beispielcode gefüllt. Neuere Versionen von Poetry generieren jedoch diese Dateien leer, um falsche Annahmen über die Struktur des Projekts oder Ihre Absichten als Entwickler zu vermeiden.

Poetry generiert auch standardmässig eine leere [README](https://en.wikipedia.org/wiki/README) Datei mit einer `.md` Erweiterung, was die Verwendung von [Markdown](https://en.wikipedia.org/wiki/Markdown) für die Formatierung vorschlägt. Wenn Sie kein Fan von Markdown sind, dann sind Ihre anderen Optionen entweder [einfacher Text](https://en.wikipedia.org/wiki/Plain_text) oder das [reStructuredText](https://en.wikipedia.org/wiki/ReStructuredText) Format. Dies sind die drei Formate, die [PyPI momentan rendern kann](https://packaging.python.org/en/latest/guides/making-a-pypi-friendly-readme/).

Zuletzt erstellt Poetry eine Konfigurationsdatei namens `pyproject.toml` mit den minimal erforderlichen Metadaten für Ihr Projekt, wie in [PEP 518](https://peps.python.org/pep-0518/) beschrieben. Sie werden sich diese nun genauer ansehen.

### Inhalt der pyproject.toml Datei

Eine der wichtigsten Dateien für die Arbeit mit Poetry ist die `pyproject.toml` Datei. Diese Datei ist keine Erfindung von Poetry, sondern ein **Konfigurationsdatei** Standard, der in PEP 518 definiert ist.

> Dieser PEP spezifiziert, wie Python-Softwarepakete angeben sollten, welche Build-Abhängigkeiten sie haben, um ihr gewähltes Build-System auszuführen. Als Teil dieser Spezifikation wird eine neue Konfigurationsdatei eingeführt, die Softwarepakete verwenden können, um ihre Build-Abhängigkeiten zu spezifizieren (mit der Erwartung, dass dieselbe Konfigurationsdatei für zukünftige Konfigurationsdetails verwendet wird). ([Quelle](https://peps.python.org/pep-0518/#abstract))

Die Autoren haben einige Dateiformate für die neue Konfigurationsdatei in Betracht gezogen, die im obigen Zitat erwähnt wird. Letztendlich haben sie sich für das **TOML**-Format entschieden, was für [Tom's Obvious Minimal Language](https://toml.io/en/) steht. Ihrer Meinung nach ist TOML flexibel genug und hat eine bessere Lesbarkeit und weniger Komplexität als andere Optionen wie [YAML], [JSON], CFG oder [INI](https://en.wikipedia.org/wiki/INI_file).

> **Hinweis**
>
> Um Python zu ermöglichen, TOML-Dateien zu lesen, die in der Python-Community kürzlich an Beliebtheit gewonnen haben, hat die Standardbibliothek das Drittanbieter-Paket [`tomli`](https://pypi.org/project/tomli/) aufgenommen und es in [`tomllib`] umbenannt. Es ist seit [Python 3.11] verfügbar, kann aber nur TOML-Dokumente lesen. Im Gegensatz dazu verlässt sich Poetry auf seine eigene [`tomlkit`](https://pypi.org/project/tomlkit/) Bibliothek, die sowohl das Lesen als auch das Schreiben unterstützt und zusätzliche Funktionen wie die Beibehaltung des ursprünglichen Dateiformats bietet.

Um zu sehen, wie ein TOML-Dokument aussieht, öffnen Sie die von Poetry erstellte `pyproject.toml`-Datei in Ihrem Projektordner:

``` toml
[tool.poetry]
name="rp-poetry"
version="0.1.0"
description=""
authors=["Philipp Acsany <philipp@realpython.com>"]
readme="README.md"

[tool.poetry.dependencies]
python="^3.12"

[build-system]
requires=["poetry-core"]
build-backend="poetry.core.masonry.api"
```

Momentan können Sie drei Abschnitte sehen, die in der `pyproject.toml` Datei oben mit eckigen Klammern gekennzeichnet sind. Diese Abschnitte sind in der TOML-Terminologie als [Tabellen](https://toml.io/en/v1.0.0#table) bekannt. Sie enthalten deklarative Anweisungen, die Werkzeuge wie Poetry erkennen und für das **Verwalten von Abhängigkeiten**, das **Bauen des Projekts** oder das Ausführen anderer Aufgaben verwenden können.

Obwohl PEP 518 einen spezifischen Tabellennamen, `[build-system]`, definiert, der die obligatorischen Build-Anforderungen für Ihr Projekt enthält, lässt der Standard Raum für benutzerdefinierte Erweiterungen. Drittanbieter-Tools können ihre Konfigurationsoptionen unter einzigartigen [Namensräumen](https://de.wikipedia.org/wiki/Namensraum) gruppieren, die mit dem Wort `tool` beginnen.

Zum Beispiel generiert Poetry die `[tool.poetry]` und `[tool.poetry.dependencies]` Tabellen. Die erste ist, wo Sie die Metadaten Ihres Projekts definieren, wie den Namen und die Version, während die zweite Tabelle Ihnen erlaubt, externe Bibliotheken, die von Poetry für Ihr Projekt verwaltet werden, anzugeben.

> \[!note\] Hinweis
>
> Diese beiden sind Beispiele für TOML's Untertabellen, die eine Hierarchie von Konfigurationsoptionen darstellen. Hier ist ihre äquivalente JSON-Darstellung:
>
> ``` json
> "werkzeug": {
>     "dichtung": {
>       "name":"rp-dichtung",
>       "version":"0.1.0",
>       ⋮
>       "abhängigkeiten": {
>           "python":"^3.12"
>       }
>   }
> }
> ```
>
> Wie Sie sehen können, ist das Punktzeichen (`.`) in einem TOML-Tabellennamen ein Trennzeichen, das die verschiedenen Ebenen der Hierarchie trennt, ähnlich wie verschachtelte Objekte in JSON.

Wie Sie sehen können, ist das Punktzeichen (`.`) in einem TOML-Tabellennamen ein Trennzeichen, das die verschiedenen Ebenen der Hierarchie trennt, ähnlich wie verschachtelte Objekte in JSON.

In diesem Fall gehören die beiden Untertabellen nur zu einem externen Tool - Poetry. Aber Sie finden oft Beispiele wie [`[tool.black]`](https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html#configuration-format), [`[tool.isort]`](https://pycqa.github.io/isort/docs/configuration/config_files.html#pyprojecttoml-preferred-format), [`[tool.mypy]`](https://mypy.readthedocs.io/en/stable/config_file.html#example-pyproject-toml) oder [`[tool.pytest.ini_options]`](https://docs.pytest.org/en/stable/reference/customize.html#pyproject-toml) für ihre entsprechenden Tools. Während viele Python-Tools ihre Konfiguration auf `pyproject.toml`-Dateien verlagern, gibt es immer noch bemerkenswerte Ausnahmen. Zum Beispiel unterstützte [`flake8` sie nicht](https://github.com/PyCQA/flake8/issues/234) zum Zeitpunkt des Schreibens, so dass Sie möglicherweise einige separate Konfigurationsdateien benötigen.

Die `pyproject.toml`-Datei beginnt mit der `[tool.poetry]`-Untertabelle, in der Sie allgemeine Informationen über Ihr Projekt speichern können. Poetry definiert einige [Tabellenschlüssel](https://python-poetry.org/docs/pyproject/), die in dieser Untertabelle gültig sind. Während einige davon optional sind, müssen Sie vier immer angeben:

1.  **`name`**: Der Name Ihres Verteilungspakets, der auf PyPI erscheinen wird
2.  **`version`**: Die Version Ihres Pakets, idealerweise nach [semantischer Versionierung](https://semver.org/)
3.  **`description`**: Eine kurze Beschreibung Ihres Pakets
4.  **`authors`**: Eine Liste der Autoren, im Format `name <email>`

Die Untertabelle `[tool.poetry.dependencies]` in Zeile 8 ist für Ihre Abhängigkeitsverwaltung unerlässlich. Sie erfahren mehr darüber und über seine Varianten im nächsten Abschnitt, wenn Sie externe Abhängigkeiten hinzufügen. Bis jetzt gibt sie nur die beabsichtigte Python-Version für Ihr Projekt an.

Die letzte Tabelle, `[build-system]` in Zeile 11 in der `pyproject.toml` Datei, definiert Metadaten, mit denen Poetry und andere Build-Tools arbeiten können. Wie bereits erwähnt, ist diese Tabelle nicht werkzeugspezifisch, da sie kein Präfix hat. Sie hat zwei Schlüssel:

1.  **`erfordert`**: Eine Liste der Abhängigkeiten, die zum Erstellen Ihres Pakets erforderlich sind, macht diesen Schlüssel obligatorisch
2.  **`build-backend`**: Das Python-Objekt, das zum Durchführen des Build-Prozesses verwendet wird

Wenn Sie mehr über diesen Abschnitt der `pyproject.toml` Datei erfahren möchten, können Sie mehr erfahren, indem Sie über [Quellbäume in PEP 517](https://www.python.org/dev/peps/pep-0517/#source-trees) lesen.

Wenn Sie ein neues Projekt mit Poetry erstellen, ist dies die `pyproject.toml` Datei, mit der Sie beginnen. Im Laufe der Zeit fügen Sie weitere Konfigurationsdetails zu Ihrem Paket und den von Ihnen verwendeten Tools hinzu. Während Ihr Projekt wächst, wird auch Ihre `pyproject.toml` Datei wachsen. Das gilt insbesondere für die `[tool.poetry.dependencies]` Unter-Tabelle.

> **Hinweis**
>
> [PEP 621](https://peps.python.org/pep-0621/) gibt an, wie man Projekt-Metadaten in einer `[project]` Tabelle innerhalb von `pyproject.toml` speichert. Es gibt eine [laufende Diskussion](https://github.com/python-poetry/poetry/issues/3332) darüber, wie man PEP 621 in Poetry unterstützen kann, anstatt `[tool.poetry]` zu verwenden.

## Arbeiten Sie mit Python Poetry

Sobald Sie ein Poetry-Projekt eingerichtet haben, kann die eigentliche Arbeit beginnen. In diesem Abschnitt erfahren Sie, wie Poetry sich um die Vorbereitung einer isolierten virtuellen Umgebung für Ihr Projekt kümmert und wie es Ihre Abhängigkeiten darin verwaltet.

### Aktivieren einer benutzerdefinierte virtuelle Umgebung

Wenn Sie ein neues Python-Projekt von Hand erstellen, ist es eine gute Praxis, auch eine dazugehörige [virtuelle Umgebung]  zu erstellen. Andernfalls könnten Sie verschiedene Abhängigkeiten von verschiedenen Projekten verwechseln. Poetry bietet eine eingebaute Unterstützung für virtuelle Umgebungen, um sicherzustellen, dass es nie mit Ihrer globalen Python-Installation interferiert. Das Tool kann den Großteil der Verwaltung von virtuellen Umgebungen für Sie übernehmen.

Jedoch erstellt Poetry nicht sofort eine virtuelle Umgebung, wenn Sie ein neues Projekt starten. Dies ist so konzipiert, dass Sie entscheiden können, ob Sie Ihre virtuellen Umgebungen selbst verwalten oder Poetry sie automatisch für Sie verwalten lassen möchten.

Wenn Sie einen der Poetry-Befehle in Ihrem Projektordner ausführen, erkennt Poetry eine **manuell aktivierte virtuelle Umgebung**.

``` bash
cd my-poetry
poetry env info --path
```

Hier, nachdem Sie Ihr [Arbeitsverzeichnis](https://en.wikipedia.org/wiki/Working_directory) auf `my-poetry` geändert haben, zeigen Sie die [Umgebungsinformationen](https://python-poetry.org/docs/managing-environments#displaying-the-environment-information) mit dem Befehl `poetry env info` an. Da die aktuelle Shell-Sitzung eine aktivierte virtuelle Umgebung hat - wie durch das Prompt-Prefix `(venv)` angezeigt - bestätigt Poetry, dass es diese Umgebung für alle nachfolgenden Befehle innerhalb Ihres Projektrahmens verwenden wird.

Mit anderen Worten, wenn Sie jetzt versuchen würden, Abhängigkeiten zu Ihrem Projekt durch Poetry hinzuzufügen, würden Sie sie in die aktivierte Umgebung installieren, als ob mit dem regulären `pip install` Befehl. Poetry würde auch die notwendigen Metadaten in `pyproject.toml` aktualisieren, wie Sie bald entdecken werden.

Andererseits erstellt Poetry automatisch eine virtuelle Umgebung - oder verwendet eine bereits erstellte - wenn Sie bestimmte Befehle *ohne* eine aktivierte Umgebung in der Shell ausführen. Zum Beispiel tut es dies, wenn Sie eine Abhängigkeit mit der Befehlszeilenschnittstelle von Poetry hinzufügen oder entfernen. Dies verhindert, dass Projekte Ihre systemweite Python-Installation durcheinander bringen und stellt sicher, dass Projektabhängigkeiten jederzeit isoliert bleiben.

> **Hinweis**
>
> Poetry wird versuchen, einen kompatiblen Interpreter in Ihrem System für die neue virtuelle Umgebung zu finden, basierend auf der in Ihrer `pyproject.toml` Datei deklarierten Python-Version.

Das Erstellen von virtuellen Umgebungen durch Poetry ist die bevorzugte Methode, um Abhängigkeiten in Ihren Projekten zu isolieren. Sie werden jetzt sehen, wie das funktioniert.

### Verwenden der virtuelle Umgebung von Poetry

Sie können [alle virtuellen Umgebungen](https://python-poetry.org/docs/managing-environments/#listing-the-environments-associated-with-the-project) auflisten, die Poetry in Ihrem Projekt verwaltet, indem Sie den folgenden Befehl im Verzeichnis Ihres Projekts ausführen:

``` bash
poetry env list
```

An diesem Punkt sehen Sie noch keine Ausgabe, da Sie noch keine Befehle ausgeführt haben, die Poetry veranlassen würden, eine virtuelle Umgebung zu erstellen. Später können Sie mehr als eine virtuelle Umgebung definieren, um Ihr Projekt gegen verschiedene Konfigurationen oder verschiedene Python-Versionen zu testen. Beachten Sie, dass der oben genannte Befehl unabhängig vom Zustand Ihrer Shell bleibt, daher spielt es keine Rolle, ob Sie derzeit eine aktivierte virtuelle Umgebung haben oder nicht.

Um die Unterstützung von Poetry für virtuelle Umgebungen in Aktion zu sehen, stellen Sie sicher, dass Sie jede virtuelle Umgebung, die Sie zuvor aktiviert haben könnten, deaktivieren:

``` bash
deactivate
```

Von nun an wird Poetry sich um die Erstellung und Verwaltung von virtuellen Umgebungen in Ihren Projekten kümmern, wenn Sie einige seiner Befehle ausführen.

Wenn Sie eine bessere Kontrolle über die Erstellung einer virtuellen Umgebung haben möchten, können Sie Poetry explizit mitteilen, welche Python-Version Sie von Anfang an verwenden möchten:

``` bash
poetry env use python3
```

Mit diesem Befehl geben Sie den Pfad zu einem gewünschten Python-Interpreter auf Ihrer Festplatte an. Die Verwendung von blossem `python3` funktioniert, solange Sie die entsprechende [Python ausführbare Datei in Ihrem `PATH`] haben. Sie können auch die **kleinere Python-Version** wie 3.12 oder einfach 3 verwenden.

> **Hinweis**
>
> Der Python-Interpreter, den Sie in Poetry angeben, muss die Versionsbeschränkung in Ihrer `pyproject.toml` Datei erfüllen. Andernfalls wird Poetry ihn mit einer Fehlermeldung ablehnen.
>
> Wenn die Versionsbeschränkung locker genug ist, können Ihre Endbenutzer eine andere Version von Python ausführen als die, mit der Sie Ihren Code ursprünglich getestet haben. Das könnte Kompatibilitätsprobleme einführen, insbesondere wenn externe Pakete auf bestimmte Python-Versionen angewiesen sind.

Wenn Poetry eine neue virtuelle Umgebung erstellt, zum Beispiel nachdem Sie zum ersten Mal den Befehl `poetry env use <python>` ausgeführt haben, sehen Sie eine Nachricht, die dieser ähnlich ist:

``` bash
poetry env use python
Creating virtualenv project-VdoBT_vR-py3.12 in /Users/daniel/Library/Caches/pypoetry/virtualenvs
Using virtualenv: /Users/daniel/Library/Caches/pypoetry/virtualenvs/project-VdoBT_vR-py3.12
```

Wie Sie sehen können, hat Poetry einen **einzigartigen Namen** für die virtuelle Umgebung Ihres Projekts erstellt. Er enthält den Namen Ihres Pakets aus `pyproject.toml` und die entsprechende Python-Version. Die scheinbar zufällige Zeichenfolge in der Mitte, `Dod5cRxq`, ist ein [Base64-kodierter](https://en.wikipedia.org/wiki/Base64) Hash-Wert des Pfads, der zu Ihrem übergeordneten Projektverzeichnis führt. Es verbindet den Namen einer virtuellen Umgebung mit dem Speicherort Ihres Projekts auf der Festplatte.

Wenn Sie das Projekt in einen anderen Ordner verschieben, erkennt Poetry dies und erstellt bei Bedarf eine brandneue virtuelle Umgebung im Hintergrund. Dank der einzigartigen Zeichenfolge in der Mitte kann Poetry mehrere Projekte mit identischen Namen und derselben Python-Version verwalten, während alle virtuellen Umgebungen standardmäßig in einem Ordner gehalten werden.

Sofern Sie nichts anderes angeben, erstellt Poetry virtuelle Umgebungen im `virtualenvs/` Unterordner seines **Zwischenspeicherverzeichnisses**, welches spezifisch für das Betriebssystem ist.

| Betriebssystem | Pfad                                               |
|----------------|----------------------------------------------------|
| Windows        | `C:\Users\<username>\AppData\Local\pypoetry\Cache` |
| macOS          | `/Users/<username>/Library/Caches/pypoetry`        |
| Linux          | `/home/<username>/.cache/pypoetry`                 |

Wenn Sie das Standard-Cache-Verzeichnis ändern möchten, können Sie die [Konfiguration von Poetry](https://python-poetry.org/docs/configuration) bearbeiten. Dies kann nützlich sein, wenn Sie bereits [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) oder ein anderes Drittanbieter-Tool zur Verwaltung Ihrer virtuellen Umgebungen verwenden und Ihre Festplatte nicht überladen oder einige Cache-Standorte mischen möchten.

Um Ihre aktuelle Poetry-Konfiguration aufzudecken, die die `cache-dir` und `virtualenvs.path` Einstellungen enthält, führen Sie diesen Befehl aus:

``` bash
poetry config --list
```

Normalerweise müssen Sie diese Pfade nicht ändern. Wenn Sie mehr über die Interaktion mit den virtuellen Umgebungen von Poetry erfahren möchten, enthält die Poetry-Dokumentation ein Kapitel über das [Verwalten von Umgebungen](https://python-poetry.org/docs/managing-environments/).

Solange du dich in deinem Projektordner befindest, wird Poetry die damit verbundene virtuelle Umgebung nutzen. Wenn du jemals unsicher bist, kannst du überprüfen, ob die virtuelle Umgebung erstellt wurde, indem du den Befehl `poetry env list` erneut ausführst:

```bash
poetry env list
project-VdoBT_vR-py3.12 (Activated)
```

Poesie zeigt an, welches der virtuellen Umgebungen, die mit Ihrem Projekt verbunden sind, derzeit als **Standard** ausgewählt ist. Obwohl es *aktiviert* heißt, ist die entsprechende virtuelle Umgebung in Ihrer Shell im traditionellen Sinne tatsächlich nicht aktiviert. Stattdessen wird Poesie diese virtuelle Umgebung vorübergehend in einem [Unterprozess] aktivieren, wenn Sie einen der Poesie-Befehle ausführen.

> **Hinweis**
>
> Um zwischen bestehenden Umgebungen zu wechseln, können Sie erneut den Befehl `poetry env use <python>` ausführen. Um schnell alle mit Ihrem Projekt verbundenen Umgebungen zu entfernen, führen Sie den Befehl `poetry env remove --all` aus.

Mit dieser Fähigkeit in Ihrem Repertoire sind Sie bereit, einige Abhängigkeiten zu Ihrem Projekt hinzuzufügen und Poetry zum Strahlen zu bringen.

### Laufzeitabhängigkeiten deklarieren

Als Sie Ihr `my-poetry` Projekt mit Poetry erstellt haben, hat es die minimale `pyproject.toml` Datei mit der `[tool.poetry.dependencies]` Unter-Tabelle erstellt. Bisher enthält es nur eine Deklaration der Python-Interpreter-Version, aber hier können Sie auch die externen Python-Pakete angeben, die Ihr Projekt benötigt.

Das manuelle Bearbeiten dieser Datei kann jedoch mühsam werden und es installiert tatsächlich nichts in die virtuelle Umgebung des Projekts. Hier kommt wieder die CLI von Poetry ins Spiel.

Du hast vielleicht schon [`pip`] verwendet, um Pakete zu installieren, die nicht Teil der Python-Standardbibliothek sind. Wenn du `pip install` mit dem Paketnamen als Argument ausführst, sucht `pip` nach Paketen im Python Package Index (PyPI). Du kannst Poetry auf ähnliche Weise verwenden.

Das Ausführen des [`poetry add`](https://python-poetry.org/docs/cli#add) Befehls aktualisiert automatisch Ihre `pyproject.toml` Datei mit der neuen Abhängigkeit und installiert gleichzeitig das Paket. Tatsächlich können Sie sogar mehrere Pakete auf einmal angeben:

``` bash
poetry add requests beautifulsoup4
```

Dies wird die neuesten Versionen beider Abhängigkeiten auf PyPI finden, sie in der entsprechenden virtuellen Umgebung installieren und die folgenden zwei Deklarationen in Ihrer `pyproject.toml` Datei einfügen:

``` toml
[tool.poetry]
name = "project"
version = "0.1.0"
description = ""
authors = ["Daniel Senften <daniel.senften@talent-factory.ch>"]
readme = "README.md"
packages = [{include = "project", from = "src"}]

[tool.poetry.dependencies]
python = "^3.12"
requests = "^2.32.3"
beautifulsoup4 = "^4.12.3"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

Die Reihenfolge dieser Deklarationen spiegelt die Reihenfolge wider, in der Sie diese Pakete in der Befehlszeile angegeben haben.

Beachten Sie das [Caret-Symbol (`^`)](https://en.wikipedia.org/wiki/Caret) vor den Versionsangaben, das darauf hinweist, dass Poetry jede Version installieren darf, die mit der am weitesten links stehenden Nicht-Null-Ziffer der Versionszeichenkette übereinstimmt. Zum Beispiel, wenn die Requests-Bibliothek eine neue Version `2.99.99` herausbringt, dann wird Poetry sie als akzeptablen Kandidaten für Ihr Projekt betrachten. Version `3.0` wäre jedoch nicht erlaubt.

> **Hinweis**
>
> Die Idee dahinter folgt dem semantischen Versionierungsschema (`major.minor.patch`), bei dem kleinere und Patch-Updates keine rückwärtsinkompatiblen Änderungen einführen sollten. Dennoch ist dies nur eine Annahme, die Ihre Builds beschädigen könnte, und einige [bekannte Python-Entwickler](https://www.youtube.com/watch?v=Gr9o8MW_pb0) sind nicht einverstanden mit einer solchen Wahl von Standardwerten im Namen von Poetry.

Wenn Sie eine bestimmte Version eines externen Pakets hinzufügen oder benutzerdefinierte [Versionsbeschränkungen](https://python-poetry.org/docs/dependency-specification/#version-constraints) definieren möchten, dann lässt Sie Poetry das auf der Kommandozeile tun:

``` bash
poetry add requests==2.25.1 "beautifulsoup4<4.10"
```

Wenn Sie diesen Befehl ausführen, wird Poetry zunächst alle zuvor installierten Versionen dieser Pakete entfernen und deren indirekte oder [transitive Abhängigkeiten](https://de.wikipedia.org/wiki/Transitive_Abh%C3%A4ngigkeit) nach Bedarf herabstufen. Anschließend ermittelt es die am besten geeigneten Versionen dieser Pakete und berücksichtigt dabei andere bestehende Einschränkungen, um potenzielle Konflikte zu lösen.

> **Hinweis**
>
> Manchmal müssen Sie Ihre Paketnamen möglicherweise in Anführungszeichen setzen, wenn deren Versionsspezifikationen Symbole mit einer besonderen Bedeutung beinhalten. In diesem Fall verhindert das Zitieren des `beautifulsoup4` Pakets, dass die Shell das kleiner-als-Symbol (`<`) als [Umleitungs](https://de.wikipedia.org/wiki/Umleitung_(Informatik))operator interpretiert.

Wenn Sie eine oder mehrere Abhängigkeiten von Ihrem Projekt entfernen möchten, dann stellt Poetry den entsprechenden [`poetry remove`](https://python-poetry.org/docs/cli#remove) Befehl zur Verfügung:

``` bash
poetry remove requests
Updating dependencies
Resolving dependencies... (0.1s)

Package operations: 0 installs, 0 updates, 5 removals

  - Removing certifi (2024.8.30)
  - Removing charset-normalizer (3.4.0)
  - Removing idna (3.10)
  - Removing requests (2.32.3)
  - Removing urllib3 (2.2.3)

Writing lock file
```

Wie Sie sehen können, entfernt es die gegebene Abhängigkeit zusammen mit ihren transitiven Abhängigkeiten, sodass Sie sich keine Sorgen über **übrig gebliebene Pakete** machen müssen, die von Ihrem Projekt nicht mehr benötigt werden. Dies ist ein Vorteil von Poetry gegenüber dem einfachen `pip`, das nur die einzelnen Pakete deinstallieren kann.

Beachten Sie, dass Poetry Sie immer informiert, wenn Sie eine Abhängigkeit hinzufügen oder entfernen, *in die Sperrdatei schreibt*. Sie werden später mehr über diese Datei erfahren, aber im Kern können Sie sie als eine Momentaufnahme der Abhängigkeiten Ihres Projekts zu einem bestimmten Zeitpunkt betrachten. Sie erfüllt den gleichen Zweck wie die von `pip` genutzte [Einschränkungsdatei](https://pip.pypa.io/en/stable/user_guide/#constraints-files).

Bisher haben Sie [Laufzeit](https://en.wikipedia.org/wiki/Execution_(computing)#Runtime) Abhängigkeiten hinzugefügt, die notwendig waren, um Ihr Programm korrekt zu betreiben. Es kann jedoch sein, dass Sie einige Abhängigkeiten nur in bestimmten Entwicklungsphasen benötigen, wie zum Beispiel während des Testens. Als nächstes sehen Sie, welche Werkzeuge Poetry Ihnen zur Verfügung stellt, um diese Art von Abhängigkeiten zu verwalten.

### Gruppenabhängigkeiten und zusätzliche Funktionen hinzufügen

Eine weitere praktische Funktion in Poetry, die in `pip` fehlt, ist die Möglichkeit, **Gruppen von Abhängigkeiten** zu verwalten, was es Ihnen ermöglicht, logisch zusammenhängende Abhängigkeiten von Ihren Laufzeitabhängigkeiten zu trennen. Zum Beispiel möchten Sie während der Entwicklung oft zusätzliche Pakete, wie [Linters], [Type Checkers](https://realpython.com/python-type-checking/) oder [Testing Frameworks], die das endgültige Verteilungspaket nur aufblähen würden. Ihre Benutzer benötigen diese schließlich nicht.

Mit Poetry können Sie Abhängigkeiten unter beliebigen Namen gruppieren, damit Sie diese Gruppen später bei Bedarf selektiv installieren können. Hier ist, wie man einige Abhängigkeiten zu einer Gruppe namens `dev` hinzufügt und einige Abhängigkeiten zu einer anderen Gruppe namens `test`:

``` bash
poetry add --group dev black flake8 isort mypy pylint
poetry add --group test pytest faker
```

Das Ausführen dieser Befehle führt dazu, dass Poetry die aufgelisteten Pakete in die virtuelle Umgebung des Projekts installiert und zusätzlich zwei weitere Untertabellen in Ihrer `pyproject.toml` Datei hinzufügt, die folgendermaßen aussehen:

``` toml
[tool.poetry]
name = "project"
version = "0.1.0"
description = ""
authors = ["Daniel Senften <daniel.senften@talent-factory.ch>"]
readme = "README.md"
packages = [{include = "project", from = "src"}]

[tool.poetry.dependencies]
python = "^3.12"
beautifulsoup4 = "^4.12.3"

[tool.poetry.group.dev.dependencies]
black = "^24.10.0"
flake8 = "^7.1.1"
isort = "^5.13.2"
mypy = "^1.13.0"
pylint = "^3.3.1"

[tool.poetry.group.test.dependencies]
pytest = "^8.3.3"
faker = "^30.8.1"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

Die neuen Untertabellen beginnen mit dem Namen `tool.poetry.group` und enden mit dem Wort `dependencies`. Der Teil in der Mitte muss ein einzigartiger Gruppenname sein.

Normalerweise, wenn Sie keinen Gruppennamen angeben, platziert Poetry die angegebenen Pakete in einer impliziten **Hauptgruppe**, die der `[tool.poetry.dependencies]` Unter-Tabelle entspricht. Daher können Sie den Namen `main` nicht für eine Ihrer Gruppen verwenden, da er reserviert ist.

> **Hinweis**
>
> Vor Poetry 1.2.0 konnten Sie die Option `-D` oder `--dev` als Abkürzung zum Hinzufügen von Abhängigkeiten zu einer Entwicklungsgruppe verwenden. Diese Option wurde jedoch als veraltet eingestuft, da sie mit regulären Abhängigkeitsgruppen unvereinbar wurde. Die veraltete Funktion diente dazu, eine separate Untergruppe in der `pyproject.toml` Datei zu erstellen.

Sie können [optionale Gruppen](https://python-poetry.org/docs/managing-dependencies/#optional-groups) definieren, indem Sie das entsprechende Attribut in der `pyproject.toml`-Datei festlegen. Zum Beispiel wird diese Deklaration Ihre `test`-Gruppe zu einer optionalen machen:

``` toml
...
[tool.poetry.group.test]
optional = true

...
```

Poesie wird Abhängigkeiten, die zu einer solchen Gruppe gehören, nicht installieren, es sei denn, Sie weisen sie ausdrücklich dazu an, indem Sie die Option [`--with`](https://python-poetry.org/docs/cli/#options-2) verwenden. Beachten Sie, dass Sie eine weitere TOML-Untertabelle deklarieren müssen, um eine Gruppe als optional zu kennzeichnen, da die Konfiguration der Gruppe getrennt von ihrer Abhängigkeitsliste aufbewahrt wird.

Zusätzlich dazu können Sie die einzelnen **Pakete als optional** hinzufügen, um dem Benutzer die Wahl zu lassen, ob er sie installieren möchte.

``` bash
poetry add --optional mysqlclient psycopg2-binary
```

Optionale Abhängigkeiten sollen zur Laufzeit verfügbar sein, wenn sie vom Benutzer während der Installation ausdrücklich angefordert werden. Es ist üblich, Pakete als optional zu kennzeichnen, wenn sie plattformspezifisch sind oder wenn sie Funktionen wie einen bestimmten Datenbankadapter bereitstellen, den nur einige Benutzer benötigen werden.

In `pyproject.toml` sehen optionale Abhängigkeiten etwas ausführlicher aus:

``` toml
...
[tool.poetry.dependencies]
python = "^3.12"
beautifulsoup4 = "^4.12.3"
mysqlclient = {version = "^2.2.5", optional = true}
psycopg2-binary = {version = "^2.9.10", optional = true}

...
```

Die `mysqlclient` und `psycopg2-binary` Abhängigkeiten haben ihre `optional` Flag auf `true` gesetzt, während ihre Versionszeichenkette in einem anderen Attribut aufbewahrt wird.

Jedoch reicht dies nicht aus, um solche optionalen Abhängigkeiten dem Benutzer offenzulegen. Sie müssen auch [extras](https://python-poetry.org/docs/pyproject/#extras) in Ihrer `pyproject.toml` Datei definieren, welche Sätze von optionalen Abhängigkeiten sind, die Ihre Benutzer gemeinsam installieren können.

``` toml
...

[tool.poetry.extras]
databases = ["mysqlclient", "psycopg2-binary"]
mysql = ["mysqlclient"]
pgsql = ["psycopg2-binary"]

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

Abhängig von Ihren speziellen Bedürfnissen können Sie sich für die gewünschten Funktionen entscheiden, indem Sie während der Installation eine oder mehrere Extras auswählen. Wie Sie sehen können, ist es auch möglich, einige Extras zu kombinieren, die auf einen bestimmten Anwendungsfall zugeschnitten sein könnten, wie zum Beispiel Tests.

Du hast gerade erst die Oberfläche gekratzt, wenn es um die Abhängigkeitsverwaltung mit Poetry geht. Es gibt noch so viel mehr zu entdecken! Das heißt aber, du bist bereits gut ausgerüstet, um Poetry in deinen Projekten umzusetzen. Im nächsten Abschnitt lernst du, wie du aus der Perspektive eines Benutzers mit einem Poetry-Projekt arbeiten kannst.

### Installieren unseres Pakets mit Poetry

Stellen Sie sich vor, Sie haben gerade ein [Git] Repository mit dem `my-poetry` Projekt von [GitHub](https://github.com/) geklont und starten neu ohne virtuelle Umgebung. Um das zu simulieren, können Sie einige Metadaten von Poetry und alle mit dem Projekt verbundenen virtuellen Umgebungen entfernen:

``` bash
rm poetry.lock
poetry env remove --all
```

Wenn Sie ein Entwickler sind, der zu diesem Projekt beitragen möchte, können Sie den Befehl [`poetry install`](https://python-poetry.org/docs/cli#install) im Ordner my-poetry/\` ausführen, um den Ball ins Rollen zu bringen:

``` bash
poetry install
```

Wenn andere Mitwirkende die `poetry.lock`-Datei in das entfernte Repository [übertragen haben](https://python-poetry.org/docs/basic-usage/#committing-your-poetrylock-file-to-version-control), was sie im Allgemeinen tun sollten, dann wird Poetry diese Datei lesen. Es wird die **genau gleiche Umgebung** auf Ihrem Computer mit identischen Versionen aller in der neuesten Momentaufnahme von `poetry.lock` aufgeführten Abhängigkeiten reproduzieren.

Andernfalls wird Poetry auf das Lesen der **top-level Abhängigkeiten** zurückgreifen, die in der `pyproject.toml` Datei skizziert sind und wird den Satz von Paketen lösen, die die Versionsbeschränkungen erfüllen. Als Ergebnis haben Sie eine neue lokale `poetry.lock` Datei. Dies könnte potenziell zu einem anderen Zustand von Abhängigkeiten in Ihrer virtuellen Umgebung führen als die von anderen Mitwirkenden, die das Projekt zu einem anderen Zeitpunkt installiert haben.

Die **Abhängigkeitsauflösung** wird unerlässlich, wenn Sie viele Abhängigkeiten haben, die mehrere Drittanbieterpakete mit verschiedenen eigenen Versionen erfordern. Bevor irgendwelche Pakete installiert werden, findet Poetry heraus, welche Version eines Pakets die Versionsbeschränkungen erfüllt, die andere Pakete als ihre Anforderungen festlegen. Das ist keine triviale Aufgabe. In seltenen Fällen existiert möglicherweise nicht einmal eine Lösung!

Standardmässig installiert Poetry Abhängigkeiten aus der impliziten **Hauptgruppe** sowie allen **Abhängigkeitsgruppen**, es sei denn, Sie haben sie als optional markiert. Es installiert auch Ihr eigenes `rp-poetry` Distributionspaket im [editierbaren Modus](https://setuptools.pypa.io/en/latest/userguide/development_mode.html), um Änderungen in Ihrem Quellcode sofort in der Umgebung widerzuspiegeln, ohne dass eine Neuinstallation erforderlich ist.

Im Gegensatz dazu wird Poetry **zusätzliche Abhängigkeitssets** und **optionale Abhängigkeitsgruppen** nicht automatisch installieren. Um diese zu erhalten, müssen Sie einige der folgenden Parameter verwenden:

- `--all-extras`
- `--extras {extra}`
- `--mit {optionale Gruppen}`

Sie können gleichzeitig einige Extras installieren, indem Sie den Parameter `--extras` für jede gewünschte Gruppe optionaler Abhängigkeiten wiederholen. Allerdings behandelt Poetry die einzelnen Extras als [gegenseitig ausschliessend](https://de.wikipedia.org/wiki/Disjunkte_Mengen), bis Sie etwas anderes angeben. Daher wird es nur die auf der Befehlszeile angegebenen installieren und alle anderen Extras aus Ihrer virtuellen Umgebung entfernen, falls erforderlich. Insbesondere wird es alle Extras entfernen, wenn Sie nicht mindestens eines während der Installation auswählen.

Abgesehen davon haben Sie noch ein paar weitere Optionen, die es Ihnen ermöglichen, genau auszuwählen, welche Abhängigkeiten Sie installieren möchten, einschließlich:

| Option               | Bedeutung                                              |
|----------------------|--------------------------------------------------------|
| `--no-root`          | Installieren Sie Abhängigkeiten ohne das Paket selbst. |
| `--only-root`        | Installieren Sie Ihr Paket ohne seine Abhängigkeiten.  |
| `--only {groups}`    | Installieren Sie nur diese Abhängigkeitsgruppen.       |
| `--without {groups}` | Installieren Sie diese Abhängigkeitsgruppen nicht.     |

Wenn Sie die Option `--only {groups}` angeben, ignoriert Poetry die Optionen `--with {optional groups}` und `--without {groups}`.

Das Auflösen von Abhängigkeiten führt dazu, dass eine neue `poetry.lock` Datei aktualisiert oder erstellt wird. Hier behält Poetry den Überblick über alle Pakete und ihre genauen Versionen, die Ihr Projekt verwendet. Sie werden sich diese Datei jetzt genauer ansehen.

## Abhängigkeiten mit Poetry verwalten

Immer wenn Sie mit Poetry über seine Befehlszeilenschnittstelle interagieren, aktualisiert es die `pyproject.toml` Datei und fixiert die gelösten Versionen in der `poetry.lock` Datei. Sie müssen jedoch nicht zulassen, dass Poetry die ganze Arbeit erledigt. Sie können Abhängigkeiten in der `pyproject.toml` Datei manuell ändern und sie danach sperren.

### Manuelles Sperren von Abhängigkeiten

Poetry generiert und aktualisiert die `poetry.lock` Datei bei Bedarf, solange Sie sich an ihre Befehlszeilenschnittstelle halten. Obwohl die Sperrdatei *nicht* von Hand geändert werden soll, können Sie die zugehörige `pyproject.toml` Datei nach Belieben bearbeiten. Leider kann dies manchmal dazu führen, dass beide Dateien nicht mehr synchron sind.

> **Hinweis**
>
> Wenn Sie darauf bestehen, manuell in die `poetry.lock` Datei einzugreifen, werden Sie wahrscheinlich die zugrunde liegenden Hashes ungültig machen, was die Datei kaputt und unbrauchbar macht.

Angenommen, Sie möchten die Requests-Bibliothek, die Sie zuvor in diesem Tutorial aus dem `my-poetry` Projekt entfernt haben, zurückbringen. Sie können die `pyproject.toml` Datei in Ihrem Texteditor öffnen und die notwendige Deklaration in der Hauptgruppe der Abhängigkeiten eingeben.

``` toml
...

[tool.poetry.dependencies]
requests = "*"              # <- Neue Abhängigkeit eingefügt
python = "^3.12"
...
```

Indem Sie das Sternchen (`*`) als Versionsbeschränkung verwenden, zeigen Sie an, dass Sie keine bestimmte Version der Requests-Bibliothek angeben und jede Version akzeptabel ist. Aber diese Bibliothek ist noch nicht installiert.

Wenn Sie nun Ihr Terminal öffnen und zum übergeordneten Verzeichnis des Projekts navigieren, können Sie Poetry anweisen, die manuell hinzugefügten Abhängigkeiten in die zugehörige virtuelle Umgebung zu installieren und die Sperrdatei zu aktualisieren:

``` bash
poetry install
Installing dependencies from lock file

pyproject.toml changed significantly since poetry.lock was last generated. Run `poetry lock [--no-update]` to fix the lock file.
```

In diesem Fall weigert sich Poetry, die Abhängigkeiten zu installieren, weil Ihre `poetry.lock` Datei momentan die Requests-Bibliothek, die in der begleitenden `pyproject.toml` Datei vorhanden ist, nicht erwähnt. Umgekehrt, wenn Sie eine Deklaration einer aufgelösten und installierten Abhängigkeit aus `pyproject.toml` entfernen, würden Sie auf eine ähnliche Beschwerde stoßen. Warum passiert das?

Denken Sie daran, dass Poetry immer die **aufgelösten Abhängigkeiten** aus der `poetry.lock`-Datei installiert, in der es die genauen Paketversionen festgelegt hat. Es berücksichtigt nur die Abhängigkeiten, die Sie in der `pyproject.toml`-Datei aufgelistet haben, wenn es eine fehlende Lock-Datei aktualisieren oder neu generieren muss.

Daher könnten Sie, um eine solche Diskrepanz zu beheben, die Sperrdatei löschen und `poetry install` erneut ausführen, um Poetry alle Abhängigkeiten von Grund auf neu lösen zu lassen. Das ist jedoch nicht der beste Ansatz. Es ist potenziell zeitaufwendig. Aber noch schlimmer ist, dass es die spezifischen Versionen der zuvor gelösten Abhängigkeiten ignoriert und die Garantie für reproduzierbare Builds entfernt.

Ein weit besserer Ansatz, um die beiden Dateien auszurichten, besteht darin, die neuen Abhängigkeiten mit dem Befehl [`poetry lock`](https://python-poetry.org/docs/cli/#lock) **manuell zu sperren**:

``` bash
poetry lock
Updating dependencies
Resolving dependencies... (1.6s)

Writing lock file
```

Dies wird Ihre `poetry.lock` Datei aktualisieren, um der aktuellen `pyproject.toml` Datei zu entsprechen, ohne irgendwelche Abhängigkeiten zu installieren.

Poesie verarbeitet alle Abhängigkeiten in Ihrer `pyproject.toml` Datei, findet Pakete, die die deklarierten Einschränkungen erfüllen, und fixiert ihre genauen Versionen in der Sperrdatei. Aber Poesie hört nicht dort auf. Wenn Sie `poetry lock` ausführen, durchläuft und sperrt es auch rekursiv alle Abhängigkeiten Ihrer direkten Abhängigkeiten.

> **Hinweis**
>
> Der Befehl `poetry lock` aktualisiert auch Ihre bestehenden Abhängigkeiten, wenn neuere Versionen verfügbar sind, die immer noch zu Ihren Versionsbeschränkungen passen. Wenn Sie keine Abhängigkeiten aktualisieren möchten, die bereits in der `poetry.lock` Datei vorhanden sind, fügen Sie die Option `--no-update` zum poetry lock Befehl hinzu:
>
> ``` bash
> poetry lock --no-update
> Resolving dependencies... (0.1s)
> ```
>
> In diesem Fall löst Poetry nur die neuen Abhängigkeiten auf, lässt jedoch bestehende Abhängigkeitsversionen in der `poetry.lock` Datei unberührt.

Es ist wichtig zu beachten, dass die Abhängigkeitssperre nur um zwei Dinge geht:

1.  *Resolving*: Finden von Paketen, die alle Versionsbeschränkungen erfüllen
2.  *Pinning*: Erstellen einer Momentaufnahme der gelösten Versionen in der `poetry.lock` Datei

### Synchronisieren der Umgebung

Wenn die `poetry.lock` Datei mit ihrer `pyproject.toml` übereinstimmt, können Sie alle Abhängigkeiten installieren, die Poetry für Sie gesperrt hat:

``` bash
poetry install
Installing dependencies from lock file

No dependencies to install or update

Installing the current project: project (0.1.0)
```

Was ist, wenn Ihre virtuelle Umgebung **überflüssige Pakete** enthält, die Sie zuvor installiert haben, aber nicht mehr benötigen? Poetry stört sich nicht an solchen Paketen, auch wenn sie nicht formell in `pyproject.toml` oder `poetry.lock` deklariert sind. Sie könnten sie vor einiger Zeit als optionale Abhängigkeitsgruppen installiert haben oder völlig ausserhalb der Kontrolle von Poetry, zum Beispiel durch direkte Verwendung von `pip`.

``` bash
poetry run python -m pip install httpie
```

Das [`httpie`](https://pypi.org/project/httpie/) Paket bringt indirekt zehn zusätzliche Abhängigkeiten mit sich, die Platz beanspruchen und potenziell mit den eigentlichen Abhängigkeiten Ihres Projekts interferieren könnten. Darüber hinaus könnten externe Pakete manchmal Sicherheitslücken erzeugen, wenn Sie sie nicht auf dem neuesten Stand halten.

Um Ihre **virtuelle Umgebung** mit den in `poetry.lock` fixierten Paketen zu synchronisieren, können Sie den optionalen `--sync` Flag zum `poetry install` Befehl hinzufügen:

``` bash
poetry install --sync
Installing dependencies from lock file

Package operations: 0 installs, 1 update, 10 removals

  - Removing defusedxml (0.7.1)
  - Removing httpie (3.2.3)
  - Removing markdown-it-py (3.0.0)
  - Removing mdurl (0.1.2)
  - Removing multidict (6.1.0)
  - Removing pygments (2.18.0)
  - Removing pysocks (1.7.1)
  - Removing requests-toolbelt (1.0.0)
  - Removing rich (13.9.3)
  - Removing setuptools (75.3.0)
  - Updating requests (2.31.0 -> 2.32.3)

Installing the current project: project (0.1.0)
```

Dies stellt sicher, dass Ihre virtuelle Umgebung nur die in Ihren `pyproject.toml` und `poetry.lock` Dateien angegebenen Pakete enthält und verhindert potenzielle Konflikte, die durch unnötige oder veraltete Abhängigkeiten verursacht werden könnten.

### Aktualisieren von Abhängigkeiten

Nehmen wir an, Sie haben im Dezember 2020 die Requests-Bibliothek zu Ihrem Projekt hinzugefügt, als die neueste Version dieser Bibliothek die [2.25.1 Veröffentlichung](https://pypi.org/project/requests/2.25.1/) war. Standardmässig hat Poetry in Ihrer `pyproject.toml` Datei eine **permissive Versionsbeschränkung** konfiguriert, die ein Caret (`^2.25.1`) beinhaltet, um zukünftige nicht-zerstörende Updates zu ermöglichen.

Im Laufe der Jahre haben Sie Ihrem Projekt mit `poetry add` viele weitere Abhängigkeiten hinzugefügt, und Poetry hat automatisch neuere Releases von Requests aufgenommen, die immer noch die ursprüngliche Versionsbeschränkung erfüllten. Poetry hat dann die Lock-Datei entsprechend aktualisiert und neue Versionen von Abhängigkeiten in Ihre virtuelle Umgebung installiert. Jetzt haben Sie die [2.29.0 Version](https://pypi.org/project/requests/2.29.0/) von Requests in der `poetry.lock` Datei festgelegt und in Ihrer Umgebung installiert.

Springen Sie vorwärts zur Zeit der Abfassung, als die Bibliotheksversion [2.31.0](https://pypi.org/project/requests/2.31.0/) eine Spitzenversion geworden ist. Um dies zu überprüfen, können Sie Poetry bitten, Ihre gesperrten Abhängigkeiten mit ihren **neuesten Veröffentlichungen auf PyPI** zu vergleichen, indem Sie diesen Befehl ausführen:

``` bash
poetry show --latest --top-level
beautifulsoup4     4.12.3      4.12.3      Screen-scraping library
black              24.10.0     24.10.0     The uncompromising code formatter
...
pytest             8.3.3       8.3.3       pytest: simple powerful testing with Python
requests           2.32.3      2.32.3      Python HTTP-for-Humans
...
```

Diese neue Version erfüllt weiterhin Ihre Versionsbeschränkung für Anfragen, daher sollte Poetry sie akzeptieren. Wenn Sie jedoch versuchen, `poetry install` erneut auszuführen, passiert nichts:

``` bash
poetry install
Installing dependencies from lock file

No dependencies to install or update

Installing the current project: project (0.1.0)
```

Denken Sie daran, dass der Befehl `poetry install` die `poetry.lock` Datei gegenüber Ihren in `pyproject.toml` deklarierten Versionseinschränkungen priorisiert, um reproduzierbare Umgebungen zu gewährleisten. Wenn Sie Abhängigkeiten mit kompatiblen Versionen aktualisieren möchten, haben Sie folgende Möglichkeiten:

- Entfernen Sie `poetry.lock` und führen Sie `poetry install` aus
- Führen Sie `poetry lock` gefolgt von `poetry install` aus
- Führen Sie `poetry update` aus

Wie bereits erwähnt, hat die erste Option ihre Nachteile, da sie Poetry dazu zwingt, alle Abhängigkeiten von Grund auf neu zu berechnen. Die beiden anderen Optionen sind im Grunde gleichwertig, daher könnten Sie die letztere wählen, um beide Schritte auf einmal zu erledigen.

Das Aktualisieren von Abhängigkeiten birgt immer ein gewisses Risiko. Um besser zu verstehen, was gleich passieren wird, können Sie Poetry bitten, einen **Probelauf** durchzuführen, bevor Sie den Sprung wagen:

``` bash
poetry update --dry-run
Updating dependencies
Resolving dependencies... (0.4s)

Package operations: 0 installs, 0 updates, 0 removals, 32 skipped

  - Installing astroid (3.3.5): Skipped for the following reason: Already installed
  - Installing black (24.10.0): Skipped for the following reason: Already installed
  - Installing beautifulsoup4 (4.12.3): Skipped for the following reason: Already installed

...
```

Normalerweise müssen Sie, um eine **Abhängigkeit auf eine Version zu aktualisieren**, die ausserhalb der in Ihrer `pyproject.toml`-Datei deklarierten Versionsbeschränkungen liegt, diese Datei vorher anpassen. Alternativ können Sie eine Abhängigkeit mit dem Befehl `poetry add` und dem [at Operator (`@`)](https://python-poetry.org/docs/dependency-specification/#using-the--operator) sowie einem speziellen Schlüsselwort, `latest`, auf die **neueste Version** erzwingen.

``` bash
poetry add requests@latest
```

Wenn Sie den Befehl `poetry add` mit dem Schlüsselwort `latest` ausführen, wird Poetry Ihre aktuelle Versionseinschränkung in `pyproject.toml` ignorieren und sie durch eine neue Einschränkung ersetzen, die auf der neuesten gefundenen Version basiert. Es ist, als ob Sie diese Abhängigkeit noch nie zuvor zu Ihrem Projekt hinzugefügt hätten. Verwenden Sie diese Option mit Vorsicht, da eine inkompatible Version einer Ihrer Abhängigkeiten das Projekt beschädigen könnte.

Wenn Sie jetzt Ihre `pyproject.toml` Datei öffnen, wird die Versionseinschränkung für die Requests-Bibliothek wie folgt aussehen:

``` toml
[tool.poetry]
name = "project"
version = "0.1.0"
description = ""
authors = ["Daniel Senften <daniel.senften@talent-factory.ch>"]
readme = "README.md"
packages = [{include = "project", from = "src"}]

[tool.poetry.dependencies]
requests = "^2.32.3"               # <- Die Version wurde aktualisiert
python = "^3.12"
...
```

Ohne das `latest` Schlüsselwort oder eine explizite Versionsbeschränkung im `poetry add` Befehl zu verwenden, würde Poetry schlussfolgern, dass das angeforderte Paket bereits in Ihrem Projekt vorhanden ist und nichts tun.

Nun haben Sie verstanden, wie Poetry `pyproject.toml` und `poetry.lock` verwendet. Als nächstes werfen Sie einen letzten Blick auf beide Dateien.

### Vergleich von pyproject.toml und poetry.lock

Die Versionsbeschränkungen der in Ihrer `pyproject.toml`-Datei deklarierten Abhängigkeiten können ziemlich locker sein. Dies ermöglicht eine gewisse Flexibilität bei der Einbeziehung von **Fehlerbehebungen** oder der Lösung von **Versionskonflikten**. Indem mehr Paketversionen zur Auswahl stehen, ist Poetry eher in der Lage, eine Kombination von kompatiblen Abhängigkeiten zu finden.

Andererseits verfolgt Poetry die genauen Versionen der Abhängigkeiten, die Sie tatsächlich in der `poetry.lock` Datei verwenden. Dies verbessert die **Leistung** von Poetry, indem die aufgelösten Paketversionen zwischengespeichert werden, sodass sie nicht jedes Mal erneut aufgelöst werden müssen, wenn Sie Ihre Abhängigkeiten installieren oder aktualisieren.

Um **reproduzierbare Umgebungen** in Ihrem Team zu gewährleisten, sollten Sie in Betracht ziehen, die `poetry.lock` Datei in Ihr [Versionskontrollsystem](https://de.wikipedia.org/wiki/Versionsverwaltung) wie Git zu übernehmen. Indem Sie diese Datei in einem Versionskontrollsystem verfolgen, stellen Sie sicher, dass alle Entwickler identische Versionen der erforderlichen Pakete verwenden. Es gibt jedoch eine bemerkenswerte Ausnahme.

Wenn Sie eine [Bibliothek entwickeln](https://python-poetry.org/docs/basic-usage/#as-a-library-developer) anstatt einer Anwendung, ist es üblich, die `poetry.lock` Datei *nicht* zu committen. Bibliotheken müssen in der Regel mit mehreren Versionen ihrer Abhängigkeiten kompatibel bleiben, anstatt mit einem einzigen, festgelegten Set.

Wenn Sie auf ein Repository stoßen, das eine `poetry.lock` Datei enthält, ist es eine gute Idee, Poetry zur Verwaltung seiner Abhängigkeiten zu verwenden. Andererseits, wenn andere Entwickler in Ihrem Team Poetry noch nicht verwenden, sollten Sie sich mit ihnen über die mögliche Einführung von Poetry im gesamten Team abstimmen, bevor Sie Entscheidungen treffen. Sie müssen immer die Kompatibilität mit anderen Abhängigkeitsverwaltungstools aufrechterhalten, die das Team verwenden könnte.

## Poetry in einem bestehenden Projekt verwenden

Es ist wahrscheinlich, dass Sie bereits einige Projekte haben, die nicht mit dem Befehl `poetry new` gestartet wurden. Oder vielleicht haben Sie ein Projekt geerbt, das nicht mit Poetry erstellt wurde, aber jetzt möchten Sie Poetry für Ihr Abhängigkeitsmanagement verwenden. In solchen Situationen können Sie Poetry zu bestehenden Python-Projekten hinzufügen.

### Einen Ordner in ein Poetry-Projekt umwandeln

Angenommen, Sie haben einen `my-hello` Ordner mit einem `hello.py` Skript darin:

Es ist das klassische [`Hello, World!` Programm](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program), welches den berühmten String auf dem Bildschirm ausgibt. Aber vielleicht ist dies nur der Anfang eines grossen Projekts, also entscheiden Sie sich, Poetry hinzuzufügen. Anstatt den `poetry new` Befehl von vorher zu verwenden, verwenden Sie den [`poetry init`](https://python-poetry.org/docs/cli/#init) Befehl in Ihrem Projektordner:

``` bash
cd my-hallo
poetry init
```

Dieser Befehl führt Sie durch die Erstellung Ihrer pyproject.toml Konfiguration.

``` bash
poetry init

This command will guide you through creating your pyproject.toml config.

Package name [my-hello]:
Version [0.1.0]:
Description []:  Mein erstes Programm
Author [Daniel Senften <daniel.senften@talent-factory.ch>, n to skip]:
License []:  MIT
Compatible Python versions [^3.13]:

Would you like to define your main dependencies interactively? (yes/no) [yes] no
Would you like to define your development dependencies interactively? (yes/no) [yes] no

(...)
```

Der Befehl `poetry init` sammelt die notwendigen Informationen, um eine `pyproject.toml` Datei zu generieren, indem er Ihnen interaktiv Fragen stellt. Er gibt Ihnen Empfehlungen mit sinnvollen Standardwerten für die meisten Konfigurationen, die Sie einrichten müssen, und Sie können Enter drücken, um sie zu akzeptieren. Wenn Sie keine Abhängigkeiten deklarieren, sieht die `pyproject.toml` Datei, die Poetry erstellt, ungefähr so aus:

``` toml
[tool.poetry]
name = "my-hello"
version = "0.1.0"
description = "Mein erstes Programm"
authors = ["Daniel Senften <daniel.senften@talent-factory.ch>"]
license = "MIT"
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.13"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

Dieser Inhalt ähnelt den Beispielen, die Sie in den vorherigen Abschnitten durchgegangen sind.

Nun können Sie alle Befehle verwenden, die Poetry bietet. Mit einer vorhandenen `pyproject.toml` Datei können Sie nun Ihr Skript aus einer isolierten virtuellen Umgebung ausführen.

``` bash
poetry run python hello.py
Creating virtualenv my-hello-qs2Rris8-py3.13 in /Users/daniel/Library/Caches/pypoetry/virtualenvs
Hello, World
```

Da Poetry keine virtuellen Umgebungen zum Verwenden gefunden hat, hat es eine neue erstellt, bevor es Ihr Skript ausgeführt hat. Nachdem dies geschehen ist, zeigt es Ihre `Hello, World` Nachricht ohne Fehler an. Das bedeutet, dass Sie nun ein funktionierendes Poetry-Projekt haben.

### Abhängigkeiten in Poetry importieren

Manchmal hast du ein Projekt, das bereits mit seiner eigenen [Anforderungsdatei] kommt, die alle externen Abhängigkeiten auflistet. Schau dir die `requirements.txt` Datei dieses [Python Web Scraper] Projekts an:

``` txt
beautifulsoup4==4.9.3
certifi==2020.12.5
chardet==4.0.0
idna==2.10
requests==2.25.1
soupsieve==2.2.1
urllib3==1.26.4
```

Dieses Projekt erfordert sieben Drittanbieter-Pakete, um ordnungsgemäss zu funktionieren. Zugegeben, nur die [Requests] und [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/) Bibliotheken werden direkt im Quellcode referenziert, während der Rest als ihre transitive Abhängigkeiten eingezogen wird.

Poetry kommt standardmässig nicht mit solchen Anforderungsdateien zurecht, da sie die Abhängigkeiten Ihres Projekts anderswo speichert. Sobald Sie jedoch ein Poetry-Projekt mit `poetry init` erstellt haben, können Sie schnell eine vorhandene `requirements.txt`-Datei in das Projekt importieren, indem Sie diesen Befehl verwenden:

``` bash
poetry add $(cat requirements.txt)

Updating dependencies
Resolving dependencies... (1.3s)

Package operations: 7 installs, 0 updates, 0 removals

  - Installing certifi (2020.12.5)
  - Installing chardet (4.0.0)
  - Installing idna (2.10)
  - Installing soupsieve (2.2.1)
  - Installing urllib3 (1.26.4)
  - Installing beautifulsoup4 (4.9.3)
  - Installing requests (2.25.1)

Writing lock file
```

Das [`cat`](https://en.wikipedia.org/wiki/Cat_(Unix)) Hilfsprogramm liest die angegebene Datei und schreibt ihren Inhalt in den Standardausgabestrom. In diesem Fall leiten Sie diesen Inhalt mit Hilfe der [Befehlssubstitutionssyntax](https://en.wikipedia.org/wiki/Command_substitution) der Shell an den `poetry add` Befehl weiter. Dies installiert wiederum jede in der `requirements.txt` Datei aufgeführte Abhängigkeit in Ihr Poetry-Projekt.

Wenn eine Anforderungsdatei so einfach ist wie diese, können `poetry add` und `cat` Ihnen einige manuelle Arbeiten ersparen. Dies ist jedoch nicht ideal, da alle Abhängigkeiten in Ihrer `pyproject.toml` Datei aufgelistet werden.

``` toml
[tool.poetry]
name = "my-hello"
version = "0.1.0"
description = "Mein erstes Programm"
authors = ["Daniel Senften <daniel.senften@talent-factory.ch>"]
license = "MIT"
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.13"
beautifulsoup4 = "4.9.3"  #
certifi = "2020.12.5"     #
chardet = "4.0.0"         #
idna = "2.10"             #
requests = "2.25.1"       #
soupsieve = "2.2.1"       #
urllib3 = "1.26.4"        #


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

Normalerweise möchten Sie nur die Pakete auflisten, von denen Ihr Projekt *direkt* abhängt. Abgesehen davon sollten Sie im Allgemeinen vermeiden, genaue Versionsnummern zu verwenden, da dies zu Konflikten mit bestehenden Paketen führen oder Sie daran hindern kann, die neuesten Funktionen und Sicherheitsupdates zu erhalten. Stattdessen sollten Sie einen Versionsbereich angeben, der eine gewisse Flexibilität zulässt, während Sie sich immer noch an die Prinzipien der semantischen Versionierung halten.

In einer perfekten Welt sollte Ihre `pyproject.toml` Datei nur diese zwei Abhängigkeiten mit etwas liberaleren Versionsspezifikationen enthalten:

``` toml
[tool.poetry.dependencies]
python = "^3.13"
beautifulsoup4 = "^4.9.3"
requests = "^2.25.1"

...
```

Poetry wird die verbleibenden Abhängigkeiten auflösen und sie in der entsprechenden `poetry.lock` Datei sperren.

Nun, wenn Sie [die Abhängigkeiten Ihres Projekts](https://python-poetry.org/docs/cli/#show) als Baum anzeigen, wissen Sie genau, welche davon direkt von Ihrem Projekt verwendet werden und welche deren transitive Abhängigkeiten sind.

``` bash
poetry show --tree

beautifulsoup4 4.12.3 Screen-scraping library
└── soupsieve >1.2
requests 2.32.3 Python HTTP for Humans.
├── certifi >=2017.4.17
├── charset-normalizer >=2,<4
├── idna >=2.5,<4
└── urllib3 >=1.21.1,<3
```

### Abhängigkeiten von Poetry exportieren

In einigen Situationen müssen Sie eine `requirements.txt` Datei haben. Zum Beispiel möchten Sie vielleicht Ihr Django-Projekt auf Heroku hosten, das die `requirements.txt` Datei erwartet, um zu bestimmen, welche Abhängigkeiten zu installieren sind. Poetry gibt Ihnen einige Optionen, um diese Datei zu erstellen.

Solange die virtuelle Umgebung Ihres Projekts auf dem neuesten Stand ist, können Sie Ihre Abhängigkeitsversionen mit dem traditionellen `pip freeze` Befehl festlegen:

``` bash
poetry run python -m pip freeze > requirements.txt
```

Um den Befehl im Kontext Ihrer von Poetry verwalteten virtuellen Projektumgebung auszuführen, müssen Sie `poetry run` verwenden. Alternativ könnten Sie die virtuelle Umgebung in einer [interaktiven Shell](https://python-poetry.org/docs/cli#shell) aktiviert und dann den gleichen Befehl von dort aus ausgeführt haben. So oder so, Sie müssen zuerst sicherstellen, dass alle erforderlichen Abhängigkeiten in ihren erwarteten Versionen installiert sind, zum Beispiel durch Ausgabe des Befehls `poetry install`.

Wenn Ihnen das zu umständlich erscheint, können Sie das [Export-Plugin von Poetry](https://pypi.org/project/poetry-plugin-export/) installieren, welches den veralteten [`poetry export`](https://python-poetry.org/docs/cli#export) Befehl ersetzt. Es ermöglicht Ihnen im Grunde, Abhängigkeiten von `poetry.lock` in verschiedene Dateiformate zu exportieren, einschließlich `requirements.txt`, welches das Standardformat ist.

Je nachdem, wie Sie Poetry selbst installiert haben, sind dies die Befehle, die Sie zur Installation des erwähnten Plugins auswählen können:

- `poetry self add poetry-plugin-export`
- `pipx inject poetry poetry-plugin-export`
- `python -m pip install poetry-plugin-export`

Sobald das Plugin installiert ist, können Sie den folgenden Befehl verwenden, um Abhängigkeiten von Ihrem von Poetry verwalteten Projekt in eine `requirements.txt` Datei zu exportieren:

``` bash
poetry export --output requirements.txt
```

Die resultierende Datei enthält standardmässig [Hashes](https://pip.pypa.io/en/stable/topics/secure-installs/#hash-checking-mode) und [Umgebungsmarker](https://www.python.org/dev/peps/pep-0508/#environment-markers), was bedeutet, dass Sie mit sehr strengen Anforderungen arbeiten können, die dem Inhalt Ihrer `poetry.lock` Datei ähneln. Tatsächlich benötigt das Export-Plugin die Lock-Datei, um die Anforderungsdatei zu generieren. Wenn diese Datei nicht existiert, erstellt Poetry sie nach dem Auflösen und Sperren Ihrer Abhängigkeiten.

Obwohl das Plugin die Sperrdatei betrachtet, um ein Gesamtbild der Abhängigkeiten Ihres Projekts zu erhalten, exportiert es nur Abhängigkeiten aus der impliziten **Hauptgruppe** in Ihrer `pyproject.toml`-Datei. Wenn Sie zusätzliche Abhängigkeiten aus **Abhängigkeitsgruppen** einschließen möchten, einschließlich der optionalen und nicht optionalen Gruppen, verwenden Sie dann den Parameter `--with`, gefolgt von kommagetrennten Namen dieser Gruppen:

``` bash
poetry export --output requirements.txt --with dev,test
```

Umgekehrt, um eine Anforderungsdatei mit Abhängigkeiten zu erstellen, die nur zu einigen Ihrer Abhängigkeitsgruppen gehören, während die implizite `main` Gruppe ausgeschlossen wird, verwenden Sie die `--only` Option:

``` bash
poetry export --output requirements-dev.txt --only development
```

In allen Fällen werden die **Extras** mit optionalen Abhängigkeiten nicht exportiert. Um sie ebenfalls einzuschließen, müssen Sie sie entweder explizit auflisten, indem Sie den Parameter `--extras` wiederholen, oder sie alle auf einmal mit der Flag `--all-extras` aktivieren.

Sie haben vielleicht bemerkt, dass das Export-Plugin einige Optionen mit dem Befehl `poetry install` teilt, den Sie zuvor gesehen haben. Das ist kein Zufall. Um die verfügbaren Optionen des Plugins und ihre Beschreibungen anzuzeigen, führen Sie `poetry export --help` in Ihrem Terminal aus.

## Befehlsreferenz

In diesem Tutorial haben Sie eine Einführung in das Abhängigkeitsmanagement von Poetry erhalten. Dabei haben Sie einige Befehle der Kommandozeilenschnittstelle (CLI) von Poetry verwendet:

| Poetry Befehl               | Erklärung                                                                                  |
|-----------------------------|--------------------------------------------------------------------------------------------|
| `$ poetry --version`        | Zeigen Sie die Version Ihrer Poetry-Installation an.                                       |
| `$ poetry new`              | Erstellen Sie ein neues Poetry-Projekt.                                                    |
| `$ poetry init`             | Fügen Sie Poetry zu einem bestehenden Projekt hinzu.                                       |
| `$ poetry run`              | Führen Sie einen Befehl in einer von Poetry verwalteten virtuellen Umgebung aus.           |
| `$ poetry add`              | Fügen Sie ein Paket zu `pyproject.toml` hinzu und installieren Sie es.                     |
| `$ poetry update`           | Aktualisieren Sie die Abhängigkeiten Ihres Projekts.                                       |
| `$ poetry install`          | Installieren Sie die Abhängigkeiten.                                                       |
| `$ poetry show`             | Liste der installierten Pakete.                                                            |
| `$ poetry lock`             | Fixieren Sie die neueste Version Ihrer Abhängigkeiten in `poetry.lock`.                    |
| `$ poetry lock --no-update` | Aktualisieren Sie die `poetry.lock` Datei ohne eine Abhängigkeitsversion zu aktualisieren. |
| `$ poetry check`            | Validieren Sie `pyproject.toml`.                                                           |
| `$ poetry config --list`    | Zeigen Sie die Poetry-Konfiguration an.                                                    |
| `$ poetry env list`         | Liste der virtuellen Umgebungen Ihres Projekts.                                            |
| `$ poetry export`           | Exportieren Sie `poetry.lock` in andere Formate.                                           |

Sie können die [Poetry CLI-Dokumentation](https://python-poetry.org/docs/cli/) konsultieren, um mehr über die oben genannten Befehle und viele andere Befehle, die Poetry bietet, zu erfahren. Sie können auch `poetry --help` ausführen, um Informationen direkt in Ihrem Terminal zu sehen!
