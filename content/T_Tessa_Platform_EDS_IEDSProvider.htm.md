# IEDSProvider - интерфейс
Объект, обеспечивающий низкоуровневые функции по работе с электронной
подписью.
## __Definition
 **Пространство имён:** [Tessa.Platform.EDS](N_Tessa_Platform_EDS.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IEDSProvider
VB __Копировать
     Public Interface IEDSProvider
C++ __Копировать
     public interface class IEDSProvider
F# __Копировать
     type IEDSProvider = interface end
##  __Методы
[ExtendDocumentAsync](M_Tessa_Platform_EDS_IEDSProvider_ExtendDocumentAsync.htm)|
Расширяет объект подписи информацией по меткам времени и другой информацией, в
соответствии с настройками. Возвращает расширенную подпись в base64,
информация о проверке подписи. Для подписи в формате BES возвращает исходную
подпись.  
---|---  
[GetBesSignatureAsync](M_Tessa_Platform_EDS_IEDSProvider_GetBesSignatureAsync.htm)|
Возвращает подпись в формате BES в base64.  
[GetSignatureAttributesFromSignatureAsync](M_Tessa_Platform_EDS_IEDSProvider_GetSignatureAttributesFromSignatureAsync.htm)|
Возвращает параметры подписи для указанного объекта подписи.  
[GetSignedDocumentAsync](M_Tessa_Platform_EDS_IEDSProvider_GetSignedDocumentAsync.htm)|
Возвращает объект в base64, содержащий ЭП подписанного файла.  
[GetToBeSignedAsync](M_Tessa_Platform_EDS_IEDSProvider_GetToBeSignedAsync.htm)|
Возвращает объект подписи в base64, подготовленный для подписания на клиенте.  
[ValidateDocumentAsync](M_Tessa_Platform_EDS_IEDSProvider_ValidateDocumentAsync.htm)|
Выполняет валидацию электронной подписи. Возвращает сериализованную структуру,
которая содержит информацию по проверке различных параметров подписи.  
## __См. также
#### Ссылки
[Tessa.Platform.EDS - пространство имён](N_Tessa_Platform_EDS.htm)
