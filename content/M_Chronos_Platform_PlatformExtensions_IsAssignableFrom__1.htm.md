# PlatformExtensions.IsAssignableFrom<T> \- метод
Возвращает признак того, что тип реализует заданный интерфейс.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool IsAssignableFrom<T>(
    	this Type type
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function IsAssignableFrom(Of T) ( 
    	type As Type
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    generic<typename T>
    static bool IsAssignableFrom(
    	Type^ type
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member IsAssignableFrom : 
            type : Type -> bool 
#### Параметры
type [Type](https://learn.microsoft.com/dotnet/api/system.type)
    Тип, для которого необходимо определить, реализует ли он заданный интерфейс.
#### Параметры типа
T
    Тип интерфейса, реализацию которого требуется проверить.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если тип type реализует заданный интерфейс T; false, если тип не
реализует интерфейс или T не является типом интерфейса.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [Type](https://learn.microsoft.com/dotnet/api/system.type). При
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
