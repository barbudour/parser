# ResponseMessage - класс
Represents the base class for e-mail related responses (Reply, Reply all and
Forward).
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ResponseMessage : ResponseObject<EmailMessage>
VB __Копировать
     Public NotInheritable Class ResponseMessage
    	Inherits ResponseObject(Of EmailMessage)
C++ __Копировать
     public ref class ResponseMessage sealed : public ResponseObject<EmailMessage^>
F# __Копировать
     [<SealedAttribute>]
    type ResponseMessage = 
        class
            inherit ResponseObject<EmailMessage>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ServiceObject](T_Tessa_Exchange_WebServices_Data_ServiceObject.htm) __[ResponseObject](T_Tessa_Exchange_WebServices_Data_ResponseObject_1.htm)<[EmailMessage](T_Tessa_Exchange_WebServices_Data_EmailMessage.htm)> __ ResponseMessage
##  __Свойства
[BccRecipients](P_Tessa_Exchange_WebServices_Data_ResponseMessage_BccRecipients.htm)|
Gets a list of recipients this response will be sent to as Bcc.  
---|---  
[Body](P_Tessa_Exchange_WebServices_Data_ResponseMessage_Body.htm)|  Gets or
sets the body of the response.  
[BodyPrefix](P_Tessa_Exchange_WebServices_Data_ResponseMessage_BodyPrefix.htm)|
Gets or sets the body prefix of this response. The body prefix will be
prepended to the original message's body when the response is created.  
[CcRecipients](P_Tessa_Exchange_WebServices_Data_ResponseMessage_CcRecipients.htm)|
Gets a list of recipients the response will be sent to as Cc.  
[IsDeliveryReceiptRequested](P_Tessa_Exchange_WebServices_Data_ResponseObject_1_IsDeliveryReceiptRequested.htm)|
Gets or sets a value indicating whether delivery receipts should be sent to
the sender.  
(Унаследован от
[ResponseObject<TMessage>](T_Tessa_Exchange_WebServices_Data_ResponseObject_1.htm))  
[IsDirty](P_Tessa_Exchange_WebServices_Data_ServiceObject_IsDirty.htm)|  Gets
a value indicating whether the object has been modified and should be saved.  
(Унаследован от
[ServiceObject](T_Tessa_Exchange_WebServices_Data_ServiceObject.htm))  
[IsNew](P_Tessa_Exchange_WebServices_Data_ServiceObject_IsNew.htm)|  Indicates
whether this object is a real store item, or if it's a local object that has
yet to be saved.  
(Унаследован от
[ServiceObject](T_Tessa_Exchange_WebServices_Data_ServiceObject.htm))  
[IsReadReceiptRequested](P_Tessa_Exchange_WebServices_Data_ResponseObject_1_IsReadReceiptRequested.htm)|
Gets or sets a value indicating whether read receipts will be requested from
recipients of this response.  
(Унаследован от
[ResponseObject<TMessage>](T_Tessa_Exchange_WebServices_Data_ResponseObject_1.htm))  
[Item](P_Tessa_Exchange_WebServices_Data_ServiceObject_Item.htm)|  Gets the
value of specified property in this instance.  
(Унаследован от
[ServiceObject](T_Tessa_Exchange_WebServices_Data_ServiceObject.htm))  
[ResponseType](P_Tessa_Exchange_WebServices_Data_ResponseMessage_ResponseType.htm)|
Gets a value indicating the type of response this object represents.  
[Schema](P_Tessa_Exchange_WebServices_Data_ServiceObject_Schema.htm)|  Gets
the schema associated with this type of object.  
(Унаследован от
[ServiceObject](T_Tessa_Exchange_WebServices_Data_ServiceObject.htm))  
[Service](P_Tessa_Exchange_WebServices_Data_ServiceObject_Service.htm)|  Gets
the ExchangeService the object is bound to.  
(Унаследован от
[ServiceObject](T_Tessa_Exchange_WebServices_Data_ServiceObject.htm))  
[Subject](P_Tessa_Exchange_WebServices_Data_ResponseMessage_Subject.htm)|
Gets or sets the subject of this response.  
[ToRecipients](P_Tessa_Exchange_WebServices_Data_ResponseMessage_ToRecipients.htm)|
Gets a list of recipients the response will be sent to.  
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
[GetLoadedPropertyDefinitions](M_Tessa_Exchange_WebServices_Data_ServiceObject_GetLoadedPropertyDefinitions.htm)|
Gets the collection of loaded property definitions.  
(Унаследован от
[ServiceObject](T_Tessa_Exchange_WebServices_Data_ServiceObject.htm))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Load(CancellationToken)](M_Tessa_Exchange_WebServices_Data_ServiceObject_Load.htm)|
Loads the first class properties. Calling this method results in a call to
EWS.  
(Унаследован от
[ServiceObject](T_Tessa_Exchange_WebServices_Data_ServiceObject.htm))  
[Load(PropertySet,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ServiceObject_Load_1.htm)|
Loads the specified set of properties. Calling this method results in a call
to EWS.  
(Унаследован от
[ServiceObject](T_Tessa_Exchange_WebServices_Data_ServiceObject.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Save(CancellationToken)](M_Tessa_Exchange_WebServices_Data_ResponseObject_1_Save.htm)|
Saves the response in the Drafts folder. Calling this method results in a call
to EWS.  
(Унаследован от
[ResponseObject<TMessage>](T_Tessa_Exchange_WebServices_Data_ResponseObject_1.htm))  
[Save(FolderId,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ResponseObject_1_Save_1.htm)|
Saves the response in the specified folder. Calling this method results in a
call to EWS.  
(Унаследован от
[ResponseObject<TMessage>](T_Tessa_Exchange_WebServices_Data_ResponseObject_1.htm))  
[Save(WellKnownFolderName,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ResponseObject_1_Save_2.htm)|
Saves the response in the specified folder. Calling this method results in a
call to EWS.  
(Унаследован от
[ResponseObject<TMessage>](T_Tessa_Exchange_WebServices_Data_ResponseObject_1.htm))  
[Send](M_Tessa_Exchange_WebServices_Data_ResponseObject_1_Send.htm)|  Sends
this response without saving a copy. Calling this method results in a call to
EWS.  
(Унаследован от
[ResponseObject<TMessage>](T_Tessa_Exchange_WebServices_Data_ResponseObject_1.htm))  
[SendAndSaveCopy(CancellationToken)](M_Tessa_Exchange_WebServices_Data_ResponseObject_1_SendAndSaveCopy.htm)|
Sends this response and saves a copy in the Sent Items folder. Calling this
method results in a call to EWS.  
(Унаследован от
[ResponseObject<TMessage>](T_Tessa_Exchange_WebServices_Data_ResponseObject_1.htm))  
[SendAndSaveCopy(FolderId,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ResponseObject_1_SendAndSaveCopy_1.htm)|
Sends this response and saves a copy in the specified folder. Calling this
method results in a call to EWS.  
(Унаследован от
[ResponseObject<TMessage>](T_Tessa_Exchange_WebServices_Data_ResponseObject_1.htm))  
[SendAndSaveCopy(WellKnownFolderName,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ResponseObject_1_SendAndSaveCopy_2.htm)|
Sends this response and saves a copy in the specified folder. Calling this
method results in a call to EWS.  
(Унаследован от
[ResponseObject<TMessage>](T_Tessa_Exchange_WebServices_Data_ResponseObject_1.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetProperty(PropertyDefinitionBase,
Object)](M_Tessa_Exchange_WebServices_Data_ServiceObject_TryGetProperty.htm)|
Try to get the value of a specified property in this instance.  
(Унаследован от
[ServiceObject](T_Tessa_Exchange_WebServices_Data_ServiceObject.htm))  
[TryGetProperty<T>(PropertyDefinitionBase,
T)](M_Tessa_Exchange_WebServices_Data_ServiceObject_TryGetProperty__1.htm)|
Try to get the value of a specified property in this instance.  
(Унаследован от
[ServiceObject](T_Tessa_Exchange_WebServices_Data_ServiceObject.htm))  
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
