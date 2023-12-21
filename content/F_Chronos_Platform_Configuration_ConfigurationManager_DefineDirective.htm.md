# ConfigurationManager.DefineDirective - поле
Директива в конфигурационном файле, выполняющая включение или исключение
символов из текущей конфигурации. Символы в дальнейшей используются в
директиве
[IfDirective](F_Chronos_Platform_Configuration_ConfigurationManager_IfDirective.htm).
Пример: ".define": [ "addedSymbol", "!removedSymbol" ]
##  __Definition
 **Пространство имён:**
[Chronos.Platform.Configuration](N_Chronos_Platform_Configuration.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public const string DefineDirective = ".define"
VB __Копировать
     Public Const DefineDirective As String = ".define"
C++ __Копировать
     public:
    literal String^ DefineDirective = ".define"
F# __Копировать
     static val mutable DefineDirective: string
#### Значение поля
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __См. также
#### Ссылки
[ConfigurationManager -
](T_Chronos_Platform_Configuration_ConfigurationManager.htm)
[Chronos.Platform.Configuration - пространство
имён](N_Chronos_Platform_Configuration.htm)
