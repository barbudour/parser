# ConfigurationManager.Settings - свойство
Настройки для приложения, доступные по умолчанию. В качестве ключа выступает
имя настройки, а в качестве значения - её значение (строка, число и т.п.).
Целые числа обычно представление как тип
[Int64](https://learn.microsoft.com/dotnet/api/system.int64).
## __Definition
 **Пространство имён:**
[Chronos.Platform.Configuration](N_Chronos_Platform_Configuration.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static Dictionary<string, Object> Settings { get; }
VB __Копировать
     Public Shared ReadOnly Property Settings As Dictionary(Of String, Object)
    	Get
C++ __Копировать
     public:
    static property Dictionary<String^, Object^>^ Settings {
    	Dictionary<String^, Object^>^ get ();
    }
F# __Копировать
     static member Settings : Dictionary<string, Object> with get
#### Значение свойства
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
##  __См. также
#### Ссылки
[ConfigurationManager -
](T_Chronos_Platform_Configuration_ConfigurationManager.htm)
[Chronos.Platform.Configuration - пространство
имён](N_Chronos_Platform_Configuration.htm)
