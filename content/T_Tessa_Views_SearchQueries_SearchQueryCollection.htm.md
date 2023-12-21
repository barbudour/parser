# SearchQueryCollection - класс
Коллекция содержащая список поисковых запросов
## __Definition
 **Пространство имён:**
[Tessa.Views.SearchQueries](N_Tessa_Views_SearchQueries.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    [CollectionDataContractAttribute]
    public class SearchQueryCollection : SealableObjectList<ISearchQueryMetadata>, 
    	ICloneable
VB __Копировать
    <SerializableAttribute>
    <CollectionDataContractAttribute>
    Public Class SearchQueryCollection
    	Inherits SealableObjectList(Of ISearchQueryMetadata)
    	Implements ICloneable
C++ __Копировать
    [SerializableAttribute]
    [CollectionDataContractAttribute]
    public ref class SearchQueryCollection : public SealableObjectList<ISearchQueryMetadata^>, 
    	ICloneable
F# __Копировать
     [<SerializableAttribute>]
    [<CollectionDataContractAttribute>]
    type SearchQueryCollection = 
        class
            inherit SealableObjectList<ISearchQueryMetadata>
            interface ICloneable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[SealableList](T_Tessa_Platform_Collections_SealableList_1.htm)<[ISearchQueryMetadata](T_Tessa_Views_SearchQueries_ISearchQueryMetadata.htm)> __[SealableObjectList](T_Tessa_Platform_Collections_SealableObjectList_1.htm)<[ISearchQueryMetadata](T_Tessa_Views_SearchQueries_ISearchQueryMetadata.htm)> __ SearchQueryCollection
Implements
    [ICloneable](https://learn.microsoft.com/dotnet/api/system.icloneable)
##  __Конструкторы
[SearchQueryCollection()](M_Tessa_Views_SearchQueries_SearchQueryCollection__ctor.htm)|
Создаёт экземпляр класса с параметрами по умолчанию.  
---|---  
[SearchQueryCollection(IEnumerable<ISearchQueryMetadata>)](M_Tessa_Views_SearchQueries_SearchQueryCollection__ctor_1.htm)|
Инициализирует новый экземпляр класса SearchQueryCollection  
[SearchQueryCollection(Int32)](M_Tessa_Views_SearchQueries_SearchQueryCollection__ctor_2.htm)|
Создаёт экземпляр класса с указанием начальной вместимости списка.  
##  __Свойства
[Count](P_Tessa_Platform_Collections_SealableList_1_Count.htm)| Количество
элементов в коллекции.  
(Унаследован от
[SealableList<T>](T_Tessa_Platform_Collections_SealableList_1.htm))  
---|---  
[IsSealed](P_Tessa_Platform_Collections_SealableList_1_IsSealed.htm)| Признак
того, что объект был защищён от изменений.  
(Унаследован от
[SealableList<T>](T_Tessa_Platform_Collections_SealableList_1.htm))  
[Item](P_Tessa_Platform_Collections_SealableList_1_Item.htm)| Получает или
задаёт элемент по отсчитываемому от нуля индексу.  
(Унаследован от
[SealableList<T>](T_Tessa_Platform_Collections_SealableList_1.htm))  
##  __Методы
[Add](M_Tessa_Platform_Collections_SealableList_1_Add.htm)| Добавляет заданный
элемент в коллекцию.  
(Унаследован от
[SealableList<T>](T_Tessa_Platform_Collections_SealableList_1.htm))  
---|---  
[AddInternal](M_Tessa_Platform_Collections_SealableObjectList_1_AddInternal.htm)|
Добавляет заданный элемент в коллекцию без проверки на защиту объекта от
изменений.
Метод может быть переопределён в классах-наследниках.
(Унаследован от
[SealableObjectList<T>](T_Tessa_Platform_Collections_SealableObjectList_1.htm))  
[CheckSealed](M_Tessa_Platform_Collections_SealableList_1_CheckSealed.htm)|
Выбрасывает исключение [Tessa.Platform.ObjectSealedException], если объект был
защищён от изменений.  
(Унаследован от
[SealableList<T>](T_Tessa_Platform_Collections_SealableList_1.htm))  
[Clear](M_Tessa_Platform_Collections_SealableList_1_Clear.htm)| Удаляет все
элементы коллекции.  
(Унаследован от
[SealableList<T>](T_Tessa_Platform_Collections_SealableList_1.htm))  
[ClearInternal](M_Tessa_Platform_Collections_SealableList_1_ClearInternal.htm)|
Удаляет все элементы из коллекции без проверки на защиту объекта от изменений.
Метод может быть переопределён в классах-наследниках.
(Унаследован от
[SealableList<T>](T_Tessa_Platform_Collections_SealableList_1.htm))  
[Clone](M_Tessa_Views_SearchQueries_SearchQueryCollection_Clone.htm)| Creates
a new object that is a copy of the current instance.  
[Contains](M_Tessa_Platform_Collections_SealableList_1_Contains.htm)|
Возвращает признак того, что заданный элемент содержится в коллекции.  
(Унаследован от
[SealableList<T>](T_Tessa_Platform_Collections_SealableList_1.htm))  
[CopyTo](M_Tessa_Platform_Collections_SealableList_1_CopyTo.htm)| Копирует
элементы коллекции в массив, начиная с заданного отсчитываемого от нуля
индекса.  
(Унаследован от
[SealableList<T>](T_Tessa_Platform_Collections_SealableList_1.htm))  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetEnumerator](M_Tessa_Platform_Collections_SealableList_1_GetEnumerator.htm)|
Возвращает итератор по элементам коллекции.  
(Унаследован от
[SealableList<T>](T_Tessa_Platform_Collections_SealableList_1.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[IndexOf](M_Tessa_Platform_Collections_SealableList_1_IndexOf.htm)| Возвращает
отсчитываемый от нуля индекс заданного элемента в коллекции.  
(Унаследован от
[SealableList<T>](T_Tessa_Platform_Collections_SealableList_1.htm))  
[Insert](M_Tessa_Platform_Collections_SealableList_1_Insert.htm)| Вставляет
элемент в заданную позицию.  
(Унаследован от
[SealableList<T>](T_Tessa_Platform_Collections_SealableList_1.htm))  
[InsertInternal](M_Tessa_Platform_Collections_SealableObjectList_1_InsertInternal.htm)|
Вставляет элемент в заданную позицию без проверки на защиту объекта от
изменений.
Метод может быть переопределён в классах-наследниках.
(Унаследован от
[SealableObjectList<T>](T_Tessa_Platform_Collections_SealableObjectList_1.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Remove](M_Tessa_Platform_Collections_SealableList_1_Remove.htm)| Удаляет
заданный элемент из коллекции.  
(Унаследован от
[SealableList<T>](T_Tessa_Platform_Collections_SealableList_1.htm))  
[RemoveAt](M_Tessa_Platform_Collections_SealableList_1_RemoveAt.htm)| Удаляет
элемент в заданной позиции.  
(Унаследован от
[SealableList<T>](T_Tessa_Platform_Collections_SealableList_1.htm))  
[RemoveAtInternal](M_Tessa_Platform_Collections_SealableList_1_RemoveAtInternal.htm)|
Удаляет элемент в заданной позиции без проверки на защиту объекта от
изменений.  
(Унаследован от
[SealableList<T>](T_Tessa_Platform_Collections_SealableList_1.htm))  
[RemoveInternal](M_Tessa_Platform_Collections_SealableObjectList_1_RemoveInternal.htm)|
Удаляет заданный элемент из коллекции без проверки на защиту объекта от
изменений.
Метод может быть переопределён в классах-наследниках.
(Унаследован от
[SealableObjectList<T>](T_Tessa_Platform_Collections_SealableObjectList_1.htm))  
[Seal](M_Tessa_Platform_Collections_SealableList_1_Seal.htm)| Защищает объект
от изменений.  
(Унаследован от
[SealableList<T>](T_Tessa_Platform_Collections_SealableList_1.htm))  
[SealInternal](M_Tessa_Platform_Collections_SealableObjectList_1_SealInternal.htm)|
Защищает объект от изменений.
Метод может быть переопределён в классах-наследниках.
(Унаследован от
[SealableObjectList<T>](T_Tessa_Platform_Collections_SealableObjectList_1.htm))  
[SetInternal](M_Tessa_Platform_Collections_SealableObjectList_1_SetInternal.htm)|
Устанавливает элемент по отсчитываемому от нуля индексу без проверки на защиту
объекта от изменений.
Метод может быть переопределён в классах-наследниках.
(Унаследован от
[SealableObjectList<T>](T_Tessa_Platform_Collections_SealableObjectList_1.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __События
[CollectionChanged](E_Tessa_Platform_Collections_SealableList_1_CollectionChanged.htm)|
Событие, уведомляющее об изменении коллекции у модели представления.  
(Унаследован от
[SealableList<T>](T_Tessa_Platform_Collections_SealableList_1.htm))  
---|---  
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
[Tessa.Views.SearchQueries - пространство
имён](N_Tessa_Views_SearchQueries.htm)
