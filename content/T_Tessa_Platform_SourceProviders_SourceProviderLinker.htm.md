# SourceProviderLinker - класс
Связывает между собой ресурсы, представляющие собой источник контента или
директорий через провайдеры
[ISourceContentProvider](T_Tessa_Platform_SourceProviders_ISourceContentProvider.htm)
или
[ISourceDirectoryProvider](T_Tessa_Platform_SourceProviders_ISourceDirectoryProvider.htm),
с возможностью создания нового ресурса в качестве связанного, а также
перезаписи данных из связанного ресурса в изначальный.
## __Definition
 **Пространство имён:**
[Tessa.Platform.SourceProviders](N_Tessa_Platform_SourceProviders.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class SourceProviderLinker : ISourceProviderLinker
VB __Копировать
     Public Class SourceProviderLinker
    	Implements ISourceProviderLinker
C++ __Копировать
     public ref class SourceProviderLinker : ISourceProviderLinker
F# __Копировать
     type SourceProviderLinker = 
        class
            interface ISourceProviderLinker
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ SourceProviderLinker
Derived
[Tessa.Platform.SourceProviders.FileSystemSourceProviderLinker](T_Tessa_Platform_SourceProviders_FileSystemSourceProviderLinker.htm)
Implements
    [ISourceProviderLinker](T_Tessa_Platform_SourceProviders_ISourceProviderLinker.htm)
##  __Конструкторы
[SourceProviderLinker](M_Tessa_Platform_SourceProviders_SourceProviderLinker__ctor.htm)|
Инициализирует новый экземпляр класса SourceProviderLinker  
---|---  
##  __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetContentLinksAsync](M_Tessa_Platform_SourceProviders_SourceProviderLinker_GetContentLinksAsync.htm)|
Возвращает коллекцию связей между провайдерами контента.  
[GetDirectoryLinksAsync](M_Tessa_Platform_SourceProviders_SourceProviderLinker_GetDirectoryLinksAsync.htm)|
Возвращает коллекцию связей между провайдерами директорий.  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetLinkedProviderByOriginalAsync(ISourceContentProvider,
CancellationToken)](M_Tessa_Platform_SourceProviders_SourceProviderLinker_GetLinkedProviderByOriginalAsync.htm)|
Возвращает связанный провайдер контента на основании оригинального провайдера.  
[GetLinkedProviderByOriginalAsync(ISourceDirectoryProvider,
CancellationToken)](M_Tessa_Platform_SourceProviders_SourceProviderLinker_GetLinkedProviderByOriginalAsync_1.htm)|
Возвращает связанный провайдер директории на основании оригинального
провайдера.  
[GetOriginalProviderByLinkedAsync(ISourceContentProvider,
CancellationToken)](M_Tessa_Platform_SourceProviders_SourceProviderLinker_GetOriginalProviderByLinkedAsync.htm)|
Возвращает оригинальный провайдер контента на основании связанного провайдера.  
[GetOriginalProviderByLinkedAsync(ISourceDirectoryProvider,
CancellationToken)](M_Tessa_Platform_SourceProviders_SourceProviderLinker_GetOriginalProviderByLinkedAsync_1.htm)|
Возвращает оригинальный провайдер директории на основании связанного
провайдера.  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[LinkProviderAsync(ISourceContentProvider, ISourceContentProvider, Boolean,
CancellationToken)](M_Tessa_Platform_SourceProviders_SourceProviderLinker_LinkProviderAsync.htm)|
Связывает провайдеры контента.  
[LinkProviderAsync(ISourceDirectoryProvider, ISourceDirectoryProvider,
Boolean,
CancellationToken)](M_Tessa_Platform_SourceProviders_SourceProviderLinker_LinkProviderAsync_1.htm)|
Связывает провайдеры директорий.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[OverwriteAll](M_Tessa_Platform_SourceProviders_SourceProviderLinker_OverwriteAll.htm)|
Для всех связей перезаписывает контент оригинальных провайдеров контентом из
связанных провайдеров.  
[OverwriteDirectoryContent](M_Tessa_Platform_SourceProviders_SourceProviderLinker_OverwriteDirectoryContent.htm)|  
[OverwriteOriginalContentInternalAsync](M_Tessa_Platform_SourceProviders_SourceProviderLinker_OverwriteOriginalContentInternalAsync.htm)|
Перезаписывает контент оригинального провайдера контентом из связанного
провайдера.  
[OverwriteOriginalDirectoryInternalAsync](M_Tessa_Platform_SourceProviders_SourceProviderLinker_OverwriteOriginalDirectoryInternalAsync.htm)|
Перезаписывает контент директории оригинального провайдера контентом из
связанного провайдера.  
[OverwriteOriginalProviderAsync(ISourceContentProvider, Boolean,
CancellationToken)](M_Tessa_Platform_SourceProviders_SourceProviderLinker_OverwriteOriginalProviderAsync.htm)|
Перезаписывает контент оригинального провайдера контентом из связанного
провайдера.  
[OverwriteOriginalProviderAsync(ISourceDirectoryProvider, Boolean,
CancellationToken)](M_Tessa_Platform_SourceProviders_SourceProviderLinker_OverwriteOriginalProviderAsync_1.htm)|
Перезаписывает контент директории оригинального провайдера контентом из
связанного провайдера.  
[SetValidationResult](M_Tessa_Platform_SourceProviders_SourceProviderLinker_SetValidationResult.htm)|
Устанавливает объект для построения результата валидации.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[UnlinkAll](M_Tessa_Platform_SourceProviders_SourceProviderLinker_UnlinkAll.htm)|
Удаляет все текущие связи между провайдерами.  
[UnlinkContentProviderInternalAsync](M_Tessa_Platform_SourceProviders_SourceProviderLinker_UnlinkContentProviderInternalAsync.htm)|  
[UnlinkDirectoryProviderInternalAsync](M_Tessa_Platform_SourceProviders_SourceProviderLinker_UnlinkDirectoryProviderInternalAsync.htm)|  
[UnlinkProviderAsync(ISourceContentProvider, Boolean,
CancellationToken)](M_Tessa_Platform_SourceProviders_SourceProviderLinker_UnlinkProviderAsync.htm)|
Удаляет связь между провайдерами контента.  
[UnlinkProviderAsync(ISourceDirectoryProvider, Boolean,
CancellationToken)](M_Tessa_Platform_SourceProviders_SourceProviderLinker_UnlinkProviderAsync_1.htm)|
Удаляет связь между провайдерами директорий.  
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
[Tessa.Platform.SourceProviders - пространство
имён](N_Tessa_Platform_SourceProviders.htm)
