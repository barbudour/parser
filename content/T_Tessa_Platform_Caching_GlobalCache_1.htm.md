# GlobalCache<TEventArgs> \- класс
Потокобезопасный кэш, обеспечивающий синхронный сброс кэша всех экземпляров с
заданным именем независимо от того, располагаются ли такие экземпляры в том же
приложении или в другом процессе.
## __Definition
 **Пространство имён:** [Tessa.Platform.Caching](N_Tessa_Platform_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class GlobalCache<TEventArgs> : IAsyncDisposable
    where TEventArgs : class, new(), ISharedEventArgs
VB __Копировать
     Public MustInherit Class GlobalCache(Of TEventArgs As {Class, New, ISharedEventArgs})
    	Implements IAsyncDisposable
C++ __Копировать
    generic<typename TEventArgs>
    where TEventArgs : ref class, gcnew(), ISharedEventArgs
    public ref class GlobalCache abstract : IAsyncDisposable
F# __Копировать
     [<AbstractClassAttribute>]
    type GlobalCache<'TEventArgs when 'TEventArgs : not struct, new() and ISharedEventArgs> = 
        class
            interface IAsyncDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ GlobalCache<TEventArgs>
Derived
[Tessa.Cards.Caching.CardGlobalCache](T_Tessa_Cards_Caching_CardGlobalCache.htm)
[Tessa.Cards.Metadata.CardMetadataCache](T_Tessa_Cards_Metadata_CardMetadataCache.htm)
[Tessa.Localization.LocalizationCache](T_Tessa_Localization_LocalizationCache.htm)
[Tessa.Scheme.SchemeDatabaseCache](T_Tessa_Scheme_SchemeDatabaseCache.htm)
[Tessa.Views.ViewAccessCache](T_Tessa_Views_ViewAccessCache.htm)
[Tessa.Views.ViewsCache](T_Tessa_Views_ViewsCache.htm)
[Tessa.Views.Workplaces.WorkplacesCache](T_Tessa_Views_Workplaces_WorkplacesCache.htm)
Подробнее __Less __
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable)
#### Параметры типа
TEventArgs
     Аргументы события, сериализуемые между процессами. Тип должен реализовывать интерфейс [ISharedEventArgs](T_Tessa_Platform_IPC_ISharedEventArgs.htm). 
## __Заметки
Доступ на чтение из кэша и наполнение кэша осуществляет только синхронизацию
между потоками для доступа к экземпляру, поэтому чтение может осуществляться
сравнительно часто небольшими порциями.
Доступ к локальному кэшу экземпляра для его наполнения, сброса и чтения данных
потокобезопасен и не требует дополнительной синхронизации.
Доступ и наполнение локального кэша возможно даже после освобождения объекта
вызовом
[DisposeAsync()](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable.disposeasync#system-
iasyncdisposable-disposeasync), но после такого вызова все глобальные объекты
синхронизации освобождаются и более не используются.
##  __Конструкторы
[GlobalCache<TEventArgs>(String, IGlobalCacheLock,
ISharedEventSubscriberFactory,
Boolean)](M_Tessa_Platform_Caching_GlobalCache_1__ctor_2.htm)|  Создаёт
экземпляр класса с указанием имени, являющегося глобально уникальным для
экземпляров кэша, расположенных в различных процессах. Это рекомендуемый
конструктор для создания базовых объектов глобального кэша.  
---|---  
[GlobalCache<TEventArgs>(String, String, Boolean, IGlobalCacheLock,
ISharedEventSubscriberFactory,
Boolean)](M_Tessa_Platform_Caching_GlobalCache_1__ctor.htm)|  Создаёт
экземпляр класса с указанием имени, являющегося глобально уникальным для
экземпляров кэша того же типа, расположенных в различных процессах.  
[GlobalCache<TEventArgs>(String, String, Type, IGlobalCacheLock,
ISharedEventSubscriberFactory,
Boolean)](M_Tessa_Platform_Caching_GlobalCache_1__ctor_1.htm)|  Создаёт
экземпляр класса с указанием имени, являющегося глобально уникальным для
экземпляров кэша заданного типа instanceType, расположенных в различных
процессах.  
## __Свойства
[InstanceName](P_Tessa_Platform_Caching_GlobalCache_1_InstanceName.htm)|  Имя
экземпляра класса, являющееся глобально уникальным для экземпляров кэша того
же типа, расположенных в различных процессах. Значение null определяет, что
синхронизация не используется.  
---|---  
[InstanceType](P_Tessa_Platform_Caching_GlobalCache_1_InstanceType.htm)|  Тип
объекта, используемый для синхронизации экземпляров между потоками и
процессами.  
[InterprocessCommunicationIsEnabled](P_Tessa_Platform_Caching_GlobalCache_1_InterprocessCommunicationIsEnabled.htm)|
Возвращает признак того, что кэш использует коммуникацию между процессами.
Значение false определяет, что кэш перестаёт быть глобальным и кэширует данные
только в текущем объекте.  
[IsDisposed](P_Tessa_Platform_Caching_GlobalCache_1_IsDisposed.htm)| Признак
того, что ресурсы объекта были освобождены.  
##  __Методы
[DisposeAsync()](M_Tessa_Platform_Caching_GlobalCache_1_DisposeAsync.htm)|
Освобождает ресурсы, занимаемые объектом.  
---|---  
[DisposeAsync(Boolean)](M_Tessa_Platform_Caching_GlobalCache_1_DisposeAsync_1.htm)|
Освобождает ресурсы, занимаемые объектом.  
[EnsureInvalidateCacheSubscribedAsync](M_Tessa_Platform_Caching_GlobalCache_1_EnsureInvalidateCacheSubscribedAsync.htm)|
Выполняет подписку на глобальное событие сброса кэша, если объект ещё не был
подписан. Метод следует вызывать только в том случае, если доступ к кэшируемым
данным осуществляется не только через методы
[GetAsync<T>(Func<CancellationToken, Task<T>>, Func<CancellationToken,
Task<T>>, Boolean,
CancellationToken)](M_Tessa_Platform_Caching_GlobalCache_1_GetAsync__1.htm) и
[TryGetAsync<T>(Func<CancellationToken, Task<T>>, Boolean,
CancellationToken)](M_Tessa_Platform_Caching_GlobalCache_1_TryGetAsync__1.htm).  
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
[GetAsync<T>](M_Tessa_Platform_Caching_GlobalCache_1_GetAsync__1.htm)|
Инициирует заполнение кэша при необходимости и возвращает запрошенное из кэша
значение.  
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
[InvalidateGlobalCacheAsync](M_Tessa_Platform_Caching_GlobalCache_1_InvalidateGlobalCacheAsync.htm)|
Инициирует глобальный сброс кэша, который затрагивает как текущий, так и
другие экземпляры кэша с тем же именем, которые могут располагаться в других
процессах.  
[InvalidateLocalCacheAsync](M_Tessa_Platform_Caching_GlobalCache_1_InvalidateLocalCacheAsync.htm)|
Метод, реализующий сброс кэша в текущем экземпляре. Метод является
потокобезопасным и может обращаться к кэшу без дополнительной синхронизации.  
[InvalidateLocalCacheOverrideAsync](M_Tessa_Platform_Caching_GlobalCache_1_InvalidateLocalCacheOverrideAsync.htm)|
Метод, реализующий сброс кэша в текущем экземпляре. Метод является
потокобезопасным и может обращаться к кэшу без дополнительной синхронизации.
Любые необработанные исключения, возникшие внутри делегата, игнорируются с
записью в лог.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetAsync<T>](M_Tessa_Platform_Caching_GlobalCache_1_TryGetAsync__1.htm)|
Возвращает запрошенное из кэша значение или null, если значение отсутствует.  
## __События
[Invalidated](E_Tessa_Platform_Caching_GlobalCache_1_Invalidated.htm)|
Событие, которое содержит вызовы на сброс внешнего кэша, зависимого от
текущего кэша. Обработчики событий должны как можно более быстро выполнить код
по сбросу кэша. Все исключения, возникшие в обработчиках, игнорируются с
записью в лог.  
---|---  
## __Поля
[InvalidatedEventName](F_Tessa_Platform_Caching_GlobalCache_1_InvalidatedEventName.htm)|
Семантическое имя события по сбросу кэша.  
---|---  
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
[RegisterInConstructor<TEventArgs>](M_Tessa_Platform_PlatformExtensions_RegisterInConstructor__1.htm)|
Выполняет регистрацию текущего глобального кэша cache в контейнере container.
Все ресурсы глобального кэша могут быть освобождены, если регистрация в
контейнере container завершена по причине того, что все объекты контейнера уже
были освобождены. Возвращает признак того, что ресурсы глобального кэша не
были освобождены.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Caching - пространство имён](N_Tessa_Platform_Caching.htm)
