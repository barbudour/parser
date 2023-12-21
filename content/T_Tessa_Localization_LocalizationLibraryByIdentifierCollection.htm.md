# LocalizationLibraryByIdentifierCollection - класс
##  __Definition
 **Пространство имён:** [Tessa.Localization](N_Tessa_Localization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class LocalizationLibraryByIdentifierCollection : HashSet<Guid, LocalizationLibrary>
VB __Копировать
     Public NotInheritable Class LocalizationLibraryByIdentifierCollection
    	Inherits HashSet(Of Guid, LocalizationLibrary)
C++ __Копировать
     public ref class LocalizationLibraryByIdentifierCollection sealed : public HashSet<Guid, LocalizationLibrary^>
F# __Копировать
     [<SealedAttribute>]
    type LocalizationLibraryByIdentifierCollection = 
        class
            inherit HashSet<Guid, LocalizationLibrary>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[HashSet](T_Tessa_Platform_Collections_HashSet_2.htm)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid), [LocalizationLibrary](T_Tessa_Localization_LocalizationLibrary.htm)> __ LocalizationLibraryByIdentifierCollection
##  __Конструкторы
[LocalizationLibraryByIdentifierCollection()](M_Tessa_Localization_LocalizationLibraryByIdentifierCollection__ctor.htm)|
Инициализирует новый экземпляр класса
LocalizationLibraryByIdentifierCollection  
---|---  
[LocalizationLibraryByIdentifierCollection(IEnumerable<LocalizationLibrary>)](M_Tessa_Localization_LocalizationLibraryByIdentifierCollection__ctor_1.htm)|
Инициализирует новый экземпляр класса
LocalizationLibraryByIdentifierCollection  
##  __Свойства
[Count](P_Tessa_Platform_Collections_HashSet_2_Count.htm)|  Количество
элементов в коллекции.  
(Унаследован от [HashSet<TKey,
TValue>](T_Tessa_Platform_Collections_HashSet_2.htm))  
---|---  
[Item](P_Tessa_Platform_Collections_HashSet_2_Item.htm)|  Получить/установить
значение по заданному ключу.  
(Унаследован от [HashSet<TKey,
TValue>](T_Tessa_Platform_Collections_HashSet_2.htm))  
##  __Методы
[Add](M_Tessa_Platform_Collections_HashSet_2_Add.htm)| Adds an element to the
current set and returns a value to indicate if the element was successfully
added.  
(Унаследован от [HashSet<TKey,
TValue>](T_Tessa_Platform_Collections_HashSet_2.htm))  
---|---  
[Clear](M_Tessa_Platform_Collections_HashSet_2_Clear.htm)| Removes all items
from the
[ICollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1).  
(Унаследован от [HashSet<TKey,
TValue>](T_Tessa_Platform_Collections_HashSet_2.htm))  
[Contains](M_Tessa_Platform_Collections_HashSet_2_Contains.htm)| Determines
whether the
[ICollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)
contains a specific value.  
(Унаследован от [HashSet<TKey,
TValue>](T_Tessa_Platform_Collections_HashSet_2.htm))  
[ContainsKey](M_Tessa_Platform_Collections_HashSet_2_ContainsKey.htm)|
Проверить, содержится ли в коллекции элемент с заданным ключом.  
(Унаследован от [HashSet<TKey,
TValue>](T_Tessa_Platform_Collections_HashSet_2.htm))  
[CopyTo](M_Tessa_Platform_Collections_HashSet_2_CopyTo.htm)| Copies the
elements of the
[ICollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)
to an [Array](https://learn.microsoft.com/dotnet/api/system.array), starting
at a particular [Array](https://learn.microsoft.com/dotnet/api/system.array)
index.  
(Унаследован от [HashSet<TKey,
TValue>](T_Tessa_Platform_Collections_HashSet_2.htm))  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ExceptWith](M_Tessa_Platform_Collections_HashSet_2_ExceptWith.htm)| Removes
all elements in the specified collection from the current set.  
(Унаследован от [HashSet<TKey,
TValue>](T_Tessa_Platform_Collections_HashSet_2.htm))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetEnumerator](M_Tessa_Platform_Collections_HashSet_2_GetEnumerator.htm)|
Получить энумератор для коллекции.  
(Унаследован от [HashSet<TKey,
TValue>](T_Tessa_Platform_Collections_HashSet_2.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetPairs](M_Tessa_Platform_Collections_HashSet_2_GetPairs.htm)|  Вернуть
коллекцию [KeyValuePair<TKey,
TValue>](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2)
содержащихся в сете элементов.  
(Унаследован от [HashSet<TKey,
TValue>](T_Tessa_Platform_Collections_HashSet_2.htm))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[IntersectWith](M_Tessa_Platform_Collections_HashSet_2_IntersectWith.htm)|
Modifies the current set so that it contains only elements that are also in a
specified collection.  
(Унаследован от [HashSet<TKey,
TValue>](T_Tessa_Platform_Collections_HashSet_2.htm))  
[IsProperSubsetOf](M_Tessa_Platform_Collections_HashSet_2_IsProperSubsetOf.htm)|
Determines whether the current set is a proper (strict) subset of a specified
collection.  
(Унаследован от [HashSet<TKey,
TValue>](T_Tessa_Platform_Collections_HashSet_2.htm))  
[IsProperSupersetOf](M_Tessa_Platform_Collections_HashSet_2_IsProperSupersetOf.htm)|
Determines whether the current set is a proper (strict) superset of a
specified collection.  
(Унаследован от [HashSet<TKey,
TValue>](T_Tessa_Platform_Collections_HashSet_2.htm))  
[IsSubsetOf](M_Tessa_Platform_Collections_HashSet_2_IsSubsetOf.htm)|
Determines whether a set is a subset of a specified collection.  
(Унаследован от [HashSet<TKey,
TValue>](T_Tessa_Platform_Collections_HashSet_2.htm))  
[IsSupersetOf](M_Tessa_Platform_Collections_HashSet_2_IsSupersetOf.htm)|
Determines whether the current set is a superset of a specified collection.  
(Унаследован от [HashSet<TKey,
TValue>](T_Tessa_Platform_Collections_HashSet_2.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Overlaps](M_Tessa_Platform_Collections_HashSet_2_Overlaps.htm)| Determines
whether the current set overlaps with the specified collection.  
(Унаследован от [HashSet<TKey,
TValue>](T_Tessa_Platform_Collections_HashSet_2.htm))  
[Remove](M_Tessa_Platform_Collections_HashSet_2_Remove.htm)| Removes the first
occurrence of a specific object from the
[ICollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1).  
(Унаследован от [HashSet<TKey,
TValue>](T_Tessa_Platform_Collections_HashSet_2.htm))  
[RemoveByKey](M_Tessa_Platform_Collections_HashSet_2_RemoveByKey.htm)|
Удалить элемент с заданным ключом из коллекции.  
(Унаследован от [HashSet<TKey,
TValue>](T_Tessa_Platform_Collections_HashSet_2.htm))  
[Replace](M_Tessa_Platform_Collections_HashSet_2_Replace.htm)|  Заменить
элемент в коллекции.  
(Унаследован от [HashSet<TKey,
TValue>](T_Tessa_Platform_Collections_HashSet_2.htm))  
[SetEquals](M_Tessa_Platform_Collections_HashSet_2_SetEquals.htm)| Determines
whether the current set and the specified collection contain the same
elements.  
(Унаследован от [HashSet<TKey,
TValue>](T_Tessa_Platform_Collections_HashSet_2.htm))  
[SymmetricExceptWith](M_Tessa_Platform_Collections_HashSet_2_SymmetricExceptWith.htm)|
Modifies the current set so that it contains only elements that are present
either in the current set or in the specified collection, but not both.  
(Унаследован от [HashSet<TKey,
TValue>](T_Tessa_Platform_Collections_HashSet_2.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetItem](M_Tessa_Platform_Collections_HashSet_2_TryGetItem.htm)|
Попробовать получить элемент по заданному ключу.  
(Унаследован от [HashSet<TKey,
TValue>](T_Tessa_Platform_Collections_HashSet_2.htm))  
[UnionWith](M_Tessa_Platform_Collections_HashSet_2_UnionWith.htm)| Modifies
the current set so that it contains all elements that are present in the
current set, in the specified collection, or in both.  
(Унаследован от [HashSet<TKey,
TValue>](T_Tessa_Platform_Collections_HashSet_2.htm))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Localization - пространство имён](N_Tessa_Localization.htm)
