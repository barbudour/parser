# IOnlyOfficeFileCacheInfo - интерфейс
Содержит информацию о файле, добавленном в кэш
[IOnlyOfficeFileCache](T_Tessa_Extensions_Default_Server_OnlyOffice_IOnlyOfficeFileCache.htm).
Информация используется для редактирования документов в редакторах OnlyOffice.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.OnlyOffice](N_Tessa_Extensions_Default_Server_OnlyOffice.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IOnlyOfficeFileCacheInfo
VB __Копировать
     Public Interface IOnlyOfficeFileCacheInfo
C++ __Копировать
     public interface class IOnlyOfficeFileCacheInfo
F# __Копировать
     type IOnlyOfficeFileCacheInfo = interface end
##  __Свойства
[CreatedByID](P_Tessa_Extensions_Default_Server_OnlyOffice_IOnlyOfficeFileCacheInfo_CreatedByID.htm)|
Идентификатор пользователя.  
---|---  
[EditorWasOpen](P_Tessa_Extensions_Default_Server_OnlyOffice_IOnlyOfficeFileCacheInfo_EditorWasOpen.htm)|
Признак того, что сервер документов уведомил нас о том, что редактор был
открыт с этим файлом.  
[HasChangesAfterClose](P_Tessa_Extensions_Default_Server_OnlyOffice_IOnlyOfficeFileCacheInfo_HasChangesAfterClose.htm)|
Признак того, что после закрытия редактора файл был изменён, или null, если
редактор не был закрыт.  
[ID](P_Tessa_Extensions_Default_Server_OnlyOffice_IOnlyOfficeFileCacheInfo_ID.htm)|
Идентификатор записи.  
[LastAccessTime](P_Tessa_Extensions_Default_Server_OnlyOffice_IOnlyOfficeFileCacheInfo_LastAccessTime.htm)|
Время последнего обращения или создания, изменения этой информации.  
[LastModifiedFileUrlTime](P_Tessa_Extensions_Default_Server_OnlyOffice_IOnlyOfficeFileCacheInfo_LastModifiedFileUrlTime.htm)|
Время последнего изменения URL к модицированному файлу
[ModifiedFileUrl](P_Tessa_Extensions_Default_Server_OnlyOffice_IOnlyOfficeFileCacheInfo_ModifiedFileUrl.htm).  
[ModifiedFileUrl](P_Tessa_Extensions_Default_Server_OnlyOffice_IOnlyOfficeFileCacheInfo_ModifiedFileUrl.htm)|
URL к отредактированному файлу на сервере документов.  
[SourceFileName](P_Tessa_Extensions_Default_Server_OnlyOffice_IOnlyOfficeFileCacheInfo_SourceFileName.htm)|
Имя исходного файла.  
[SourceFileVersionID](P_Tessa_Extensions_Default_Server_OnlyOffice_IOnlyOfficeFileCacheInfo_SourceFileVersionID.htm)|
Идентификатор исходной версии файла.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.OnlyOffice - пространство
имён](N_Tessa_Extensions_Default_Server_OnlyOffice.htm)
