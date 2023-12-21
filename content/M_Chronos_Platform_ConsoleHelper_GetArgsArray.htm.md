# ConsoleHelper.GetArgsArray - метод
Возвращает массив аргументов командной строки, полученный из массива,
переданного методу Main того процесса, который был запущен со строкой
аргументов, возвращённой методом
[GetArgumentString(String[])](M_Chronos_Platform_ConsoleHelper_GetArgumentString.htm).
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static string[] GetArgsArray(
    	string[] argsWithQuotes
    )
VB __Копировать
     Public Shared Function GetArgsArray ( 
    	argsWithQuotes As String()
    ) As String()
C++ __Копировать
     public:
    static array<String^>^ GetArgsArray(
    	array<String^>^ argsWithQuotes
    )
F# __Копировать
     static member GetArgsArray : 
            argsWithQuotes : string[] -> string[] 
#### Параметры
argsWithQuotes
[String](https://learn.microsoft.com/dotnet/api/system.string)[]
    Массив аргументов командной строки, заключённых в кавычки.
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)[]  
Массив аргументов командной строки.
##  __Заметки
Метод выполняет удаление кавычек из аргументов, если они присутствуют.
## __См. также
#### Ссылки
[ConsoleHelper - ](T_Chronos_Platform_ConsoleHelper.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
