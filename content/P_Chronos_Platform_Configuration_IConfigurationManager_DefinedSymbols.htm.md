# IConfigurationManager.DefinedSymbols - свойство
Текущие объявленные символы. По умолчанию соответствуют операционной системе,
разрядности процессора и другим параметрам среды выполнения. В ходе разбора
конфигурационных файлов список символов может изменяться директивой ".define".
## __Definition
 **Пространство имён:**
[Chronos.Platform.Configuration](N_Chronos_Platform_Configuration.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
    Dictionary<string, string> DefinedSymbols { get; }
VB __Копировать
     ReadOnly Property DefinedSymbols As Dictionary(Of String, String)
    	Get
C++ __Копировать
    property Dictionary<String^, String^>^ DefinedSymbols {
    	Dictionary<String^, String^>^ get ();
    }
F# __Копировать
     abstract DefinedSymbols : Dictionary<string, string> with get
#### Значение свойства
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[String](https://learn.microsoft.com/dotnet/api/system.string)>
##  __Заметки
Значение свойства никогда не равно null.
## __См. также
#### Ссылки
[IConfigurationManager -
](T_Chronos_Platform_Configuration_IConfigurationManager.htm)
[Chronos.Platform.Configuration - пространство
имён](N_Chronos_Platform_Configuration.htm)
