# PlatformExtensions.GetHashedString - метод
Возвращает строку, содержащую криптостойкое хеш-значение от текущей строки.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static string GetHashedString(
    	this string value
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetHashedString ( 
    	value As String
    ) As String
C++ __Копировать
     public:
    [ExtensionAttribute]
    static String^ GetHashedString(
    	String^ value
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetHashedString : 
            value : string -> string 
#### Параметры
value [String](https://learn.microsoft.com/dotnet/api/system.string)
     Строка, для которой требуется получить строку с хешем. Может быть равна null, тогда результат идентичен пустой строке. 
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Хеш текущей строки.
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
