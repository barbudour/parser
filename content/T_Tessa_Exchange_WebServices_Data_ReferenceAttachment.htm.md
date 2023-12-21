# ReferenceAttachment - класс
Represents an attachment by reference.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ReferenceAttachment : Attachment
VB __Копировать
     Public NotInheritable Class ReferenceAttachment
    	Inherits Attachment
C++ __Копировать
     public ref class ReferenceAttachment sealed : public Attachment
F# __Копировать
     [<SealedAttribute>]
    type ReferenceAttachment = 
        class
            inherit Attachment
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ComplexProperty](T_Tessa_Exchange_WebServices_Data_ComplexProperty.htm) __[Attachment](T_Tessa_Exchange_WebServices_Data_Attachment.htm) __ ReferenceAttachment
##  __Свойства
[AttachLongPathName](P_Tessa_Exchange_WebServices_Data_ReferenceAttachment_AttachLongPathName.htm)|
Gets or sets a fully-qualified path identifying the attachment.  
---|---  
[AttachmentIsFolder](P_Tessa_Exchange_WebServices_Data_ReferenceAttachment_AttachmentIsFolder.htm)|
Gets or sets a value indicating whether the attachment points to a folder.  
[AttachmentPreviewUrl](P_Tessa_Exchange_WebServices_Data_ReferenceAttachment_AttachmentPreviewUrl.htm)|
Gets or sets the URL of the attachment preview.  
[AttachmentThumbnailUrl](P_Tessa_Exchange_WebServices_Data_ReferenceAttachment_AttachmentThumbnailUrl.htm)|
Gets or sets the URL of the attachment thumbnail.  
[ContentId](P_Tessa_Exchange_WebServices_Data_Attachment_ContentId.htm)|  Gets
or sets the content Id of the attachment. ContentId can be used as a custom
way to identify an attachment in order to reference it from within the body of
the item the attachment belongs to.  
(Унаследован от
[Attachment](T_Tessa_Exchange_WebServices_Data_Attachment.htm))  
[ContentLocation](P_Tessa_Exchange_WebServices_Data_Attachment_ContentLocation.htm)|
Gets or sets the content location of the attachment. ContentLocation can be
used to associate an attachment with a Url defining its location on the Web.  
(Унаследован от
[Attachment](T_Tessa_Exchange_WebServices_Data_Attachment.htm))  
[ContentType](P_Tessa_Exchange_WebServices_Data_Attachment_ContentType.htm)|
Gets or sets the content type of the attachment.  
(Унаследован от
[Attachment](T_Tessa_Exchange_WebServices_Data_Attachment.htm))  
[Id](P_Tessa_Exchange_WebServices_Data_Attachment_Id.htm)|  Gets the Id of the
attachment.  
(Унаследован от
[Attachment](T_Tessa_Exchange_WebServices_Data_Attachment.htm))  
[IsInline](P_Tessa_Exchange_WebServices_Data_Attachment_IsInline.htm)|  Gets
or sets a value indicating whether this is an inline attachment. Inline
attachments are not visible to end users.  
(Унаследован от
[Attachment](T_Tessa_Exchange_WebServices_Data_Attachment.htm))  
[LastModifiedTime](P_Tessa_Exchange_WebServices_Data_Attachment_LastModifiedTime.htm)|
Gets the date and time when this attachment was last modified.  
(Унаследован от
[Attachment](T_Tessa_Exchange_WebServices_Data_Attachment.htm))  
[Name](P_Tessa_Exchange_WebServices_Data_Attachment_Name.htm)|  Gets or sets
the name of the attachment.  
(Унаследован от
[Attachment](T_Tessa_Exchange_WebServices_Data_Attachment.htm))  
[PermissionType](P_Tessa_Exchange_WebServices_Data_ReferenceAttachment_PermissionType.htm)|
Gets or sets the permission of the attachment.  
[ProviderEndpointUrl](P_Tessa_Exchange_WebServices_Data_ReferenceAttachment_ProviderEndpointUrl.htm)|
Gets or sets the URL of the attachment provider.  
[ProviderType](P_Tessa_Exchange_WebServices_Data_ReferenceAttachment_ProviderType.htm)|
Gets or sets the type of the attachment provider.  
[Size](P_Tessa_Exchange_WebServices_Data_Attachment_Size.htm)|  Gets the size
of the attachment.  
(Унаследован от
[Attachment](T_Tessa_Exchange_WebServices_Data_Attachment.htm))  
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
[Load](M_Tessa_Exchange_WebServices_Data_Attachment_Load.htm)|  Loads the
attachment. Calling this method results in a call to EWS.  
(Унаследован от
[Attachment](T_Tessa_Exchange_WebServices_Data_Attachment.htm))  
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
[Tessa.Exchange.WebServices.Data - пространство
имён](N_Tessa_Exchange_WebServices_Data.htm)
