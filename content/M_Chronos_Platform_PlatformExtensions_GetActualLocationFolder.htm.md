# PlatformExtensions.GetActualLocationFolder - метод
Возвращает действительное местоположение сборки (обычно это местоположение до
того, как сборка была скопирована механизмом shadow copy). При этом
используется делегат
[AssemblyResolveActualLocationFunc](P_Chronos_Platform_RuntimeHelper_AssemblyResolveActualLocationFunc.htm)
или метод
[GetLocationFolderFromCodeBase(Assembly)](M_Chronos_Platform_PlatformExtensions_GetLocationFolderFromCodeBase.htm),
если делегат не был определён.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static string GetActualLocationFolder(
    	this Assembly assembly
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetActualLocationFolder ( 
    	assembly As Assembly
    ) As String
C++ __Копировать
     public:
    [ExtensionAttribute]
    static String^ GetActualLocationFolder(
    	Assembly^ assembly
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetActualLocationFolder : 
            assembly : Assembly -> string 
#### Параметры
assembly
[Assembly](https://learn.microsoft.com/dotnet/api/system.reflection.assembly)
    Сборка, для которой определяется путь.
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Путь к действительному местоположению сборки.
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
##  __См. также
#### Ссылки
[PlatformExtensions - ](T_Chronos_Platform_PlatformExtensions.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
