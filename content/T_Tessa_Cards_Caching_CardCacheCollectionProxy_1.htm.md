# CardCacheCollectionProxy<T> \- класс
Прокси для потокобезопасной коллекции объектов для карточек, кэшируемых по
строковому ключу и создаваемых единым способом для всех объектов.
## __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardCacheCollectionProxy<T> : ICardCacheCollection<T>
    where T : class
VB __Копировать
     Public NotInheritable Class CardCacheCollectionProxy(Of T As Class)
    	Implements ICardCacheCollection(Of T)
C++ __Копировать
    generic<typename T>
    where T : ref class
    public ref class CardCacheCollectionProxy sealed : ICardCacheCollection<T>
F# __Копировать
     [<SealedAttribute>]
    type CardCacheCollectionProxy<'T when 'T : not struct> = 
        class
            interface ICardCacheCollection<'T>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardCacheCollectionProxy<T>
Implements
    [ICardCacheCollection](T_Tessa_Cards_Caching_ICardCacheCollection_1.htm)<T>
#### Параметры типа
T
    Тип кэшируемого объекта.
##  __Заметки
Объект используется для сброса глобального кэша при сбросе локального.
## __Конструкторы
[CardCacheCollectionProxy<T>](M_Tessa_Cards_Caching_CardCacheCollectionProxy_1__ctor.htm)|
Создаёт экземпляр класса с указанием декорируемого объекта и методов,
выполняемых при очистке кэша вызовом методов интерфейса
[ICardCacheCollection<T>](T_Tessa_Cards_Caching_ICardCacheCollection_1.htm).  
---|---  
## __Методы
[ContainsAsync](M_Tessa_Cards_Caching_CardCacheCollectionProxy_1_ContainsAsync.htm)|
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
[GetAsync](M_Tessa_Cards_Caching_CardCacheCollectionProxy_1_GetAsync.htm)|
Возвращает значение из кэша по заданному ключу, при этом выполняется создание
значения при его отсутствии в кэше. Например, выполняется загрузка карточки из
базы данных или от сервера, если она отсутствовала в кэше.  
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
[InvalidateAsync(CancellationToken)](M_Tessa_Cards_Caching_CardCacheCollectionProxy_1_InvalidateAsync_1.htm)|
Очищает кэш, при этом удаляются все значения.  
[InvalidateAsync(String,
CancellationToken)](M_Tessa_Cards_Caching_CardCacheCollectionProxy_1_InvalidateAsync.htm)|
Выполняет удаление значения из кэша по заданному ключу.  
[InvalidateSourceAsync(CancellationToken)](M_Tessa_Cards_Caching_CardCacheCollectionProxy_1_InvalidateSourceAsync_1.htm)|
Очищает кэш, при этом удаляются все значения.  
[InvalidateSourceAsync(String,
CancellationToken)](M_Tessa_Cards_Caching_CardCacheCollectionProxy_1_InvalidateSourceAsync.htm)|
Выполняет удаление значения из кэша по заданному ключу.  
[IsAllowedAsync](M_Tessa_Cards_Caching_CardCacheCollectionProxy_1_IsAllowedAsync.htm)|
Возвращает признак того, что заданный ключ допустим для кэша.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryAddAsync](M_Tessa_Cards_Caching_CardCacheCollectionProxy_1_TryAddAsync.htm)|
Добавляет значение в кэш по заданному ключу, если значение отсутствовало в
кэше. Возвращает признак того, что значение было успешно добавлено.  
[TryGetAlreadyCachedAsync](M_Tessa_Cards_Caching_CardCacheCollectionProxy_1_TryGetAlreadyCachedAsync.htm)|
Возвращает значение из кэша по заданному ключу или null, если значение
отсутствует в кэше. Значение может отсутствовать, если оно ещё не было
загружено, например, если карточка с указанным именем не была загружена из
базы данных или от сервера. Используйте индексатор коллекции, если требуется
загрузить значение, когда оно недоступно, например: await
cardCache.Cards.GetAsync("CardTypeName").  
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
