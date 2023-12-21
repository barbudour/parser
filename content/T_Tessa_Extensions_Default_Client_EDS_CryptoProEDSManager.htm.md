# CryptoProEDSManager - класс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Client.EDS](N_Tessa_Extensions_Default_Client_EDS.htm)  
 **Сборка:** Tessa.Extensions.Default.Client (в
Tessa.Extensions.Default.Client.dll) Версия: 3.6.0.17
C# __Копировать
     public class CryptoProEDSManager : CAdESManager
VB __Копировать
     Public Class CryptoProEDSManager
    	Inherits CAdESManager
C++ __Копировать
     public ref class CryptoProEDSManager : public CAdESManager
F# __Копировать
     type CryptoProEDSManager = 
        class
            inherit CAdESManager
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[CAdESManager](T_Tessa_Extensions_Default_Shared_EDS_CAdESManager.htm) __ CryptoProEDSManager
##  __Конструкторы
[CryptoProEDSManager](M_Tessa_Extensions_Default_Client_EDS_CryptoProEDSManager__ctor.htm)|
Инициализирует новый экземпляр класса CryptoProEDSManager  
---|---  
##  __Свойства
[CardCache](P_Tessa_Extensions_Default_Shared_EDS_CAdESManager_CardCache.htm)|  
(Унаследован от
[CAdESManager](T_Tessa_Extensions_Default_Shared_EDS_CAdESManager.htm))  
---|---  
[CardRepository](P_Tessa_Extensions_Default_Shared_EDS_CAdESManager_CardRepository.htm)|  
(Унаследован от
[CAdESManager](T_Tessa_Extensions_Default_Shared_EDS_CAdESManager.htm))  
##  __Методы
[CheckExtendedSignatureAsync](M_Tessa_Extensions_Default_Shared_EDS_CAdESManager_CheckExtendedSignatureAsync.htm)|  
(Унаследован от
[CAdESManager](T_Tessa_Extensions_Default_Shared_EDS_CAdESManager.htm))  
---|---  
[DecodeCertificateFromSignature](M_Tessa_Extensions_Default_Shared_EDS_CAdESManager_DecodeCertificateFromSignature.htm)|  
(Унаследован от
[CAdESManager](T_Tessa_Extensions_Default_Shared_EDS_CAdESManager.htm))  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ExtendSignatureAsync](M_Tessa_Extensions_Default_Shared_EDS_CAdESManager_ExtendSignatureAsync.htm)|  
(Унаследован от
[CAdESManager](T_Tessa_Extensions_Default_Shared_EDS_CAdESManager.htm))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GenerateSignatureAsync](M_Tessa_Extensions_Default_Client_EDS_CryptoProEDSManager_GenerateSignatureAsync.htm)|
Подписывает документ при помощи указанного сертификата.  
(Переопределяет [CAdESManager.GenerateSignatureAsync(Byte[], ISignatureFile,
String,
CancellationToken)](M_Tessa_Extensions_Default_Shared_EDS_CAdESManager_GenerateSignatureAsync.htm))  
[GetAttributesFromSignatureAsync](M_Tessa_Extensions_Default_Shared_EDS_CAdESManager_GetAttributesFromSignatureAsync.htm)|  
(Унаследован от
[CAdESManager](T_Tessa_Extensions_Default_Shared_EDS_CAdESManager.htm))  
[GetBesSignatureFromExtendedAsync](M_Tessa_Extensions_Default_Shared_EDS_CAdESManager_GetBesSignatureFromExtendedAsync.htm)|  
(Унаследован от
[CAdESManager](T_Tessa_Extensions_Default_Shared_EDS_CAdESManager.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetSignatureBytesFromFileAsync](M_Tessa_Extensions_Default_Shared_EDS_CAdESManager_GetSignatureBytesFromFileAsync.htm)|  
(Унаследован от
[CAdESManager](T_Tessa_Extensions_Default_Shared_EDS_CAdESManager.htm))  
[GetToBeSignedDocumentAsync](M_Tessa_Extensions_Default_Shared_EDS_CAdESManager_GetToBeSignedDocumentAsync.htm)|  
(Унаследован от
[CAdESManager](T_Tessa_Extensions_Default_Shared_EDS_CAdESManager.htm))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MakeBesSignaturePkcs7Async](M_Tessa_Extensions_Default_Shared_EDS_CAdESManager_MakeBesSignaturePkcs7Async.htm)|  
(Унаследован от
[CAdESManager](T_Tessa_Extensions_Default_Shared_EDS_CAdESManager.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[SignDocumentAsync](M_Tessa_Extensions_Default_Shared_EDS_CAdESManager_SignDocumentAsync.htm)|  
(Унаследован от
[CAdESManager](T_Tessa_Extensions_Default_Shared_EDS_CAdESManager.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[VerifySignatureAsync](M_Tessa_Extensions_Default_Client_EDS_CryptoProEDSManager_VerifySignatureAsync.htm)|
Проверяет электронную подпись документа, возвращает признак успешной проверки
и текст ошибки, если проверка неуспешна.  
(Переопределяет [CAdESManager.VerifySignatureAsync(Byte[], ISignatureFile,
CancellationToken)](M_Tessa_Extensions_Default_Shared_EDS_CAdESManager_VerifySignatureAsync.htm))  
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
[Tessa.Extensions.Default.Client.EDS - пространство
имён](N_Tessa_Extensions_Default_Client_EDS.htm)
