# ConfigurationManager.GlobalDefinedSymbols - свойство
Глобально объявленные символы по умолчанию, доступные для всех объектов
конфигурации. По умолчанию соответствуют операционной системе, разрядности
процессора и другим параметрам среды выполнения. Используются для
инициализации начального значения свойства
[DefinedSymbols](P_Chronos_Platform_Configuration_ConfigurationManager_DefinedSymbols.htm)
для каждого объекта конфигурации.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Configuration](N_Chronos_Platform_Configuration.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static HashSet<string> GlobalDefinedSymbols { get; }
VB __Копировать
     Public Shared ReadOnly Property GlobalDefinedSymbols As HashSet(Of String)
    	Get
C++ __Копировать
     public:
    static property HashSet<String^>^ GlobalDefinedSymbols {
    	HashSet<String^>^ get ();
    }
F# __Копировать
     static member GlobalDefinedSymbols : HashSet<string> with get
#### Значение свойства
[HashSet](https://learn.microsoft.com/dotnet/api/system.collections.generic.hashset-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
##  __См. также
#### Ссылки
[ConfigurationManager -
](T_Chronos_Platform_Configuration_ConfigurationManager.htm)
[Chronos.Platform.Configuration - пространство
имён](N_Chronos_Platform_Configuration.htm)
