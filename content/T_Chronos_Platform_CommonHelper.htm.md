# CommonHelper - класс
Хэлперы общего назначения.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static class CommonHelper
VB __Копировать
     Public NotInheritable Class CommonHelper
C++ __Копировать
     public ref class CommonHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type CommonHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CommonHelper
##  __Свойства
[ChronosSyncTimeout](P_Chronos_Platform_CommonHelper_ChronosSyncTimeout.htm)|
Таймаут ожидания синхронизации между процессами.  
---|---  
[ProbingPath](P_Chronos_Platform_CommonHelper_ProbingPath.htm)|  Список папок,
используемых для загрузки сборок в плагинах помимо папки с самим плагином.
Список разделяется точкой с запятой. Для получения списка путей отдельно
используйте метод
[GetProbingPathList()](M_Chronos_Platform_CommonHelper_GetProbingPathList.htm).  
## __Методы
[AddSuppressResolveFailWarningForAssembly](M_Chronos_Platform_CommonHelper_AddSuppressResolveFailWarningForAssembly.htm)|
Добавляет указанное имя в список простых имён для сборок, для которых не
выводятся предупреждения в логе при невозможности их загрузить. Добавьте сюда
сборки, например "System.Data.SqlClient", если возможное отсутствие такой
сборки является корректным для используемых библиотек.  
---|---  
[CanAssemblyResolveFail](M_Chronos_Platform_CommonHelper_CanAssemblyResolveFail.htm)|
Возвращает признак того, что не следует писать в лог при ошибке загрузки
сборки. Сборка "Serilog" пытается загрузиться через библиотеку "Quartz" при
сканировании доступных средств логирование, и это совершенно нормально, что
загрузить её не получается. Сборка "System.Data.SqlClient" пытается
загрузиться через библиотеку "linq2db", и это нормально, что загрузить её не
получается. Сборка "Microsoft.SqlServer.Types" пытается загрузиться через
библиотеку "linq2db" при соединении с базой SQL Server для поддержки spatial-
типов, которые у нас не используются. Ошибка загрузки игнорируется. Сборка
"StackExchange.Redis" пытается загрузить
"Microsoft.WindowsAzure.ServiceRuntime", и загружать её не требуется, т.к.
подключение к Azure для Redis не используется.  
[CleanHostGlobalObjectAsync](M_Chronos_Platform_CommonHelper_CleanHostGlobalObjectAsync.htm)|
Очищает глобальные объекты синхронизации, задействуемые для хост-процесса.
Вызывается хост-процессом перед запуском дочерних процессов всех найденных
плагинов. Актуально только для Linux.  
[CleanPluginGlobalObjectsAsync](M_Chronos_Platform_CommonHelper_CleanPluginGlobalObjectsAsync.htm)|
Очищает глобальные объекты синхронизации, задействуемые для плагина.
Вызывается хост-процессом перед запуском дочерних процессов всех найденных
плагинов. Для плагинов, добавляемых при перепланировании, не вызывается.
Актуально только для Linux.  
[ContainsSuppressResolveFailWarningForAssembly](M_Chronos_Platform_CommonHelper_ContainsSuppressResolveFailWarningForAssembly.htm)|
Возвращает признак того, что указанное имя входит в список простых имён для
сборок, для которых не выводятся предупреждения в логе при невозможности их
загрузить.  
[ConvertBoolToShortString](M_Chronos_Platform_CommonHelper_ConvertBoolToShortString.htm)|
Преобразует логическое значение в краткое строковое представление.  
[ConvertShortStringToBool](M_Chronos_Platform_CommonHelper_ConvertShortStringToBool.htm)|
Преобразует краткое строковое представление в логическое значение.  
[GetActualProbingPathList](M_Chronos_Platform_CommonHelper_GetActualProbingPathList.htm)|
Возвращает список фактически существующих полных путей к папкам, из которых
требуется загружать сборки помимо папки с плагином. Список определяется на
основании метода
[GetProbingPathList()](M_Chronos_Platform_CommonHelper_GetProbingPathList.htm).
Метод может вернуть пустой список, но он не возвращает null.  
[GetDictionaryKey<T>](M_Chronos_Platform_CommonHelper_GetDictionaryKey__1.htm)|
Возвращает уникальный ключ для использования в хеш-таблицах вида
IDictionary{string,object}.  
[GetGlobalName<T>()](M_Chronos_Platform_CommonHelper_GetGlobalName__1.htm)|
Возвращает глобально уникальное имя для заданного типа.  
[GetGlobalName<T>(String)](M_Chronos_Platform_CommonHelper_GetGlobalName__1_1.htm)|
Возвращает глобально уникальное имя для заданного типа.  
[GetHashedString](M_Chronos_Platform_CommonHelper_GetHashedString.htm)|
Возвращает строку, полученную в результате хеширования заданной строки.  
[GetHostGlobalName(Assembly,
String)](M_Chronos_Platform_CommonHelper_GetHostGlobalName.htm)|  Возвращает
глобально уникальное имя в пределах хоста для заданной сборки, полученное по
заданному локальному имени.  
[GetHostGlobalName<T>()](M_Chronos_Platform_CommonHelper_GetHostGlobalName__1.htm)|
Возвращает глобально уникальное имя в пределах хоста для заданного типа.  
[GetHostGlobalName<T>(String)](M_Chronos_Platform_CommonHelper_GetHostGlobalName__1_1.htm)|
Возвращает глобально уникальное имя в пределах хоста для заданного типа.  
[GetProbingPathList](M_Chronos_Platform_CommonHelper_GetProbingPathList.htm)|
Возвращает список папок, используемых для загрузки сборок в плагинах помимо
папки с самим плагином. Метод может вернуть пустой список, но он не возвращает
null.  
[ObjectIsNotNull](M_Chronos_Platform_CommonHelper_ObjectIsNotNull.htm)|
Возвращает true, если ссылка на объект не равна null.  
[ObjectIsNull](M_Chronos_Platform_CommonHelper_ObjectIsNull.htm)|  Возвращает
true, если ссылка на объект равна null.  
[RemoveSuppressResolveFailWarningForAssembly](M_Chronos_Platform_CommonHelper_RemoveSuppressResolveFailWarningForAssembly.htm)|
Удаляет указанное имя из списка простых имён для сборок, для которых не
выводятся предупреждения в логе при невозможности их загрузить. Возвращает
признак того, что сборка присутствовала в списке до удаления.  
## __Поля
[DefaultHostServiceName](F_Chronos_Platform_CommonHelper_DefaultHostServiceName.htm)|
Имя сервиса по умолчанию, используемое для логирования от имени хост-процесса
в [PluginFacade](T_Chronos_Platform_Scheduling_PluginFacade.htm).  
---|---  
[DirectorySeparatorString](F_Chronos_Platform_CommonHelper_DirectorySeparatorString.htm)|
Символ
[DirectorySeparatorChar](https://learn.microsoft.com/dotnet/api/system.io.path.directoryseparatorchar)
для разделения пути и имени файла в операционной системе, представленный в
виде строки.  
## __См. также
#### Ссылки
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
