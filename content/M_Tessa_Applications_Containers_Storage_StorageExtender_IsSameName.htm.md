# StorageExtender.IsSameName - метод
Осуществляет сравнение строк как имен.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Containers.Storage](N_Tessa_Applications_Containers_Storage.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool IsSameName(
    	[CanBeNullAttribute] this string source,
    	[CanBeNullAttribute] string name
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function IsSameName ( 
    	<CanBeNullAttribute> source As String,
    	<CanBeNullAttribute> name As String
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool IsSameName(
    	[CanBeNullAttribute] String^ source, 
    	[CanBeNullAttribute] String^ name
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member IsSameName : 
            [<CanBeNullAttribute>] source : string * 
            [<CanBeNullAttribute>] name : string -> bool 
#### Параметры
source [String](https://learn.microsoft.com/dotnet/api/system.string)
     Исходная строка 
name [String](https://learn.microsoft.com/dotnet/api/system.string)
     Сравниваемая строка 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Результат сравнения
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
[StorageExtender -
](T_Tessa_Applications_Containers_Storage_StorageExtender.htm)
[Tessa.Applications.Containers.Storage - пространство
имён](N_Tessa_Applications_Containers_Storage.htm)
