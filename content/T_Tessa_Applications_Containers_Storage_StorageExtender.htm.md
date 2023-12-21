# StorageExtender - класс
Функции расширяющие возможности работы с хранилищем элементов
## __Definition
 **Пространство имён:**
[Tessa.Applications.Containers.Storage](N_Tessa_Applications_Containers_Storage.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class StorageExtender
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class StorageExtender
C++ __Копировать
    [ExtensionAttribute]
    public ref class StorageExtender abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type StorageExtender = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ StorageExtender
##  __Методы
[GetElements(IStorageElement,
String)](M_Tessa_Applications_Containers_Storage_StorageExtender_GetElements_1.htm)|
Возвращает список дочерних элементов элемента element с именем name  
---|---  
[GetElements(IStorageElement, IEnumerable<String>,
Boolean)](M_Tessa_Applications_Containers_Storage_StorageExtender_GetElements.htm)|
Возвращает список элементов находящихся вниз по иерархическому пути path от
элемента element  
[GetElements(IStorageElement, String, Func<IStorageElement,
Boolean>)](M_Tessa_Applications_Containers_Storage_StorageExtender_GetElements_2.htm)|
Возвращает список дочерних элементов элемента element с именем name  
[IsSameName](M_Tessa_Applications_Containers_Storage_StorageExtender_IsSameName.htm)|
Осуществляет сравнение строк как имен.  
[TryGetElement(IStorageElement,
String)](M_Tessa_Applications_Containers_Storage_StorageExtender_TryGetElement.htm)|
Возвращает первый элемент из списка дочерних элементов element с именем name
или null, если элемент отсутствует в списке  
[TryGetElement(IStorageElement, String, Func<IStorageElement,
Boolean>)](M_Tessa_Applications_Containers_Storage_StorageExtender_TryGetElement_1.htm)|
Возвращает первый элемент из списка дочерних элементов element с именем name
или null, если элемент отсутствует в списке  
## __См. также
#### Ссылки
[Tessa.Applications.Containers.Storage - пространство
имён](N_Tessa_Applications_Containers_Storage.htm)
