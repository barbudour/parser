# MultiSourceLocalizationService - класс
##  __Definition
 **Пространство имён:** [Tessa.Localization](N_Tessa_Localization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class MultiSourceLocalizationService : LocalizationServiceBase, 
    	ICacheableLocalizationService, ILocalizationService, IAsyncDisposable
VB __Копировать
     Public NotInheritable Class MultiSourceLocalizationService
    	Inherits LocalizationServiceBase
    	Implements ICacheableLocalizationService, ILocalizationService, IAsyncDisposable
C++ __Копировать
     public ref class MultiSourceLocalizationService sealed : public LocalizationServiceBase, 
    	ICacheableLocalizationService, ILocalizationService, IAsyncDisposable
F# __Копировать
     [<SealedAttribute>]
    type MultiSourceLocalizationService = 
        class
            inherit LocalizationServiceBase
            interface ICacheableLocalizationService
            interface ILocalizationService
            interface IAsyncDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm) __ MultiSourceLocalizationService
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [ICacheableLocalizationService](T_Tessa_Localization_ICacheableLocalizationService.htm), [ILocalizationService](T_Tessa_Localization_ILocalizationService.htm)
##  __Конструкторы
[MultiSourceLocalizationService()](M_Tessa_Localization_MultiSourceLocalizationService__ctor.htm)|
Инициализирует новый экземпляр класса MultiSourceLocalizationService  
---|---  
[MultiSourceLocalizationService(Boolean)](M_Tessa_Localization_MultiSourceLocalizationService__ctor_1.htm)|
Инициализирует новый экземпляр класса MultiSourceLocalizationService  
[MultiSourceLocalizationService(ILocalizationService[])](M_Tessa_Localization_MultiSourceLocalizationService__ctor_3.htm)|
Инициализирует новый экземпляр класса MultiSourceLocalizationService  
[MultiSourceLocalizationService(Boolean,
ILocalizationService[])](M_Tessa_Localization_MultiSourceLocalizationService__ctor_2.htm)|
Инициализирует новый экземпляр класса MultiSourceLocalizationService  
##  __Свойства
[AllowImplicitInitialization](P_Tessa_Localization_LocalizationServiceBase_AllowImplicitInitialization.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
---|---  
[InitializationPending](P_Tessa_Localization_LocalizationServiceBase_InitializationPending.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[IsInitialized](P_Tessa_Localization_LocalizationServiceBase_IsInitialized.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
##  __Методы
[AddHook](M_Tessa_Localization_MultiSourceLocalizationService_AddHook.htm)|  
---|---  
[AddSource](M_Tessa_Localization_MultiSourceLocalizationService_AddSource.htm)|
Вызовите метод
[InvalidateCacheAsync(CancellationToken)](M_Tessa_Localization_MultiSourceLocalizationService_InvalidateCacheAsync.htm)
после добавления всех сервисов, если к текущему объекту ранее были обращения.  
[BeginInit](M_Tessa_Localization_LocalizationServiceBase_BeginInit.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[BeginInitCore](M_Tessa_Localization_MultiSourceLocalizationService_BeginInitCore.htm)|  
(Переопределяет
[LocalizationServiceBase.BeginInitCore()](M_Tessa_Localization_LocalizationServiceBase_BeginInitCore.htm))  
[CheckInitializationPending](M_Tessa_Localization_LocalizationServiceBase_CheckInitializationPending.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[CheckIsInitialized](M_Tessa_Localization_LocalizationServiceBase_CheckIsInitialized.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[DeferInitialization](M_Tessa_Localization_LocalizationServiceBase_DeferInitialization.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[DisposeAsync](M_Tessa_Localization_MultiSourceLocalizationService_DisposeAsync.htm)|
Освобождает ресурсы, занимаемые объектом.  
[EndInit](M_Tessa_Localization_LocalizationServiceBase_EndInit.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[EndInitCore](M_Tessa_Localization_MultiSourceLocalizationService_EndInitCore.htm)|  
(Переопределяет
[LocalizationServiceBase.EndInitCore()](M_Tessa_Localization_LocalizationServiceBase_EndInitCore.htm))  
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
[GetEntriesAsync](M_Tessa_Localization_LocalizationServiceBase_GetEntriesAsync.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[GetEntriesCoreAsync](M_Tessa_Localization_MultiSourceLocalizationService_GetEntriesCoreAsync.htm)|  
(Переопределяет [LocalizationServiceBase.GetEntriesCoreAsync(CultureInfo,
Boolean,
CancellationToken)](M_Tessa_Localization_LocalizationServiceBase_GetEntriesCoreAsync.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetLibrariesAsync](M_Tessa_Localization_LocalizationServiceBase_GetLibrariesAsync.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[GetLibrariesCoreAsync](M_Tessa_Localization_MultiSourceLocalizationService_GetLibrariesCoreAsync.htm)|  
(Переопределяет [LocalizationServiceBase.GetLibrariesCoreAsync(Boolean,
CancellationToken)](M_Tessa_Localization_LocalizationServiceBase_GetLibrariesCoreAsync.htm))  
[GetLibraryAsync(Guid, Boolean,
CancellationToken)](M_Tessa_Localization_LocalizationServiceBase_GetLibraryAsync.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[GetLibraryAsync(String, Boolean,
CancellationToken)](M_Tessa_Localization_LocalizationServiceBase_GetLibraryAsync_1.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[GetLibraryCoreAsync(Guid, Boolean,
CancellationToken)](M_Tessa_Localization_MultiSourceLocalizationService_GetLibraryCoreAsync.htm)|  
(Переопределяет [LocalizationServiceBase.GetLibraryCoreAsync(Guid, Boolean,
CancellationToken)](M_Tessa_Localization_LocalizationServiceBase_GetLibraryCoreAsync.htm))  
[GetLibraryCoreAsync(String, Boolean,
CancellationToken)](M_Tessa_Localization_MultiSourceLocalizationService_GetLibraryCoreAsync_1.htm)|  
(Переопределяет [LocalizationServiceBase.GetLibraryCoreAsync(String, Boolean,
CancellationToken)](M_Tessa_Localization_LocalizationServiceBase_GetLibraryCoreAsync_1.htm))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[InvalidateCacheAsync](M_Tessa_Localization_MultiSourceLocalizationService_InvalidateCacheAsync.htm)|  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[RemoveHook](M_Tessa_Localization_MultiSourceLocalizationService_RemoveHook.htm)|  
[RemoveLibraryAsync](M_Tessa_Localization_LocalizationServiceBase_RemoveLibraryAsync.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[RemoveLibraryCoreAsync](M_Tessa_Localization_MultiSourceLocalizationService_RemoveLibraryCoreAsync.htm)|  
(Переопределяет
[LocalizationServiceBase.RemoveLibraryCoreAsync(LocalizationLibrary,
CancellationToken)](M_Tessa_Localization_LocalizationServiceBase_RemoveLibraryCoreAsync.htm))  
[SaveLibraryAsync](M_Tessa_Localization_LocalizationServiceBase_SaveLibraryAsync.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[SaveLibraryCoreAsync](M_Tessa_Localization_MultiSourceLocalizationService_SaveLibraryCoreAsync.htm)|  
(Переопределяет
[LocalizationServiceBase.SaveLibraryCoreAsync(LocalizationLibrary,
CancellationToken)](M_Tessa_Localization_LocalizationServiceBase_SaveLibraryCoreAsync.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[GetCompressedLibraryAsync](M_Tessa_Localization_LocalizationExtensions_GetCompressedLibraryAsync.htm)|  
(Определяется
[LocalizationExtensions](T_Tessa_Localization_LocalizationExtensions.htm))  
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
