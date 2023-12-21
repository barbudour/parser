# ISourceDirectoryProvider - интерфейс
Провайдер для источника, представляющего собой дирректорию ресурсов. Например,
папку с файлами и т.п.
## __Definition
 **Пространство имён:**
[Tessa.Platform.SourceProviders](N_Tessa_Platform_SourceProviders.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ISourceDirectoryProvider : ISourceProviderBase
VB __Копировать
     Public Interface ISourceDirectoryProvider
    	Inherits ISourceProviderBase
C++ __Копировать
     public interface class ISourceDirectoryProvider : ISourceProviderBase
F# __Копировать
     type ISourceDirectoryProvider = 
        interface
            interface ISourceProviderBase
        end
Implements
    [ISourceProviderBase](T_Tessa_Platform_SourceProviders_ISourceProviderBase.htm)
##  __Свойства
[IsReadOnly](P_Tessa_Platform_SourceProviders_ISourceProviderBase_IsReadOnly.htm)|
Флаг указывает на то, что источник предназначен только для чтения. Зависит от
реализаций провайдеров.  
(Унаследован от
[ISourceProviderBase](T_Tessa_Platform_SourceProviders_ISourceProviderBase.htm))  
---|---  
##  __Методы
[CreateIfNotExistsAsync](M_Tessa_Platform_SourceProviders_ISourceDirectoryProvider_CreateIfNotExistsAsync.htm)|
Создает директорию, если она не существует.  
---|---  
[DeleteAsync](M_Tessa_Platform_SourceProviders_ISourceDirectoryProvider_DeleteAsync.htm)|
Позволяет удалить источник, для которого предназначен провайдер.  
[GetContentNamesListAsync](M_Tessa_Platform_SourceProviders_ISourceDirectoryProvider_GetContentNamesListAsync.htm)|
Получает список имен ресурсов в директории, для которой предназначен текущий
провайдер.  
[GetContentNamesListWithCollisionResolutionAsync](M_Tessa_Platform_SourceProviders_ISourceDirectoryProvider_GetContentNamesListWithCollisionResolutionAsync.htm)|
Получает список имен ресурсов в директории, для которой предназначен текущий
провайдер, предварительно фильтруя данный список с учетом коллизий.  
[GetContentProvider](M_Tessa_Platform_SourceProviders_ISourceDirectoryProvider_GetContentProvider.htm)|
Получает провайдер для конкретного ресурса в директории, для которой
предназначен текущий провайдер.  
[GetFullName](M_Tessa_Platform_SourceProviders_ISourceProviderBase_GetFullName.htm)|
Возвращает абсолютный путь к ресурсу.  
(Унаследован от
[ISourceProviderBase](T_Tessa_Platform_SourceProviders_ISourceProviderBase.htm))  
[GetParentDirectoryProvider](M_Tessa_Platform_SourceProviders_ISourceDirectoryProvider_GetParentDirectoryProvider.htm)|
Получает провайдер для родительской директории относительно текущего
провайдера.  
[GetSubDirectoryProvider](M_Tessa_Platform_SourceProviders_ISourceDirectoryProvider_GetSubDirectoryProvider.htm)|
Получает провайдер для поддиректории относительно текущего провайдера.  
[IsExistsAsync](M_Tessa_Platform_SourceProviders_ISourceProviderBase_IsExistsAsync.htm)|
Получает значение, показывающее существует ли источник для которого
предназначен текущий провайдер.  
(Унаследован от
[ISourceProviderBase](T_Tessa_Platform_SourceProviders_ISourceProviderBase.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.SourceProviders - пространство
имён](N_Tessa_Platform_SourceProviders.htm)
