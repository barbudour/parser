# ConsoleHelper.GetArgumentString - метод
Возвращает строку, в которой объединены перечисленные аргументы командной
строки с заключением их в кавычки.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static string GetArgumentString(
    	params string[] args
    )
VB __Копировать
     Public Shared Function GetArgumentString ( 
    	ParamArray args As String()
    ) As String
C++ __Копировать
     public:
    static String^ GetArgumentString(
    	... array<String^>^ args
    )
F# __Копировать
     static member GetArgumentString : 
            args : string[] -> string 
#### Параметры
args [String](https://learn.microsoft.com/dotnet/api/system.string)[]
    Аргументы командной строки, которое требуется объединить.
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Строка, объединяющая заданные аргументы командной строки.
##  __См. также
#### Ссылки
[ConsoleHelper - ](T_Chronos_Platform_ConsoleHelper.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
