# RuntimeHelper - свойства
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
## __См. также
#### Ссылки
[RuntimeHelper - ](T_Chronos_Platform_RuntimeHelper.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
