# FileSystemSourceProviderLinker - класс
Реализация
[ISourceProviderLinker](T_Tessa_Platform_SourceProviders_ISourceProviderLinker.htm),
оптимизированная для работы с файловой системой.
## __Definition
 **Пространство имён:**
[Tessa.Platform.SourceProviders](N_Tessa_Platform_SourceProviders.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class FileSystemSourceProviderLinker : SourceProviderLinker
VB __Копировать
     Public Class FileSystemSourceProviderLinker
    	Inherits SourceProviderLinker
C++ __Копировать
     public ref class FileSystemSourceProviderLinker : public SourceProviderLinker
F# __Копировать
     type FileSystemSourceProviderLinker = 
        class
            inherit SourceProviderLinker
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[SourceProviderLinker](T_Tessa_Platform_SourceProviders_SourceProviderLinker.htm) __ FileSystemSourceProviderLinker
##  __Конструкторы
[FileSystemSourceProviderLinker](M_Tessa_Platform_SourceProviders_FileSystemSourceProviderLinker__ctor.htm)|
Инициализирует новый экземпляр класса FileSystemSourceProviderLinker  
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
(Унаследован от
[SourceProviderLinker](T_Tessa_Platform_SourceProviders_SourceProviderLinker.htm))  
[GetDirectoryLinksAsync](M_Tessa_Platform_SourceProviders_SourceProviderLinker_GetDirectoryLinksAsync.htm)|
Возвращает коллекцию связей между провайдерами директорий.  
(Унаследован от
[SourceProviderLinker](T_Tessa_Platform_SourceProviders_SourceProviderLinker.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetLinkedProviderByOriginalAsync(ISourceContentProvider,
CancellationToken)](M_Tessa_Platform_SourceProviders_SourceProviderLinker_GetLinkedProviderByOriginalAsync.htm)|
Возвращает связанный провайдер контента на основании оригинального провайдера.  
(Унаследован от
[SourceProviderLinker](T_Tessa_Platform_SourceProviders_SourceProviderLinker.htm))  
[GetLinkedProviderByOriginalAsync(ISourceDirectoryProvider,
CancellationToken)](M_Tessa_Platform_SourceProviders_SourceProviderLinker_GetLinkedProviderByOriginalAsync_1.htm)|
Возвращает связанный провайдер директории на основании оригинального
провайдера.  
(Унаследован от
[SourceProviderLinker](T_Tessa_Platform_SourceProviders_SourceProviderLinker.htm))  
[GetOriginalProviderByLinkedAsync(ISourceContentProvider,
CancellationToken)](M_Tessa_Platform_SourceProviders_SourceProviderLinker_GetOriginalProviderByLinkedAsync.htm)|
Возвращает оригинальный провайдер контента на основании связанного провайдера.  
(Унаследован от
[SourceProviderLinker](T_Tessa_Platform_SourceProviders_SourceProviderLinker.htm))  
[GetOriginalProviderByLinkedAsync(ISourceDirectoryProvider,
CancellationToken)](M_Tessa_Platform_SourceProviders_SourceProviderLinker_GetOriginalProviderByLinkedAsync_1.htm)|
Возвращает оригинальный провайдер директории на основании связанного
провайдера.  
(Унаследован от
[SourceProviderLinker](T_Tessa_Platform_SourceProviders_SourceProviderLinker.htm))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[LinkProviderAsync(ISourceContentProvider, ISourceContentProvider, Boolean,
CancellationToken)](M_Tessa_Platform_SourceProviders_SourceProviderLinker_LinkProviderAsync.htm)|
Связывает провайдеры контента.  
(Унаследован от
[SourceProviderLinker](T_Tessa_Platform_SourceProviders_SourceProviderLinker.htm))  
[LinkProviderAsync(ISourceDirectoryProvider, ISourceDirectoryProvider,
Boolean,
CancellationToken)](M_Tessa_Platform_SourceProviders_SourceProviderLinker_LinkProviderAsync_1.htm)|
Связывает провайдеры директорий.  
(Унаследован от
[SourceProviderLinker](T_Tessa_Platform_SourceProviders_SourceProviderLinker.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[OverwriteAll](M_Tessa_Platform_SourceProviders_SourceProviderLinker_OverwriteAll.htm)|
Для всех связей перезаписывает контент оригинальных провайдеров контентом из
связанных провайдеров.  
(Унаследован от
[SourceProviderLinker](T_Tessa_Platform_SourceProviders_SourceProviderLinker.htm))  
[OverwriteOriginalContentInternalAsync](M_Tessa_Platform_SourceProviders_FileSystemSourceProviderLinker_OverwriteOriginalContentInternalAsync.htm)|
Перезаписывает контент оригинального провайдера контентом из связанного
провайдера.  
(Переопределяет
[SourceProviderLinker.OverwriteOriginalContentInternalAsync(ContentProviderLink,
Boolean,
CancellationToken)](M_Tessa_Platform_SourceProviders_SourceProviderLinker_OverwriteOriginalContentInternalAsync.htm))  
[OverwriteOriginalDirectoryInternalAsync](M_Tessa_Platform_SourceProviders_FileSystemSourceProviderLinker_OverwriteOriginalDirectoryInternalAsync.htm)|
Перезаписывает контент директории оригинального провайдера контентом из
связанного провайдера.  
(Переопределяет
[SourceProviderLinker.OverwriteOriginalDirectoryInternalAsync(DirectoryProviderLink,
Boolean,
CancellationToken)](M_Tessa_Platform_SourceProviders_SourceProviderLinker_OverwriteOriginalDirectoryInternalAsync.htm))  
[OverwriteOriginalProviderAsync(ISourceContentProvider, Boolean,
CancellationToken)](M_Tessa_Platform_SourceProviders_SourceProviderLinker_OverwriteOriginalProviderAsync.htm)|
Перезаписывает контент оригинального провайдера контентом из связанного
провайдера.  
(Унаследован от
[SourceProviderLinker](T_Tessa_Platform_SourceProviders_SourceProviderLinker.htm))  
[OverwriteOriginalProviderAsync(ISourceDirectoryProvider, Boolean,
CancellationToken)](M_Tessa_Platform_SourceProviders_SourceProviderLinker_OverwriteOriginalProviderAsync_1.htm)|
Перезаписывает контент директории оригинального провайдера контентом из
связанного провайдера.  
(Унаследован от
[SourceProviderLinker](T_Tessa_Platform_SourceProviders_SourceProviderLinker.htm))  
[SetValidationResult](M_Tessa_Platform_SourceProviders_SourceProviderLinker_SetValidationResult.htm)|
Устанавливает объект для построения результата валидации.  
(Унаследован от
[SourceProviderLinker](T_Tessa_Platform_SourceProviders_SourceProviderLinker.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[UnlinkAll](M_Tessa_Platform_SourceProviders_SourceProviderLinker_UnlinkAll.htm)|
Удаляет все текущие связи между провайдерами.  
(Унаследован от
[SourceProviderLinker](T_Tessa_Platform_SourceProviders_SourceProviderLinker.htm))  
[UnlinkContentProviderInternalAsync](M_Tessa_Platform_SourceProviders_SourceProviderLinker_UnlinkContentProviderInternalAsync.htm)|  
(Унаследован от
[SourceProviderLinker](T_Tessa_Platform_SourceProviders_SourceProviderLinker.htm))  
[UnlinkDirectoryProviderInternalAsync](M_Tessa_Platform_SourceProviders_SourceProviderLinker_UnlinkDirectoryProviderInternalAsync.htm)|  
(Унаследован от
[SourceProviderLinker](T_Tessa_Platform_SourceProviders_SourceProviderLinker.htm))  
[UnlinkProviderAsync(ISourceContentProvider, Boolean,
CancellationToken)](M_Tessa_Platform_SourceProviders_SourceProviderLinker_UnlinkProviderAsync.htm)|
Удаляет связь между провайдерами контента.  
(Унаследован от
[SourceProviderLinker](T_Tessa_Platform_SourceProviders_SourceProviderLinker.htm))  
[UnlinkProviderAsync(ISourceDirectoryProvider, Boolean,
CancellationToken)](M_Tessa_Platform_SourceProviders_SourceProviderLinker_UnlinkProviderAsync_1.htm)|
Удаляет связь между провайдерами директорий.  
(Унаследован от
[SourceProviderLinker](T_Tessa_Platform_SourceProviders_SourceProviderLinker.htm))  
##  __Поля
[LinkerForWriteCardsName](F_Tessa_Platform_SourceProviders_FileSystemSourceProviderLinker_LinkerForWriteCardsName.htm)|  
---|---  
[LinkerForWriteCardsSuffix](F_Tessa_Platform_SourceProviders_FileSystemSourceProviderLinker_LinkerForWriteCardsSuffix.htm)|  
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
