# RuntimeHelper - класс
Вспомогательные методы для пространства имён Chronos.Platform.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static class RuntimeHelper
VB __Копировать
     Public NotInheritable Class RuntimeHelper
C++ __Копировать
     public ref class RuntimeHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type RuntimeHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ RuntimeHelper
##  __Свойства
[AssemblyResolveActualLocationFunc](P_Chronos_Platform_RuntimeHelper_AssemblyResolveActualLocationFunc.htm)|
Делегат, обеспечивающий алгоритм определения путей к файлу заданной сборки
вызовом
[GetActualLocationFolder(Assembly)](M_Chronos_Platform_PlatformExtensions_GetActualLocationFolder.htm).
Если делегат равен null (по умолчанию) или он возвращает null, то используется
стандартный алгоритм из метода
[GetLocationFileNameFromCodeBase(Assembly)](M_Chronos_Platform_PlatformExtensions_GetLocationFileNameFromCodeBase.htm),
определяющий местоположение сборки до того, как она могла быть скопирована
механизмом shadow copy.  
---|---  
[ConfigRootPath](P_Chronos_Platform_RuntimeHelper_ConfigRootPath.htm)|  Путь к
папке, в которой выполняется поиск конфигурационных файлов, таких как app.json
и extensions.xml. Для поиска используется делегат
[ConfigRootPathFunc](P_Chronos_Platform_RuntimeHelper_ConfigRootPathFunc.htm).
Если он не задан или вернул null, то поиск выполняется в переменной окружения
с именем
[ConfigRootPathEnvironmentVariable](F_Chronos_Platform_RuntimeHelper_ConfigRootPathEnvironmentVariable.htm).
Если переменная равна точке ".", то используется текущая папка приложения
Directory.GetCurrentDirectory(). Если переменная не задана, то выполняется
поиск относительно папки со сборкой Tessa.dll.  
[ConfigRootPathFunc](P_Chronos_Platform_RuntimeHelper_ConfigRootPathFunc.htm)|
Делегат, вызываемый для определения папки с конфигурационными файлами
[ConfigRootPath](P_Chronos_Platform_RuntimeHelper_ConfigRootPath.htm).
Вызывается один раз при запросе свойства
[ConfigRootPath](P_Chronos_Platform_RuntimeHelper_ConfigRootPath.htm). При
изменении делегата свойство
[ConfigRootPath](P_Chronos_Platform_RuntimeHelper_ConfigRootPath.htm) будет
вычислено повторно в момент обращения. Если делегат равен null (по умолчанию)
или вернул строку null, то будет использоваться определение папки по умолчанию
[GetDefaultConfigRootPath()](M_Chronos_Platform_RuntimeHelper_GetDefaultConfigRootPath.htm).
Не используйте свойства из файла конфигурации app.json, в т.ч. посредством
[ConfigurationManager](T_Chronos_Platform_Configuration_ConfigurationManager.htm),
потому что для поиска app.json также используется свойство
[ConfigRootPath](P_Chronos_Platform_RuntimeHelper_ConfigRootPath.htm), и его
использование приведёт к бесконечной рекурсии. Пример использования: () =>
Directory.GetCurrentDirectory(). Для WCF можно использовать: () =>
System.Web.Hosting.HostingEnvironment.ApplicationPhysicalPath.  
## __Методы
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
## __Поля
[ConfigRootPathEnvironmentVariable](F_Chronos_Platform_RuntimeHelper_ConfigRootPathEnvironmentVariable.htm)|
Имя переменной окружения, в которой выполняется поиск конфигурационных файлов,
таких как app.json и extensions.xml. Если переменная равна точке ".", то
используется текущая папка приложения Directory.GetCurrentDirectory(). Если
переменная не задана, то выполняется поиск относительно папки Tessa.dll
вызовом
[GetActualLocationFolder(Assembly)](M_Chronos_Platform_PlatformExtensions_GetActualLocationFolder.htm).  
---|---  
## __См. также
#### Ссылки
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
