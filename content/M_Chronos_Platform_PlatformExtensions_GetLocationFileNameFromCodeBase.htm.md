# PlatformExtensions.GetLocationFileNameFromCodeBase - метод
Возвращает полный путь к файлу сборки.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static string GetLocationFileNameFromCodeBase(
    	this Assembly assembly
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetLocationFileNameFromCodeBase ( 
    	assembly As Assembly
    ) As String
C++ __Копировать
     public:
    [ExtensionAttribute]
    static String^ GetLocationFileNameFromCodeBase(
    	Assembly^ assembly
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetLocationFileNameFromCodeBase : 
            assembly : Assembly -> string 
#### Параметры
assembly
[Assembly](https://learn.microsoft.com/dotnet/api/system.reflection.assembly)
    Сборка, полный путь к которой определяется.
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Полный путь к файлу сборки.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[Assembly](https://learn.microsoft.com/dotnet/api/system.reflection.assembly).
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __Заметки
Для .NET Framework CodeBase для IIS вернёт местоположение сборки до того, как
IIS скопировал её во временную папку через механизм shadow copy. Для .NET Core
это неактуально, поэтому всегда используется свойство
[Location](https://learn.microsoft.com/dotnet/api/system.reflection.assembly.location#system-
reflection-assembly-location) сборки.
## __См. также
#### Ссылки
[PlatformExtensions - ](T_Chronos_Platform_PlatformExtensions.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
