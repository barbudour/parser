# ConfigurationManager.IfDirective - поле
Директива в конфигурационном файле, выполняющая включение в текущую
конфигурацию нижележащего блока при условии, что выполняется условие,
связанное с перечисленными символами. Пример: ".if": [ [ "existentSymbol",
"!absentSymbol" ], { "Key": value } ]
##  __Definition
 **Пространство имён:**
[Chronos.Platform.Configuration](N_Chronos_Platform_Configuration.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public const string IfDirective = ".if"
VB __Копировать
     Public Const IfDirective As String = ".if"
C++ __Копировать
     public:
    literal String^ IfDirective = ".if"
F# __Копировать
     static val mutable IfDirective: string
#### Значение поля
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __См. также
#### Ссылки
[ConfigurationManager -
](T_Chronos_Platform_Configuration_ConfigurationManager.htm)
[Chronos.Platform.Configuration - пространство
имён](N_Chronos_Platform_Configuration.htm)
