# ConfigurationManager - поля
##  __Поля
[DefaultSymbolValue](F_Chronos_Platform_Configuration_ConfigurationManager_DefaultSymbolValue.htm)|
Значение по умолчанию для символов.  
---|---  
[DefineDirective](F_Chronos_Platform_Configuration_ConfigurationManager_DefineDirective.htm)|
Директива в конфигурационном файле, выполняющая включение или исключение
символов из текущей конфигурации. Символы в дальнейшей используются в
директиве
[IfDirective](F_Chronos_Platform_Configuration_ConfigurationManager_IfDirective.htm).
Пример: ".define": [ "addedSymbol", "!removedSymbol" ]  
[IfDirective](F_Chronos_Platform_Configuration_ConfigurationManager_IfDirective.htm)|
Директива в конфигурационном файле, выполняющая включение в текущую
конфигурацию нижележащего блока при условии, что выполняется условие,
связанное с перечисленными символами. Пример: ".if": [ [ "existentSymbol",
"!absentSymbol" ], { "Key": value } ]  
[IncludeDirective](F_Chronos_Platform_Configuration_ConfigurationManager_IncludeDirective.htm)|
Директива в конфигурационном файле, выполняющая включение содержимого
указанного файла в текущую конфигурацию. Пример: ".include": "../app.json"  
[LinuxSymbol](F_Chronos_Platform_Configuration_ConfigurationManager_LinuxSymbol.htm)|
Символ, объявленный при выполнении на Linux.  
[Process32BitSymbol](F_Chronos_Platform_Configuration_ConfigurationManager_Process32BitSymbol.htm)|
Символ, объявленный при выполнении в 32-битном процессе.  
[Process64BitSymbol](F_Chronos_Platform_Configuration_ConfigurationManager_Process64BitSymbol.htm)|
Символ, объявленный при выполнении в 64-битном процессе.  
[WindowsSymbol](F_Chronos_Platform_Configuration_ConfigurationManager_WindowsSymbol.htm)|
Символ, объявленный при выполнении на Windows.  
## __См. также
#### Ссылки
[ConfigurationManager -
](T_Chronos_Platform_Configuration_ConfigurationManager.htm)
[Chronos.Platform.Configuration - пространство
имён](N_Chronos_Platform_Configuration.htm)
