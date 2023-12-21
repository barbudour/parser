# SealableObjectList<T> \- класс
Список, поддерживающий защиту от изменений как для себя, так и для
содержащихся в нём объектов. Не может содержать ссылки null. При удалении
элементов производит удаление только по точному совпадению ссылок удаляемых
элементов.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Collections](N_Tessa_Platform_Collections.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public class SealableObjectList<T> : SealableList<T>
    where T : class, ISealable
VB __Копировать
    <SerializableAttribute>
    Public Class SealableObjectList(Of T As {Class, ISealable})
    	Inherits SealableList(Of T)
C++ __Копировать
    [SerializableAttribute]
    generic<typename T>
    where T : ref class, ISealable
    public ref class SealableObjectList : public SealableList<T>
F# __Копировать
     [<SerializableAttribute>]
    type SealableObjectList<'T when 'T : not struct and ISealable> = 
        class
            inherit SealableList<'T>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[SealableList](T_Tessa_Platform_Collections_SealableList_1.htm)<T> __ SealableObjectList<T>
Derived
[Tessa.Views.SearchQueries.SearchQueryCollection](T_Tessa_Views_SearchQueries_SearchQueryCollection.htm)
#### Параметры типа
T
     Ссылочный тип элементов списка. Должен реализовывать интерфейс [ISealable](T_Tessa_Platform_ISealable.htm). 
## __Конструкторы
[SealableObjectList<T>()](M_Tessa_Platform_Collections_SealableObjectList_1__ctor.htm)|
Создаёт экземпляр класса с параметрами по умолчанию.  
---|---  
[SealableObjectList<T>(Boolean)](M_Tessa_Platform_Collections_SealableObjectList_1__ctor_1.htm)|
Создаёт экземпляр класса с указанием признака того, что объект должен быть
защищён от изменений.  
[SealableObjectList<T>(IEnumerable<T>)](M_Tessa_Platform_Collections_SealableObjectList_1__ctor_2.htm)|
Создаёт экземпляр класса с указанием коллекции элементов, используемой для
инициализации списка.  
[SealableObjectList<T>(Int32)](M_Tessa_Platform_Collections_SealableObjectList_1__ctor_4.htm)|
Создаёт экземпляр класса с указанием начальной вместимости списка.  
[SealableObjectList<T>(IEnumerable<T>,
Boolean)](M_Tessa_Platform_Collections_SealableObjectList_1__ctor_3.htm)|
Создаёт экземпляр класса с указанием коллекции элементов, используемой для
инициализации списка, и признака того, что объект должен быть защищён от
изменений.  
## __Свойства
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
(Переопределяет
[SealableList<T>.AddInternal(T)](M_Tessa_Platform_Collections_SealableList_1_AddInternal.htm))  
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
(Переопределяет [SealableList<T>.InsertInternal(Int32,
T)](M_Tessa_Platform_Collections_SealableList_1_InsertInternal.htm))  
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
(Переопределяет [SealableList<T>.RemoveInternal(T,
Int32)](M_Tessa_Platform_Collections_SealableList_1_RemoveInternal.htm))  
[Seal](M_Tessa_Platform_Collections_SealableList_1_Seal.htm)| Защищает объект
от изменений.  
(Унаследован от
[SealableList<T>](T_Tessa_Platform_Collections_SealableList_1.htm))  
[SealInternal](M_Tessa_Platform_Collections_SealableObjectList_1_SealInternal.htm)|
Защищает объект от изменений.
Метод может быть переопределён в классах-наследниках.
(Переопределяет
[SealableList<T>.SealInternal()](M_Tessa_Platform_Collections_SealableList_1_SealInternal.htm))  
[SetInternal](M_Tessa_Platform_Collections_SealableObjectList_1_SetInternal.htm)|
Устанавливает элемент по отсчитываемому от нуля индексу без проверки на защиту
объекта от изменений.
Метод может быть переопределён в классах-наследниках.
(Переопределяет [SealableList<T>.SetInternal(Int32,
T)](M_Tessa_Platform_Collections_SealableList_1_SetInternal.htm))  
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
[Tessa.Platform.Collections - пространство
имён](N_Tessa_Platform_Collections.htm)
