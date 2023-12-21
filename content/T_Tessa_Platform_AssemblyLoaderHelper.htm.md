# AssemblyLoaderHelper - класс
Вспомогательные методы для поиска и загрузки любых сборок.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class AssemblyLoaderHelper
VB __Копировать
     Public NotInheritable Class AssemblyLoaderHelper
C++ __Копировать
     public ref class AssemblyLoaderHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type AssemblyLoaderHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ AssemblyLoaderHelper
##  __Свойства
[HasAssemblyResolveHandler](P_Tessa_Platform_AssemblyLoaderHelper_HasAssemblyResolveHandler.htm)|
Признак того, что с текущим доменом уже связан ранее заданный обработчик
загрузки сборок.  
---|---  
## __Методы
[AddAssemblyResolveHandler](M_Tessa_Platform_AssemblyLoaderHelper_AddAssemblyResolveHandler.htm)|
Добавляет обработчик загрузки сборок AssemblyLoadContext.Default.Resolving для
указанного списка сборок probingPathList, который обычно загружается вызовом
метода [GetActualProbingPathList(IEnumerable<String>, Assembly,
Boolean)](M_Tessa_Platform_AssemblyLoaderHelper_GetActualProbingPathList.htm).
Метод удаляет регистрацию предыдущего обработчика, если таковой был
зарегистрирован. Вызов метода потокобезопасен.  
---|---  
[AddSuppressResolveFailWarningForAssembly](M_Tessa_Platform_AssemblyLoaderHelper_AddSuppressResolveFailWarningForAssembly.htm)|
Добавляет указанное имя в список простых имён для сборок, для которых не
выводятся предупреждения в логе при невозможности их загрузить. Добавьте сюда
сборки, например "System.Data.SqlClient", если возможное отсутствие такой
сборки является корректным для используемых библиотек.  
[CanAssemblyResolveFail](M_Tessa_Platform_AssemblyLoaderHelper_CanAssemblyResolveFail.htm)|
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
[ContainsSuppressResolveFailWarningForAssembly](M_Tessa_Platform_AssemblyLoaderHelper_ContainsSuppressResolveFailWarningForAssembly.htm)|
Возвращает признак того, что указанное имя входит в список простых имён для
сборок, для которых не выводятся предупреждения в логе при невозможности их
загрузить.  
[GetActualProbingPathList](M_Tessa_Platform_AssemblyLoaderHelper_GetActualProbingPathList.htm)|
Возвращает список фактически существующих полных путей к папкам, из которых
требуется загружать сборки помимо папки с плагином. Метод может вернуть пустой
список, но он не возвращает null. Метод всегда возвращает другой экземпляр
списка, нежели задан в probingPathList.  
[GetAssemblyResolveEventHandler](M_Tessa_Platform_AssemblyLoaderHelper_GetAssemblyResolveEventHandler.htm)|
Возвращает обработчик загрузки сборок AssemblyLoadContext.Default.Resolving
для указанного списка сборок probingPathList, который обычно загружается
вызовом метода [GetActualProbingPathList(IEnumerable<String>, Assembly,
Boolean)](M_Tessa_Platform_AssemblyLoaderHelper_GetActualProbingPathList.htm).
Обработчик создаётся, но не добавляется в домен. Вызов метода потокобезопасен.  
[GetProbingPathList](M_Tessa_Platform_AssemblyLoaderHelper_GetProbingPathList.htm)|
Возвращает список папок, используемых для загрузки сборок помимо папки с
приложением. Метод может вернуть пустой список, но он не возвращает null.  
[RemoveSuppressResolveFailWarningForAssembly](M_Tessa_Platform_AssemblyLoaderHelper_RemoveSuppressResolveFailWarningForAssembly.htm)|
Удаляет указанное имя из списка простых имён для сборок, для которых не
выводятся предупреждения в логе при невозможности их загрузить. Возвращает
признак того, что сборка присутствовала в списке до удаления.  
## __Поля
[ProbingPathKey](F_Tessa_Platform_AssemblyLoaderHelper_ProbingPathKey.htm)|
Ключ в настройках, которому соответствует строка со списком относительных
путей допапок, используемых для загрузки сборок помимо папки с приложением.  
---|---  
## __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
