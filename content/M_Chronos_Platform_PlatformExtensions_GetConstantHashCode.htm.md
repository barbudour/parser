# PlatformExtensions.GetConstantHashCode - метод
Возвращает постоянный хеш-код для строки, значение которого не зависит от
текущего процесса.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static int GetConstantHashCode(
    	this string text
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetConstantHashCode ( 
    	text As String
    ) As Integer
C++ __Копировать
     public:
    [ExtensionAttribute]
    static int GetConstantHashCode(
    	String^ text
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetConstantHashCode : 
            text : string -> int 
#### Параметры
text [String](https://learn.microsoft.com/dotnet/api/system.string)
    Текст, для которого вычисляется хеш-код. Не должен быть равен null.
#### Возвращаемое значение
[Int32](https://learn.microsoft.com/dotnet/api/system.int32)  
Хеш-код строки text, значение которого не зависит от текущего процесса.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [String](https://learn.microsoft.com/dotnet/api/system.string).
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[PlatformExtensions - ](T_Chronos_Platform_PlatformExtensions.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
