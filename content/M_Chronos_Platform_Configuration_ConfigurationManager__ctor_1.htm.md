# ConfigurationManager(Assembly, String, IEnumerable<KeyValuePair<String,
String>>) - конструктор
Создаёт экземпляр класса с указанием сборки, рядом с которой лежит файл
конфигурации app.json. Вызов конструктора не может завершиться исключением.
После создания объекта необходимо вызвать метод асинхронной инициализации
[InitializeAsync(CancellationToken)](M_Chronos_Platform_IAsyncInitializable_InitializeAsync.htm).
## __Definition
 **Пространство имён:**
[Chronos.Platform.Configuration](N_Chronos_Platform_Configuration.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public ConfigurationManager(
    	Assembly assembly = null,
    	string fileName = "app.json",
    	IEnumerable<KeyValuePair<string, string>> definedSymbols = null
    )
VB __Копировать
     Public Sub New ( 
    	Optional assembly As Assembly = Nothing,
    	Optional fileName As String = "app.json",
    	Optional definedSymbols As IEnumerable(Of KeyValuePair(Of String, String)) = Nothing
    )
C++ __Копировать
     public:
    ConfigurationManager(
    	Assembly^ assembly = nullptr, 
    	String^ fileName = L"app.json", 
    	IEnumerable<KeyValuePair<String^, String^>>^ definedSymbols = nullptr
    )
F# __Копировать
     new : 
            ?assembly : Assembly * 
            ?fileName : string * 
            ?definedSymbols : IEnumerable<KeyValuePair<string, string>> 
    (* Defaults:
            let _assembly = defaultArg assembly null
            let _fileName = defaultArg fileName "app.json"
            let _definedSymbols = defaultArg definedSymbols null
    *)
    -> ConfigurationManager
#### Параметры
assembly
[Assembly](https://learn.microsoft.com/dotnet/api/system.reflection.assembly)
(Optional)
     Сборка, рядом с которой лежит файл конфигурации app.json, или null, если поиск файла выполняется в соответствии с [ConfigRootPath](P_Chronos_Platform_RuntimeHelper_ConfigRootPath.htm). 
fileName [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
     Имя файла конфигурации без указания пути. Не должно быть равно null или пустой строке. 
definedSymbols
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[KeyValuePair](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[String](https://learn.microsoft.com/dotnet/api/system.string)>> (Optional)
     Символы, объявленные по умолчанию в дополнение к [GlobalDefinedSymbols](P_Chronos_Platform_Configuration_ConfigurationManager_GlobalDefinedSymbols.htm) или null, если такие символы отсутствуют. 
## __См. также
#### Ссылки
[ConfigurationManager -
](T_Chronos_Platform_Configuration_ConfigurationManager.htm)
[ConfigurationManager -
перегрузка](Overload_Chronos_Platform_Configuration_ConfigurationManager__ctor.htm)
[Chronos.Platform.Configuration - пространство
имён](N_Chronos_Platform_Configuration.htm)
