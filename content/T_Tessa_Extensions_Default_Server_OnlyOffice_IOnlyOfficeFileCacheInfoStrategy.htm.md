# IOnlyOfficeFileCacheInfoStrategy - интерфейс
Объект, управляющий информацией по файлу в кэше.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.OnlyOffice](N_Tessa_Extensions_Default_Server_OnlyOffice.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IOnlyOfficeFileCacheInfoStrategy
VB __Копировать
     Public Interface IOnlyOfficeFileCacheInfoStrategy
C++ __Копировать
     public interface class IOnlyOfficeFileCacheInfoStrategy
F# __Копировать
     type IOnlyOfficeFileCacheInfoStrategy = interface end
##  __Методы
[CleanCacheInfoAsync](M_Tessa_Extensions_Default_Server_OnlyOffice_IOnlyOfficeFileCacheInfoStrategy_CleanCacheInfoAsync.htm)|
Очищает кэш от информации по файлам, доступ к содержимому которых выполнялся
раньше заданной даты. Не удаляет сами файлы, для этого также вызовите
[CleanCacheAsync(Nullable<DateTime>,
CancellationToken)](M_Tessa_FileConverters_IFileConverterCache_CleanCacheAsync.htm).  
---|---  
[DeleteAsync](M_Tessa_Extensions_Default_Server_OnlyOffice_IOnlyOfficeFileCacheInfoStrategy_DeleteAsync.htm)|
Удаляет информацию о файле из кэша.  
[InsertAsync](M_Tessa_Extensions_Default_Server_OnlyOffice_IOnlyOfficeFileCacheInfoStrategy_InsertAsync.htm)|
Добавляет указанную информацию о файле в кэш.  
[TryGetInfoAsync](M_Tessa_Extensions_Default_Server_OnlyOffice_IOnlyOfficeFileCacheInfoStrategy_TryGetInfoAsync.htm)|
Возвращает информацию по файлу в кэше или null, если файл не найден по
указанному идентификатору.  
[UpdateInfoAsync](M_Tessa_Extensions_Default_Server_OnlyOffice_IOnlyOfficeFileCacheInfoStrategy_UpdateInfoAsync.htm)|
Обновляет информацию по файлу в кэше. Выбрасывает исключение, если файл не
найден по указанному идентификатору.  
[UpdateInfoOnEditorOpenedAsync](M_Tessa_Extensions_Default_Server_OnlyOffice_IOnlyOfficeFileCacheInfoStrategy_UpdateInfoOnEditorOpenedAsync.htm)|
Устанавливает флаг "Редактор был открыт"
[EditorWasOpen](P_Tessa_Extensions_Default_Server_OnlyOffice_IOnlyOfficeFileCacheInfo_EditorWasOpen.htm)
для файла в кэше. Выбрасывает исключение, если файл не найден по указанному
идентификатору.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.OnlyOffice - пространство
имён](N_Tessa_Extensions_Default_Server_OnlyOffice.htm)
