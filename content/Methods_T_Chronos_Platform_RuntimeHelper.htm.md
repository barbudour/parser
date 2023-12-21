# RuntimeHelper - методы
##  __Методы
[GetDefaultConfigRootPath](M_Chronos_Platform_RuntimeHelper_GetDefaultConfigRootPath.htm)|
Алгоритм поиска по умолчанию для папки, в которой выполняется поиск
конфигурационных файлов, таких как app.json и extensions.xml. Поиск сначала
выполняется в переменной окружения с именем
[ConfigRootPathEnvironmentVariable](F_Chronos_Platform_RuntimeHelper_ConfigRootPathEnvironmentVariable.htm).
Если переменная равна точке ".", то используется текущая папка приложения
Directory.GetCurrentDirectory(). Если переменная не задана, то выполняется
поиск относительно папки со сборкой Tessa.dll.  
---|---  
[GetExecutableFileName](M_Chronos_Platform_RuntimeHelper_GetExecutableFileName.htm)|
Возвращает имя основного исполняемого файла или полный путь к нему, если
параметр fullPath указан как true. При невозможности получить имя файла или
путь будет возвращено null или выброшено исключение.  
## __См. также
#### Ссылки
[RuntimeHelper - ](T_Chronos_Platform_RuntimeHelper.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
