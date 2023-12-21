# ISourceProviderBase - интерфейс
Представляет общий базовый функционал для ISourceContentProvider и
ISourceDirectoryProvider
## __Definition
 **Пространство имён:**
[Tessa.Platform.SourceProviders](N_Tessa_Platform_SourceProviders.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ISourceProviderBase
VB __Копировать
     Public Interface ISourceProviderBase
C++ __Копировать
     public interface class ISourceProviderBase
F# __Копировать
     type ISourceProviderBase = interface end
##  __Свойства
[IsReadOnly](P_Tessa_Platform_SourceProviders_ISourceProviderBase_IsReadOnly.htm)|
Флаг указывает на то, что источник предназначен только для чтения. Зависит от
реализаций провайдеров.  
---|---  
## __Методы
[GetFullName](M_Tessa_Platform_SourceProviders_ISourceProviderBase_GetFullName.htm)|
Возвращает абсолютный путь к ресурсу.  
---|---  
[IsExistsAsync](M_Tessa_Platform_SourceProviders_ISourceProviderBase_IsExistsAsync.htm)|
Получает значение, показывающее существует ли источник для которого
предназначен текущий провайдер.  
## __См. также
#### Ссылки
[Tessa.Platform.SourceProviders - пространство
имён](N_Tessa_Platform_SourceProviders.htm)
