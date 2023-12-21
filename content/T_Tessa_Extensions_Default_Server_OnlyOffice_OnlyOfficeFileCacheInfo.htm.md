# OnlyOfficeFileCacheInfo - класс
Содержит информацию о файле, добавленном в кэш
[IOnlyOfficeFileCache](T_Tessa_Extensions_Default_Server_OnlyOffice_IOnlyOfficeFileCache.htm).
Информация используется для редактирования документов в редакторах OnlyOffice.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.OnlyOffice](N_Tessa_Extensions_Default_Server_OnlyOffice.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class OnlyOfficeFileCacheInfo : IOnlyOfficeFileCacheInfo
VB __Копировать
     Public NotInheritable Class OnlyOfficeFileCacheInfo
    	Implements IOnlyOfficeFileCacheInfo
C++ __Копировать
     public ref class OnlyOfficeFileCacheInfo sealed : IOnlyOfficeFileCacheInfo
F# __Копировать
     [<SealedAttribute>]
    type OnlyOfficeFileCacheInfo = 
        class
            interface IOnlyOfficeFileCacheInfo
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ OnlyOfficeFileCacheInfo
Implements
    [IOnlyOfficeFileCacheInfo](T_Tessa_Extensions_Default_Server_OnlyOffice_IOnlyOfficeFileCacheInfo.htm)
##  __Конструкторы
[OnlyOfficeFileCacheInfo](M_Tessa_Extensions_Default_Server_OnlyOffice_OnlyOfficeFileCacheInfo__ctor.htm)|
Инициализирует новый экземпляр класса OnlyOfficeFileCacheInfo  
---|---  
##  __Свойства
[CreatedByID](P_Tessa_Extensions_Default_Server_OnlyOffice_OnlyOfficeFileCacheInfo_CreatedByID.htm)|
Идентификатор пользователя.  
---|---  
[EditorWasOpen](P_Tessa_Extensions_Default_Server_OnlyOffice_OnlyOfficeFileCacheInfo_EditorWasOpen.htm)|
Признак того, что сервер документов уведомил нас о том, что редактор был
открыт с этим файлом.  
[HasChangesAfterClose](P_Tessa_Extensions_Default_Server_OnlyOffice_OnlyOfficeFileCacheInfo_HasChangesAfterClose.htm)|
Признак того, что после закрытия редактора файл был изменён, или null, если
редактор не был закрыт.  
[ID](P_Tessa_Extensions_Default_Server_OnlyOffice_OnlyOfficeFileCacheInfo_ID.htm)|
Идентификатор записи.  
[LastAccessTime](P_Tessa_Extensions_Default_Server_OnlyOffice_OnlyOfficeFileCacheInfo_LastAccessTime.htm)|
Время последнего обращения или создания, изменения этой информации.  
[LastModifiedFileUrlTime](P_Tessa_Extensions_Default_Server_OnlyOffice_OnlyOfficeFileCacheInfo_LastModifiedFileUrlTime.htm)|
Время последнего изменения URL к модицированному файлу
[ModifiedFileUrl](P_Tessa_Extensions_Default_Server_OnlyOffice_IOnlyOfficeFileCacheInfo_ModifiedFileUrl.htm).  
[ModifiedFileUrl](P_Tessa_Extensions_Default_Server_OnlyOffice_OnlyOfficeFileCacheInfo_ModifiedFileUrl.htm)|
URL к отредактированному файлу на сервере документов.  
[SourceFileName](P_Tessa_Extensions_Default_Server_OnlyOffice_OnlyOfficeFileCacheInfo_SourceFileName.htm)|
Имя исходного файла.  
[SourceFileVersionID](P_Tessa_Extensions_Default_Server_OnlyOffice_OnlyOfficeFileCacheInfo_SourceFileVersionID.htm)|
Идентификатор исходной версии файла.  
## __Методы
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
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
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
[Tessa.Extensions.Default.Server.OnlyOffice - пространство
имён](N_Tessa_Extensions_Default_Server_OnlyOffice.htm)
