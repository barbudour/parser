# CardCacheSettingsProxy - класс
Прокси для потокобезопасной коллекции определяемых пользователем настроек,
содержащихся в кэше карточек и доступных по строковому ключу.
## __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardCacheSettingsProxy : ICardCacheSettings
VB __Копировать
     Public NotInheritable Class CardCacheSettingsProxy
    	Implements ICardCacheSettings
C++ __Копировать
     public ref class CardCacheSettingsProxy sealed : ICardCacheSettings
F# __Копировать
     [<SealedAttribute>]
    type CardCacheSettingsProxy = 
        class
            interface ICardCacheSettings
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardCacheSettingsProxy
Implements
    [ICardCacheSettings](T_Tessa_Cards_Caching_ICardCacheSettings.htm)
##  __Заметки
Объект используется для сброса глобального кэша при сбросе локального.
## __Конструкторы
[CardCacheSettingsProxy](M_Tessa_Cards_Caching_CardCacheSettingsProxy__ctor.htm)|
Создаёт экземпляр класса с указанием декорируемого объекта и методов,
выполняемых при очистке кэша вызовом методов интерфейса
[ICardCacheSettings](T_Tessa_Cards_Caching_ICardCacheSettings.htm).  
---|---  
## __Методы
[ContainsAsync](M_Tessa_Cards_Caching_CardCacheSettingsProxy_ContainsAsync.htm)|
Возвращает признак того, что настройка доступна в кэше по заданному ключу.  
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
CancellationToken)](M_Tessa_Cards_Caching_CardCacheSettingsProxy_GetAsync__1.htm)|
Возвращает настройку из кэша, или добавляет настройку в кэш, возвращённую
заданной функцией при отсутствии там настройки.  
[GetAsync<T>(String, Func<String, CancellationToken, Task<T>>,
CancellationToken)](M_Tessa_Cards_Caching_CardCacheSettingsProxy_GetAsync__1_1.htm)|
Возвращает настройку из кэша, или добавляет настройку в кэш, возвращённую
заданной функцией при отсутствии там настройки.  
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
[InvalidateAsync(CancellationToken)](M_Tessa_Cards_Caching_CardCacheSettingsProxy_InvalidateAsync_1.htm)|
Очищает кэш, при этом удаляются все настройки.  
[InvalidateAsync(String,
CancellationToken)](M_Tessa_Cards_Caching_CardCacheSettingsProxy_InvalidateAsync.htm)|
Выполняет удаление настройки из кэша по заданному ключу.  
[InvalidateSourceAsync(CancellationToken)](M_Tessa_Cards_Caching_CardCacheSettingsProxy_InvalidateSourceAsync_1.htm)|
Очищает кэш, при этом удаляются все настройки.  
[InvalidateSourceAsync(String,
CancellationToken)](M_Tessa_Cards_Caching_CardCacheSettingsProxy_InvalidateSourceAsync.htm)|
Выполняет удаление настройки из кэша по заданному ключу.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetAlreadyCachedAsync<T>](M_Tessa_Cards_Caching_CardCacheSettingsProxy_TryGetAlreadyCachedAsync__1.htm)|
Возвращает настройку из кэша по заданному ключу или null, если настройка
отсутствует в кэше.  
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
