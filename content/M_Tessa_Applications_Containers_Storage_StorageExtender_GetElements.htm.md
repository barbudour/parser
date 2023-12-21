# StorageExtender.GetElements(IStorageElement, IEnumerable<String>, Boolean) -
метод
Возвращает список элементов находящихся вниз по иерархическому пути path от
элемента element
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Containers.Storage](N_Tessa_Applications_Containers_Storage.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    public static IEnumerable<IStorageElement> GetElements(
    	[NotNullAttribute] this IStorageElement element,
    	[NotNullAttribute] IEnumerable<string> path,
    	bool findFirst = false
    )
VB __Копировать
    <ExtensionAttribute>
    <NotNullAttribute>
    Public Shared Function GetElements ( 
    	<NotNullAttribute> element As IStorageElement,
    	<NotNullAttribute> path As IEnumerable(Of String),
    	Optional findFirst As Boolean = false
    ) As IEnumerable(Of IStorageElement)
C++ __Копировать
     public:
    [ExtensionAttribute]
    [NotNullAttribute]
    static IEnumerable<IStorageElement^>^ GetElements(
    	[NotNullAttribute] IStorageElement^ element, 
    	[NotNullAttribute] IEnumerable<String^>^ path, 
    	bool findFirst = false
    )
F# __Копировать
     [<ExtensionAttribute>]
    [<NotNullAttribute>]
    static member GetElements : 
            [<NotNullAttribute>] element : IStorageElement * 
            [<NotNullAttribute>] path : IEnumerable<string> * 
            ?findFirst : bool 
    (* Defaults:
            let _findFirst = defaultArg findFirst false
    *)
    -> IEnumerable<IStorageElement> 
#### Параметры
element
[IStorageElement](T_Tessa_Applications_Containers_Storage_IStorageElement.htm)
     Корневой элемент иерарахии 
path
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
     Путь к элементам 
findFirst [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
     Признак необходимости получения только первого элемента удовлетворяющего условию 
#### Возвращаемое значение
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[IStorageElement](T_Tessa_Applications_Containers_Storage_IStorageElement.htm)>  
Список полученных элементов
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
