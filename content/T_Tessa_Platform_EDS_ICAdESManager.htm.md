# ICAdESManager - интерфейс
##  __Definition
 **Пространство имён:** [Tessa.Platform.EDS](N_Tessa_Platform_EDS.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICAdESManager : IEDSManager
VB __Копировать
     Public Interface ICAdESManager
    	Inherits IEDSManager
C++ __Копировать
     public interface class ICAdESManager : IEDSManager
F# __Копировать
     type ICAdESManager = 
        interface
            interface IEDSManager
        end
Implements
    [IEDSManager](T_Tessa_Platform_EDS_IEDSManager.htm)
##  __Методы
[CheckExtendedSignatureAsync](M_Tessa_Platform_EDS_ICAdESManager_CheckExtendedSignatureAsync.htm)|  
---|---  
[DecodeCertificateFromSignature](M_Tessa_Platform_EDS_IEDSManager_DecodeCertificateFromSignature.htm)|
Извлекает сертификат из подписи. Возвращает сертификат и текст ошибки, если
сертификат равен null.  
(Унаследован от [IEDSManager](T_Tessa_Platform_EDS_IEDSManager.htm))  
[ExtendSignatureAsync](M_Tessa_Platform_EDS_ICAdESManager_ExtendSignatureAsync.htm)|  
[GenerateSignatureAsync](M_Tessa_Platform_EDS_IEDSManager_GenerateSignatureAsync.htm)|
Подписывает документ при помощи указанного сертификата.  
(Унаследован от [IEDSManager](T_Tessa_Platform_EDS_IEDSManager.htm))  
[GetAttributesFromSignatureAsync](M_Tessa_Platform_EDS_ICAdESManager_GetAttributesFromSignatureAsync.htm)|  
[GetBesSignatureFromExtendedAsync](M_Tessa_Platform_EDS_ICAdESManager_GetBesSignatureFromExtendedAsync.htm)|  
[GetSignatureBytesFromFileAsync](M_Tessa_Platform_EDS_IEDSManager_GetSignatureBytesFromFileAsync.htm)|
Получение байтов подписи из DER или PEM форматов  
(Унаследован от [IEDSManager](T_Tessa_Platform_EDS_IEDSManager.htm))  
[GetToBeSignedDocumentAsync](M_Tessa_Platform_EDS_ICAdESManager_GetToBeSignedDocumentAsync.htm)|  
[MakeBesSignaturePkcs7Async](M_Tessa_Platform_EDS_ICAdESManager_MakeBesSignaturePkcs7Async.htm)|  
[SignDocumentAsync](M_Tessa_Platform_EDS_ICAdESManager_SignDocumentAsync.htm)|  
[VerifySignatureAsync](M_Tessa_Platform_EDS_IEDSManager_VerifySignatureAsync.htm)|
Проверяет электронную подпись документа, возвращает признак успешной проверки
и текст ошибки, если проверка неуспешна.  
(Унаследован от [IEDSManager](T_Tessa_Platform_EDS_IEDSManager.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.EDS - пространство имён](N_Tessa_Platform_EDS.htm)
