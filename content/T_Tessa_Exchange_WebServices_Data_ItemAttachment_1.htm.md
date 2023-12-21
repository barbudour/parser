# ItemAttachment<TItem> \- класс
Represents a strongly typed item attachment.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ItemAttachment<TItem> : ItemAttachment
    where TItem : Item
VB __Копировать
     Public NotInheritable Class ItemAttachment(Of TItem As Item)
    	Inherits ItemAttachment
C++ __Копировать
    generic<typename TItem>
    where TItem : Item
    public ref class ItemAttachment sealed : public ItemAttachment
F# __Копировать
     [<SealedAttribute>]
    type ItemAttachment<'TItem when 'TItem : Item> = 
        class
            inherit ItemAttachment
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ComplexProperty](T_Tessa_Exchange_WebServices_Data_ComplexProperty.htm) __[Attachment](T_Tessa_Exchange_WebServices_Data_Attachment.htm) __[ItemAttachment](T_Tessa_Exchange_WebServices_Data_ItemAttachment.htm) __ ItemAttachment<TItem>
#### Параметры типа
TItem
    Item type.
##  __Свойства
[ContentId](P_Tessa_Exchange_WebServices_Data_Attachment_ContentId.htm)|  Gets
or sets the content Id of the attachment. ContentId can be used as a custom
way to identify an attachment in order to reference it from within the body of
the item the attachment belongs to.  
(Унаследован от
[Attachment](T_Tessa_Exchange_WebServices_Data_Attachment.htm))  
---|---  
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
[Item](P_Tessa_Exchange_WebServices_Data_ItemAttachment_1_Item.htm)|  Gets the
item associated with the attachment.  
[LastModifiedTime](P_Tessa_Exchange_WebServices_Data_Attachment_LastModifiedTime.htm)|
Gets the date and time when this attachment was last modified.  
(Унаследован от
[Attachment](T_Tessa_Exchange_WebServices_Data_Attachment.htm))  
[Name](P_Tessa_Exchange_WebServices_Data_Attachment_Name.htm)|  Gets or sets
the name of the attachment.  
(Унаследован от
[Attachment](T_Tessa_Exchange_WebServices_Data_Attachment.htm))  
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
[Load(CancellationToken)](M_Tessa_Exchange_WebServices_Data_Attachment_Load.htm)|
Loads the attachment. Calling this method results in a call to EWS.  
(Унаследован от
[Attachment](T_Tessa_Exchange_WebServices_Data_Attachment.htm))  
[Load(CancellationToken,
PropertyDefinitionBase[])](M_Tessa_Exchange_WebServices_Data_ItemAttachment_Load_1.htm)|
Loads this attachment.  
(Унаследован от
[ItemAttachment](T_Tessa_Exchange_WebServices_Data_ItemAttachment.htm))  
[Load(IEnumerable<PropertyDefinitionBase>,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ItemAttachment_Load.htm)|
Loads this attachment.  
(Унаследован от
[ItemAttachment](T_Tessa_Exchange_WebServices_Data_ItemAttachment.htm))  
[Load(BodyType, IEnumerable<PropertyDefinitionBase>,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ItemAttachment_Load_2.htm)|
Loads this attachment.  
(Унаследован от
[ItemAttachment](T_Tessa_Exchange_WebServices_Data_ItemAttachment.htm))  
[Load(BodyType, CancellationToken,
PropertyDefinitionBase[])](M_Tessa_Exchange_WebServices_Data_ItemAttachment_Load_3.htm)|
Loads this attachment.  
(Унаследован от
[ItemAttachment](T_Tessa_Exchange_WebServices_Data_ItemAttachment.htm))  
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
