# ExchangeCredentials - класс
Base class of Exchange credential types.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class ExchangeCredentials
VB __Копировать
     Public MustInherit Class ExchangeCredentials
C++ __Копировать
     public ref class ExchangeCredentials abstract
F# __Копировать
     [<AbstractClassAttribute>]
    type ExchangeCredentials = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ExchangeCredentials
Derived
[Tessa.Exchange.WebServices.Data.ClientCertificateCredentials](T_Tessa_Exchange_WebServices_Data_ClientCertificateCredentials.htm)
[Tessa.Exchange.WebServices.Data.Credentials.DualAuthCredentials](T_Tessa_Exchange_WebServices_Data_Credentials_DualAuthCredentials.htm)
[Tessa.Exchange.WebServices.Data.OAuthCredentials](T_Tessa_Exchange_WebServices_Data_OAuthCredentials.htm)
[Tessa.Exchange.WebServices.Data.WebCredentials](T_Tessa_Exchange_WebServices_Data_WebCredentials.htm)
[Tessa.Exchange.WebServices.Data.WSSecurityBasedCredentials](T_Tessa_Exchange_WebServices_Data_WSSecurityBasedCredentials.htm)
##  __Конструкторы
[ExchangeCredentials](M_Tessa_Exchange_WebServices_Data_ExchangeCredentials__ctor.htm)|
Инициализирует новый экземпляр класса ExchangeCredentials  
---|---  
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
##  __Операторы
[ Implicit(CredentialCache to
ExchangeCredentials)](M_Tessa_Exchange_WebServices_Data_ExchangeCredentials_op_Implicit.htm)|
Performs an implicit conversion from
[CredentialCache](https://learn.microsoft.com/dotnet/api/system.net.credentialcache)
to ExchangeCredentials. This allows a CredentialCache object to be implictly
converted to an ExchangeCredential which is useful when setting credentials on
an ExchangeService.  
---|---  
[Implicit(NetworkCredential to
ExchangeCredentials)](M_Tessa_Exchange_WebServices_Data_ExchangeCredentials_op_Implicit_1.htm)|
Performs an implicit conversion from
[NetworkCredential](https://learn.microsoft.com/dotnet/api/system.net.networkcredential)
to ExchangeCredentials. This allows a NetworkCredential object to be implictly
converted to an ExchangeCredential which is useful when setting credentials on
an ExchangeService.  
## __Методы расширения
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
