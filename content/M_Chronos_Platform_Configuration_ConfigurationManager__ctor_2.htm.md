# ConfigurationManager(String, IEnumerable<KeyValuePair<String, String>>) -
конструктор
Создаёт экземпляр класса с указанием полного пути до файла с конфигурацией.
Вызов конструктора не может завершиться исключением. После создания объекта
необходимо вызвать метод асинхронной инициализации
[InitializeAsync(CancellationToken)](M_Chronos_Platform_IAsyncInitializable_InitializeAsync.htm).
## __Definition
 **Пространство имён:**
[Chronos.Platform.Configuration](N_Chronos_Platform_Configuration.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public ConfigurationManager(
    	string path,
    	IEnumerable<KeyValuePair<string, string>> definedSymbols = null
    )
VB __Копировать
     Public Sub New ( 
    	path As String,
    	Optional definedSymbols As IEnumerable(Of KeyValuePair(Of String, String)) = Nothing
    )
C++ __Копировать
     public:
    ConfigurationManager(
    	String^ path, 
    	IEnumerable<KeyValuePair<String^, String^>>^ definedSymbols = nullptr
    )
F# __Копировать
     new : 
            path : string * 
            ?definedSymbols : IEnumerable<KeyValuePair<string, string>> 
    (* Defaults:
            let _definedSymbols = defaultArg definedSymbols null
    *)
    -> ConfigurationManager
#### Параметры
path [String](https://learn.microsoft.com/dotnet/api/system.string)
    Полный путь до файла с конфигурацией.
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
