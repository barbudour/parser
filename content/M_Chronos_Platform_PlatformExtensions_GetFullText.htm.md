# PlatformExtensions.GetFullText - метод
Возвращает полную информацию по заданному исключению, включая текст нескольких
исключений для
[AggregateException](https://learn.microsoft.com/dotnet/api/system.aggregateexception).
Для обычных исключений результат аналогичен вызову метода
[ToString()](https://learn.microsoft.com/dotnet/api/system.exception.tostring#system-
exception-tostring).
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static string GetFullText(
    	this Exception exception
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetFullText ( 
    	exception As Exception
    ) As String
C++ __Копировать
     public:
    [ExtensionAttribute]
    static String^ GetFullText(
    	Exception^ exception
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetFullText : 
            exception : Exception -> string 
#### Параметры
exception [Exception](https://learn.microsoft.com/dotnet/api/system.exception)
    Исключение, для которого требуется вернуть полную информацию.
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Полная информация по заданному исключению.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[Exception](https://learn.microsoft.com/dotnet/api/system.exception). При
вызове метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[PlatformExtensions - ](T_Chronos_Platform_PlatformExtensions.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
