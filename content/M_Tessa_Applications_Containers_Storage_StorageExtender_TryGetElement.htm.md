# StorageExtender.TryGetElement(IStorageElement, String) - метод
Возвращает первый элемент из списка дочерних элементов element с именем name
или null, если элемент отсутствует в списке
## __Definition
 **Пространство имён:**
[Tessa.Applications.Containers.Storage](N_Tessa_Applications_Containers_Storage.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [CanBeNullAttribute]
    public static IStorageElement TryGetElement(
    	[NotNullAttribute] this IStorageElement element,
    	[NotNullAttribute] string name
    )
VB __Копировать
    <ExtensionAttribute>
    <CanBeNullAttribute>
    Public Shared Function TryGetElement ( 
    	<NotNullAttribute> element As IStorageElement,
    	<NotNullAttribute> name As String
    ) As IStorageElement
C++ __Копировать
     public:
    [ExtensionAttribute]
    [CanBeNullAttribute]
    static IStorageElement^ TryGetElement(
    	[NotNullAttribute] IStorageElement^ element, 
    	[NotNullAttribute] String^ name
    )
F# __Копировать
     [<ExtensionAttribute>]
    [<CanBeNullAttribute>]
    static member TryGetElement : 
            [<NotNullAttribute>] element : IStorageElement * 
            [<NotNullAttribute>] name : string -> IStorageElement 
#### Параметры
element
[IStorageElement](T_Tessa_Applications_Containers_Storage_IStorageElement.htm)
     Элемент из которого требуется получить дочерний элемент 
name [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя элемента 
#### Возвращаемое значение
[IStorageElement](T_Tessa_Applications_Containers_Storage_IStorageElement.htm)  
Найденный элемент или null, если элемент отсутствует в списке
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[IStorageElement](T_Tessa_Applications_Containers_Storage_IStorageElement.htm).
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
[TryGetElement -
перегрузка](Overload_Tessa_Applications_Containers_Storage_StorageExtender_TryGetElement.htm)
[Tessa.Applications.Containers.Storage - пространство
имён](N_Tessa_Applications_Containers_Storage.htm)
