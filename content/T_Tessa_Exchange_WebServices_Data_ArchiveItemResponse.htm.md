# ArchiveItemResponse - класс
Represents a response to a Move or Copy operation.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ArchiveItemResponse : ServiceResponse
VB __Копировать
     Public NotInheritable Class ArchiveItemResponse
    	Inherits ServiceResponse
C++ __Копировать
     public ref class ArchiveItemResponse sealed : public ServiceResponse
F# __Копировать
     [<SealedAttribute>]
    type ArchiveItemResponse = 
        class
            inherit ServiceResponse
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ServiceResponse](T_Tessa_Exchange_WebServices_Data_ServiceResponse.htm) __ ArchiveItemResponse
##  __Свойства
[ErrorCode](P_Tessa_Exchange_WebServices_Data_ServiceResponse_ErrorCode.htm)|
Gets the error code associated with this response.  
(Унаследован от
[ServiceResponse](T_Tessa_Exchange_WebServices_Data_ServiceResponse.htm))  
---|---  
[ErrorDetails](P_Tessa_Exchange_WebServices_Data_ServiceResponse_ErrorDetails.htm)|
Gets error details associated with the response. If Result is set to Success,
ErrorDetailsDictionary returns null. Error details will only available for
some error codes. For example, when error code is
ErrorRecurrenceHasNoOccurrence, the ErrorDetailsDictionary will contain keys
for EffectiveStartDate and EffectiveEndDate.  
(Унаследован от
[ServiceResponse](T_Tessa_Exchange_WebServices_Data_ServiceResponse.htm))  
[ErrorMessage](P_Tessa_Exchange_WebServices_Data_ServiceResponse_ErrorMessage.htm)|
Gets a detailed error message associated with the response. If Result is set
to Success, ErrorMessage returns null. ErrorMessage is localized according to
the PreferredCulture property of the ExchangeService object that was used to
call the method that generated the response.  
(Унаследован от
[ServiceResponse](T_Tessa_Exchange_WebServices_Data_ServiceResponse.htm))  
[ErrorProperties](P_Tessa_Exchange_WebServices_Data_ServiceResponse_ErrorProperties.htm)|
Gets information about property errors associated with the response. If Result
is set to Success, ErrorProperties returns null. ErrorProperties is only
available for some error codes. For example, when the error code is
ErrorInvalidPropertyForOperation, ErrorProperties will contain the definition
of the property that was invalid for the request.  
(Унаследован от
[ServiceResponse](T_Tessa_Exchange_WebServices_Data_ServiceResponse.htm))  
[Item](P_Tessa_Exchange_WebServices_Data_ArchiveItemResponse_Item.htm)|  Gets
the copied or moved item.  
[Result](P_Tessa_Exchange_WebServices_Data_ServiceResponse_Result.htm)|  Gets
the result associated with this response.  
(Унаследован от
[ServiceResponse](T_Tessa_Exchange_WebServices_Data_ServiceResponse.htm))  
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
