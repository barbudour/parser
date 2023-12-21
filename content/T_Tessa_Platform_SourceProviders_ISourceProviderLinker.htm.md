# ISourceProviderLinker - интерфейс
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
     public interface ISourceProviderLinker
VB __Копировать
     Public Interface ISourceProviderLinker
C++ __Копировать
     public interface class ISourceProviderLinker
F# __Копировать
     type ISourceProviderLinker = interface end
##  __Методы
[GetAllLinksAsync](M_Tessa_Platform_SourceProviders_ISourceProviderLinker_GetAllLinksAsync.htm)|
Возвращает коллекции всех текущих связей провайдеров.  
---|---  
[GetContentLinksAsync](M_Tessa_Platform_SourceProviders_ISourceProviderLinker_GetContentLinksAsync.htm)|
Возвращает коллекцию связей между провайдерами контента.  
[GetDirectoryLinksAsync](M_Tessa_Platform_SourceProviders_ISourceProviderLinker_GetDirectoryLinksAsync.htm)|
Возвращает коллекцию связей между провайдерами директорий.  
[GetLinkedProviderByOriginalAsync(ISourceContentProvider,
CancellationToken)](M_Tessa_Platform_SourceProviders_ISourceProviderLinker_GetLinkedProviderByOriginalAsync.htm)|
Возвращает связанный провайдер контента на основании оригинального провайдера.  
[GetLinkedProviderByOriginalAsync(ISourceDirectoryProvider,
CancellationToken)](M_Tessa_Platform_SourceProviders_ISourceProviderLinker_GetLinkedProviderByOriginalAsync_1.htm)|
Возвращает связанный провайдер директории на основании оригинального
провайдера.  
[GetOriginalProviderByLinkedAsync(ISourceContentProvider,
CancellationToken)](M_Tessa_Platform_SourceProviders_ISourceProviderLinker_GetOriginalProviderByLinkedAsync.htm)|
Возвращает оригинальный провайдер контента на основании связанного провайдера.  
[GetOriginalProviderByLinkedAsync(ISourceDirectoryProvider,
CancellationToken)](M_Tessa_Platform_SourceProviders_ISourceProviderLinker_GetOriginalProviderByLinkedAsync_1.htm)|
Возвращает оригинальный провайдер директории на основании связанного
провайдера.  
[LinkProviderAsync(ISourceContentProvider, ISourceContentProvider, Boolean,
CancellationToken)](M_Tessa_Platform_SourceProviders_ISourceProviderLinker_LinkProviderAsync.htm)|
Связывает провайдеры контента.  
[LinkProviderAsync(ISourceDirectoryProvider, ISourceDirectoryProvider,
Boolean,
CancellationToken)](M_Tessa_Platform_SourceProviders_ISourceProviderLinker_LinkProviderAsync_1.htm)|
Связывает провайдеры директорий.  
[OverwriteAll](M_Tessa_Platform_SourceProviders_ISourceProviderLinker_OverwriteAll.htm)|
Для всех связей перезаписывает контент оригинальных провайдеров контентом из
связанных провайдеров.  
[OverwriteOriginalProviderAsync(ISourceContentProvider, Boolean,
CancellationToken)](M_Tessa_Platform_SourceProviders_ISourceProviderLinker_OverwriteOriginalProviderAsync.htm)|
Перезаписывает контент оригинального провайдера контентом из связанного
провайдера.  
[OverwriteOriginalProviderAsync(ISourceDirectoryProvider, Boolean,
CancellationToken)](M_Tessa_Platform_SourceProviders_ISourceProviderLinker_OverwriteOriginalProviderAsync_1.htm)|
Перезаписывает контент директории оригинального провайдера контентом из
связанного провайдера.  
[SetValidationResult](M_Tessa_Platform_SourceProviders_ISourceProviderLinker_SetValidationResult.htm)|
Устанавливает объект для построения результата валидации.  
[UnlinkAll](M_Tessa_Platform_SourceProviders_ISourceProviderLinker_UnlinkAll.htm)|
Удаляет все текущие связи между провайдерами.  
[UnlinkProviderAsync(ISourceContentProvider, Boolean,
CancellationToken)](M_Tessa_Platform_SourceProviders_ISourceProviderLinker_UnlinkProviderAsync.htm)|
Удаляет связь между провайдерами контента.  
[UnlinkProviderAsync(ISourceDirectoryProvider, Boolean,
CancellationToken)](M_Tessa_Platform_SourceProviders_ISourceProviderLinker_UnlinkProviderAsync_1.htm)|
Удаляет связь между провайдерами директорий.  
## __См. также
#### Ссылки
[Tessa.Platform.SourceProviders - пространство
имён](N_Tessa_Platform_SourceProviders.htm)
