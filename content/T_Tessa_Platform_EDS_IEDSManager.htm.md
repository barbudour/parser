# IEDSManager - интерфейс
##  __Definition
 **Пространство имён:** [Tessa.Platform.EDS](N_Tessa_Platform_EDS.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IEDSManager
VB __Копировать
     Public Interface IEDSManager
C++ __Копировать
     public interface class IEDSManager
F# __Копировать
     type IEDSManager = interface end
##  __Методы
[DecodeCertificateFromSignature](M_Tessa_Platform_EDS_IEDSManager_DecodeCertificateFromSignature.htm)|
Извлекает сертификат из подписи. Возвращает сертификат и текст ошибки, если
сертификат равен null.  
---|---  
[GenerateSignatureAsync](M_Tessa_Platform_EDS_IEDSManager_GenerateSignatureAsync.htm)|
Подписывает документ при помощи указанного сертификата.  
[GetSignatureBytesFromFileAsync](M_Tessa_Platform_EDS_IEDSManager_GetSignatureBytesFromFileAsync.htm)|
Получение байтов подписи из DER или PEM форматов  
[VerifySignatureAsync](M_Tessa_Platform_EDS_IEDSManager_VerifySignatureAsync.htm)|
Проверяет электронную подпись документа, возвращает признак успешной проверки
и текст ошибки, если проверка неуспешна.  
## __См. также
#### Ссылки
[Tessa.Platform.EDS - пространство имён](N_Tessa_Platform_EDS.htm)
