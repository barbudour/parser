# LookupContainer<TKey, TValue> \- класс
Контейнер для значений, доступных по неуникальным ключам.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Collections](N_Tessa_Platform_Collections.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class LookupContainer<TKey, TValue> : ILookupContainer<TKey, TValue>
    where TValue : class
VB __Копировать
     Public NotInheritable Class LookupContainer(Of TKey, TValue As Class)
    	Implements ILookupContainer(Of TKey, TValue)
C++ __Копировать
    generic<typename TKey, typename TValue>
    where TValue : ref class
    public ref class LookupContainer sealed : ILookupContainer<TKey, TValue>
F# __Копировать
     [<SealedAttribute>]
    type LookupContainer<'TKey, 'TValue when 'TValue : not struct> = 
        class
            interface ILookupContainer<'TKey, 'TValue>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ LookupContainer<TKey, TValue>
Implements
    [ILookupContainer](T_Tessa_Platform_Collections_ILookupContainer_2.htm)<TKey, TValue>
#### Параметры типа
TKey
    Тип ключа, по которому могут быть найдены значения.
TValue
    Ссылочный тип значения.
##  __Конструкторы
[LookupContainer<TKey,
TValue>()](M_Tessa_Platform_Collections_LookupContainer_2__ctor.htm)| Создаёт
экземпляр класса с параметрами по умолчанию.  
---|---  
[LookupContainer<TKey,
TValue>(Int32)](M_Tessa_Platform_Collections_LookupContainer_2__ctor_1.htm)|
Создаёт экземпляр класса с указанием вместимости объекта по количеству ключей.  
## __Свойства
[Item](P_Tessa_Platform_Collections_LookupContainer_2_Item.htm)|  Получает или
задаёт одно из значений, доступных по заданному ключу, которое гарантированно
не равно null. Получение значения при отсутствии таких значений выбрасывает
исключение
[KeyNotFoundException](https://learn.microsoft.com/dotnet/api/system.collections.generic.keynotfoundexception).
Присваивание значения переопределяет все доступные значения.  
---|---  
## __Методы
[Add](M_Tessa_Platform_Collections_LookupContainer_2_Add.htm)|  Добавляет
значение по заданному ключу. Для одного и того же ключа может быть добавлено
множество значений.  
---|---  
[Clear](M_Tessa_Platform_Collections_LookupContainer_2_Clear.htm)|  Удаляет
все доступные значения.  
[Contains](M_Tessa_Platform_Collections_LookupContainer_2_Contains.htm)|
Возвращает признак того, что контейнер содержит хотя бы одно значение по
заданному ключу.  
[ContainsValue](M_Tessa_Platform_Collections_LookupContainer_2_ContainsValue.htm)|
Возвращает признак того, что контейнер содержит значение value по указанному
ключу key.  
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
[GetAll](M_Tessa_Platform_Collections_LookupContainer_2_GetAll.htm)|
Возвращает все значения, доступные по заданному ключу. Если таких значений
нет, то возвращается пустая коллекция.  
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
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Remove](M_Tessa_Platform_Collections_LookupContainer_2_Remove.htm)|  Удаляет
одно из значений, содержащихся в контейнере по заданному ключу. Возвращает
признак того, что одно из значений было удалено.  
[RemoveAll](M_Tessa_Platform_Collections_LookupContainer_2_RemoveAll.htm)|
Удаляет все значения, содержащиеся в контейнере по заданному ключу. Возвращает
признак того, что хотя бы одно из значений было удалено.  
[RemoveValue](M_Tessa_Platform_Collections_LookupContainer_2_RemoveValue.htm)|
Удаляет заданное значение value по указанное ключу key. Возвращает признак
того, что заданное значение было найдено и удалено.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGet](M_Tessa_Platform_Collections_LookupContainer_2_TryGet.htm)|
Возвращает одно из значений по заданному ключу или null, если контейнер не
содержит значений.  
## __Методы расширения
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
