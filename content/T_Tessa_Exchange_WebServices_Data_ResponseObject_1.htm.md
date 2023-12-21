# ResponseObject<TMessage> \- класс
Represents the base class for all responses that can be sent.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
    [EditorBrowsableAttribute(EditorBrowsableState.Never)]
    public abstract class ResponseObject<TMessage> : ServiceObject
    where TMessage : EmailMessage
VB __Копировать
    <EditorBrowsableAttribute(EditorBrowsableState.Never)>
    Public MustInherit Class ResponseObject(Of TMessage As EmailMessage)
    	Inherits ServiceObject
C++ __Копировать
    [EditorBrowsableAttribute(EditorBrowsableState::Never)]
    generic<typename TMessage>
    where TMessage : EmailMessage
    public ref class ResponseObject abstract : public ServiceObject
F# __Копировать
     [<AbstractClassAttribute>]
    [<EditorBrowsableAttribute(EditorBrowsableState.Never)>]
    type ResponseObject<'TMessage when 'TMessage : EmailMessage> = 
        class
            inherit ServiceObject
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ServiceObject](T_Tessa_Exchange_WebServices_Data_ServiceObject.htm) __ ResponseObject<TMessage>
Derived
[Tessa.Exchange.WebServices.Data.CalendarResponseMessageBase<TMessage>](T_Tessa_Exchange_WebServices_Data_CalendarResponseMessageBase_1.htm)
[Tessa.Exchange.WebServices.Data.ResponseMessage](T_Tessa_Exchange_WebServices_Data_ResponseMessage.htm)
#### Параметры типа
TMessage
    Type of message.
##  __Свойства
[IsDeliveryReceiptRequested](P_Tessa_Exchange_WebServices_Data_ResponseObject_1_IsDeliveryReceiptRequested.htm)|
Gets or sets a value indicating whether delivery receipts should be sent to
the sender.  
---|---  
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
[Item](P_Tessa_Exchange_WebServices_Data_ServiceObject_Item.htm)|  Gets the
value of specified property in this instance.  
(Унаследован от
[ServiceObject](T_Tessa_Exchange_WebServices_Data_ServiceObject.htm))  
[Schema](P_Tessa_Exchange_WebServices_Data_ServiceObject_Schema.htm)|  Gets
the schema associated with this type of object.  
(Унаследован от
[ServiceObject](T_Tessa_Exchange_WebServices_Data_ServiceObject.htm))  
[Service](P_Tessa_Exchange_WebServices_Data_ServiceObject_Service.htm)|  Gets
the ExchangeService the object is bound to.  
(Унаследован от
[ServiceObject](T_Tessa_Exchange_WebServices_Data_ServiceObject.htm))  
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
[Save(FolderId,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ResponseObject_1_Save_1.htm)|
Saves the response in the specified folder. Calling this method results in a
call to EWS.  
[Save(WellKnownFolderName,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ResponseObject_1_Save_2.htm)|
Saves the response in the specified folder. Calling this method results in a
call to EWS.  
[Send](M_Tessa_Exchange_WebServices_Data_ResponseObject_1_Send.htm)|  Sends
this response without saving a copy. Calling this method results in a call to
EWS.  
[SendAndSaveCopy(CancellationToken)](M_Tessa_Exchange_WebServices_Data_ResponseObject_1_SendAndSaveCopy.htm)|
Sends this response and saves a copy in the Sent Items folder. Calling this
method results in a call to EWS.  
[SendAndSaveCopy(FolderId,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ResponseObject_1_SendAndSaveCopy_1.htm)|
Sends this response and saves a copy in the specified folder. Calling this
method results in a call to EWS.  
[SendAndSaveCopy(WellKnownFolderName,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ResponseObject_1_SendAndSaveCopy_2.htm)|
Sends this response and saves a copy in the specified folder. Calling this
method results in a call to EWS.  
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
