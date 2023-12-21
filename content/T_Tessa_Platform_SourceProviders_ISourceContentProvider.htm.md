# ISourceContentProvider - интерфейс
Провайдер для источника, представляющего собой конкретный ресурс. Например,
файл и т.п.
## __Definition
 **Пространство имён:**
[Tessa.Platform.SourceProviders](N_Tessa_Platform_SourceProviders.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ISourceContentProvider : ISourceProviderBase
VB __Копировать
     Public Interface ISourceContentProvider
    	Inherits ISourceProviderBase
C++ __Копировать
     public interface class ISourceContentProvider : ISourceProviderBase
F# __Копировать
     type ISourceContentProvider = 
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
[CreateStreamReadAsync](M_Tessa_Platform_SourceProviders_ISourceContentProvider_CreateStreamReadAsync.htm)|
Получает поток контента для чтения ресурса, который представляет данный
провайдер.  
---|---  
[CreateStreamWriteAsync](M_Tessa_Platform_SourceProviders_ISourceContentProvider_CreateStreamWriteAsync.htm)|
Получает поток контента для записи или создания ресурса, который представляет
данный провайдер.  
[DeleteAsync](M_Tessa_Platform_SourceProviders_ISourceContentProvider_DeleteAsync.htm)|
Позволяет удалить источник, для которого предназначен провайдер.  
[GetCurrentDirectoryProvider](M_Tessa_Platform_SourceProviders_ISourceContentProvider_GetCurrentDirectoryProvider.htm)|
Получает провайдер для текущей директории ресурса.  
[GetFullName](M_Tessa_Platform_SourceProviders_ISourceProviderBase_GetFullName.htm)|
Возвращает абсолютный путь к ресурсу.  
(Унаследован от
[ISourceProviderBase](T_Tessa_Platform_SourceProviders_ISourceProviderBase.htm))  
[GetNameWithoutDirectoryPath](M_Tessa_Platform_SourceProviders_ISourceContentProvider_GetNameWithoutDirectoryPath.htm)|
Получает простое имя ресурса, который представляет данный провайдер. Например,
имя файла без остального пути и т.п.  
[IsExistsAsync](M_Tessa_Platform_SourceProviders_ISourceProviderBase_IsExistsAsync.htm)|
Получает значение, показывающее существует ли источник для которого
предназначен текущий провайдер.  
(Унаследован от
[ISourceProviderBase](T_Tessa_Platform_SourceProviders_ISourceProviderBase.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.SourceProviders - пространство
имён](N_Tessa_Platform_SourceProviders.htm)
