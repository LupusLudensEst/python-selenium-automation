$ pip allure-commandline
$ pip install selenium
$ pip install allure-behave
$ pip install allure-pytest
$ pip install pytest-allure-adaptor
$ pip uninstall behave
$ pip3 install behave

Запустить отчёт/Run report:
$ behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/hw5.1_color_selection_loop.feature
$ behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/
Загрузить отчёт/Upload report to browser:
$ allure serve test_results/




Если проблема: behave: error: format=allure_behave.formatter:AllureFormatter is unknown.
$ pip install --upgrade pip
pip install allure-behave
behave -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% ./features

Сборка html-отчета на локальной машине

Для сборки html–отчета необходима утилита, которая называется allure–commandline. Получить отчет можно несколькими способами:

Способ 1:
1. Скачать последнюю версию allure–commandline по ссылке;

2. Распаковать архив;

3. Добавить путь до директории bin из распакованного архива в системную переменную окружения.

Чтобы убедиться в корректности установки, выполните в командной строке команду

allure --version

Должно появиться сообщение вида:

$ allure --version
2.6.0

После установки allure–commandline откройте в проводнике папку с исходными для построения отчета файлами (в нашем примере target/allure-results) и в окне команд (терминале) выполните команду

allure serve

После этого должен сформироваться сам html–отчет, который откроется в браузере по умолчанию автоматически.

C:\Webdrivers\allure-2.13.0\bin>allure --version
2.13.0
C:\Webdrivers\allure-2.13.0\bin>allure serve
Generating report to temp directory...
allure-results does not exists
Report successfully generated to C:\Users\GUROVV~1\AppData\Local\Temp\1112192896526047821\allure-report
Starting web server...
2019-11-19 23:17:38.593:INFO::main: Logging initialized @9785ms to org.eclipse.jetty.util.log.StdErrLog
Server started at <http://192.168.56.1:53498/>. Press <Ctrl+C> to exit

http://192.168.56.1:53498/index.html
