# CardCacheSettings - класс
Потокобезопасная коллекция определяемых пользователем настроек, содержащихся в
кэше карточек и доступных по строковому ключу.
## __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardCacheSettings : CardCacheCollectionBase<Object>, 
    	ICardCacheSettings
VB __Копировать
     Public NotInheritable Class CardCacheSettings
    	Inherits CardCacheCollectionBase(Of Object)
    	Implements ICardCacheSettings
C++ __Копировать
     public ref class CardCacheSettings sealed : public CardCacheCollectionBase<Object^>, 
    	ICardCacheSettings
F# __Копировать
     [<SealedAttribute>]
    type CardCacheSettings = 
        class
            inherit CardCacheCollectionBase<Object>
            interface ICardCacheSettings
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[CardCacheCollectionBase](T_Tessa_Cards_Caching_CardCacheCollectionBase_1.htm)<[Object](https://learn.microsoft.com/dotnet/api/system.object)> __ CardCacheSettings
Implements
    [ICardCacheSettings](T_Tessa_Cards_Caching_ICardCacheSettings.htm)
##  __Конструкторы
[CardCacheSettings](M_Tessa_Cards_Caching_CardCacheSettings__ctor.htm)|
Инициализирует новый экземпляр класса CardCacheSettings  
---|---  
##  __Методы
[ContainsAsync](M_Tessa_Cards_Caching_CardCacheCollectionBase_1_ContainsAsync.htm)|
Возвращает признак того, что значение доступно в кэше по заданному ключу.  
(Унаследован от
[CardCacheCollectionBase<T>](T_Tessa_Cards_Caching_CardCacheCollectionBase_1.htm))  
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
[GetAsync<T>(String, Func<String, T>,
CancellationToken)](M_Tessa_Cards_Caching_CardCacheSettings_GetAsync__1.htm)|
Возвращает настройку из кэша, или добавляет настройку в кэш, возвращённую
заданной функцией при отсутствии там настройки.  
[GetAsync<T>(String, Func<String, CancellationToken, Task<T>>,
CancellationToken)](M_Tessa_Cards_Caching_CardCacheSettings_GetAsync__1_1.htm)|
Возвращает настройку из кэша, или добавляет настройку в кэш, возвращённую
заданной функцией при отсутствии там настройки.  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetOrAdd](M_Tessa_Cards_Caching_CardCacheCollectionBase_1_GetOrAdd.htm)|
Возвращает значение из кэша, или добавляет значение в кэш, возвращённое
заданной функцией при отсутствии там значения.  
(Унаследован от
[CardCacheCollectionBase<T>](T_Tessa_Cards_Caching_CardCacheCollectionBase_1.htm))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[InvalidateAsync(CancellationToken)](M_Tessa_Cards_Caching_CardCacheCollectionBase_1_InvalidateAsync_1.htm)|
Очищает кэш, при этом удаляются все значения.  
(Унаследован от
[CardCacheCollectionBase<T>](T_Tessa_Cards_Caching_CardCacheCollectionBase_1.htm))  
[InvalidateAsync(String,
CancellationToken)](M_Tessa_Cards_Caching_CardCacheCollectionBase_1_InvalidateAsync.htm)|
Выполняет удаление значения из кэша по заданному ключу.  
(Унаследован от
[CardCacheCollectionBase<T>](T_Tessa_Cards_Caching_CardCacheCollectionBase_1.htm))  
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
(Унаследован от
[CardCacheCollectionBase<T>](T_Tessa_Cards_Caching_CardCacheCollectionBase_1.htm))  
[TryGetAlreadyCachedAsync<T>](M_Tessa_Cards_Caching_CardCacheSettings_TryGetAlreadyCachedAsync__1.htm)|
Возвращает настройку из кэша по заданному ключу или null, если настройка
отсутствует в кэше.  
[TryGetValue](M_Tessa_Cards_Caching_CardCacheCollectionBase_1_TryGetValue.htm)|
Возвращает значение из кэша value, если оно присутствует, или false, если
значения нет в кэше.  
(Унаследован от
[CardCacheCollectionBase<T>](T_Tessa_Cards_Caching_CardCacheCollectionBase_1.htm))  
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
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)
