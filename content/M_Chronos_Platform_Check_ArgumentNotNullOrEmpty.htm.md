# Check.ArgumentNotNullOrEmpty - метод
Проверяет, что заданный строковый аргумент не равен null или пустой строке.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static void ArgumentNotNullOrEmpty(
    	string argumentValue,
    	string argumentName
    )
VB __Копировать
     Public Shared Sub ArgumentNotNullOrEmpty ( 
    	argumentValue As String,
    	argumentName As String
    )
C++ __Копировать
     public:
    static void ArgumentNotNullOrEmpty(
    	String^ argumentValue, 
    	String^ argumentName
    )
F# __Копировать
     static member ArgumentNotNullOrEmpty : 
            argumentValue : string * 
            argumentName : string -> unit 
#### Параметры
argumentValue [String](https://learn.microsoft.com/dotnet/api/system.string)
    Проверяемое значение аргумента.
argumentName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя проверяемого аргумента.
##  __Исключения
[ArgumentNullException](https://learn.microsoft.com/dotnet/api/system.argumentnullexception)|
Значение argumentValue равно null.  
---|---  
[ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception)|
Значение argumentValue равно пустой строке.  
##  __См. также
#### Ссылки
[Check - ](T_Chronos_Platform_Check.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
