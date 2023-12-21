# RuntimeHelper.ConfigRootPathFunc - свойство
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
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static Func<string> ConfigRootPathFunc { get; set; }
VB __Копировать
     Public Shared Property ConfigRootPathFunc As Func(Of String)
    	Get
    	Set
C++ __Копировать
     public:
    static property Func<String^>^ ConfigRootPathFunc {
    	Func<String^>^ get ();
    	void set (Func<String^>^ value);
    }
F# __Копировать
     static member ConfigRootPathFunc : Func<string> with get, set
#### Значение свойства
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
##  __См. также
#### Ссылки
[RuntimeHelper - ](T_Chronos_Platform_RuntimeHelper.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
