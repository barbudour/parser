# CardCacheCollectionBase<T> \- класс
Базовый класс для потокобезопасной коллекции объектов для карточек, кэшируемых
по строковому ключу.
## __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class CardCacheCollectionBase<T>
    where T : class
VB __Копировать
     Public MustInherit Class CardCacheCollectionBase(Of T As Class)
C++ __Копировать
    generic<typename T>
    where T : ref class
    public ref class CardCacheCollectionBase abstract
F# __Копировать
     [<AbstractClassAttribute>]
    type CardCacheCollectionBase<'T when 'T : not struct> = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardCacheCollectionBase<T>
Derived
[Tessa.Cards.Caching.CardCacheCollection<T>](T_Tessa_Cards_Caching_CardCacheCollection_1.htm)
[Tessa.Cards.Caching.CardCacheSettings](T_Tessa_Cards_Caching_CardCacheSettings.htm)
#### Параметры типа
T
    Тип кэшируемого значения.
##  __Конструкторы
[CardCacheCollectionBase<T>](M_Tessa_Cards_Caching_CardCacheCollectionBase_1__ctor.htm)|
Инициализирует новый экземпляр класса CardCacheCollectionBase<T>  
---|---  
##  __Методы
[ContainsAsync](M_Tessa_Cards_Caching_CardCacheCollectionBase_1_ContainsAsync.htm)|
Возвращает признак того, что значение доступно в кэше по заданному ключу.  
---|---  
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
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetOrAdd](M_Tessa_Cards_Caching_CardCacheCollectionBase_1_GetOrAdd.htm)|
Возвращает значение из кэша, или добавляет значение в кэш, возвращённое
заданной функцией при отсутствии там значения.  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[InvalidateAsync(CancellationToken)](M_Tessa_Cards_Caching_CardCacheCollectionBase_1_InvalidateAsync_1.htm)|
Очищает кэш, при этом удаляются все значения.  
[InvalidateAsync(String,
CancellationToken)](M_Tessa_Cards_Caching_CardCacheCollectionBase_1_InvalidateAsync.htm)|
Выполняет удаление значения из кэша по заданному ключу.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryAddAsync](M_Tessa_Cards_Caching_CardCacheCollectionBase_1_TryAddAsync.htm)|
Добавляет значение в кэш по заданному ключу, если значение отсутствовало в
кэше. Возвращает признак того, что значение было успешно добавлено.  
[TryGetAlreadyCachedAsync](M_Tessa_Cards_Caching_CardCacheCollectionBase_1_TryGetAlreadyCachedAsync.htm)|
Возвращает значение из кэша по заданному ключу или null, если значение
отсутствует в кэше. Значение может отсутствовать, если оно ещё не было
загружено, например, если карточка с указанным именем не была загружена из
базы данных или от сервера. Используйте индексатор коллекции, если требуется
загрузить значение, когда оно недоступно, например: await
cardCache.Cards.GetAsync("CardTypeName").  
[TryGetValue](M_Tessa_Cards_Caching_CardCacheCollectionBase_1_TryGetValue.htm)|
Возвращает значение из кэша value, если оно присутствует, или false, если
значения нет в кэше.  
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
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)
