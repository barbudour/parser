# Check.ArgumentNotNull - метод
Проверяет, что заданный аргумент не равен null.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static void ArgumentNotNull(
    	Object argumentValue,
    	string argumentName
    )
VB __Копировать
     Public Shared Sub ArgumentNotNull ( 
    	argumentValue As Object,
    	argumentName As String
    )
C++ __Копировать
     public:
    static void ArgumentNotNull(
    	Object^ argumentValue, 
    	String^ argumentName
    )
F# __Копировать
     static member ArgumentNotNull : 
            argumentValue : Object * 
            argumentName : string -> unit 
#### Параметры
argumentValue [Object](https://learn.microsoft.com/dotnet/api/system.object)
    Проверяемое значение аргумента.
argumentName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя проверяемого аргумента.
##  __Исключения
[ArgumentNullException](https://learn.microsoft.com/dotnet/api/system.argumentnullexception)|
Значение argumentValue равно null.  
---|---  
##  __См. также
#### Ссылки
[Check - ](T_Chronos_Platform_Check.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
