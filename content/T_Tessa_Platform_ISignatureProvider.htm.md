# ISignatureProvider - интерфейс
Объект, предоставляющий криптографические средства для подписания и проверки
подписи.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ISignatureProvider
VB __Копировать
     Public Interface ISignatureProvider
C++ __Копировать
     public interface class ISignatureProvider
F# __Копировать
     type ISignatureProvider = interface end
##  __Методы
[Sign](M_Tessa_Platform_ISignatureProvider_Sign.htm)|  Возвращает электронную
цифровую подпись для заданных бинарных данных лицензии.  
---|---  
[Verify](M_Tessa_Platform_ISignatureProvider_Verify.htm)|  Проверяет
валидность электронной цифровой подписи для заданных бинарных данных лицензии.  
## __Методы расширения
[GenerateSignature](M_Tessa_Platform_Runtime_RuntimeExtensions_GenerateSignature.htm)|
Создаёт подпись для заданных свойств, связанных с сессией.  
(Определяется
[RuntimeExtensions](T_Tessa_Platform_Runtime_RuntimeExtensions.htm))  
---|---  
[ValidateType](M_Tessa_Platform_Licensing_LicensingExtensions_ValidateType.htm)|
Проверяет, что тип объекта является допустимым. Это гарантирует, что объект не
был нигде подменён злоумышленником.  
(Определяется
[LicensingExtensions](T_Tessa_Platform_Licensing_LicensingExtensions.htm))  
[VerifySignature](M_Tessa_Platform_Runtime_RuntimeExtensions_VerifySignature_1.htm)|
Выполняет проверку подписи для заданного токена
[ISessionToken](T_Tessa_Platform_Runtime_ISessionToken.htm) и возвращает
признак того, что подпись корректна.  
(Определяется
[RuntimeExtensions](T_Tessa_Platform_Runtime_RuntimeExtensions.htm))  
[VerifySignature](M_Tessa_Platform_Runtime_RuntimeExtensions_VerifySignature.htm)|
Выполняет проверку подписи для заданных свойств, связанных с сессией, и
возвращает признак того, что подпись корректна.  
(Определяется
[RuntimeExtensions](T_Tessa_Platform_Runtime_RuntimeExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
