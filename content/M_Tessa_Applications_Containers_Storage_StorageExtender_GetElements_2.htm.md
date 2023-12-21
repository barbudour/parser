# StorageExtender.GetElements(IStorageElement, String, Func<IStorageElement,
Boolean>) - метод
Возвращает список дочерних элементов элемента element с именем name
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Containers.Storage](N_Tessa_Applications_Containers_Storage.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    public static IEnumerable<IStorageElement> GetElements(
    	[NotNullAttribute] this IStorageElement element,
    	[NotNullAttribute] string name,
    	[NotNullAttribute] Func<IStorageElement, bool> selector
    )
VB __Копировать
    <ExtensionAttribute>
    <NotNullAttribute>
    Public Shared Function GetElements ( 
    	<NotNullAttribute> element As IStorageElement,
    	<NotNullAttribute> name As String,
    	<NotNullAttribute> selector As Func(Of IStorageElement, Boolean)
    ) As IEnumerable(Of IStorageElement)
C++ __Копировать
     public:
    [ExtensionAttribute]
    [NotNullAttribute]
    static IEnumerable<IStorageElement^>^ GetElements(
    	[NotNullAttribute] IStorageElement^ element, 
    	[NotNullAttribute] String^ name, 
    	[NotNullAttribute] Func<IStorageElement^, bool>^ selector
    )
F# __Копировать
     [<ExtensionAttribute>]
    [<NotNullAttribute>]
    static member GetElements : 
            [<NotNullAttribute>] element : IStorageElement * 
            [<NotNullAttribute>] name : string * 
            [<NotNullAttribute>] selector : Func<IStorageElement, bool> -> IEnumerable<IStorageElement> 
#### Параметры
element
[IStorageElement](T_Tessa_Applications_Containers_Storage_IStorageElement.htm)
     Элемент из которого требуется получить список дочерних элементов 
name [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя элементов 
selector
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[IStorageElement](T_Tessa_Applications_Containers_Storage_IStorageElement.htm),
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>
     Селектор отбора результатов 
#### Возвращаемое значение
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[IStorageElement](T_Tessa_Applications_Containers_Storage_IStorageElement.htm)>  
Список элементов
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
[GetElements -
перегрузка](Overload_Tessa_Applications_Containers_Storage_StorageExtender_GetElements.htm)
[Tessa.Applications.Containers.Storage - пространство
имён](N_Tessa_Applications_Containers_Storage.htm)
