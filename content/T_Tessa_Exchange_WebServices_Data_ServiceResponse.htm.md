# ServiceResponse - класс
Represents the standard response to an Exchange Web Services operation.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public class ServiceResponse
VB __Копировать
     Public Class ServiceResponse
C++ __Копировать
     public ref class ServiceResponse
F# __Копировать
     type ServiceResponse = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ServiceResponse
Derived
[Tessa.Exchange.WebServices.Data.ArchiveItemResponse](T_Tessa_Exchange_WebServices_Data_ArchiveItemResponse.htm)
[Tessa.Exchange.WebServices.Data.AttendeeAvailability](T_Tessa_Exchange_WebServices_Data_AttendeeAvailability.htm)
[Tessa.Exchange.WebServices.Data.ConvertIdResponse](T_Tessa_Exchange_WebServices_Data_ConvertIdResponse.htm)
[Tessa.Exchange.WebServices.Data.CreateAttachmentResponse](T_Tessa_Exchange_WebServices_Data_CreateAttachmentResponse.htm)
[Tessa.Exchange.WebServices.Data.DelegateUserResponse](T_Tessa_Exchange_WebServices_Data_DelegateUserResponse.htm)
[Tessa.Exchange.WebServices.Data.DeleteAttachmentResponse](T_Tessa_Exchange_WebServices_Data_DeleteAttachmentResponse.htm)
[Tessa.Exchange.WebServices.Data.FindFolderResponse](T_Tessa_Exchange_WebServices_Data_FindFolderResponse.htm)
[Tessa.Exchange.WebServices.Data.GetAttachmentResponse](T_Tessa_Exchange_WebServices_Data_GetAttachmentResponse.htm)
[Tessa.Exchange.WebServices.Data.GetClientAccessTokenResponse](T_Tessa_Exchange_WebServices_Data_GetClientAccessTokenResponse.htm)
[Tessa.Exchange.WebServices.Data.GetClientExtensionResponse](T_Tessa_Exchange_WebServices_Data_GetClientExtensionResponse.htm)
[Tessa.Exchange.WebServices.Data.GetConversationItemsResponse](T_Tessa_Exchange_WebServices_Data_GetConversationItemsResponse.htm)
[Tessa.Exchange.WebServices.Data.GetDiscoverySearchConfigurationResponse](T_Tessa_Exchange_WebServices_Data_GetDiscoverySearchConfigurationResponse.htm)
[Tessa.Exchange.WebServices.Data.GetFolderResponse](T_Tessa_Exchange_WebServices_Data_GetFolderResponse.htm)
[Tessa.Exchange.WebServices.Data.GetHoldOnMailboxesResponse](T_Tessa_Exchange_WebServices_Data_GetHoldOnMailboxesResponse.htm)
[Tessa.Exchange.WebServices.Data.GetItemResponse](T_Tessa_Exchange_WebServices_Data_GetItemResponse.htm)
[Tessa.Exchange.WebServices.Data.GetNonIndexableItemDetailsResponse](T_Tessa_Exchange_WebServices_Data_GetNonIndexableItemDetailsResponse.htm)
[Tessa.Exchange.WebServices.Data.GetNonIndexableItemStatisticsResponse](T_Tessa_Exchange_WebServices_Data_GetNonIndexableItemStatisticsResponse.htm)
[Tessa.Exchange.WebServices.Data.GetOMEConfigurationResponse](T_Tessa_Exchange_WebServices_Data_GetOMEConfigurationResponse.htm)
[Tessa.Exchange.WebServices.Data.GetSearchableMailboxesResponse](T_Tessa_Exchange_WebServices_Data_GetSearchableMailboxesResponse.htm)
[Tessa.Exchange.WebServices.Data.GetUserRetentionPolicyTagsResponse](T_Tessa_Exchange_WebServices_Data_GetUserRetentionPolicyTagsResponse.htm)
[Tessa.Exchange.WebServices.Data.MarkAsJunkResponse](T_Tessa_Exchange_WebServices_Data_MarkAsJunkResponse.htm)
[Tessa.Exchange.WebServices.Data.MoveCopyFolderResponse](T_Tessa_Exchange_WebServices_Data_MoveCopyFolderResponse.htm)
[Tessa.Exchange.WebServices.Data.MoveCopyItemResponse](T_Tessa_Exchange_WebServices_Data_MoveCopyItemResponse.htm)
[Tessa.Exchange.WebServices.Data.SearchMailboxesResponse](T_Tessa_Exchange_WebServices_Data_SearchMailboxesResponse.htm)
[Tessa.Exchange.WebServices.Data.SetHoldOnMailboxesResponse](T_Tessa_Exchange_WebServices_Data_SetHoldOnMailboxesResponse.htm)
[Tessa.Exchange.WebServices.Data.SyncResponse<TServiceObject,
TChange>](T_Tessa_Exchange_WebServices_Data_SyncResponse_2.htm)
[Tessa.Exchange.WebServices.Data.UpdateItemResponse](T_Tessa_Exchange_WebServices_Data_UpdateItemResponse.htm)
Подробнее __Less __
##  __Свойства
[ErrorCode](P_Tessa_Exchange_WebServices_Data_ServiceResponse_ErrorCode.htm)|
Gets the error code associated with this response.  
---|---  
[ErrorDetails](P_Tessa_Exchange_WebServices_Data_ServiceResponse_ErrorDetails.htm)|
Gets error details associated with the response. If Result is set to Success,
ErrorDetailsDictionary returns null. Error details will only available for
some error codes. For example, when error code is
ErrorRecurrenceHasNoOccurrence, the ErrorDetailsDictionary will contain keys
for EffectiveStartDate and EffectiveEndDate.  
[ErrorMessage](P_Tessa_Exchange_WebServices_Data_ServiceResponse_ErrorMessage.htm)|
Gets a detailed error message associated with the response. If Result is set
to Success, ErrorMessage returns null. ErrorMessage is localized according to
the PreferredCulture property of the ExchangeService object that was used to
call the method that generated the response.  
[ErrorProperties](P_Tessa_Exchange_WebServices_Data_ServiceResponse_ErrorProperties.htm)|
Gets information about property errors associated with the response. If Result
is set to Success, ErrorProperties returns null. ErrorProperties is only
available for some error codes. For example, when the error code is
ErrorInvalidPropertyForOperation, ErrorProperties will contain the definition
of the property that was invalid for the request.  
[Result](P_Tessa_Exchange_WebServices_Data_ServiceResponse_Result.htm)|  Gets
the result associated with this response.  
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
[Tessa.Exchange.WebServices.Data - пространство
имён](N_Tessa_Exchange_WebServices_Data.htm)
